from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import attrs
from typeguard import typechecked

from tecton._internals import display
from tecton._internals import metadata_service
from tecton._internals import sdk_decorators
from tecton.declarative import base as declarative_base
from tecton.declarative import feature_service as declarative_feature_service
from tecton.declarative import logging_config
from tecton.unified import common as unified_common
from tecton.unified import feature_view as unified_feature_view
from tecton.unified import utils as unified_utils
from tecton_core import fco_container
from tecton_core import feature_set_config
from tecton_core import specs
from tecton_proto.args import basic_info_pb2
from tecton_proto.args import fco_args_pb2
from tecton_proto.args import feature_service_pb2 as feature_service__args_pb2
from tecton_proto.common import fco_locator_pb2
from tecton_proto.metadataservice import metadata_service_pb2


@attrs.define
class FeatureService(unified_common.BaseTectonObject):
    """A Tecton Feature Service.

    Attributes:
        _spec:  A Feature Service spec, i.e. a dataclass representation of the Tecton object that is used in most
            functional use cases, e.g. constructing queries. Set only after the object has been validated. Remote
            objects, i.e. applied objects fetched from the backend, are assumed valid.
        _args: A Tecton "args" proto. Only set if this object was defined locally, i.e. this object was not applied
            and fetched from the Tecton backend.
        _feature_references: The feature references that make up this Feature Service.
        _feature_set_config: The feature set config for thie Feature Service. The feature set config is used for query
            construction and represents a super set of the feature references in _feature_references because of indirect
            feature definition dependencies. For example, _feature_references may contain a single ODFV, but
            _feature_set_config may represent that ODFV plus a batch feature view input to that ODFV. The
            _feature_set_config is set only after the FeatureService object has been validated.
    """

    _spec: Optional[specs.FeatureServiceSpec] = attrs.field(repr=False)
    _args: Optional[feature_service__args_pb2.FeatureServiceArgs] = attrs.field(
        repr=False, on_setattr=attrs.setters.frozen
    )
    _feature_references: Tuple[declarative_base.FeatureReference, ...] = attrs.field(on_setattr=attrs.setters.frozen)
    _feature_set_config: Optional[feature_set_config.FeatureSetConfig] = attrs.field(repr=False)

    def __init__(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        owner: Optional[str] = None,
        online_serving_enabled: bool = True,
        features: List[Union[declarative_base.FeatureReference, unified_feature_view.FeatureView]] = None,
        logging: Optional[logging_config.LoggingConfig] = None,
    ):
        """
        Instantiates a new FeatureService.

        :param name: A unique name for the Feature Service.
        :param description: A human-readable description.
        :param tags: Tags associated with this Tecton Object (key-value pairs of arbitrary metadata).
        :param owner: Owner name (typically the email of the primary maintainer).
        :param online_serving_enabled: (Optional, default True) If True, users can send realtime requests
            to this FeatureService, and only FeatureViews with online materialization enabled can be added
            to this FeatureService.
        :param features: The list of FeatureView or FeatureReference that this FeatureService will serve.
        :param logging: A configuration for logging feature requests sent to this Feature Service.

        An example of Feature Service declaration

        .. code-block:: python

            from tecton import FeatureService, LoggingConfig
            # Import your feature views declared in your feature repo directory
            from feature_repo.features.feature_views import last_transaction_amount_sql, transaction_amount_is_high
            ...

            # Declare Feature Service
            fraud_detection_feature_service = FeatureService(
                name='fraud_detection_feature_service',
                description='A FeatureService providing features for a model that predicts if a transaction is fraudulent.',
                features=[
                    last_transaction_amount_sql,
                    transaction_amount_is_high,
                    ...
                ]
                logging=LoggingConfig(
                    sample_rate=0.5,
                    log_effective_times=False,
                )
                tags={'release': 'staging'},
            )
        """
        from tecton.cli import common as cli_common

        feature_references = []
        for feature in features:
            if isinstance(feature, declarative_base.FeatureReference):
                # TODO(jake): Remove this after cleaning up the declarative objects.
                assert isinstance(
                    feature._fv, unified_feature_view.FeatureView
                ), f"Can only use unified Feature Views with the Unified Feature Service. Got {feature._fv}"
                feature_references.append(feature)
            elif isinstance(feature, unified_feature_view.FeatureView):
                feature_references.append(declarative_base.FeatureReference(feature_definition=feature))
            else:
                raise TypeError(
                    f"Object in FeatureService.features with an invalid type: {type(feature)}. Should be of type FeatureReference or Feature View."
                )

        args = declarative_feature_service.build_feature_service_args(
            basic_info=basic_info_pb2.BasicInfo(name=name, description=description, tags=tags, owner=owner),
            online_serving_enabled=online_serving_enabled,
            features=feature_references,
            logging=logging,
        )
        info = unified_common.TectonObjectInfo.from_args_proto(args.info, args.feature_service_id)
        source_info = cli_common.get_fco_source_info()
        self.__attrs_init__(
            info=info,
            spec=None,
            args=args,
            source_info=source_info,
            feature_references=feature_references,
            feature_set_config=None,
        )

    @classmethod
    @typechecked
    def _from_spec(cls, spec: specs.FeatureServiceSpec, fco_container: fco_container.FcoContainer) -> "FeatureService":
        """Create a Feature Service from directly from a spec. Specs are assumed valid and will not be re-validated."""
        feature_set_config_ = feature_set_config.FeatureSetConfig.from_spec(spec, fco_container)
        info = unified_common.TectonObjectInfo.from_spec(spec)
        feature_references = tuple()  # TODO(jake): Construct these.
        obj = cls.__new__(cls)  # Instantiate the object. Does not call init.
        obj.__attrs_init__(
            info=info,
            spec=spec,
            args=None,
            source_info=None,
            feature_references=feature_references,
            feature_set_config=feature_set_config_,
        )
        return obj

    @unified_utils.requires_local_object
    def _build_args(self) -> fco_args_pb2.FcoArgs:
        return fco_args_pb2.FcoArgs(feature_service=self._args)

    @property
    def _is_valid(self) -> bool:
        return self._spec is not None

    @sdk_decorators.sdk_public_method
    def validate(self):
        # TODO
        pass

    @sdk_decorators.sdk_public_method
    @unified_utils.requires_remote_object
    def summary(self) -> display.Displayable:
        """Displays a human readable summary of this Feature View."""
        request = metadata_service_pb2.GetFeatureServiceSummaryRequest(
            fco_locator=fco_locator_pb2.FcoLocator(id=self._spec.id_proto, workspace=self._spec.workspace)
        )
        response = metadata_service.instance().GetFeatureServiceSummary(request)
        return display.Displayable.from_fco_summary(response.fco_summary)

    @property
    def features(self) -> List[declarative_base.FeatureReference]:
        """TODO(jake): Documentation with code snippet."""
        return list(self._feature_references)

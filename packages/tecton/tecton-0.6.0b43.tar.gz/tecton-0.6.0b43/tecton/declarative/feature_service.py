from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from tecton._internals.fco import Fco
from tecton.declarative.base import BaseFeatureDefinition
from tecton.declarative.base import FeatureReference
from tecton.declarative.basic_info import prepare_basic_info
from tecton.declarative.logging_config import LoggingConfig
from tecton_core.feature_definition_wrapper import FrameworkVersion
from tecton_core.id_helper import IdHelper
from tecton_core.logger import get_logger
from tecton_proto.args import feature_service_pb2
from tecton_proto.args.basic_info_pb2 import BasicInfo
from tecton_proto.args.feature_service_pb2 import FeatureServiceArgs
from tecton_proto.args.repo_metadata_pb2 import SourceInfo
from tecton_proto.common.id_pb2 import Id


logger = get_logger("FeatureService")


class FeatureService(Fco):
    """
    Declare a FeatureService.

    In Tecton, a Feature Service exposes an API for accessing a set of FeatureViews.
    FeatureServices are implemented using the ``FeatureService`` class.

    Once deployed in production, each model has one associated Feature Service that
    serves the model its features. A Feature Service contains a list of the Feature
    Views associated with a model. It also includes user-provided metadata such as
    name, description, and owner that Tecton uses to organize feature data.
    """

    _args: FeatureServiceArgs
    _source_info: SourceInfo

    def __init__(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        owner: Optional[str] = None,
        online_serving_enabled: bool = True,
        features: List[Union[FeatureReference, BaseFeatureDefinition]] = None,
        logging: Optional[LoggingConfig] = None,
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
        from tecton.cli.common import get_fco_source_info

        basic_info = prepare_basic_info(name=name, description=description, owner=owner, family=None, tags=tags)

        self._source_info = get_fco_source_info()
        self._args = build_feature_service_args(
            basic_info=basic_info,
            online_serving_enabled=online_serving_enabled,
            features=features or [],
            logging=logging,
        )

        Fco._register(self)

    @property
    def _id(self) -> Id:
        return self._args.feature_service_id

    @property
    def name(self) -> str:
        """
        Name of this FeatureService.
        """
        return self._args.info.name


def build_feature_service_args(
    *,
    basic_info: BasicInfo,
    online_serving_enabled: bool,
    features: List[Union[FeatureReference, BaseFeatureDefinition]],
    logging: Optional[LoggingConfig],
) -> FeatureServiceArgs:
    if features:
        feature_packages = [_feature_to_feature_service_feature_package(feature) for feature in features]
    else:
        feature_packages = None

    return FeatureServiceArgs(
        feature_service_id=IdHelper.from_string(IdHelper.generate_string_id()),
        info=basic_info,
        online_serving_enabled=online_serving_enabled,
        feature_packages=feature_packages,
        version=FrameworkVersion.FWV5.value,
        logging=logging._to_proto() if logging is not None else None,
    )


def _feature_to_feature_service_feature_package(
    feature: Union[FeatureReference, BaseFeatureDefinition],
) -> feature_service_pb2.FeatureServiceFeaturePackage:
    if not isinstance(feature, (FeatureReference, BaseFeatureDefinition)):
        raise TypeError(
            f"Object in FeatureService.features with an invalid type: {type(feature)}. Should be of type FeatureReference or BaseFeatureDefinition."
        )

    if isinstance(feature, BaseFeatureDefinition):
        # Get a default FeatureReference.
        feature = FeatureReference(feature_definition=feature)

    if feature.override_join_keys:
        override_join_keys = [
            feature_service_pb2.ColumnPair(feature_column=k, spine_column=v)
            for k, v in sorted(feature.override_join_keys.items())
        ]
    else:
        override_join_keys = None

    return feature_service_pb2.FeatureServiceFeaturePackage(
        feature_package_id=feature.id,
        namespace=feature.namespace,
        override_join_keys=override_join_keys,
        features=feature.features if feature.features else None,
    )

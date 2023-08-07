# AUTO-GENERATED FILE. Do not edit. Run chalkpy stubgen to generate.
# fmt: off
# isort: skip_file
from __future__ import annotations

from chalk.features import Features as Features
from chalk.features import Tags as Tags
from chalk.features.feature_set import FeaturesMeta as FeaturesMeta
from chalk.utils.duration import Duration as Duration
from typing import Optional as Optional
from typing import Protocol as Protocol
from typing import Type as Type
from typing import overload as overload

@overload
def features(
    *,
    owner: Optional[str] = ...,
    tags: Optional[Tags] = ...,
    max_staleness: Optional[Duration] = ...,
    etl_offline_to_online: Optional[bool] = ...,
) -> __stubgen__features_proto: ...

class __stubgen__features_proto(Protocol):
    ...

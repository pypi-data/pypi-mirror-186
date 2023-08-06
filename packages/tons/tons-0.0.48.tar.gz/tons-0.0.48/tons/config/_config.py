from enum import Enum
from typing import Any, List, Tuple, Union, Generator

from pydantic import BaseModel

from ._provider import ProviderConfig, DAppConfig
from ._tons import TonsConfig


class ConfigLocation(str, Enum):
    local_location = 'local'
    global_location = 'global'


class Config(BaseModel):
    tons: TonsConfig = TonsConfig()
    provider: ProviderConfig = ProviderConfig()

    class Config:
        use_enum_values = True
        validate_assignment = True

    @classmethod
    def field_names(cls) -> List[str]:
        fields = []
        fields += [f"tons.{field}" for field in list(
            TonsConfig.__fields__)]
        fields += [f"provider.dapp.{field}" for field in list(
            DAppConfig.__fields__)]

        return fields

    def key_value(self, exclude_unset=False) -> Generator[Tuple[str, Any], None, None]:
        for key, val in self.tons.dict(exclude_unset=exclude_unset).items():
            yield f"tons.{key}", val

        for key, val in self.provider.dapp.dict(exclude_unset=exclude_unset).items():
            yield f"provider.dapp.{key}", val

    def get_nondefault_value(self, field: str) -> Union[None, Any]:
        attrs_tree = field.split(".")
        val = self.dict(exclude_unset=True)

        for attr in attrs_tree:
            if attr in val:
                val = val[attr]
            else:
                return None
        return val

    def update_value(self, field: str, value: Any):
        tree = field.split(".")
        field_name = tree[-1]
        attrs = tree[:-1]
        attrs_tree = [self]

        for attr_name in attrs:
            attr = getattr(attrs_tree[-1], attr_name, None)
            attrs_tree.append(attr)

        for idx, attr in enumerate(attrs_tree[::-1], 1):
            setattr(attr, field_name, value)
            value = attr
            if idx <= len(attrs):
                field_name = attrs[-idx]

    def to_nondefault_dict_without_field(self, field: str):
        fields_tree = field.split('.')
        to_exclude = self.__nested_dict({}, fields_tree[:-1], fields_tree[-1])
        return self.dict(exclude_unset=True, exclude=to_exclude)

    def __nested_dict(self, tree, vector, value):
        key = vector[0]
        tree[key] = {value} \
            if len(vector) == 1 \
            else self.__nested_dict(tree[key] if key in tree else {},
                                    vector[1:],
                                    value)
        return tree

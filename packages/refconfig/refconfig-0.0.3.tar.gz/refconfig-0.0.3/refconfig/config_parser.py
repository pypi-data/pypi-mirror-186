import smartdict
import yaml
import json

from refconfig import config_type
from refconfig.config_type import CType


class AtomConfig:
    def __init__(self, config, key=None, t=CType.SMART):
        self.config = config
        self.key = key
        self.t = self.parse_type(t)

        self.value = self.parse_config()

    def parse_type(self, t):
        t = config_type.parse_type(t)

        if t is not CType.SMART:
            return t

        if not isinstance(self.config, str):
            return CType.RAW

        if self.config.endswith('.yaml'):
            return CType.YAML
        if self.config.endswith('.json'):
            return CType.JSON
        return CType.RAW
        # return CType.STRING

    def parse_config(self):
        if self.t is CType.RAW:
            return self.config
        if self.t is CType.JSON:
            return json.load(open(self.config, 'rb+'))
        if self.t is CType.YAML:
            return yaml.safe_load(open(self.config, 'rb+'))
        raise ValueError('Can not identify ConfigType')

    def __str__(self):
        return f'Config({self.key}-{self.t})'


def parse(*configs: AtomConfig):
    kv = dict()

    for config in configs:
        if config.key is None:
            assert len(configs) == 1, ValueError('Too much configs with key = None')
            return smartdict.parse(config.value)
        kv[config.key] = config.value

    return smartdict.parse(kv)


def parse_by_tuple(*configs: tuple):
    return parse(*[AtomConfig(config=config[0], key=config[1], t=config[2]) for config in configs])


class RefConfig:
    def __init__(self):
        self.configs = []

    def add(self, t, __config=None, **configs):
        if __config:
            configs = [(__config, None, t)]
        else:
            configs = [(v, k, t) for k, v in configs.items()]
        configs = [AtomConfig(config=config[0], key=config[1], t=config[2]) for config in configs]
        self.configs.extend(configs)
        return self

    def add_yaml(self, __config: str = None, **configs):
        return self.add(CType.YAML, __config, **configs)

    def add_json(self, __config: str = None, **configs):
        return self.add(CType.JSON, __config, **configs)

    def add_raw(self, __config: str = None, **configs):
        return self.add(CType.RAW, __config, **configs)

    def parse(self):
        return parse(*self.configs)


def parse_with_single_type(t, __config=None, **configs):
    # if __config:
    #     return parse_by_tuple((__config, None, t))
    # return parse_by_tuple(*[(v, k, t) for k, v in configs.items()])
    return RefConfig().add(t, __config, **configs).parse()


def parse_yaml(__config: str = None, **configs):
    return parse_with_single_type(CType.YAML, __config, **configs)


def parse_json(__config: str = None, **configs):
    return parse_with_single_type(CType.JSON, __config, **configs)


def parse_raw(__config: dict = None, **configs):
    return parse_with_single_type(CType.RAW, __config, **configs)

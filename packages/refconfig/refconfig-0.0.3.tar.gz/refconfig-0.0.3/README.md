# RefConfig

Powered by [SmartDict](https://pypi.org/project/smartdict/).

## Usage

- Configure with references

## Install 

`pip install refconfig`

## Description

```yaml
# ./data/zhihu.yaml

dataset: zhihu
store:
  data_dir: data/FANS/${config.dataset}
  save_dir: saving/${config.dataset}/${exp.model}-E${config.model_config.hidden_size}/
model_config:
  hidden_size: 64
  num_hidden_layers: 3
  num_attention_heads: 8
```

```yaml
# ./exp/train.yaml

exp: step-${exp.tasks.0.params.steps}
model: bert
mode: train
freeze_emb: false
tasks:
  -
    name: mlm
    params:
      steps: 5
store:
  interval: 10
policy:
  epoch: 200
```

```python
import refconfig

config = refconfig.parse_yaml(
    exp='./exp/train.yaml',
    config='./data/zhihu.yaml',
)

print(config['config']['store']['data_dir'])  # => data/FANS/zhihu
print(config['config']['store']['save_dir'])  # => saving/zhihu/bert-E64/
print(config['exp']['exp'])  # => step-5

# use with the Oba library to achieve a smoother effect

from oba import Obj

config = Obj(config)
config, exp = config.config, config.exp
print(config.store.data_dir)  # => data/FANS/zhihu
print(config.store.save_dir)  # => saving/zhihu/bert-E64/
print(exp.exp)  # => step-5
```

```yaml
# ./data/any.yaml

store:
  data_dir: data/FANS/${dataset}
  save_dir: saving/${dataset}/${exp.model}-E${config.model_config.hidden_size}/
model_config:
  hidden_size: 64
  num_hidden_layers: 3
  num_attention_heads: 8
```

```python
from refconfig import RefConfig

config = RefConfig().add_yaml(
    exp='./exp/train.yaml',
    config='./data/any.yaml',
).add_raw(
    dataset='youtube',
).parse()

from oba import Obj

config = Obj(config)
config, exp = config.config, config.exp
print(config.store.data_dir)  # => data/FANS/youtube
print(config.store.save_dir)  # => saving/youtube/bert-E64/
print(exp.exp)  # => step-5
```

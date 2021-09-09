import os
import json
from configs import Configs
from templates import config_types as __config_types

CONFIG_PATH = os.path.expanduser('~/.config/bodosdrive/config.json')

if not os.path.exists(CONFIG_PATH):
    from templates import config_defaults as __config_defaults
    conf = Configs(__config_types, __config_defaults)
else:
    conf = Configs(__config_types, json.load(open(CONFIG_PATH)))

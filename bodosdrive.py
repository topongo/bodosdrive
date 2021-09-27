import os.path
import json
from TopongoConfigs.configs import Configs
from templates import config_defaults as __config_defaults

CONFIG_PATH = os.path.expandvars('$HOME/.config/bodosdrive/config.json')

if not os.path.exists(CONFIG_PATH):
    conf = Configs(__config_defaults)
    if not os.path.exists(os.path.dirname(CONFIG_PATH)):
        os.makedirs(os.path.dirname(CONFIG_PATH))
    conf.write(open(CONFIG_PATH, "w+"))
    print("Created config file with default values:")
    conf.write()
else:
    conf = Configs(__config_defaults, config_path=open(CONFIG_PATH))
    conf.write()

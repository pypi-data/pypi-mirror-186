import os as __os
import json as __json
import appdirs as __appdirs

_appname = "websocket_rpcs_tool"
_appauthor = "zyg"
_appdir = __appdirs.user_data_dir(_appname, _appauthor)
_config_path = __os.path.join(_appdir, f"{_appname}.json")

repo_releases = "https://api.github.com/repos/protocolbuffers/protobuf/releases"
use_built_in_protoc = True
ghproxy_proxy = True
ghproxy_url = "https://ghproxy.com"

def _all_config():
    return {k:v for k,v in globals().items() if not k.startswith("_")}

def _save_config():
    with open(_config_path, "w") as file:
        __json.dump(_all_config(), file)

def _load_from_appdir():
    if not __os.path.exists(_appdir):
        __os.makedirs(_appdir)
    if not __os.path.exists(_config_path):
        _save_config()
    else:
        try:
            with open(_config_path, "r") as file:
                config = __json.load(file)
                for k in config:
                    globals()[k] = config[k]
        except:
            _save_config()

_load_from_appdir()
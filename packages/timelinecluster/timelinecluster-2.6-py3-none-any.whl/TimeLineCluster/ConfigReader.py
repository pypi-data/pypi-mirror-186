import os
class ConfigPath:

    root_path_app = os.path.dirname(os.path.abspath(__file__))
    path_util = root_path_app + "/utils/"
    path_js = path_util + "js/"

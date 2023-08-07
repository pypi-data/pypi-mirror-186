from __future__ import print_function
import os
import sys
import json
import subprocess
from Accuinsight.modeler.core.LcConst import LcConst

_BASH_RC_PATH = '/home/notebook/.bashrc'


def get_os_env(env_type='LC', env_path=None, env_file=None):
    _ENV_PREFIX = env_type + '_'

    env_value = {}
    if env_path is None:
        env_path = '/usr'
    if env_file is None:
        env_file = '.accu_env'

    env_file = open(env_path + '/' + env_file, 'r')
    while True:
        line = env_file.readline()
        if not line:
            break

        if _ENV_PREFIX in line:
            key, value = line.split('=')
            if key is not None:
                if _ENV_PREFIX in key:
                    value = value.rstrip()
                    env_value.setdefault(key, value)

    return env_value


def is_in_ipython():
    return 'ipykernel_launcher.py' in sys.argv[0]


def get_current_notebook():
    if is_in_ipython():
        target_path = LcConst.ENV_JUPYTER_WORKSPACE
        # '/home/notebook/.jupyter/lab/workspaces'
        if os.path.isdir(target_path):  # if jupyter lab
            file_lists = list()
            file_name = None
            for (dir_path, dir_names, file_names) in os.walk(target_path):
                for fn in file_names:
                    if not fn.endswith('.swp'):
                        if 'default' in fn:
                            file_name = fn
                            break
                        file_lists.append(fn)

            if not file_name:
                file_name = file_lists[0]

            with open(target_path + '/' + file_name, 'r') as tf:
                strlines = tf.readlines()
                json_file = json.loads(strlines[0])
                return json_file['data']['layout-restorer:data']['main']['current'].split(':')[1]
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", 'ipyparams'])
            import ipyparams
            return ipyparams.notebook_name

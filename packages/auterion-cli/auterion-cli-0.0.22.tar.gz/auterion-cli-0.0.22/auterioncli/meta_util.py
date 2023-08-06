import os.path
from pathlib import Path
import json
import hashlib
import sys
import requests
import time
import re
import pkg_resources
from packaging import version


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_version():
    return pkg_resources.require('auterion-cli')[0].version


class PersistentState:
    def __init__(self):
        user_home = Path.home()
        self.persistent_dir = user_home / ".auterion-cli"

        # make sure the persistent dir exits
        # Older auterion-cli had .auterion-cli as a file. Remove that file if it exists
        if self.persistent_dir.exists() and self.persistent_dir.is_file():
            os.unlink(self.persistent_dir)

        if not self.persistent_dir.exists():
            os.mkdir(self.persistent_dir)

        self._config_path = self.persistent_dir / "persistent.json"

        self._config = {}
        self._load_hash = ''
        if self._config_path.exists():
            with open(self._config_path, 'r') as f:
                contents = f.read()
                try:
                    self._config = json.loads(contents)
                    self._load_hash = hashlib.sha1(contents.encode()).hexdigest()
                except Exception as e:
                    eprint(f"Warning: Config file {str(self._config_path)} seems to be corrupt")
                    eprint(e)

    def get(self, key, default):
        if key in self._config:
            return self._config[key]
        else:
            return default

    def __getitem__(self, key):
        return self.get(key, None)

    def __setitem__(self, key, value):
        self._config[key] = value

    def __delitem__(self, key):
        if key in self._config:
            del self._config[key]

    def persist(self):
        contents = json.dumps(self._config)
        persist_hash = hashlib.sha1(contents.encode()).hexdigest()
        if persist_hash == self._load_hash:
            return

        with open(self._config_path, 'w') as f:
            f.write(contents)


def get_host_device_type():
    device_type_file = '/persistent/mender/device_type'
    if os.path.exists(device_type_file):
        with open(device_type_file, 'r') as f:
            for l in f.readlines():
                m = re.match('^device_type=(.*)$', l)
                return m.group(1)
    return 'unknown'


def get_device_presence(address):
    """Tries to find device at supplied address. Returns tuple (device_found, serial)"""
    device_info_endpoint = f"http://{address}/api/sysinfo/v1.0/device"
    try:
        response = requests.get(device_info_endpoint, timeout=5)
        if response:
            return True, response.json()['uuid']
        else:
            return False, 'Request failed'

    except requests.exceptions.Timeout:
        # There is something there, but times out
        return True, ''

    except:
        return False, 'Request failed'


def check_for_updates(persistent_state):
    last_update_check_time = persistent_state.get('last_update_check_time', 0)
    current_time = time.time()

    # Check for updates at most once a day
    if current_time - last_update_check_time < 24 * 3600:
        return

    persistent_state['last_update_check_time'] = int(current_time)

    print('Checking for updates...')
    res = requests.get('https://pypi.org/pypi/auterion-cli/json')
    if res.ok:
        data = res.json()
        up_version = data.get('info', {}).get('version', None)

        our_version = get_version()
        try:
            if version.parse(up_version) > version.parse(our_version):
                print("  ┌──────────────────────────────────────────────────────────────────────────────────────┐")
                print("  │                                                                                      │")
                print("  │  A new version of auterion-cli is available!   {:>16} -> {:<16}  │".format(
                    our_version, up_version))
                print("  │                                                                                      │")
                print("  │  Run `pip install --upgrade auterion-cli` to upgrade.                                │")
                print("  │                                                                                      │")
                print("  └──────────────────────────────────────────────────────────────────────────────────────┘")
        except version.InvalidVersion:
            eprint("Warning: Could not parse version")

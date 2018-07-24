# -*- coding: utf-8 -*-
"""
Display number of issues in gitlab


Requires:
    requests: python library

Examples:
```
gitlab {
    timeout = 90
    url = "https://gitlab.example.com/api/v4/"
    api_key_path = "/path/to/my/api/key"
    color = '#FF0000'
}
```

"""

import requests
import os


class Py3status:
    api_key_path = "~/.gitlab-token"
    url = "https://gitlab.labs.nic.cz/api/v4/"
    timeout = 60
    color = '#FFFF00'

    def post_config_hook(self):
        with open(os.path.expanduser(self.api_key_path)) as f:
            self.token = f.read().strip()

    def gitlab(self):
        headers = {
            "Private-Token": self.token,
        }
        params = {
            "scope": "assigned-to-me",
            "state": "opened",
        }
        resp = requests.get(f"{self.url}/issues", params=params, headers=headers)
        if resp.status_code != 200:
            raise Exception("Failed to download issues!")

        resp.close()

        return {
            "full_text": f"GL issues #{resp.headers['X-Total']}",
            "cached_until": self.py3.time_in(int(self.timeout)),
            "color": self.color
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)

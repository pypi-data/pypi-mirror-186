"""Update a kubeconfig file."""

import functools
import os
import pathlib
import platform
import sys
import typing
from urllib import parse

import yaml

KUBE_CONFIG_PATH_DEFAULT = '~/.kube/config'


class KubeConfig:
    """Update a kubeconfig file."""

    def __init__(self, context: str, api_url: str, namespace: typing.Optional[str]):
        """Update a kubeconfig file."""
        self.context = context
        self.api_url = api_url
        self.namespace = namespace

        self.config: typing.Dict[str, typing.Any] = {
            "apiVersion": "v1", "kind": "Config",
            "clusters": [], "users": [], "contexts": []}

    @functools.cached_property
    def config_path(self) -> pathlib.Path:
        """Return the path for the best kubeconfig file."""
        # from kubernetes/config/kube_config.py
        kube_config_paths = os.environ.get('KUBECONFIG') or KUBE_CONFIG_PATH_DEFAULT
        kube_config_separator = ';' if platform.system() == 'Windows' else ':'

        locations = [pathlib.Path(location).expanduser() for location
                     in kube_config_paths.split(kube_config_separator)]
        existing_locations = [location for location in locations if location.exists()]

        for location in existing_locations:
            config = yaml.safe_load(location.read_text(encoding='utf8'))
            if any(c['name'] == self.context for c in config.get('contexts', [])):
                return location

        return existing_locations[0] if existing_locations else locations[0]

    @staticmethod
    def _add(items: typing.Any, key: str, name: str, item: typing.Any) -> None:
        """Add a config item to a list, and remove existing duplicates."""
        items[key + 's'] = [i for i in items[key + 's']
                            if i['name'] != name] + [{'name': name, key: item}]

    def try_read_config(self) -> None:
        """Try to read the configuration from disk."""
        if self.config_path.exists():
            self.config = yaml.safe_load(self.config_path.read_text(encoding='utf8'))
        else:
            print(f'Kubeconfig not found: {self.config_path}', file=sys.stderr)

    def update(self, token: str) -> None:
        """Update or recreate the context in the configuration."""
        if context := next((c for c in self.config.get('contexts', [])
                            if c['name'] == self.context), None):
            if self.namespace:
                context['context']['namespace'] = self.namespace
            user = next(u for u in self.config.get('users', [])
                        if u['name'] == context['context']['user'])
            user['user'].clear()
            user['user']['token'] = token
        else:
            nick = parse.urlsplit(self.api_url).netloc.replace('.', '-')
            self._add(self.config, 'cluster', nick, {"server": self.api_url})
            self._add(self.config, 'user', nick, {"token": token})
            context_item = {"cluster": nick, "user": nick}
            if self.namespace:
                context_item['namespace'] = self.namespace
            self._add(self.config, 'context', self.context, context_item)

    def write_config(self) -> None:
        """Write the configuration to disk."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(yaml.safe_dump(self.config), encoding='utf8')

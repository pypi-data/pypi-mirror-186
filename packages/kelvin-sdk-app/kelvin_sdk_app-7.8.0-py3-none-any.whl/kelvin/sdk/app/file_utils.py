"""File utilities."""

from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import inotify.adapters
import yaml

from .mapping_proxy import MappingProxy

IN_CLOSE_WRITE = "IN_CLOSE_WRITE"


def check_file_updated(file_watcher: inotify.adapters.Inotify) -> bool:
    """Provide a file watcher to check the status of without blocking. Returns true if the file has been written and closed."""
    events = file_watcher.event_gen(yield_nones=False, timeout_s=0)  # no block
    events = list(events)
    ret = False
    # if was modified, build new message
    if events:
        for ev in events:
            _, e, _, _ = ev
            if IN_CLOSE_WRITE in e:
                ret = True
    return ret


def inflate_messages_from_key(yaml_file: Path, key: str) -> List[Dict[str, Any]]:
    """Returns inflated messages from a YAML file found under the given key, e.g. app.kelvin.parameters."""
    ret: List[Dict[str, Any]] = [{}]
    with open(yaml_file) as f:
        c = MappingProxy(yaml.safe_load(f))
        ret = c.get(key, {})
    return ret


def watch_file(path: Path) -> inotify.adapters.Inotify:
    file_watcher = inotify.adapters.Inotify()
    file_watcher.add_watch(path.resolve().absolute().as_posix())
    return file_watcher


class YamlFileWatcher:
    def __init__(self, file: Union[Path, str]) -> None:
        self.file_path = Path(file)
        self.watched_file = watch_file(self.file_path)

        self._stat = self._get_stat()
        self._hash = sha256(self.file_path.read_bytes()).digest()

    def check(self) -> bool:
        return check_file_updated(self.watched_file)

    def get_updates(self, key: str) -> List[Dict[str, Any]]:
        return [{**r} for r in inflate_messages_from_key(self.file_path, key)]

    def _get_stat(self) -> Tuple[int, int]:
        """Get file stats."""

        stat = self.file_path.stat()

        return stat.st_mtime_ns, stat.st_size

    def check_stat(self) -> bool:
        """Check for updates by file modification time."""

        stat = self._get_stat()

        if stat != self._stat:
            hash = sha256(self.file_path.read_bytes()).digest()
            if hash == self._hash:
                return False

            self._stat, self._hash = stat, hash

            return True

        return False

    def get_data(self) -> Dict[str, Any]:
        """Get updated data."""

        with self.file_path.open("r") as file:
            return yaml.safe_load(file)

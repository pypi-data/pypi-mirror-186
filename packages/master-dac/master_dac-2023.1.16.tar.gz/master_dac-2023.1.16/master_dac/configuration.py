try:
    from functools import cached_property
except:
    from cached_property import cached_property
import json
import logging
import json
from pathlib import Path
from appdirs import user_config_dir


class Configuration:
    def __init__(self):
        logging.info(f"Reading configuration from {self.path}")
        config = {}
        if self.path.exists():
            with self.path.open("r") as fp:
                config = json.load(fp)
            
        self.courses = set(config.get("courses", []))

    def save(self):
        self.path.parent.mkdir(exist_ok=True, parents=True)
        s = json.dumps({
            "courses": [c for c in self.courses]
        })
        self.path.write_text(s)

    @cached_property
    def path(self) -> Path:
        return Path(user_config_dir("master-dac", "isir")) / "config.json"

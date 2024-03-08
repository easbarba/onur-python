# Onur is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Onur is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Onur. If not, see <https://www.gnu.org/licenses/>.

"""."""

import json
from pathlib import Path
from typing import Dict

from onur.models import project, config
from onur.misc import info
from . import files


class Parse:
    """Parse configuration files."""

    def __init__(self):
        """..."""
        self.config_dir = info.config_dir
        self.files = files.Files()

    def one(self, filepath: Path) -> config.Config:
        """Parse file to a configuration object."""
        with open(str(filepath), "rb") as json_raw:
            data = json.load(json_raw)

        return config.Config(
            filepath.stem,
            {
                key: [self.to_project(projekt) for projekt in value]
                for key, value in data.items()
            },
        )

    def all(self) -> list[config.Config]:
        """Bundle all configuration."""
        configs: list[project.Project] = []

        for config_current in self.files.namespath():
            config_path = self.config_dir.joinpath(config_current)
            configs.append(self.one(config_path))

        return configs

    def to_project(self, projekt: Dict[str, str]) -> project.Project:
        """Return a Project out of dict, branch defaulting to master."""
        return project.Project(
            name=projekt.get("name"),
            url=projekt.get("url"),
            branch=projekt.get("branch", "master"),
        )

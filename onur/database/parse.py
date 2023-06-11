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

from onur.models import project, config
from onur.misc import globals
from . import files

class Parse:
    """Parse configuration files."""

    def __init__(self):
        """..."""
        self.configDir = globals.configDir
        self.files = files.Files()

    def one(self, filepath: Path) -> list[config.Config]:
        """Parse one configuration file."""
        with open(str(filepath), "rb") as rawjson:
            data = json.load(rawjson)

        return config.Config(filepath.stem, [self.parse(proj) for proj in data])

    def all(self) -> list[config.Config]:
        """Parse all configuration files."""
        configs: list[project.Project] = []

        for config_current in self.files.namespath():
            config_path = self.configDir.joinpath(config_current)
            configs.append(self.one(config_path))

        return configs

    def parse(self, projekt: dict[str]) -> project.Project:
        """Return a Project out of dict, branch defaulting to master."""
        return project.Project(
            name=projekt.get("name"),
            url=projekt.get("url"),
            branch=projekt.get("branch", "master"),
        )

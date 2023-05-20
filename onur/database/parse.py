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

from ..models import project


class Parse:
    """Parse configuration files."""

    def __init__(self):
        """..."""

    def one(self, filepath: Path) -> list[project.Project]:
        """Parse one configuration file."""
        with open(str(filepath), "rb") as rawjson:
            data = json.load(rawjson)

        return [self.parse(pj) for pj in data]

    def parse(self, pj: dict[str]) -> project.Project:
        """Return a Project out of dict, branch defaulting to master."""
        return project.Project(
            name=pj["name"], url=pj["url"], branch=pj.get("branch", "master")
        )

    # def all(self):
    # """Parse all configuration files."""

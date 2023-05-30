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

from pathlib import Path

from onur.misc import globals


class Files:
    """Farming of files."""

    def __init__(self):
        """.."""
        self.configDir: Path = globals.configDir

    def names(self) -> list[str]:
        """."""
        return [
            item.name for item in list(self.configDir.glob("*.json")) if item.exists()
        ]

    def namespath(self) -> list[str]:
        """."""
        return [
            self.configDir.joinpath(item.name)
            for item in list(self.configDir.glob("*.json"))
        ]

    def count(self) -> int:
        """."""
        return len(list(self.configDir.glob("*.json")))

    def exists(self) -> bool:
        """."""
        return self.configDir.exists()

    def path(self) -> str:
        """."""
        return str(self.configDir)

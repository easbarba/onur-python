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

from onur.misc import info, log


class Files:
    """Farming of configuration files."""

    def __init__(self):
        """.."""
        self.config_dir: Path = info.config_dir

    def names(self) -> list[str]:
        """Name of all configuration files found."""
        return [item.name for item in self.valid()]

    def valid(self) -> list[str]:
        """Name of all acceptable files."""
        extension = "json"
        result = []

        for files in self.config_dir.glob(f"*.{extension}"):
            if files.exists():
                result.append(files)
            else:
                log.error(f"suspicious file ignored: {files}")

        return list(result)

    def namespath(self) -> list[str]:
        """File name with path."""
        return [self.config_dir.joinpath(item.name) for item in self.valid()]

    def count(self) -> int:
        """Count of all files."""
        return len(self.valid())

    def exists(self) -> bool:
        """Check if Configuration folder exist."""
        return self.config_dir.exists()

    def path(self) -> str:
        """Configurtion folder path as string."""
        return str(self.config_dir)

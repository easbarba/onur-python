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

from pathlib import Path

from onur.models import project

from git import Repo


class Klone:
    """Clone repository."""

    def __init__(self, filepath: Path, project: project.Project, options: list[str]):
        """..."""
        self.project = project
        self.filepath = filepath
        self.options = options

    def run(self) -> None:
        """..."""
        opts = self.options.append(f"--branch={self.project.branch}")
        Repo.clone_from(url=self.project.url, to_path=self.filepath, multi_options=opts)

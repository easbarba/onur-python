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

from onur.database import parse
from onur.misc import globals
from onur.models import project
from onur.misc import settings

from git import Repo


class Grab:
    """..."""

    def __init__(self, verbose: bool):
        """..."""
        self.all = parse.Parse().all()
        self.projectsDir = globals.projectsDir
        self.values = settings.values()
        self.verbose = verbose

    def run(self) -> None:
        """..."""
        if self.verbose:
            print(f"options: {self.__options()}\n")

        for config in self.all:
            print(f"\n ❯ {config.topic}\n")

            for projekt in config.projects:
                self.__print_info(projekt)
                filepath = Path(self.projectsDir.joinpath(config.topic, projekt.name))
                if self.__checkrepo(filepath):
                    self.pull(filepath)
                else:
                    self.klone(filepath, projekt)

    def pull(self, filepath: Path) -> None:
        """..."""
        o = Repo(filepath).remotes.origin
        o.pull()

    def klone(self, filepath: Path, project: project.Project) -> None:
        """..."""
        options = self.__options().append(f"--branch={project.branch}")
        Repo.clone_from(url=project.url, to_path=filepath, multi_options=options)

    def __checkrepo(self, filepath: Path) -> bool:
        """."""
        return filepath.joinpath(".git", "config").exists()

    def __print_info(self, projekt: dict[str]) -> None:
        """."""
        print(f"name: {projekt.name}")

        if self.verbose:
            print(f"url: {projekt.url}")
            print(f"branch: {projekt.branch}\n")

    def __options(self) -> list[str]:
        """.."""
        options: list[str] = []

        if self.values.get("quiet") and self.values.get("quiet") is False:
            options.append("--progress")

        if self.values.get("depth"):
            options.append(f"--depth={self.values.get('depth')}")

        if self.values.get("single-branch") and self.values.get("quiet") is True:
            options.append("--singlebranch")

        return options

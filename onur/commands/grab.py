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

from termcolor import colored

from onur.database import parse
from onur.misc import info
from onur.misc import settings
from onur.actions import klone, pull


class Grab:
    """..."""

    def __init__(self, verbose: bool):
        """..."""
        self.all = parse.Parse().all()
        self.projects_dir = info.projects_dir
        self.settings = settings.values()
        self.verbose = verbose

    def run(self) -> None:
        """..."""
        for config in self.all:
            print(
                f"""-- {colored(config.topic.capitalize(), 'cyan')}
"""
            )

            for key, projects in config.projects.items():
                for projekt in projects:
                    filepath = Path(self.projects_dir.joinpath(config.topic))
                    if len(config.projects.keys()) > 1:
                        filepath = filepath.joinpath(key)

                    filepath = filepath.joinpath(projekt.name)

                    print(self.__info(projekt, filepath))

                    if self.__repo_exists(filepath):
                        pull.Pull(filepath).run()
                    else:
                        klone.Klone(filepath, projekt, self.__options()).run()

    def __repo_exists(self, filepath: Path) -> bool:
        """."""
        return filepath.joinpath(".git", "config").exists()

    def __info(self, projekt: dict[str], folder: str) -> str:
        """Collect running project information."""
        if self.verbose:
            return f"""{colored('name', 'yellow')}: {projekt.name}
{colored('url', 'yellow')}: {projekt.url}
{colored('branch', 'yellow')}: {projekt.branch}
{colored('folder', 'yellow')}: {folder}
"""

        return f"{projekt.name} - {projekt.url} - {projekt.branch} - {folder}"

    def __options(self) -> list[str]:
        """.."""
        options: list[str] = []

        if self.settings.get("quiet") and self.settings.get("quiet") is False:
            options.append("--progress")

        if self.settings.get("depth"):
            options.append(f"--depth={self.settings.get('depth')}")

        if self.settings.get("single-branch") and self.settings.get("quiet") is True:
            options.append("--single-branch")

        return options

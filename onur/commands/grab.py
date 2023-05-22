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

from ..database import parse
from ..misc import globals
from ..models import project

from git import Repo


class Grab:
    """..."""

    def __init__(self):
        """..."""
        self.all = parse.Parse().all()
        self.projectsDir = globals.projectsDir

    def run(self) -> None:
        """..."""
        for cfg in self.all:
            print(f"\n  topic: {cfg.topic}\n")
            for proj in cfg.projects:
                self.print_info(proj)
                filepath = Path(self.projectsDir.joinpath(cfg.topic, proj.name))
                if self.checkrepo(filepath):
                    self.pull(filepath)
                else:
                    self.klone(filepath, proj)

    def pull(self, filepath: Path) -> None:
        """..."""
        o = Repo(filepath).remotes.origin
        o.pull()

    def klone(self, filepath: Path, project: project.Project) -> None:
        """..."""
        Repo.clone_from(
            url=project.url,
            to_path=filepath,
            multi_options=[
                f"--branch={project.branch}",
                "--depth=1",
                "--single-branch",
            ],
        )

    def checkrepo(self, filepath: Path) -> bool:
        """."""
        return filepath.joinpath(".git", "config").exists()

    def print_info(self, proj: dict[str]) -> None:
        """."""
        print(f"name: {proj.name}")
        print(f"url: {proj.url}")
        print(f"branch: {proj.branch}\n")

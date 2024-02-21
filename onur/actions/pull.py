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

"""..."""


from pathlib import Path

from git import Repo


class Pull:
    """Pull update from repository."""

    def __init__(self, filepath: Path):
        """..."""
        self.repopath = filepath

    def run(self) -> None:
        """..."""
        repo = Repo(self.repopath)
        repo.git.reset(hard=True)
        o = repo.remotes.origin
        o.pull(rebase=True)

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

"""Main class."""

import argparse

from .commands import grab


# ================================= CLI
def cli():
    """Provide cli interface."""
    parser = argparse.ArgumentParser(
        prog="Onur", description="Easily manage multiple FLOSS repositories."
    )
    # parser.add_argument("-g", "--grab", help="grab all projects", action="store_true")
    # parser.add_argument("-a", "--archive", help="archive projects", action="store_true")
    parser.add_argument(
        "-i", "--verbose", help="provide additional information", action="store_true"
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.4")

    return parser.parse_args()


def run() -> None:
    """..."""
    grab.Grab(cli().verbose).run()


if __name__ == "__main__":
    run()

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


def welcome() -> str:
    """Say something."""
    return "Hello, World!"


# ================================= CLI
def cli():
    """."""
    parser = argparse.ArgumentParser(
        prog="Gota", description="Packages installation made easy!"
    )
    parser.add_argument("-g", "--grab", help="grab all projects", action="store_true")
    parser.add_argument("-a", "--archive", help="archive projects", action="store_true")
    parser.add_argument(
        "-i", "--verbose", help="provide additional information", action="store_true"
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1")
    args = parser.parse_args()

    if args.archive:
        print("Archiving")
    elif args.grab:
        print("Grabbing")
    else:
        parser.print_help()
        exit(1)

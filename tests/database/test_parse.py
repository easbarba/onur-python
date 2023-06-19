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

from onur.misc import info

from onur.database import parse


p = parse.Parse()


def test_one_config():
    config = info.config_dir.joinpath("etc.json").resolve()
    assert p.one(config).projects[0].name == "guzzle"


def test_all_config():
    assert p.all()[0].topic == "misc"
    assert p.all()[0].projects[0].name == "awesomewm"

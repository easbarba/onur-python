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

from onur.database import files


f = files.Files()


def test_names():
    assert sorted(f.names()) == ["etc.json", "misc.json"]


def test_namespath():
    assert str(sorted(f.namespath())[0]) == '/root/.config/onur/etc.json'


def test_count():
    assert f.count() == 2


def test_exists():
    assert f.exists()


def test_path():
    assert f.path() == "/root/.config/onur"

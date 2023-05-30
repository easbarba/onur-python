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


from onur.misc import settings


def test_singlebranch() -> None:
    """Single branch?."""
    assert settings.values().get("single-branch") is True


def test_quite_noisy() -> None:
    """I like it noisy!."""
    assert settings.values().get("quiet") is False


def test_depth() -> None:
    """And its depth?."""
    assert settings.values().get("depth") == 3

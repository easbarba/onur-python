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

# DEPENDENCIES: podman, gawk, fzf.

.DEFAULT_GOAL := tests

RUNNER ?= podman

NAME := onur
VERSION := $(shell gawk '/version/ {version=substr($$3, 2,5); print version}' pyproject.toml )
IMAGE_NAME := registry.gitlab.com/${USER}/${NAME}:${VERSION}

.phony: repl
repl:
	${RUNNER} run --rm -it \
		--volume ${PWD}:/app:Z \
		--workdir /app \
		${IMAGE_NAME} bash

.phony: prfix
prfix:
	${RUNNER} run --rm -it \
		--volume ${PWD}:/app:Z \
		--workdir /app \
		${IMAGE_NAME} bash -c './prfix.bash'

.phony: grab
grab:
	python3 -m onur --grab

.phony: install
install:
	python3 -m pip install . --break-system-packages

.phony: uninstall
uninstall:
	python3 -m pip uninstall onur --break-system-packages

.phony: command
command:
	${RUNNER} run --rm -it \
		--volume ${PWD}:/app:Z \
		--workdir /app \
		${IMAGE_NAME} bash -c '$(shell cat commands | fzf)'

.phony: image.build
image.build:
	${RUNNER} build --file ./Containerfile --tag ${IMAGE_NAME}

.PHONY: image.publish
image.publish:
	${RUNNER} push ${IMAGE_NAME}

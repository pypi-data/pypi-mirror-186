#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Libpsl(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "libpsl",
            version="0.21.2",
            archive_url="https://github.com/rockdaboot/libpsl/releases/download/{version}/libpsl-{version}.tar.gz",
            hash="e35991b6e17001afa2c0ca3b10c357650602b92596209b7492802f3768a6285f",
            dependencies=[
                "meson",
                "ninja",
                "pkgconf",
                "icu",
            ],
            patches=["0001-localtime_r.patch"],
        )

        self.add_param("-Druntime=libicu")
        self.add_param("-Dbuiltin=true")

    def build(self):
        Meson.build(self)

        self.install(r".\LICENSE share\doc\libpsl")

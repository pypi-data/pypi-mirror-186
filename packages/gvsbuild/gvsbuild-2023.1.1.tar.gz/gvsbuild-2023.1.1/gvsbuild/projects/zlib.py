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

from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Zlib(Tarball, Project):
    def __init__(self):
        Project.__init__(
            self,
            "zlib",
            version="1.2.13",
            archive_url="https://github.com/madler/zlib/releases/download/v{version}/zlib-{version}.tar.xz",
            hash="d14c38e313afc35a9a8760dadf26042f51ea0f5d154b0630a31da0540107fb98",
        )

    def build(self):
        options = ""
        if self.builder.opts.configuration == "debug":
            options = 'CFLAGS="-nologo -MDd -W3 -Od -Zi -Fd\\"zlib\\""'

        self.exec_vs(
            r"nmake /nologo /f win32\Makefile.msc STATICLIB=zlib-static.lib IMPLIB=zlib1.lib "
            + options
        )

        self.install(r".\zlib.h .\zconf.h include")
        self.install(r".\zlib1.dll .\zlib1.pdb bin")
        self.install(r".\zlib1.lib lib")

        self.install_pc_files()
        self.install(r".\README share\doc\zlib")

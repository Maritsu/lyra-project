# ============================================================================ #
#
# Copyright (C) 2023 Maritsu
#
# This file is part of lyra. lyra is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# lyra is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# lyra. If not, see <https://www.gnu.org/licenses/>.
#
# ============================================================================ #

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QWidget

def getFileLoader(filename:str) -> QWidget:
    filename = f"src/ui/{filename}.ui"
    f = QFile(filename)
    if not f.open(QIODevice.OpenModeFlag.ReadOnly):
        print(f"Cannot open {filename}: {f.errorString()}")
        return QWidget()
    loader = QUiLoader()
    widget = loader.load(f, None)
    f.close()
    if not widget:
        print(loader.errorString())
    return widget

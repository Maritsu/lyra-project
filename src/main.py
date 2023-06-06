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

import sys
import librus as api
import ui.mainwindow as mw

if __name__ == '__main__':
    print('jan ale o toki!')
    app = mw.QtWidgets.QApplication([])
    print('your mother')
    widget = mw.MainWindow()
    widget.show()

    sys.exit(app.exec())

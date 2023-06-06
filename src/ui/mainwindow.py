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

from PySide6 import QtCore, QtWidgets, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.fcbarcelona=0
        somelabel = QtWidgets.QLabel("mi unpa e mama sina",alignment=QtCore.Qt.AlignCenter)
        self.fuckcount = QtWidgets.QLabel(f"count:{self.fcbarcelona}",alignment=QtCore.Qt.AlignCenter)
        layout = QtWidgets.QVBoxLayout(self)
        btn = QtWidgets.QPushButton("o unpa e ona!!")
        layout.addWidget(somelabel)
        layout.addWidget(self.fuckcount)
        layout.addWidget(btn)

        btn.clicked.connect(self.fuc)

        self.setLayout(layout)

    @QtCore.Slot()
    def fuc(self):
        print("*mi o unpa e mama sina*")
        self.fcbarcelona+=1
        self.fuckcount.setText(f"count:{self.fcbarcelona}")


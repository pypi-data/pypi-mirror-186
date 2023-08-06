#! /usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2020 AlexPDev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Widgets and procedures for the "Torrent Editor" tab."""

import os
from copy import deepcopy

import pyben
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QToolBar, QVBoxLayout,
                               QWidget)

from torrentfileQt.utils import browse_torrent, get_icon


class EditorWidget(QWidget):
    """Main widget for the torrent editor tab."""

    def __init__(self, parent=None):
        """
        Construct editor tab widget.

        Parameters
        ----------
        parent : QWidget
            parent widget of this widge.
        """
        super().__init__(parent=parent)
        self.window = parent.window
        self.counter = 0
        self.layout = QVBoxLayout()
        self.line = QLineEdit(parent=self)
        self.line.setProperty("editLine", "true")
        self.setProperty("editWidget", "true")
        self.button = Button("Save", parent=self)
        self.fileButton = FileButton(parent=self)
        self.label = QLabel("Torrent File Editor", parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.table = Table(parent=self)
        self.hlayout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.hlayout.addWidget(self.line)
        self.hlayout.addWidget(self.fileButton)
        self.layout.addLayout(self.hlayout)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button)
        self.layout.setObjectName("Editor_layout")
        self.line.setObjectName("Editor_line")
        self.button.setObjectName("Editor_button")
        self.fileButton.setObjectName("Editor_fileButton")
        self.label.setObjectName("Editor_label")
        self.table.setObjectName("Editor_table")
        self.setLayout(self.layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """Drag enter event for widget."""
        if event.mimeData().hasUrls:
            self.counter += 1
            event.accept()
            return True
        self.counter -= 1
        return event.ignore()

    def dragMoveEvent(self, event):
        """Drag Move Event for widgit."""
        if event.mimeData().hasUrls:
            self.counter -= 1
            event.accept()
            return True
        self.counter += 1
        return event.ignore()

    def dropEvent(self, event) -> bool:
        """Drag drop event for widgit."""
        urls = event.mimeData().urls()
        path = urls[0].toLocalFile()
        if os.path.exists(path):
            self.table.clear()
            self.line.setText(path)
            self.table.handleTorrent.emit(path)
            return True
        return False


class Button(QPushButton):
    """Button Widget for saving results to .torrent file."""

    def __init__(self, text: str, parent=None):
        """Construct for the save button on torrent editor tab."""
        super().__init__(text, parent=parent)
        self.widget = parent
        self.clicked.connect(self.save)

    def save(self):
        """Save method for writing edit results to .torrent file."""
        table = self.widget.table
        text = self.widget.line.text()
        meta = table.original
        info = meta["info"]
        for row in range(table.rowCount()):
            label = table.item(row, 0).text()
            if label in ["url-list", "httpseeds", "announce-list"]:
                widget = table.cellWidget(row, 1)
                combo = widget.combo
                value = []
                for i in range(combo.count()):
                    txt = combo.itemText(i).strip(" ")
                    if txt:
                        value.append(txt)
                if label == "announce-list":
                    value = [value]
            else:
                value = table.item(row, 1).text().strip(" ")
            if not value:
                continue
            if label in ["piece length", "private", "creation date"]:
                value = int(value)
            if label in meta and meta[label] != value:
                meta[label] = value
            elif label in info and info[label] != value:
                info[label] = value  # pragma: no cover
        pyben.dump(meta, text)
        self.window.statusBar().showMessage("File Saved")


class FileButton(QPushButton):
    """Tool Button for selecting a .torrent file to edit."""

    def __init__(self, parent=None):
        """Construct for the FileDialog button on Torrent Editor tab."""
        super().__init__(parent=parent)
        self.setProperty("editFileButton", "true")
        self.widget = parent
        self.setIcon(QIcon(get_icon("browse_file")))
        self.setText("File")
        self.window = parent.window
        self.clicked.connect(self.browse)

    def browse(self, paths: list = None):
        """Browse method for finding the .torrent file user wishes to edit."""
        paths = browse_torrent(self, paths)
        self.widget.table.clear()
        self.widget.line.setText(paths[0])
        self.widget.table.handleTorrent.emit(paths[0])


class AddItemButton(QAction):
    """Button for editing adjacent ComboBox."""

    def __init__(self, parent):
        """Construct the Button."""
        super().__init__(parent)
        self.setProperty("editButton", "true")
        self.parent = parent
        self.box = None
        self.triggered.connect(self.add_item)

    def add_item(self):
        """Take action when button is pressed."""
        items = [self.box.itemText(i) for i in range(self.box.count())]
        current = self.box.currentText().strip(" ")
        if current and current not in items:
            self.box.insertItem(0, current, 2)
        self.box.insertItem(0, "", 2)
        self.box.setCurrentIndex(0)
        self.parent.line_edit.setReadOnly(True)


class RemoveItemButton(QAction):
    """Button for editing adjacent ComboBox."""

    def __init__(self, parent):
        """Construct the Button."""
        super().__init__(parent)
        self.setProperty("editButton", "true")
        self.parent = parent
        self.box = None
        self.triggered.connect(self.remove_item)

    def remove_item(self):
        """Take action when button is pressed."""
        index = self.box.currentIndex()
        self.box.removeItem(index)
        self.parent.line_edit.setReadOnly(True)


class Table(QTableWidget):
    """Table widget for displaying editable information from .torrent file."""

    handleTorrent = Signal(str)

    def __init__(self, parent=None):
        """Construct for the Table Widget on torrent editor tab."""
        super().__init__(parent=parent)
        self.info = {}
        self.window = parent.window
        self.original = None
        self.setColumnCount(2)
        self.setRowCount(0)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        vheader = self.verticalHeader()
        vheader.setSectionResizeMode(vheader.ResizeMode.Stretch)
        vheader.setHidden(True)
        self.handleTorrent.connect(self.export_data)

    def clear(self):
        """Remove any data previously added to table."""
        self.info = {}
        for row in range(self.rowCount()):
            self.removeRow(row)
        self.setRowCount(0)
        super().clear()
        self.setHorizontalHeaderLabels(["Label", "Value"])

    def export_data(self, path):
        """Export slot for the handleTorrent signal."""
        if not os.path.exists(path):  # pragma: no cover
            return
        data = pyben.load(path)
        self.original = deepcopy(data)
        self.flatten_data(data)
        counter = 0
        for k, v in sorted(self.info.items()):
            self.window.app.processEvents()
            self.setRowCount(self.rowCount() + 1)
            item = QTableWidgetItem(0)
            item.setText(str(k))
            item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            self.setItem(counter, 0, item)
            if k in ["announce-list", "url-list", "httpseeds"]:
                widget = ToolBar(parent=self)
                self.setCellWidget(counter, 1, widget)
                widget.set_values(k, v)
            else:
                item2 = QTableWidgetItem(0)
                item2.setText(str(v))
                self.setItem(counter, 1, item2)
            counter += 1

    def flatten_data(self, data):
        """Flatten the meta dictionary found in the selected .torrent file."""
        fields = [
            "source",
            "private",
            "announce",
            "name",
            "comment",
            "creation date",
            "created by",
            "announce-list",
            "url-list",
            "httpseeds",
        ]
        info = data["info"]
        del data["info"]
        data.update(info)
        for field in fields:
            if field not in data:
                self.info[field] = ""
            else:
                self.info[field] = data[field]


class Combo(QComboBox):
    """A Combo Box widget for inside table cells."""

    def __init__(self, parent=None):
        """Construct a combobox for table widget cell."""
        super().__init__(parent=parent)
        self.widget = parent
        self.sizePolicy().setVerticalPolicy(QSizePolicy.Minimum)
        self.setMinimumContentsLength(48)
        self.sizePolicy().setHorizontalPolicy(QSizePolicy.Minimum)
        self.setInsertPolicy(self.InsertPolicy.InsertAtBottom)
        self.setDuplicatesEnabled(False)
        self.widget.line_edit.setReadOnly(True)

    def focusOutEvent(self, _):  # pragma: nocover
        """Add item when focus changes."""
        super().focusOutEvent(_)
        current = self.currentText().strip()
        items = [self.itemText(i) for i in range(self.count())]
        blanks = [i for i in range(len(items)) if not items[i].strip()]
        list(map(self.removeItem, blanks[::-1]))
        if current and current not in items:
            self.insertItem(0, current, 2)
        self.widget.line_edit.setReadOnly(True)

    def focusInEvent(self, _):  # pragma: nocover
        """Make line edit widget active when clicking in to box."""
        super().focusInEvent(_)
        self.widget.line_edit.setReadOnly(False)


class ToolBar(QToolBar):
    """Toolbar for the combobox and buttons."""

    def __init__(self, parent=None):
        """Construct the toolbar instance."""
        super().__init__(parent=parent)
        self.setProperty("editToolBar", "true")
        self.sizePolicy().setHorizontalPolicy(QSizePolicy.Minimum)
        self.setMinimumWidth(800)
        self.line_edit = QLineEdit(parent=self)
        self.combo = Combo(self)
        self.combo.setLineEdit(self.line_edit)
        self.add_button = AddItemButton(self)
        addIcon = QIcon(get_icon("plus"))
        self.add_button.setIcon(addIcon)
        self.add_button.box = self.combo
        self.remove_button = RemoveItemButton(self)
        removeIcon = QIcon(get_icon("minus"))
        self.remove_button.setIcon(removeIcon)
        self.remove_button.box = self.combo
        self.addWidget(self.combo)
        self.addActions([self.add_button, self.remove_button])

    def set_values(self, key, val):
        """Fill in the values of pre-set urls for each list."""
        if val and isinstance(val, list):
            if key == "announce-list":
                lst = [k for j in val for k in j]
            else:
                lst = val
            for url in lst:
                self.combo.addItem(url, 2)

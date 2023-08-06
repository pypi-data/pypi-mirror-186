#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: HSPyLib
   @package: clitt.core.tui.table
      @file: table_renderer.py
   @created: Tue, 4 May 2021
    @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior"
      @site: https://github.com/yorevs/hspylib
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright 2022, HSPyLib team
"""

from abc import ABC
from typing import List

from hspylib.core.preconditions import check_argument
from hspylib.core.tools.commons import sysout
from hspylib.core.tools.text_tools import elide_text, justified_center, justified_left, justified_right


class TableRenderer:
    """TODO"""

    # pylint: disable=too-few-public-methods
    class TextAlignment(ABC):
        """
        Table cell text justification helper.
        """

        # fmt: off
        LEFT    = justified_left
        CENTER  = justified_center
        RIGHT   = justified_right
        # fmt: on

    def __init__(self, headers: List[str], data: iter, caption: str | None = None):
        """
        :param headers: table headers to be displayed.
        :param data: table record set with the selected rows.
        :param caption: table caption to be displayed.
        """

        self.headers = headers
        self.rows = data if data else []
        self.caption = caption
        self.header_alignment = TableRenderer.TextAlignment.CENTER
        self.cell_alignment = TableRenderer.TextAlignment.LEFT
        self.min_cell_size = 6
        if self.rows:
            check_argument(
                len(min(self.rows, key=len)) == len(self.headers),
                "Headers and Columns must have the same size: {} vs {}",
                len(min(self.rows, key=len)),
                len(self.headers),
            )
        self.column_sizes = [max(self.min_cell_size, len(header)) for header in self.headers]
        self.indexes = range(len(self.column_sizes))

    def set_header_alignment(self, alignment: TextAlignment) -> None:
        """Set table headers alignment.
        :param alignment: table header text alignment function.
        :return:
        """
        self.header_alignment = alignment

    def set_cell_alignment(self, alignment: TextAlignment) -> None:
        """Set table cell alignment.
        :param alignment: table cell text alignment function.
        :return:
        """
        self.cell_alignment = alignment

    def set_min_cell_size(self, size: int) -> None:
        """Set the minimum length of a cell.
        :param size: minimum table cell size.
        :return:
        """
        self.min_cell_size = size

    def adjust_cells_by_largest(self) -> None:
        """Adjust cell sizes based on the maximum length of a cell.
        :return: None
        """
        for row in self.rows:
            for idx, _ in enumerate(row):
                self.column_sizes[idx] = max(self.column_sizes[idx], len(str(row[idx])))

    def set_fixed_cell_size(self, size: int) -> None:
        """Adjust cell sizes to a fixed size.
        :param size: the fixed cell size.
        :return: None
        """
        for row in self.rows:
            for idx in range(0, len(row)):
                self.column_sizes[idx] = max(size, self.min_cell_size)

    def set_cell_sizes(self, cell_sizes: List[int]) -> None:
        """Render table based on a list of fixed sizes.
        :param cell_sizes: TODO
        :return: None
        """
        check_argument(
            len(min(self.rows, key=len)) == len(cell_sizes),
            "Sizes and Columns must have the same size: {} vs {}",
            len(min(self.rows, key=len)),
            len(cell_sizes),
        )
        for row in self.rows:
            for idx in range(0, len(row)):
                self.column_sizes[idx] = max(cell_sizes[idx], self.min_cell_size)

    def render(self) -> None:
        """Render table based on the maximum size of a column header.
        :return: None
        """
        header_cols, data_cols = self._join_header_columns(), self._join_data_columns()
        table_borders = "+" + "".join((("-" * (self.column_sizes[idx] + 2) + "+") for idx in self.indexes))
        self._print_table(table_borders, header_cols, data_cols)

    def _join_header_columns(self) -> list:
        """TODO"""
        # fmt: off
        return [
            "| " + " | ".join(
                [self.header_alignment(self._header_text(idx), self.column_sizes[idx]) for idx in self.indexes]
            ) + " |"
        ]
        # fmt: on

    def _join_data_columns(self) -> list:
        """TODO"""
        # fmt: off
        return [
            "| " + "".join(
                f"{self.cell_alignment(self._cell_text(row, idx), self.column_sizes[idx])} | " for idx in self.indexes
            )
            for row in self.rows
        ]
        # fmt: on

    def _header_text(self, idx: int) -> str:
        """TODO"""
        return elide_text(self.headers[idx], self._cell_size(idx))

    def _cell_text(self, row: tuple, idx: int) -> str:
        """TODO"""
        return elide_text(str(row[idx]), self._cell_size(idx))

    def _cell_size(self, idx: int) -> int:
        """TODO"""
        return self.column_sizes[idx]

    def _print_table(self, table_line: str, header_cols: List[str], data_cols: List[str]) -> None:
        """TODO"""

        sysout(table_line.replace("+", "-"))
        if self.caption:
            sysout(
                "| " + elide_text(self.caption, len(table_line) - 4).center(len(header_cols[0]) - 4, " ") + " |",
            )
            sysout(f"|{table_line[1:-1]}|")
        sysout("%EOL%".join(header_cols))
        sysout(f"|{table_line[1:-1]}|")
        sysout(
            "%EOL%".join(data_cols) if data_cols else "| " + "<empty>".center(len(table_line) - 4, " ") + " |"
        )
        sysout(table_line.replace("+", "-"))

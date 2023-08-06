from __future__ import annotations

import re
from typing import Dict, List, Union

import numpy as np
import pandas as pd


def get_column_number(column_name: str) -> int:
    """
    Returns the 0-indexed column number from an A1 formatted column name.

    Args:
        column_name (str): An Spreadsheet-like column name ('a', 'A', 'AA').

    Returns:
        (int): The equivalent 0-indexed column number.
    """
    # Init
    place = 0
    number = 0
    column_name = column_name.upper()

    # 'A' -> 1, 'AA' -> 26*(1) + 1 = 27
    for letter in reversed(column_name):
        number += (ord(letter) - ord('A') + 1) * (26 ** place)
        place += 1

    # Decreases 1, so that 'A' == 0, 'AA' == 26
    return number - 1


def get_column_name(column_number: int) -> str:
    """
    Returns the A1 formatted column name from a 0-index column number.

    Args:
        column_number (int): The 0-indexed column number.

    Returns:
        str: The A1 formatted column index ('A', 'AA').
    """
    # Do
    name = chr(65 + column_number % 26)
    column_number //= 26

    # While
    while column_number > 0:
        name = chr(65 + (column_number - 1) % 26) + name
        column_number //= 26

    return name


def parse_range(range_: str) -> Dict:
    """
    Extracts information about an A1 Format range, and returns it as a dict.

    The dict keys are 'start_row', 'start_column', 'end_row' and 'end_column'.

    Args:
        range_ (str): The range (minus the sheet) to be retrieved, in a A1 format. Example: 'A1:B2', 'B', '3', 'A1'.

    Returns:
        (Dict) A dict containing the information about the range.
    """
    # Special Case: Empty Range
    if range_ is None or range_ == '':
        return {
            'start_column': None,
            'end_column': None,
            'start_row': None,
            'end_row': None
        }

    # Checks if a valid range was provided
    if not re.match('\\A[a-zA-Z]*\\d*:?[a-zA-Z]*\\d*\\Z', range_):
        raise ValueError('Invalid Range')

    # 'A' -> 'A:A'
    if range_.count(':') == 0:
        range_ = range_ + ':' + range_

    # Extract information from the range
    start, end = range_.split(':')
    start_column = re.search('([a-zA-Z]+)', start)
    start_row = re.search('(\\d+)', start)
    end_column = re.search('([a-zA-Z]+)', end)
    end_row = re.search('(\\d+)', end)

    # Returns the
    return {
        'start_column': get_column_number(start_column.group(0)) if start_column else None,
        'end_column': get_column_number(end_column.group(0)) + 1 if end_column else None,
        'start_row': int(start_row.group(0)) - 1 if start_row else None,
        'end_row': int(end_row.group(0)) if end_row else None
    }


class BotExcelPlugin:
    def __init__(self, active_sheet: str = None) -> None:
        """
        This class stores the data in a Excel-like (sheets) format.

        This plugin supports multiple sheets into a object of this class. To access sheets other than the first,
        either pass the sheet index or name, or change the default sheet this class will point to with the
        set_active_sheet() method.

        Args:
            active_sheet (str, Optional): The name of the sheet this class will be created with. Defaults to 'sheet1'.

        Attributes:
            active_sheet (str, Optional): The default sheet this class's methods will work with. Defaults to 'sheet1'.
        """
        self.active_sheet = active_sheet
        self._sheets = {active_sheet: pd.DataFrame()}

    def active_sheet(self) -> str:
        return self.active_sheet

    def set_active_sheet(self, sheet: str = None) -> BotExcelPlugin:
        self.active_sheet = next(iter(self._sheets.keys())) if sheet is None else sheet
        return self

    def rename_sheet(self, new_name: str, sheet: str) -> BotExcelPlugin:
        """
        Renames a sheet.

        Keep in mind that in doing so the new sheet will be reordered to the last position.

        Args:
            new_name (str): The sheet will be renamed to this.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[new_name] = self._sheets.pop(sheet)
        return self

    def create_sheet(self, sheet: str) -> BotExcelPlugin:
        """
        Creates a new sheet.

        Args:
            sheet (str): The new sheet's name.

        Returns:
            self (allows Method Chaining)
        """
        self._sheets[sheet] = pd.DataFrame()
        return self

    def remove_sheet(self, sheet: str) -> BotExcelPlugin:
        """
        Removes a sheet.

        Keep in mind that if you remove the active_sheet, you must set another sheet as active before using trying to
            modify it!

        Args:
            sheet (str): The sheet's name.

        Returns:
            self (allows Method Chaining)
        """
        self._sheets.pop(sheet)
        return self

    def list_sheets(self) -> List[str]:
        """
        Returns a list with the name of all the sheets in this spreadsheet.

        Returns:
            List[str]: A list of sheet names.
        """
        return list(self._sheets.keys())

    def get_range(self, range_: str, sheet: str = None) -> List[List[object]]:
        """
        Returns the values of all cells within an area of the sheet in a list of list format.

        Args:
            range_ (str): The range (minus the sheet) to be retrieved, in a A1 format. Example: 'A1:B2', 'B', '3', 'A1'.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[List[object]]: A list with the recovered rows. Each row is a list of objects.
        """
        info = parse_range(range_)
        rows = self.as_list(sheet)[info['start_row']:info['end_row']]
        return [row[info['start_column']:info['end_column']] for row in rows]

    def get_cell(self, column: str, row: int, sheet: str = None) -> object:
        """
        Returns the value of a single cell.

        Args:
            column (str): The letter-indexed column name ('a', 'A', 'AA').
            row (int): The 1-indexed row number.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            object: The cell's value.
        """
        sheet = self.active_sheet if sheet is None else sheet
        return self._sheets[sheet].iloc[row - 1, get_column_number(column)]

    def get_row(self, row: int, sheet: str = None) -> List[object]:
        """
        Returns the contents of an entire row in a list format.

        Please note that altering the values in this list will not alter the values in the original sheet.

        Args:
            row (int): The 1-indexed number of the row to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[object]: The values of all cells within the row.
        """
        sheet = self.active_sheet if sheet is None else sheet
        return self.as_list(sheet)[row - 1]

    def get_column(self, column: str, sheet: str = None) -> List[object]:
        """
        Returns the contents of an entire column in a list format.

        Please note that altering the values in this list will not alter the values in the original sheet.

        Args:
            column (str): The letter-indexed column name ('a', 'A', 'AA').
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[object]: The values of all cells within the column.
        """
        sheet = self.active_sheet if sheet is None else sheet
        return [row[get_column_number(column)] for row in self.as_list(sheet)]

    # noinspection PyTypeChecker
    def as_list(self, sheet: str = None) -> List[List[object]]:
        """
        Returns the contents of an entire sheet in a list of lists format.

        This is equivalent to get_range("", sheet).

        Args:
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[List[object]]: A list of rows. Each row is a list of cell values.
        """
        sheet = self.active_sheet if sheet is None else sheet
        return self._sheets[sheet].values.tolist()

    def as_dataframe(self, sheet: str = None) -> pd.DataFrame:
        """
        Returns the contents of an entire sheet in a Pandas DataFrame format.

        Args:
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            DataFrame: A Pandas DataFrame object.
        """
        sheet = self.active_sheet if sheet is None else sheet
        return self._sheets[sheet]

    def add_row(self, row: List[object], sheet: str = None) -> BotExcelPlugin:
        """
        Adds a new row to the bottom of the sheet.

        Args:
            row (List[object]): A list of cell values.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        # List Treatment
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = pd.concat([self._sheets[sheet], pd.DataFrame([row])], ignore_index=True)
        return self

    def add_rows(self, rows: List[List[object]], sheet: str = None) -> BotExcelPlugin:
        """
        Adds new rows to the sheet.

        Args:
            rows (List[List[object]]): A list of rows.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
        Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = pd.concat([self._sheets[sheet], pd.DataFrame(rows)], ignore_index=True)
        return self

    def add_column(self, column: List[object], sheet: str = None) -> BotExcelPlugin:
        """
        Adds a new column to the sheet.

        Args:
            column (List[object]): A list of cells.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
        Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        n_columns = self._sheets[sheet].shape[1]
        self._sheets[sheet][n_columns] = column
        return self

    def add_columns(self, columns: List[List[object]], sheet: str = None) -> BotExcelPlugin:
        """
        Adds new columns to the sheet.

        Args:
            columns (List[List[object]]): A list of columns. Each column is a list of cells.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
        Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        for column in columns:
            self.add_column(column, sheet)
        return self

    def set_range(self, values: List[List[object]], range_: str = None, sheet: str = None) -> BotExcelPlugin:
        """
        Replace the values within an area of the sheet by the values supplied.

        Args:
            values (List[List[object]]): A list of rows. Each row is list of cell values.
            range_ (str, Optional): The range (minus the sheet) to have its values replaced, in A1 format. Ex: 'A1:B2',
                'B', '3', 'A1'. If None, the entire sheet will be used as range. Defaults to None.
            sheet:  (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        # Parses the range to obtain its starting cell
        info = parse_range(range_)
        start_row = info['start_row'] if info['start_row'] else 0
        start_column = info['start_column'] if info['start_column'] else 0

        # Set the cells of the range one by one
        for i, row in enumerate(values):
            for j, cell in enumerate(row):
                self.set_cell(get_column_name(start_column + j), start_row + i + 1, cell, sheet)

        return self

    def set_cell(self, column: str, row: int, value: object, sheet: str = None) -> BotExcelPlugin:
        """
        Replaces the value of a single cell.

        Args:
            column (str): The cell's letter-indexed column name ('a', 'A', 'AA').
            row (int): The cell's 1-indexed row number.
            value (object): The new value of the cell.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet].loc[row - 1, get_column_number(column)] = value
        return self

    def set_nan_as(self, value: str or int = "", sheet: str = None) -> BotExcelPlugin:
        """
        Set the NaN values.
        Args:
            value: (str, Optional): The value to replace the NaN values.
                Defaults to ""
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.
        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet].replace(np.nan, value, inplace=True)
        return self

    def remove_row(self, row: int, sheet: str = None) -> BotExcelPlugin:
        """
        Removes a single row from the sheet.

        Keep in mind that the rows below will be moved up.

        Args:
            row (int): The 1-indexed number of the row to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = self._sheets[sheet].drop(index=row - 1)
        self._sheets[sheet] = self._sheets[sheet].reset_index(drop=True)
        return self

    def remove_rows(self, rows: List[int], sheet: str = None) -> BotExcelPlugin:
        """
        Removes rows from the sheet.

        Keep in mind that each row removed will cause the rows below it to be moved up after they are all removed.

        Args:
            rows (List[int]): A list of the 1-indexed numbers of the rows to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        # Turns 1-indexing into 0-indexing
        rows = [row - 1 for row in rows]

        # Removes the rows
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = self._sheets[sheet].drop(index=rows)
        self._sheets[sheet] = self._sheets[sheet].reset_index(drop=True)
        return self

    def remove_column(self, column: str, sheet: str = None) -> BotExcelPlugin:
        """
        Removes single column from the sheet.

        Keep in mind that the columns to its right will be moved to the left.

        Args:
            column (str): The letter-indexed name ('a', 'A', 'AA') of the column to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = self._sheets[sheet].drop(columns=get_column_number(column))
        self._sheets[sheet].columns = range(self._sheets[sheet].columns.size)
        return self

    def remove_columns(self, columns: List[str], sheet: str = None) -> BotExcelPlugin:
        """
        Removes a list of columns from the sheet.

        Keep in mind that each column removed will cause the columns to their right to be moved left after they are
        all removed.

        Args:
            columns (List[str]): A list of the letter-indexed names of the columns to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        # Converts column names to column numbers
        columns = [get_column_number(column) for column in columns]

        # Removes the columns
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = self._sheets[sheet].drop(columns=columns)
        self._sheets[sheet].columns = range(self._sheets[sheet].columns.size)
        return self

    def clear_range(self, range_: str = None, sheet: str = None) -> BotExcelPlugin:
        """
        Clears the provided area of the sheet.

        Keep in mind that this method will not remove any rows or columns, only erase their values.

        Args:
            range_ (str, Optional): The range to be cleared, in A1 format. Example: 'A1:B2', 'B', '3', 'A1'. If None,
                the entire sheet will be used as range. Defaults to None.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        # Init
        sheet = self.active_sheet if sheet is None else sheet

        # Parses the range to obtain its starting cell
        info = parse_range(range_)
        start_row = info['start_row'] if info['start_row'] else 0
        start_column = info['start_column'] if info['start_column'] else 0
        end_row = info['end_row'] if info['end_row'] else self._sheets[sheet].shape[0]
        end_column = info['end_column'] if info['end_column'] else self._sheets[sheet].shape[1]

        # Set the cells of the range one by one
        for row in range(start_row, end_row):
            for column in range(start_column, end_column):
                self.set_cell(get_column_name(column), row + 1, np.nan, sheet)

        return self

    def clear(self, sheet: str = None) -> BotExcelPlugin:
        """
        Deletes the entire content of the sheet.

        Args:
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
        Defaults to None.

        Returns:
            self (allows Method Chaining).
        """
        sheet = self.active_sheet if sheet is None else sheet
        self._sheets[sheet] = pd.DataFrame()
        return self

    def read(self, file_or_path) -> BotExcelPlugin:
        """
        Reads an Excel file.

        Args:
            file_or_path: Either a buffered Excel file or a path to it.

        Returns:
            self (allows Method Chaining).
        """
        self._sheets = pd.read_excel(file_or_path, None, header=None)
        if self.active_sheet is None:
            self.set_active_sheet(list(self._sheets)[0])
            return self
        self.set_active_sheet(self.active_sheet)
        return self

    def write(self, file_or_path) -> BotExcelPlugin:
        """
        Writes this class's content to a file.

        Args:
            file_or_path: Either a buffered Excel file or a path to it.

        Returns:
            self (allows Method Chaining).
        """
        with pd.ExcelWriter(file_or_path) as writer:
            for sheet_name, sheet in self._sheets.items():
                sheet.to_excel(writer, sheet_name, header=False, index=False)
        return self

    def sort(
            self,
            by_columns: Union[str, List[str]],
            ascending: bool = True,
            start_row: int = 2,
            end_row: int = None,
            sheet: str = None
    ) -> BotExcelPlugin:
        """
        Sorts the sheet's rows according to the columns provided.

        Unless the start and end point are provided, all rows minus the first one will be sorted!

        Args:
            by_columns (Union[str, List[str]]): Either a letter-indexed column name to sort the rows by, or a list of
                them. In case of a tie, the second column is used, and so on.
            ascending (bool, Optional): Set to False to sort by descending order. Defaults to True.
            start_row (str, Optional): The 1-indexed row number where the sort will start from. Defaults to 2.
            end_row (str, Optional): The 1-indexed row number where the sort will end at (inclusive). Defaults to None.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        # Init
        by_columns = [get_column_number(column) for column in by_columns]
        start_row = start_row - 1 if start_row else None
        end_row = end_row - 1 if end_row else None

        # Sorts the sheet
        sheet = self.active_sheet if sheet is None else sheet
        to_sort = self._sheets[sheet].iloc[start_row:end_row].sort_values(by_columns, ascending=ascending)
        self._sheets[sheet].iloc[start_row:end_row] = to_sort
        return self

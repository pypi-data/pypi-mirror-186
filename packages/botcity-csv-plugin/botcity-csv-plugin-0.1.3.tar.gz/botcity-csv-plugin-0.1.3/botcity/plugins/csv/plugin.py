from __future__ import annotations

from typing import Dict, List, Union

import pandas as pd


class BotCSVPlugin:
    def __init__(self, has_header: bool = True, separator: str = ',') -> None:
        """
        This class stores the data in a CSV-like format.

        Args:
            has_header: True if the CSV's first row is supposed to be the header. Defaults to True.
            separator: The expected separator between each field.

        Attributes:
            has_header (bool, Optional): A list representing the header of the CSV, if it has one.
                Defaults to True.
            separator (str, Optional): The expected separator between each field. Defaults to ','.
        """
        self.has_header = has_header
        self._rows = pd.DataFrame()
        self.separator = separator

    def set_separator(self, separator: str) -> BotCSVPlugin:
        self.separator = separator
        return self

    def set_header(self, headers: List[str]) -> BotCSVPlugin:
        self.header = headers
        return self

    @property
    def header(self) -> List[str]:
        """
        Returns this CSV's header.

        Returns:
            List[str]: The header elements in str format.
        """
        return self._rows.columns.tolist()

    @header.setter
    def header(self, headers: List[str]):
        self._rows = pd.DataFrame(self._rows, columns=headers)

    def get_entry(self, column: Union[str, int], row: int) -> object:
        """
        Returns the value of a single entry of a column.

        Args:
            column (Union[str, int]): Either the entry's column name or it's 0-indexed number.
            row (int): The 0-indexed row number.

        Returns:
            object: The entry's value.
        """
        # Gets the column by its name
        if isinstance(column, str):
            return self._rows[column][row]

        # Gets the column by its number
        return self._rows.iloc[row, column]

    def get_row(self, row: int) -> List[object]:
        """
        Returns the contents of an entire row in a list format.

        Please note that altering the values in this list will not alter the values in the original CSV.

        Args:
            row (int): The 0-indexed row number.

        Returns:
            List[object]: The values of all entries within the row.
        """
        return self.as_list()[row]

    def get_column(self, column: Union[str, int]) -> List[object]:
        """
        Returns the contents of an entire column in a list format.

        Please note that altering the values in this list will not alter the values in the original CSV.

        Args:
            column (Union[str, int]): Either the column's name or it's 0-indexed number.

        Returns:
            List[object]: The values of all entries within the column.
        """
        # Gets the column by its name
        if isinstance(column, str):
            return [row.get(column) for row in self.as_dict()]

        # Gets the column by its number
        return [row[column] for row in self.as_list()]

    # noinspection PyTypeChecker
    def as_list(self, include_header: bool = False) -> List:
        """
        Returns the contents of this CSV in a list of lists format.

        Nan values will be replaced with empty strings.

        Args:
            include_header (bool, Optional): If True, the first inner-list will receive the CSV's header.
                Defaults to False.

        Returns:
            List[List[object]]: A list of rows. Each is a list of row elements.
        """
        # Includes Header if needed
        data = self._rows.fillna('').values.tolist()
        if include_header:
            data.insert(0, self.header)

        return data

    def as_dict(self) -> List[Dict[str, object]]:
        """
        Returns the contents of this CSV in a list of dicts format.

        Returns:
            List[Dict[str, object]]: A list of rows. Each row is a dict.
        """

        return self._rows.to_dict('records')

    def as_dataframe(self) -> pd.DataFrame:
        """
        Returns the contents of this CSV in a Pandas DataFrame format.

        Returns:
            pandas.DataFrame: A Pandas DataFrame object.
        """
        return self._rows

    def add_row(self, row: Union[List[object], Dict[str, object]]) -> BotCSVPlugin:
        """
        Adds a new row to the bottom of the CSV.

        If the input contains a new column, then a new column will be created in the CSV as well,
        with blank fields for the previously inserted lines.

        Args:
            row (Union(List[object] or Dict[str, object])): A list of CSV elements in string format,
                or a dict that has the column names as its keys.

        Returns:
            self (allows Method Chaining).
        """
        # List Treatment
        if isinstance(row, list):
            # Empty List
            if not row:
                return self

            # Zips this list with the header to form a dict
            row = dict(zip(self.header, row))

        # Appends the row and return
        self._rows = self._rows.append(row, ignore_index=True)
        return self

    def add_rows(self, rows: List[Union[List[object], Dict[str, object]]]) -> BotCSVPlugin:
        """
        Adds new rows to the CSV.

        If the input contains a new column, then a new column will be created in the CSV as well, with blank fields
        for the previously inserted lines.

        Args:
            rows (List[Union[List[object], Dict[str, object]]]): A list of rows. Each row is either a list of csv
                elements, or a dict whose keys are the header, and the values are the new CSV elements.

        Returns:
            self (allows Method Chaining).
        """
        for row in rows:
            self.add_row(row)
        return self

    def add_column(self, column_name: str = None, column: List[object] = None) -> BotCSVPlugin:
        """
        Adds a new column to the CSV.

        Args:
            column_name (str, Optional): The new column's name. If None is provided, the new name will
                be the numeric index of the new column.
            column (List[object]): A list of csv elements. The number of elements must match the number
                of rows already in the list.

        Returns:
            self (allows Method Chaining).
        """
        # If no name is provided, use the column number instead
        if column_name is None:
            column_name = self._rows.shape[1]

        self._rows[column_name] = column
        return self

    def add_columns(self, columns: Union[Dict[str, List[object]], List[object]]) -> BotCSVPlugin:
        """
        Adds new columns to the CSV.

        Args:
            columns (List[List[object]]): Either a dict of columns, whose keys are the new column names
                and the values are lists of CSV elements, or just a list of CSV elements, in which case
                the column name will be it's numeric index. The number of elements of each column must
                match the number of rows already in the list.

        Returns:
            self (allows Method Chaining).
        """
        for column_name, column in columns.items():
            self.add_column(column_name, column)
        return self

    def set_entry(self, column: Union[str, int], row: int, value: object) -> BotCSVPlugin:
        """
        Replaces the value of a single entry of a given column.

        Args:
            column (Union[str, int]): Either the entry's column name or it's 0-index number.
            row (int): The entry's 0-indexed row number.
            value (object): The new value of the entry.

        Returns:
            self (allows Method Chaining)
        """
        # Gets the column by its name
        if isinstance(column, str):
            self._rows[column][row] = value
            return self

        # Grabs the column name, if it exists
        if self.header and self.header[column]:
            column = self.header[column]

        # Gets the column by its name or number
        self._rows.loc[row, column] = value
        return self

    def set_row(self, row: int, values: Union[List[object], Dict[str, object]]) -> BotCSVPlugin:
        """
        Replaces the values of an entire row of the CSV.

        Args:
            row (int): The row's 0-indexed number.
            values (Union[List[object], Dict[str, object]]): Either a list of CSV elements, or a dict
                whose keys are the header, and the values are the new CSV elements.

        Returns:
            self (allows Method Chaining)
        """
        # List Treatment
        if isinstance(values, list):
            # Empty List
            if not values:
                return self

            # Zips this list with the header to form a dict
            values = dict(zip(self.header, values))

        # Appends the row and return
        self._rows.loc[row] = values
        return self

    def set_column(self, column: Union[str, int], values: List[object]) -> BotCSVPlugin:
        """
        Replaces the values of an entire column of the CSV.

        Args:
            column (Union[str, int]): Either the entry's column name or it's 0-indexed number.
            values (List[object]): A list of CSV elements.

        Returns:
            self (allows Method Chaining)
        """
        for row, value in enumerate(values):
            self.set_entry(column, row, value)
        return self

    def remove_row(self, row: int) -> BotCSVPlugin:
        """
        Removes a single row from the CSV.

        Keep in mind that the rows below will be moved up.

        Args:
            row (int): The 0-indexed number of the row to be removed.

        Returns:
            self (allows Method Chaining).
        """
        self._rows = self._rows.drop(index=row)
        self._rows = self._rows.reset_index(drop=True)
        return self

    def remove_rows(self, rows: List[int]) -> BotCSVPlugin:
        """
        Removes rows from the CSV.

        Keep in mind that each row removed will cause the rows below it to be moved up after they are all removed.

        Args:
            rows (List[int]): A list of the 0-indexed numbers of the rows to be removed.

        Returns:
            self (allows Method Chaining)
        """
        self._rows = self._rows.drop(index=rows)
        self._rows = self._rows.reset_index(drop=True)
        return self

    def remove_column(self, column: Union[str, int]) -> BotCSVPlugin:
        """
        Removes single column from the CSV.

        If the CSV has a header, this column will be removed from there as well.

        Args:
            column (Union[str, int]): Either the entry's column name or it's 0-indexed number.

        Returns:
            self (allows Method Chaining).
        """
        # Grabs the column name, if it exists
        if isinstance(column, int) and self.header and self.header[column]:
            column = self.header[column]

        # Removes the column by name or number
        self._rows = self._rows.drop(columns=column)
        return self

    def remove_columns(self, columns: List[Union[str, int]]) -> BotCSVPlugin:
        """
        Removes a list of columns from the CSV.

        If the CSV has a header, this column will be removed from there as well.

        Args:
            columns (List[Union[str, int]]): A list of column names or their 0-indexed numbers.

        Returns:
            self (allows Method Chaining).
        """
        # Grabs each column name, if it exists
        for i, column in enumerate(columns):
            if isinstance(column, int) and self.header and self.header[column]:
                columns[i] = self.header[column]

        # Removes the column by name or number
        self._rows = self._rows.drop(columns=columns)
        return self

    def clear(self) -> BotCSVPlugin:
        """
        Clears all the rows of the CSV, but the header remains.

        Returns:
            self (allows Method Chaining)
        """
        # Saves the header, gets a new DataFrame, and reuse the old header
        self._rows = pd.DataFrame(columns=self.header)
        return self

    def read(self, file_or_path) -> BotCSVPlugin:
        """
        Reads a CSV file using the delimiter and the has_header attributes of this class.

        Args:
            file_or_path: Either a buffered CSV file or a path to it.

        Returns:
            self (allows Method Chaining).
        """
        self._rows = pd.read_csv(file_or_path, sep=self.separator, header=0 if self.has_header else None)
        return self

    def write(self, file_or_path) -> BotCSVPlugin:
        """
        Writes this class's CSV content to a file using it's delimiter and has_header attributes.

        Args:
            file_or_path: Either a buffered CSV file or a path to it.

        Returns:
            self (allows Method Chaining).
        """
        self._rows.to_csv(file_or_path, sep=self.separator, header=True if self.has_header else False, index=False)
        return self

    def sort(self, by_columns: Union[int, str, List[Union[int, str]]], ascending: bool = True) -> BotCSVPlugin:
        """
        Sorts the CSV rows using the first column of the by_columns parameter as a reference. In case of a tie,
        the second column provided is used, and so on.

        Args:
            by_columns (Union[int, str, List[Union[int, str]]]): Either a column name or its 0-indexed number; or a
                list of those.
            ascending (bool, Optional): Set to False if you want to use descending order. Defaults to True.

        Returns:
            self (allows Method Chaining)
        """
        # Grabs the column name, if it exists
        if isinstance(by_columns, int) and self.header and self.header[by_columns]:
            by_columns = self.header[by_columns]

        # Grabs each column name, if it exists
        for i, column in enumerate(by_columns):
            if isinstance(column, int) and self.header and self.header[column]:
                by_columns[i] = self.header[column]

        self._rows = self._rows.sort_values(by_columns, ascending=ascending)
        return self

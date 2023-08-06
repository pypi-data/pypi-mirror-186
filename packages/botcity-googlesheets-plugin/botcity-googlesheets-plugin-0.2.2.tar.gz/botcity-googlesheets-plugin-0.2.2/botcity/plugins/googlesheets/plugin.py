from __future__ import annotations

import os.path
from typing import List, Optional, Union

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery


def get_credentials(client_secret_path: str = "client_secret.json"):
    # The token_sheets.json file stores the credentials
    credentials = None
    token_path = os.path.abspath(os.path.dirname(client_secret_path)) + '/token_sheets.json'
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    if os.path.exists(token_path):
        credentials = Credentials.from_authorized_user_file(token_path, scopes)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        # Refresh credentials
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, scopes)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(credentials.to_json())

    return credentials


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


class BotGoogleSheetsPlugin:
    def __init__(self, client_secret_path: str, spreadsheet_id: str, active_sheet: str = None) -> None:
        """
        This class gives you easy access to Google Sheets API's functionalities. This plugin works with one
        spreadsheet at a time, so if you want to access multiple files, simply create multiple objects of this class.
        However, if you need to work with different sheets within the same file, you can do so by supplying the
        sheet's name to this class's methods, or change the default sheet with set_active_sheet().

        Args:
            client_secret_path (str): The path to your client_secret file. Get it from your Google Cloud Console!
            spreadsheet_id (str): The ID of a Google Spreadsheet file. You can get it from the file's URL.
            active_sheet (str, Optional): The sheet this plugin will access by default. If None, the first sheet is
                used. Defaults to None.
        """
        self._spreadsheet_id = spreadsheet_id
        self._service = discovery.build('sheets', 'v4', credentials=get_credentials(client_secret_path)).spreadsheets()
        self.active_sheet = self._get_sheet_name(0) if active_sheet is None else active_sheet

    @classmethod
    def new_spreadsheet(cls, client_secret_path: str, name: str) -> BotGoogleSheetsPlugin:
        """
        An alternative way to initialize the plugin. This factory method will create a new spreadsheet, and return an
        initialized object of the plugin that refers to it.

        Args:
            client_secret_path (str): The path to your client_secret file. Get it from your Google Cloud Console!
            name (str): The name of the new spreadsheet.

        Returns:
            BotGoogleSheetsPlugin: An initialized object of the plugin points to the newly created sheet.
        """
        bot = cls(client_secret_path, '0', '0')
        args = {
            'fields': 'spreadsheetId',
            'body': {'properties': {'title': name}}
        }
        bot._spreadsheet_id = bot._service.create(**args).execute().get('spreadsheetId')
        bot.set_active_sheet()
        return bot

    def active_sheet(self) -> str:
        return self.active_sheet

    def set_active_sheet(self, sheet: str = None) -> BotGoogleSheetsPlugin:
        self.active_sheet = self._get_sheet_name(0) if sheet is None else sheet
        return self

    def get_spreadsheet_id(self) -> str:
        """
        Returns the ID of the spreadsheet this plugin is currently linked to.

        Specially useful if created a new sheet using the new_spreadsheet class method, since you wouldn't know it's ID.

        Returns:
            str: The ID of a Google Spreadsheet file.
        """
        return self._spreadsheet_id

    def get_spreadsheet_link(self) -> str:
        """
        Returns the URL Link to the spreadsheet this plugin is currently linked to.

        Returns:
            str: The URL to a Google Spreadsheet file.
        """
        return self._service.get(spreadsheetId=self._spreadsheet_id).execute()['spreadsheetUrl']

    def _get_sheet_id(self, sheet: str = None) -> Optional[int]:
        """
        Given a sheet name, returns the respective sheet id.

        Args:
            sheet (str, Optional): If a name is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            str: The respective sheet id, or None if not found.
        """
        # Init
        sheet = self.active_sheet if sheet is None else sheet

        # For each sheet...
        sheets = self._service.get(spreadsheetId=self._spreadsheet_id).execute()['sheets']
        for sheet_obj in sheets:
            # If the sheet name is equal to the one we're searching for, return the sheet's id
            if sheet_obj['properties']['title'] == sheet:
                return sheet_obj['properties']['sheetId']

        # Returns None if no sheet with that name was found
        return None

    def _get_sheet_name(self, sheet_id: int) -> Optional[str]:
        """
        Given a sheet id, returns the respective sheet name.

        Args:
            sheet_id (int): The ID of the sheet you are searching for.

        Returns:
            str: The respective sheet name, or None if not found.
        """
        # For each sheet...
        sheets = self._service.get(spreadsheetId=self._spreadsheet_id).execute()['sheets']
        for sheet_obj in sheets:
            # If the sheet name is equal to the one we're searching for, return the sheet's id
            if sheet_obj['properties']['sheetId'] == sheet_id:
                return sheet_obj['properties']['title']

        # In some cases, the only sheet of the spreadsheet does not have the special id 0
        if sheet_id == 0 and len(sheets) == 1:
            return sheets[0]['properties']['title']

        # Returns None if no sheet with that Id was found
        return None

    def _make_range(self, range_: str = None, sheet: str = None) -> str:
        """
        Combines a range (minus sheet) with a sheet name to obtain the full range.
        If range_ is empty, this method returns the sheet name, which is the range for "all cells in that sheet".

        Args:
            range_ (str, Optional): The range, but without information about sheets. Defaults to None.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            str: The new range, in the 'sheet'!A1:B2 format.
        """
        # Init
        sheet = self.active_sheet if sheet is None else sheet

        # If no range is provided, returns the sheet name surrounded by single quotes. Ex: 'Sheet1'.
        if not range_:
            return "'" + sheet + "'"

        # Otherwise, returns the complete range. Ex: 'Sheet1'!A1:B2
        return "'" + sheet + "'" + '!' + range_

    def _send_request(self, request: dict) -> BotGoogleSheetsPlugin:
        self._service.batchUpdate(spreadsheetId=self._spreadsheet_id, body={'requests': [request]}).execute()
        return self

    def create_sheet(self, sheet: str) -> BotGoogleSheetsPlugin:
        """
        Creates a new sheet within the spreadsheet.

        Args:
            sheet (str): The new sheet's name.

        Returns:
            self (allows Method Chaining)
        """
        self._send_request({'addSheet': {'properties': {'title': sheet}}})
        return self

    def remove_sheet(self, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Removes a sheet from the spreadsheet.

        Keep in mind that if you remove the active_sheet, you must set another sheet as active before using trying to
            modify it!

        Args:
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        self._send_request({'deleteSheet': {'sheetId': self._get_sheet_id(sheet)}})
        return self

    def list_sheets(self) -> List[str]:
        """
        Returns a list with the name of all the sheets in this spreadsheet.

        Returns:
            List[str]: A list of sheet names.
        """
        return [sheet['properties']['title'] for sheet in
                self._service.get(spreadsheetId=self._spreadsheet_id).execute()['sheets']]

    def get_range(self, range_: str, sheet: str = None) -> List[List[object]]:
        """
        Returns the values of all cells within an area of the sheet in a list of list format.

        Args:
            range_ (str): The range (minus the sheet) to be retrieved, in A1 format. Example: 'A1:B2', 'B', '3', 'A1'.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[List[object]]: A list with the recovered rows. Each row is a list of objects.
        """
        args = {
            'spreadsheetId': self._spreadsheet_id,
            'range': self._make_range(range_, sheet),
        }
        return self._service.values().get(**args).execute().get('values', [])

    def get_cell(self, column: str, row: int, sheet: str = None) -> object:
        """
        Returns the value of a single cell.

        Args:
            column (str): The letter-indexed column name ('a', 'A', 'AA').
            row (int): The cell's 1-indexed row number.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            object: The cell's value.
        """
        return self.get_range(column + str(row), sheet)[0][0]

    def get_row(self, row: int, sheet: str = None) -> List[object]:
        """
        Returns the contents of an entire row in a list format.

        Please note that altering the values in this list will not alter the values in the original sheet.

        Args:
            row (int): The 1-indexed row number.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            List[object]: The values of all cells within the row.
        """
        return self.get_range(str(row) + ':' + str(row), sheet)[0]

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
        return [row[0] for row in self.get_range(column + ':' + column, sheet)]

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
        return self.get_range("", sheet)

    def add_row(self, row: List[object], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Adds a new row to the bottom of the sheet.

        Args:
            row (List[object]): A list with the cell values.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        return self.add_rows([row], sheet)

    def add_rows(self, rows: List[List[object]], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Adds new rows to the bottom of the sheet.

        Args:
            rows (List[List[object]]): A list of rows. Each row is a list with cell values.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        args = {
            'spreadsheetId': self._spreadsheet_id,
            'range': self._make_range(sheet=sheet),
            'valueInputOption': 'RAW',
            'body': {'values': rows}
        }
        self._service.values().append(**args).execute()
        return self

    def add_column(self, column: List[object], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Adds a new column to the right end of the sheet.

        Args:
            column (List[object]): A list with the cell values.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        return self.add_columns([column], sheet)

    def add_columns(self, columns: List[List[object]], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Adds new columns to the right end of the sheet.

        Args:
            columns (List[List[object]]): A list of rows. Each row is a list with cell values.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        # Gets the name of the first empty column in the sheet
        column = get_column_name(max([len(row) for row in self.as_list()]))

        args = {
            'spreadsheetId': self._spreadsheet_id,
            'range': self._make_range(column + ':' + column, sheet),
            'valueInputOption': 'RAW',
            'body': {
                'majorDimension': 'COLUMNS',
                'values': columns
            }
        }
        self._service.values().append(**args).execute()
        return self

    def set_range(self, values: List[List[object]], range_: str = None, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Replace the values within an area of the sheet by the values supplied.

        Args:
            values (List[List[object]]): A list of rows. Each row is a list of cell values.
            range_ (str, Optional): The range (minus the sheet) to have its values replaced, in A1 format. Ex: 'A1:B2',
                'B', '3', 'A1'. If None, the entire sheet will be used as range. Defaults to None.
            sheet:  (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        args = {
            'spreadsheetId': self._spreadsheet_id,
            'range': self._make_range(range_, sheet),
            'valueInputOption': 'RAW',
            'body': {'values': values}
        }
        self._service.values().update(**args).execute()
        return self

    def set_cell(self, column: str, row: int, value: object, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Replaces the value of a single cell.

        Args:
            column (str): The cell's letter-indexed column name.
            row (int): The cell's 1-indexed row number.
            value (object): The new value of the cell.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        return self.set_range([[value]], column + str(row), sheet)

    def clear_range(self, range_: str, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Clears the provided area of the sheet. Only the cells' content is removed, while the formatting remains.

        Args:
            range_ (str): The range to be cleared, in A1 format. Example: 'A1:B2', 'B', '3', 'A1'.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        args = {
            'spreadsheetId': self._spreadsheet_id,
            'range': self._make_range(range_, sheet),
            'body': {}
        }
        self._service.values().clear(**args).execute()
        return self

    def clear(self, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Clears an entire sheet. Only the cells' content is removed, while their formatting remains.

        This method is equivalent to clear_range("").

        Args:
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        return self.clear_range("", sheet)

    def remove_row(self, row: int, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Removes a single row from the sheet.

        Keep in mind that the rows below will be moved up.

        Args:
            row (int): The 1-indexed number of the row to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        request = {
            'deleteDimension': {
                'range': {
                    'sheetId': self._get_sheet_id(sheet),
                    'dimension': 'ROWS',
                    'startIndex': row - 1,
                    'endIndex': row
                }
            }
        }
        self._send_request(request)
        return self

    def remove_rows(self, rows: List[int], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Removes rows from the sheet.

        Keep in mind that each row removed will cause the rows below it to be moved up. For this reason, this method
        will sort the indexes of the rows you provide, and remove then in descending order.

        Args:
            rows (List[int]): A list of the 1-indexed numbers of the rows to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        rows.sort(reverse=True)
        for row in rows:
            self.remove_row(row, sheet)
        return self

    def remove_column(self, column: str, sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Removes a single column from the sheet.

        Keep in mind that the columns to its right will be moved to the left.

        Args:
            column (str): The letter-indexed name ('a', 'A', 'AA') of the column to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        request = {
            'deleteDimension': {
                'range': {
                    'sheetId': self._get_sheet_id(sheet),
                    'dimension': 'COLUMNS',
                    'startIndex': get_column_number(column),
                    'endIndex': get_column_number(column) + 1
                }
            }
        }
        self._send_request(request)
        return self

    def remove_columns(self, columns: List[str], sheet: str = None) -> BotGoogleSheetsPlugin:
        """
        Removes columns from the sheet.

        Keep in mind that each column removed will cause the columns to its right to be moved left. For this reason,
        this method will sort the indexes of the columns you provide, and remove then in descending order.

        Args:
            columns (List[str]): A list of the letter-indexed names of the columns to be removed.
            sheet (str, Optional): If a sheet is provided, it'll be used by this method instead of the Active Sheet.
                Defaults to None.

        Returns:
            self (allows Method Chaining)
        """
        columns.sort(reverse=True)
        for column in columns:
            self.remove_column(column, sheet)
        return self

    def sort(
            self,
            by_columns: Union[str, List[str]],
            ascending: bool = True,
            start_row: int = 2,
            end_row: int = None,
            sheet: str = None
    ) -> BotGoogleSheetsPlugin:
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
        # Wrap in a list if needed
        if isinstance(by_columns, str):
            by_columns = [by_columns]

        # Request
        request = {
            'sortRange': {
                'range': {
                    'sheetId': self._get_sheet_id(sheet),
                    'startRowIndex': None if start_row is None else start_row - 1,
                    'endRowIndex': None if end_row is None else end_row
                },
                'sortSpecs': [
                    {
                        'sortOrder': 'ASCENDING' if ascending else 'DESCENDING',
                        'dimensionIndex': get_column_number(column)
                    }
                    for column in by_columns
                ]
            }
        }

        self._send_request(request)
        return self

from auth import authorization

import os.path
import socket
import httplib2
import pandas as pd
from dotenv import load_dotenv

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
global SOURCE_SPREADSHEET_ID
SOURCE_SPREADSHEET_ID = os.getenv("SOURCE_SPREADSHEET_ID")


def init_sheets():
    print("init sheets")
    global service, sheet
    try:
        service = build("sheets", "v4", credentials=authorization())
        sheet = service.spreadsheets()
    except Exception as err:
        print(err)


def fetch_sheet_names():
    print("fetching sheet names")
    # Call the Sheets API to retrieve spreadsheet properties
    print(SOURCE_SPREADSHEET_ID)
    try:
        spreadsheet = (
            service.spreadsheets().get(spreadsheetId=SOURCE_SPREADSHEET_ID).execute()
        )

        sheet_names = [sheet["properties"]["title"] for sheet in spreadsheet["sheets"]]
        return sheet_names
    except (socket.gaierror, httplib2.error.ServerNotFoundError) as e:
        print(
            "Error: Unable to connect to the server. Please check your internet connection.",
            e,
        )
        return []


def fetch_sheet_data(sheet_id_range):
    try:
        result = (
            sheet.values()
            .get(spreadsheetId=SOURCE_SPREADSHEET_ID, range=sheet_id_range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return None

        df = pd.DataFrame(values[1:], columns=values[0])
        return df
    except (socket.gaierror, httplib2.error.ServerNotFoundError) as e:
        print(
            "Error: Unable to connect to the server. Please check your internet connection.",
            e,
        )
        return None


def write_sheet_data(sheet_id_range):
    return
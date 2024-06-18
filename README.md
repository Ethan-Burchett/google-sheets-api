# Project Overview

This project provides a set of tools for interacting with Google Sheets and managing data using Python. It includes modules for authorization, fetching sheet data, and writing data to files.

### Modules

## 1. auth.py

Handles the authorization process for accessing Google Sheets using OAuth 2.0.

## Functions:

	•	authorization(): Authenticates the user and returns the credentials required to access Google Sheets. If no valid credentials are found, it prompts the user to log in and generates a token.json file.

## 2. sheet_helpers.py

Provides helper functions for interacting with Google Sheets.

## Functions:

	•	init_sheets(): Initializes the Google Sheets service.
	•	fetch_sheet_names(): Retrieves the names of all sheets in the spreadsheet.
	•	fetch_data(sheet_id_range): Fetches data from a specified range in the Google Sheets.
	•	write_sheet_data(sheet_id_range): (Write data to Google Sheet to a specified range)

### Environment Variables:

	•	SOURCE_SPREADSHEET_ID: The ID of the source spreadsheet, loaded from a .env file.

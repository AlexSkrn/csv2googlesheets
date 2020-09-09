import sys

SHEET_NOT_CREATED = 'No spreadsheetID returned. Spreadsheet not created.'
SHEET_CREATED = 'Created spreadsheet ID: {}'


def create_sheet(service, spreadsheet_title: str) -> str:
    """Create a Google spreadsheet."""
    spreadsheet_body = {
        'properties': {
            'title': spreadsheet_title
            }
        }
    # Call the Sheets API to create a spreadsheet
    spreadsheet = service.spreadsheets().create(
        body=spreadsheet_body,
        fields='spreadsheetId'
        ).execute()

    spreadsheet_id = spreadsheet.get('spreadsheetId')

    if not spreadsheet_id:
        sys.exit(SHEET_NOT_CREATED)
    else:
        print(SHEET_CREATED.format(spreadsheet_id))

    return spreadsheet_id

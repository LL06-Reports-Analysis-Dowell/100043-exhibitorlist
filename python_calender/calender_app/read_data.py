from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
from dateutil import parser
from .models import Event

def read_google_sheet():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    SERVICE_ACCOUNT_FILE = 'D:/python_calender/calender_app/keys.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1A0ttBHzMWmJq4YWPKGKri_McmJr8L_iRMREv4RIu_cc'


    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!A1:B10").execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
        # Print columns A and B, which correspond to indices 0 and 1.
            event_title = row[0]
            # event_date = datetime.strptime(row[1], '%b %d %Y %I:%M%p')
            event_date = parser.parse(row[1])
            Event.objects.get_or_create(title=event_title, start_time=event_date) #creating expression
            print('%s, %s' % (row[0], row[1]))

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Authorize:
    # This class is what allows you to speak to the Google sheet in
    # the Google Drive that we have shared
    def __init__(self, feeds, googleapis, json_file, spread_sheet_name):
        # This is just the init method to set up all the necessary credentials
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, [feeds, googleapis])
        authorize = gspread.authorize(credentials)
        self.source = authorize.open(spread_sheet_name)

    def initialize(self, sheet_number):
        # This gives access to individual tabs in the Worhsheet as a whole
        return self.source.get_worksheet(sheet_number)

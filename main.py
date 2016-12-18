# GSpread
# https://github.com/burnash/gspread

# GSpread API Docs
# https://gspread.readthedocs.io/en/latest/index.html#

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('oauth_credentials.json', scope)

gc = gspread.authorize(credentials)

# Open a spreadsheet by name
# wks = gc.open("GSpread Test")

# List all worksheets
# worksheet_list = wks.worksheets()
# print worksheet_list

# Open a spreadsheet to a specific worksheet
wks = gc.open("GSpread Test").sheet1

# Open a worksheet from spreadsheet by ID (from URL)
# sheet = gc.open_by_key('1ZlEavc50jFVYt-MZl5I_lpDDNm4zPivP3WWOucF8Yws')
# wks = sheet.sheet1

# Open a worksheet from spreadsheet by URL
# sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZlEavc50jFVYt-MZl5I_lpDDNm4zPivP3WWOucF8Yws')
# wks = sheet.sheet1

# Update a single cell in a worksheet
wks.update_acell('C1', "Write Test!")

# Fetch a cell range from a worksheet
cell_list = wks.range('A1:A2')
print cell_list

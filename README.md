# Google Sheets Python

Simple proof of concept to read and write from Google Sheets using OAuth2 and [gspread](https://github.com/burnash/gspread).

[Documentation on creating auth credentials](https://github.com/burnash/gspread/issues/170#issuecomment-90731740)

## Setup
Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run main.py:

```bash
python main.py
```

## Note about permissions:

Any spreadsheet you intend to access with this library has to first be shared with the client-email generated in your OAuth credentials JSON.

Example email:

```json
"client_email": "python-sheets@api-test-1234567890123.iam.gserviceaccount.com",
```

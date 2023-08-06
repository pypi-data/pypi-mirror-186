### error-alerts
Python error alerts via Telegram

Installation:
`pip install error-alerts`

Options:

`token`: Bot Telegram token.

`channel`: Your Telegram channel ID where you want the alerts to be sent.

`full_error`: Send full traceback with line of code where error occurred (False by default and shown in sample below).

`raise_error`: Raise error and exit code when there is an error. If this is not set to True an alert will be sent and the code will continue running (False by default).

Usage:
```
from error_alerts import telegram

alerts = telegram(token='TELEGRAM_TOKEN', channel=TELEGRAM_CHANNEL_ID, full_error=True, raise_error=True)

try:
    1 / 0
except Exception as error:
    alerts.send(title='Test', exception=error)
```

Output:
```
Test: Traceback (most recent call last):
  File "A:\Code\Python\packages\handler\test.py", line 6, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

Prints that in console and sends a Telegram alert to the channel you specified

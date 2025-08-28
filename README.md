Quick Start

Install dependency:

pip install twilio


Set your credentials (recommended):

export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_FROM="+1234567890"   # your Twilio phone number


Make a phone call:

python make_call.py --to "+9876543210" --message "Hello, this is an automated call from Python."

Notes

Twilio trial accounts require the recipient phone number to be verified.

You’ll be billed at Twilio’s voice call rates.

The message is spoken via Twilio’s built-in Text-to-Speech (TTS).

You can replace the simple <Say> TwiML with more advanced logic (<Play> audio files, menus, etc.).

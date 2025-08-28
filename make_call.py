#!/usr/bin/env python3
"""
make_call.py
Make a phone call using Twilio's programmable voice API.

Usage examples:
  # With environment variables (recommended)
  export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  export TWILIO_AUTH_TOKEN="your_auth_token"
  export TWILIO_FROM="+1234567890"   # Twilio phone number
  python make_call.py --to "+19876543210" --message "Hello, this is an automated call from Python."

Notes:
 - Twilio trial accounts require the recipient number to be verified.
 - Carrier/voice call rates apply.
 - Keep credentials secure (prefer environment variables).
"""

import argparse
import os
import sys

def make_call(account_sid, auth_token, from_number, to_number, message):
    try:
        from twilio.rest import Client
    except Exception as e:
        raise ImportError("twilio package not installed. Run: pip install twilio") from e

    client = Client(account_sid, auth_token)

    # TwiML for what the call should say
    twiml = f'<Response><Say>{message}</Say></Response>'

    call = client.calls.create(
        twiml=twiml,
        to=to_number,
        from_=from_number
    )
    return {"sid": call.sid, "status": call.status}

def parse_args():
    p = argparse.ArgumentParser(description="Make a phone call via Twilio.")
    p.add_argument("--to", required=True, help="Recipient phone number in E.164 format, e.g. +14155552671")
    p.add_argument("--message", required=True, help="Message to say during the call")
    p.add_argument("--account-sid", help="Twilio Account SID (defaults to TWILIO_ACCOUNT_SID env)")
    p.add_argument("--auth-token", help="Twilio Auth Token (defaults to TWILIO_AUTH_TOKEN env)")
    p.add_argument("--from", dest="from_number", help="From phone (Twilio number) (defaults to TWILIO_FROM env)")
    return p.parse_args()

def main():
    args = parse_args()
    account_sid = args.account_sid or os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = args.auth_token or os.getenv("TWILIO_AUTH_TOKEN")
    from_number = args.from_number or os.getenv("TWILIO_FROM")

    if not (account_sid and auth_token and from_number):
        sys.exit("Missing credentials. Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_FROM env vars or pass them via CLI.")

    to_number = args.to
    message = args.message

    result = make_call(account_sid, auth_token, from_number, to_number, message)
    print("Call initiated. Result:", result)

if __name__ == "__main__":
    main()

from twilio.rest import Client
import extract_info as info
import os
from dotenv import load_dotenv


def send_message_to_user(message_text):

    # Twilio credentials (use environment variables for security)
    load_dotenv()
    account_sid = os.getenv('ACCOUNT_SID')  # Replace with your actual account sid
    auth_token = os.getenv('AUTH_TOKEN')  # Replace with your actual auth token

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)


    # Create and send a message
    message = client.messages.create(
        body=message_text,         # The content of the SMS
        from_='$$',      # Replace with your Twilio phone number
        to='$$'         # Replace with the recipient's phone number
    )
    # Print the message SID to confirm successful sending
    print(f"Message sent with SID: {message.sid}")



def main():

    city = str(73) # Replace with your number city from the table in 'https://github.com/t0mer/py-weatheril'

    url = "https://ims.gov.il/he/full_forecast_data/" + city


    message_text = info.extract_info_from_json(url)

    send_message_to_user(message_text)


if __name__ == "__main__":
    main()
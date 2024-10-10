# main.py

from morning_greetings.contact_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message


def main():
    # Initialize the contacts manager
    contact_manager = ContactsManager()

    contacts = contact_manager.get_contacts()

    # Send a message to each contact
    for contact in contacts:
        try:
            message = generate_message(contact['name'])
            send_message(contact, message)
            log_message(contact, message)
        except Exception as e: 
            print(f"Failed to send message to {contact['name']}: {e}")

if __name__ == "__main__":
    main()
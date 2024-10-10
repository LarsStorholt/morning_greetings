# message_sender.py

def send_message(contact, message):
    print(f"Sending message to {contact['name']} ({contact['email']}): {message}")
    # In a real implementation, this would be where the message is sent via SMS, email, etc.
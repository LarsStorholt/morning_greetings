
# ACIT4420 - Assignment 2 - Morning Greeetings 

This Python package automates the process of sending personalized "Good Morning" messages to a list of friends. The package manages contacts, generates customized messages, simulates sending the messages, and logs the messages that were sent.

## Table of Contents
1. [Features](#features)
2. [Package Structure](#package-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modules](#modules)
6. [Error Handling](#error-handling)
7. [Logging](#logging)
8. [License](#license)


## Features
- Manage a list of friends with contact information and preferred greeting time.
- Generate personalized "Good Morning" messages.
- Simulate sending messages to each friend.
- Log messages that have been sent.
- Easy to use and customizable.

## Package Structure
```
morning_greetings/
│
├── setup.py                    # Installation script
├── README.md                   # Documentation for the package
├── LICENSE
   morning_greetings/
   │
   ├── __init__.py              # Marks the directory as a package
   ├── contacts_manager.py      # Manage contacts list
   ├── logger.py                # Log sent messages
   ├── main.py                  # Main script to run the automation task
   ├── message_generator.py     # Generate personalized messages
   ├── message_sender.py        # Simulate sending messages
   ├── message_log.txt          # Log file for messages sent
```

## Installation 

To get started, follow these steps:
1. **Clone the Repository** (or download the package): 
   ```bash
   git clone https://github.com/LarsStorholt/greetings_project.git 
   cd morning_greetings 
   ``` 

2. **Install the Package**:
   ```bash
   pip install -e .
   ```

## Usage 
After installing the package, you can run the automation task by using the following command:
   ```bash
   morning_greetings
   ```
Alternatively, you can run the main script directly:
   ```bash
   python -m morning_greetings.main
   ```

This will:

1. Retrieve the contact list.
2. Generate a personalized message for each contact.
3. Simulate sending the message.
4. Log the sent messages to message_log.txt.

### Customization
* Add or modify contacts using the contacts_manager.py module.
* Customize the message templates using the message_generator.py module.

## Modules 
- **`main.py`**: Contains the main function that launches the program.
- **`setup.py`**: Script for installing the package.
- **`contacts_manager.py`**: Manages the list of contacts. You can add, remove, and retrieve contacts with their name, email, and preferred greeting time.
- **`message_generator.py`**: Generates a personalized "Good Morning" message for each contact based on their name.
- **`message_sender.py`**: Simulates sending the message by printing it to the console and can be extended to integrate actual email-sending logic
- **`logger.py`**: Logs the message sent along with the timestamp to a log file (message_log.txt).

## Error handling 
The package includes basic error handling for:

- Missing email addresses when sending a message.
- Attempting to send messages to an empty contact list.

## Logging 
All messages that are "sent" are logged in the message_log.txt file, including timestamps and recipient names.

## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.

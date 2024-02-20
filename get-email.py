import imaplib

def search_email_by_sender(sender_email, username, password):
    # Connect to the Gmail IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_server.login(username, password)

    # Select the mailbox you want to search in (e.g., 'INBOX')
    imap_server.select('INBOX')

    # Search for emails from the specified sender
    search_criteria = f'(FROM "{sender_email}")'
    _, email_ids = imap_server.search(None, search_criteria)

    # Fetch the email details for each matching email
    for email_id in email_ids[0].split():
        _, email_data = imap_server.fetch(email_id, '(RFC822)')
        print(email_data[0][1])

    # Close the connection to the IMAP server
    imap_server.close()
    imap_server.logout()

# Example usage
sender_email = 'example@gmail.com'
username = 'your_username@gmail.com'
password = 'your_password'
search_email_by_sender(sender_email, username, password)

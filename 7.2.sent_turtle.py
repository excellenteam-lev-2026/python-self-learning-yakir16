import math

class PostOffice:
    """
    A Post Office class. Allows users to message each other.

    Message structure changes:
    We have added the following fields to the dictionary of each message:
    'title': The title of the message
    'read': A boolean that shows whether the message has already been read
    because read_inbox and search_inbox need to know which messages have been read
    and allow searching in the title as well as the message body.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, title="", urgent=False):
        """
        Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            title (str, optional): The message title. Defaults to empty string.
            urgent (bool, optional): If True, message goes to the top of inbox.

        Returns:
            int: Unique message ID.
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,  # כותרת ההודעה
            'body': message_body,  # גוף ההודעה
            'sender': sender,
            'read': False
        }
        user_box = self.boxes[recipient]
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N=None):
        """
        Return the first N unread messages from a user's inbox.
        Marks messages as read so they won't be returned again.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        inbox = self.boxes[username]
        unread_messages = [msg for msg in inbox if not msg['read']]
        messages_to_return = unread_messages[:N] if N else unread_messages

        for msg in messages_to_return:
            msg['read'] = True

        return messages_to_return

    def search_inbox(self, username, keyword):
        """
        Search for messages containing a keyword in title or body.

        Args:
            username (str): The user's username.
            keyword (str): The search string.

        Returns:
            list: List of messages containing the keyword in title or body.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        inbox = self.boxes[username]
        keyword_lower = keyword.lower()
        results = [
            msg for msg in inbox
            if keyword_lower in msg['title'].lower() or keyword_lower in msg['body'].lower()
        ]
        return results


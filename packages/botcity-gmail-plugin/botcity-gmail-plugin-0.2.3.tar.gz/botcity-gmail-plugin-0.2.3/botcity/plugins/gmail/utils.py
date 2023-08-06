from enum import Enum

from imap_tools import MailMessage


class BotGmailMessage(MailMessage):

    def _set_message_response(self, msg_response):
        self._msg_response = msg_response

    def _set_message_labels(self, labels_name):
        self._msg_labels = labels_name

    @property
    def id_(self):
        """
        The id of the gmail message
        """
        return str(self._msg_response.get('id'))

    @property
    def thread_id(self):
        """
        The thread id of the gmail message
        """
        return str(self._msg_response.get('threadId'))

    @property
    def labels(self):
        """
        The message labels
        """
        return self._msg_labels


class GmailDefaultLabels(str, Enum):
    """
    The class with the enumerated Gmail dafault labels
    Usage: GmailDefaultLabels.<LABEL_NAME>
    """
    INBOX = "INBOX"
    SPAM = "SPAM"
    TRASH = "TRASH"
    UNREAD = "UNREAD"
    STARRED = "STARRED"
    IMPORTANT = "IMPORTANT"
    SENT = "SENT"
    DRAFT = "DRAFT"
    CATEGORY_PERSONAL = "CATEGORY_PERSONAL"
    CATEGORY_SOCIAL = "CATEGORY_SOCIAL"
    CATEGORY_PROMOTIONS = "CATEGORY_PROMOTIONS"
    CATEGORY_UPDATES = "CATEGORY_UPDATES"
    CATEGORY_FORUMS = "CATEGORY_FORUMS"

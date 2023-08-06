import base64
import os
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from .utils import BotGmailMessage, GmailDefaultLabels


class BotGmailPlugin:
    def __init__(self, credentials_file_path: str, user_email: str) -> None:
        """
        BotGmailPlugin

        Args:
            credentials_file_path (str): The path of the credentials json file obtained at Google Cloud Platform.
            user_email (str): The email used to create the credentials.
        """
        # Credentials
        self.user_email = user_email
        self.creds = None
        self.gmail_service = None
        self.scopes = ['https://www.googleapis.com/auth/gmail.modify']

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        credentials_dir = os.path.abspath(os.path.dirname(credentials_file_path))

        if os.path.exists(os.path.join(credentials_dir, 'token.json')):
            self.creds = Credentials.from_authorized_user_file(
                os.path.join(credentials_dir, 'token.json'), self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.path.abspath(credentials_file_path), self.scopes)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(os.path.join(credentials_dir, 'token.json'), 'w') as token:
                token.write(self.creds.to_json())

        self.gmail_service = build('gmail', 'v1', credentials=self.creds)

    def search_messages(self, criteria: str = None, default_labels: List[GmailDefaultLabels] = None,
                        customized_labels: List[str] = None, mark_read=False, timeout=0) -> List[BotGmailMessage]:
        """
        Search for messages based on criteria and labels.
        [See how to use and more details about searches](https://support.google.com/mail/answer/7190)

        To see the labels that are available in the email, use get_mail_labels()
        [See more details about messages labels](https://developers.google.com/gmail/api/guides/labels)

        Args:
            criteria (str, optional): The criteria that will be used as a message filter.
            default_labels (List[GmailDefaultLabels], optional): The list with the names of the labels defined
                                in the GmailDefaultLabels class, which will be considered in the message filter.
            customized_labels (List[str], optional): The list with the names of the labels created by user
                                                     which will be considered in the message filter.
            mark_read (boolean, optional): Whether the email should be marked as read. Defaults to False.
            timeout (int, optional): Wait for a new message until this timeout.
                                    Defaults to 0 seconds (don't wait for new messages).
        """
        # Validating labels
        labels = []
        if not default_labels and not customized_labels:
            labels = [GmailDefaultLabels.INBOX.value]
        else:
            labels = self._get_labels_ids_list(default_labels, customized_labels)

        start_time = time.time()
        messages_list = []

        while True:
            time.sleep(1)
            result = self.gmail_service.users().messages().list(userId='me', q=criteria, labelIds=labels).execute()
            messages = result.get('messages')

            if messages:
                for msg in messages:
                    msg_content = self.gmail_service.users().messages().get(userId='me',
                                                                            id=msg['id'], format='raw').execute()
                    msg_bytes = base64.urlsafe_b64decode(msg_content['raw'].encode("utf-8"))

                    new_msg = BotGmailMessage.from_bytes(msg_bytes)
                    new_msg._set_message_response(msg)
                    new_msg._set_message_labels(self._get_labels_name(msg_content.get('labelIds')))
                    messages_list.append(new_msg)

                    if mark_read:
                        self.mark_as_read(new_msg)
                return messages_list
            elapsed_time = (time.time() - start_time)
            if elapsed_time > timeout:
                return []

    def send_message(self, subject: str, text_content: str, to_addrs: List[str], cc_addrs: List[str] = None,
                     bcc_addrs: List[str] = None, attachments: List[str] = None, use_html: bool = False) -> None:
        """
        Send a new email message.

        Args:
            subject (str): The subject of the email.
            text_content (str): The content of the email body.
            to_addrs (List[str]): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
            use_html (bool): The boolean value when you want to use body in html format.
        """
        new_message = self.__build_message(text_content, to_addrs, cc_addrs, bcc_addrs, attachments, use_html)
        new_message["Subject"] = subject
        message = {'raw': base64.urlsafe_b64encode(new_message.as_bytes()).decode()}

        self.gmail_service.users().messages().send(userId="me", body=message).execute()

    def reply(self, msg: BotGmailMessage, text_content: str, attachments: List[str] = None,
              to_addrs: List[str] = None, cc_addrs: List[str] = None, bcc_addrs: List[str] = None) -> None:
        """
        Reply a received email message.

        Args:
            msg (BotGmailMessage): The message to reply.
            text_content (str): The content of the email body.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
            to_addrs (List[str], optional): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
        """
        to = to_addrs or [msg.from_]
        reply_msg = self.__build_message(text_content, to, cc_addrs, bcc_addrs, attachments)
        reply_msg["References"] = reply_msg["In-Reply-To"] = msg.headers.get('message-id')[0]
        reply_msg["Subject"] = "Re: " + msg.subject

        message = {'raw': base64.urlsafe_b64encode(reply_msg.as_bytes()).decode(),
                   'threadId': msg.thread_id}

        self.gmail_service.users().messages().send(userId="me", body=message).execute()

    def reply_to_all(self, msg: BotGmailMessage, text_content: str, attachments: List[str] = None) -> None:
        """
        Replies to all email addresses included in the original message.

        Args:
            msg (BotGmailMessage): The message to reply.
            text_content (str): The content of the email body.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
        """
        emails_addrs = list(msg.to) + list(msg.cc)
        to = [msg.from_]
        cc = [addr for addr in emails_addrs if addr != self.user_email]
        self.reply(msg, text_content, attachments, to, cc)

    def forward(self, msg: BotGmailMessage, to_addrs: List[str], cc_addrs: List[str] = None,
                bcc_addrs: List[str] = None, include_attachments=True) -> None:
        """
        Forward a received email message.

        Args:
            msg (BotGmailMessage): The message to forward.
            to_addrs (List[str]): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
            include_attachments (boolean, optional): Include attachments from the original message.
        """
        forwarded_message = self.__build_message(msg.text, to_addrs, cc_addrs, bcc_addrs, is_forwarded=True)
        forwarded_message["Subject"] = "Fwd: " + msg.subject
        if include_attachments:
            for part in msg.attachments:
                attachment = MIMEBase("application", "octet-stream")
                attachment.set_payload(part.payload)
                encoders.encode_base64(attachment)
                attachment.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {part.filename}",
                )
                forwarded_message.attach(attachment)

        message = {'raw': base64.urlsafe_b64encode(forwarded_message.as_bytes()).decode()}
        self.gmail_service.users().messages().send(userId="me", body=message).execute()

    def download_attachments(self, msg: BotGmailMessage, download_folder_path: str) -> None:
        """
        Download attachments from a given email message.

        Args:
            msg (BotGmailMessage): The message that contains the attachments.
            download_folder_path (str): The path of the folder where the files will be saved.
        """
        attachments = msg.attachments
        if attachments:
            for file in attachments:
                with open(os.path.join(download_folder_path, file.filename), "wb") as f:
                    f.write(file.payload)

    def mark_as_read(self, msg: BotGmailMessage) -> None:
        """
        Mark a email message as read.

        Args:
            msg (BotGmailMessage): The message to be marked.
        """
        response = self.gmail_service.users().messages().modify(userId='me', id=msg.id_, body={
            'removeLabelIds': ['UNREAD']
        }).execute()
        msg._set_message_labels(self._get_labels_name(response.get('labelIds')))

    def mark_as_unread(self, msg: BotGmailMessage) -> None:
        """
        Mark a email message as unread.

        Args:
            msg (BotGmailMessage): The message to be marked.
        """
        response = self.gmail_service.users().messages().modify(userId='me', id=msg.id_, body={
            'addLabelIds': ['UNREAD']
        }).execute()
        msg._set_message_labels(self._get_labels_name(response.get('labelIds')))

    def delete(self, msg: BotGmailMessage) -> None:
        """
        Move a email message to trash.

        Args:
            msg (BotGmailMessage): The message to be deleted.
        """
        self.gmail_service.users().messages().trash(userId='me', id=msg.id_).execute()

    def get_mail_labels(self) -> List[dict]:
        """
        Get all valid labels from email.

        Returns:
            List[dict]: The list containing the name and id of each label found as a dictionary.
        """
        results = self.gmail_service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        labels_list = []
        for label in labels:
            lb = {'name': label.get('name'), 'id': label.get('id')}
            labels_list.append(lb)
        return labels_list

    def create_new_label(self, label_name: str) -> None:
        """
        Create a new label on email.

        Args:
            label_name (str): The name of the label to be created.
        """
        self.gmail_service.users().labels().create(userId='me', body={
            'name': label_name
        }).execute()

    def add_labels_to_message(self, msg: BotGmailMessage, default_labels: List[GmailDefaultLabels] = None,
                              customized_labels: List[str] = None) -> None:
        """
        Add default and custom labels to the message.

        Args:
            msg (BotGmailMessage): The message that will receive the labels.
            default_labels (List[GmailDefaultLabels], optional): The list with the names of the labels defined
                                in the GmailDefaultLabels class.
            customized_labels (List[str], optional): The list with the names of the labels created by user.
        """
        if default_labels or customized_labels:
            labels_id = self._get_labels_ids_list(default_labels, customized_labels)
            response = self.gmail_service.users().messages().modify(userId='me', id=msg.id_, body={
                'addLabelIds': labels_id
            }).execute()
            msg._set_message_labels(self._get_labels_name(response.get('labelIds')))

    def remove_labels_from_message(self, msg: BotGmailMessage, default_labels: List[GmailDefaultLabels] = None,
                                   customized_labels: List[str] = None) -> None:
        """
        Remove default and custom labels from the message.

        Args:
            msg (BotGmailMessage): The message that will have the labels removed.
            default_labels (List[GmailDefaultLabels], optional): The list with the names of the labels defined
                                in the GmailDefaultLabels class.
            customized_labels (List[str], optional): The list with the names of the labels created by user.
        """
        if default_labels or customized_labels:
            labels_id = self._get_labels_ids_list(default_labels, customized_labels)
            response = self.gmail_service.users().messages().modify(userId='me', id=msg.id_, body={
                'removeLabelIds': labels_id
            }).execute()
            msg._set_message_labels(self._get_labels_name(response.get('labelIds')))

    def _get_label_id(self, mail_labels: List[dict], label_name: str) -> str:
        for label in mail_labels:
            if label_name == label.get('name'):
                return label.get('id')
        raise ValueError(f'''The label "{label_name}" was not found.
            Maybe the name is incorrect or the label doesn't exist.
            Use get_mail_labels() to see all valid labels name you can use.''')

    def _get_labels_ids_list(self, default_labels: List[GmailDefaultLabels],
                             customized_labels: List[str]) -> List[str]:
        labels_id = []

        if default_labels:
            for label in default_labels:
                labels_id.append(label.value)
        if customized_labels:
            all_labels = self.get_mail_labels()
            for label in customized_labels:
                labels_id.append(self._get_label_id(all_labels, label))
        return labels_id

    def _get_labels_name(self, labels_id: List[str]) -> List[str]:
        labels_name = []
        for label_id in labels_id:
            label = self.gmail_service.users().labels().get(userId='me', id=label_id).execute()
            labels_name.append(label.get('name'))
        return labels_name

    def __build_message(self, text_content: str, to_addrs: List[str], cc_addrs: List[str] = None,
                        bcc_addrs: List[str] = None, attachments: List[str] = None,
                        use_html=False, is_forwarded=False) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.user_email

        to = ", ".join(to_addrs)
        message["To"] = to

        if cc_addrs:
            cc = ", ".join(cc_addrs)
            message["Cc"] = cc

        if bcc_addrs:
            bcc = ", ".join(bcc_addrs)
            message["Bcc"] = bcc

        # Add body to email
        if use_html:
            text_message = MIMEText(text_content, "html")
        else:
            text_message = MIMEText(text_content, "plain")
        message.attach(text_message)

        if is_forwarded:
            return message

        # If it contains attachments, add each one to the email body
        if attachments:
            for file in attachments:
                with open(file, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(file)}",
                )
                # Add the attachment in the email message
                message.attach(part)
        return message

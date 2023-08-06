import os
import smtplib
import ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum
from typing import List

from imap_tools import AND, MailBox, MailMessage
from imap_tools.mailbox import MailBoxTls

from .servers_config import DEFAULT_SERVERS_CONFIG, MailServers
from .utils import if_imap_configured, if_smtp_configured


class MailFilters(str, Enum):
    """
    The class with the enumerated attributes that can be used in the filter
    Usage: MailFilters.<ATTRIBUTE_NAME>
    """
    SEEN = "seen"
    FROM = "from_"
    TO = "to"
    CC = "cc"
    BCC = "bcc"
    SUBJECT = "subject"
    TEXT_CONTENT = "text"
    ON_DATE = "date"
    DATE_GREATER_THAN = "date_gte"
    DATE_LESS_THAN = "date_lt"


class BotEmailPlugin:
    def __init__(self):
        """
        BotEmailPlugin
        """
        self._imap_mail = None
        self._smtp_mail = None
        self._user_email = None
        self._user_password = None

    @classmethod
    def config_email(cls, server: MailServers, email: str, password: str):
        """
        Configures the IMAP and SMTP with the default configuration from the server
        and login with an email account.

        Args:
            server (BotMailServers): The server defined in the BotMailServers class that will
                                    be used in the configuration.
            email (str): The user email.
            password (str): The user password.

        Returns:
            BotEmailPlugin: A configured email instance.
        """
        configs = DEFAULT_SERVERS_CONFIG.get(server)
        if not configs:
            raise ValueError(f'''The default settings from "{server}" server is not available at the moment.
            The servers currently available are: {list(map(lambda s: s.value, MailServers))}''')

        mail = cls()
        mail.configure_imap(configs.get("imap_server"), configs.get("imap_port"), configs.get("imap_tls_ssl"))
        mail.configure_smtp(configs.get("smtp_server"), configs.get("smtp_port"), configs.get("smtp_tls_ssl"))
        mail.login(email, password)
        return mail

    def configure_imap(self, host_address="imap.gmail.com", port=993, tls_ssl=False) -> None:
        """
        Configures the IMAP server.

        Args:
            host_address (str, optional): The email host address to use. Defaults to Gmail server.
            port (int, optional): The port that will be used by the IMAP server. Defaults to 993.
            tls_ssl (boolean, optional): Whether tls/ssl protocols will be used.
        """
        if tls_ssl:
            self._imap_mail = MailBoxTls(host=host_address, port=port)
        else:
            self._imap_mail = MailBox(host=host_address, port=port)

    def configure_smtp(self, host_address="smtp.gmail.com", port=587, tls_ssl=True) -> None:
        """
        Configures the SMTP server.

        Args:
            host_address (str, optional): The email host address to use. Defaults to Gmail server.
            port (int, optional): The port that will be used by the SMTP server. Defaults to 587.
            tls_ssl (boolean, optional): Whether tls/ssl protocols will be used.
        """
        if tls_ssl:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS)
            self._smtp_mail = smtplib.SMTP(host=host_address, port=port)
            self._smtp_mail.starttls(context=context)
        else:
            self._smtp_mail = smtplib.SMTP_SSL(host=host_address, port=port)

    def login(self, email: str, password: str) -> None:
        """
        Log in with a valid email account.

        Args:
            email (str): The user email.
            password (str): The user password.
        """
        self._user_email = email
        self._user_password = password

        if not self._imap_mail and not self._smtp_mail:
            raise ValueError("before login it is necessary to configure at less an IMAP or SMTP server.")
        if self._smtp_mail:
            self._smtp_mail.login(user=email, password=password)
        if self._imap_mail:
            self._imap_mail.login(username=email, password=password)

    def disconnect(self) -> None:
        """
        Close the connection with de IMAP and SMTP server.
        """
        if self._smtp_mail:
            self._smtp_mail.close()
        if self._imap_mail:
            self._imap_mail.logout()

    ##############
    # IMAP methods
    ##############
    @if_imap_configured
    def get_folders(self) -> List[str]:
        """
        Get a list of available email folders.

        Returns:
            List[str]: The list containing the name of the folders.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        mailboxes = []
        for folder in self._imap_mail.folder.list():
            mailboxes.append(folder.name)
        return mailboxes

    @if_imap_configured
    def select_folder(self, folder="INBOX") -> None:
        """
        Select the folder that will be used as a reference.

        Args:
            folder (str, optional): The folder name. Defaults to INBOX, to see the available
                folders use get_folders().

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.folder.set(folder=folder)

    @if_imap_configured
    def search(self, criteria="ALL", mark_read=False, timeout=0) -> List[MailMessage]:
        """
        Searches for all emails based on criteria.
        See about search strings here: https://www.marshallsoft.com/ImapSearch.htm

        Args:
            criteria (str, optional): The criteria to be used in the search. Defaults to 'ALL',
                                    in this case all emails in the folder will be returned.
            mark_read (boolean, optional): Whether the email should be marked as read. Defaults to False.
            timeout (int, optional): Wait for a new message until this timeout.
                                    Defaults to 0 seconds (don't wait for new messages).

        Returns:
            List[MailMessage]: The list of emails found.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        start_time = time.time()

        if 'IDLE' in self._imap_mail.client.capabilities:
            while True:
                self._imap_mail.idle.wait(1)
                mail_messages = list(self._imap_mail.fetch(criteria=criteria, mark_seen=mark_read))
                if mail_messages:
                    return mail_messages
                elapsed_time = (time.time() - start_time)
                if elapsed_time > timeout:
                    return []
        else:
            mail_messages = list(self._imap_mail.fetch(criteria=criteria, mark_seen=mark_read))
            return mail_messages

    @if_imap_configured
    def filter_by(self, filter: MailFilters, value, timeout=0) -> List[MailMessage]:
        """
        Searches for all emails based on a specific filter.

        Args:
            filter (BotMailFilters): The attribute defined in the BotMailFilters class that will
                                    be used in the filter.
            value: The value of the selected filter.
            timeout (int, optional): Wait for a new message until this timeout.
                                    Defaults to 0 seconds (don't wait for new messages).

        Returns:
            List[MailMessage]: The list of emails found.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        start_time = time.time()
        criteria = {filter: value}

        if 'IDLE' in self._imap_mail.client.capabilities:
            while True:
                self._imap_mail.idle.wait(1)
                mail_messages = list(self._imap_mail.fetch(AND(**criteria)))
                if mail_messages:
                    return mail_messages
                elapsed_time = (time.time() - start_time)
                if elapsed_time > timeout:
                    return []
        else:
            mail_messages = list(self._imap_mail.fetch(AND(**criteria)))
            return mail_messages

    @if_imap_configured
    def delete(self, message: MailMessage) -> None:
        """
        Delete a email message from current folder.

        Args:
            message (MailMessage): The message to be deleted.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.delete(message.uid)

    @if_imap_configured
    def move(self, message: MailMessage, folder: str) -> None:
        """
        Move a email message from current folder to a destination folder.

        Args:
            message (MailMessage): The message to be moved.
            folder (str): The name of the destination folder.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.move(message.uid, folder)

    @if_imap_configured
    def copy(self, message: MailMessage, folder: str) -> None:
        """
        Copy a email message from current folder to a destination folder.

        Args:
            message (MailMessage): The message to be copied.
            folder (str): The name of the destination folder.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.copy(message.uid, folder)

    @if_imap_configured
    def mark_as_read(self, msg: MailMessage) -> None:
        """
        Mark a received email message as read.

        Args:
            msg (MailMessage): The message to mark.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.flag(msg.uid, "\\SEEN", True)

    @if_imap_configured
    def mark_as_unread(self, msg: MailMessage) -> None:
        """
        Mark a received email message as unread.

        Args:
            msg (MailMessage): The message to mark.

        Note:
            This method can only be used with an **IMAP** server configured.
        """
        self._imap_mail.flag(msg.uid, "\\SEEN", False)

    def download_attachments(self, message: MailMessage, download_folder_path: str) -> None:
        """
        Download attachments from a given email message.

        Args:
            message (MailMessage): The message that contains the attachments.
            download_folder_path (str): The path of the folder where the files will be saved.
        """
        attachments = message.attachments
        if attachments:
            for file in attachments:
                with open(os.path.join(download_folder_path, file.filename), "wb") as f:
                    f.write(file.payload)

    ##############
    # SMTP methods
    ##############
    @if_smtp_configured
    def send_message(self, subject: str, text_content: str, to_addrs: List[str], cc_addrs: List[str] = None,
                     bcc_addrs: List[str] = None, attachments: List[str] = None, use_html: bool = False) -> None:
        """
        Send an email message through the SMTP protocol.

        Args:
            subject (str): The subject of the email.
            text_content (str): The content of the email body.
            to_addrs (List[str]): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
            use_html (bool): The boolean value when you want to use body in html format.

        Note:
            This method can only be used with an **SMTP** server configured.
        """
        message = self.__build_message(text_content, to_addrs, cc_addrs, bcc_addrs, attachments, use_html=use_html)
        message["Subject"] = subject
        self._smtp_mail.send_message(message)

    @if_smtp_configured
    def reply(self, msg: MailMessage, text_content: str, attachments: List[str] = None,
              to_addrs: List[str] = None, cc_addrs: List[str] = None, bcc_addrs: List[str] = None,
              use_html: bool = False) -> None:
        """
        Reply a received email message.

        Args:
            msg (MailMessage): The message to reply.
            text_content (str): The content of the email body.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
            to_addrs (List[str], optional): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
            use_html (bool): The boolean value when you want to use body in html format.

        Note:
            This method can only be used with an **SMTP** server configured.
        """
        to = to_addrs or [msg.from_]
        reply_msg = self.__build_message(text_content, to, cc_addrs, bcc_addrs, attachments, use_html=use_html)
        reply_msg["References"] = reply_msg["In-Reply-To"] = msg.uid
        reply_msg["Subject"] = "Re: " + msg.subject
        self._smtp_mail.send_message(reply_msg)

    def reply_to_all(self, msg: MailMessage, text_content: str, attachments: List[str] = None,
                     use_html: bool = False) -> None:
        """
        Replies to all email addresses included in the original message.

        Args:
            msg (Message): The message to reply.
            text_content (str): The content of the email body.
            attachments (List[str], optional): The list with the paths of the files that will be sent
                as attachments.
            use_html (bool): The boolean value when you want to use body in html format.

        Note:
            This method can only be used with an **SMTP** server configured.
        """
        emails_addrs = list(msg.to) + list(msg.cc)
        to = [msg.from_]
        cc = [addr for addr in emails_addrs if addr != self._user_email]
        self.reply(msg, text_content, attachments, to, cc, use_html=use_html)

    @if_smtp_configured
    def forward(self, msg: MailMessage, to_addrs: List[str], cc_addrs: List[str] = None,
                bcc_addrs: List[str] = None, include_attachments=True, use_html: bool = False) -> None:
        """
        Forward a received email message.

        Args:
            msg (Message): The message to forward.
            to_addrs (List[str]): The list of email addresses that will receive the message.
            cc_addrs (List[str], optional): The list of email addresses that will receive the message as CC.
            bcc_addrs (List[str], optional): The list of email addresses that will receive the message as BCC.
            include_attachments (boolean, optional): Include attachments from the original message.
            use_html (bool): The boolean value when you want to use body in html format.

        Note:
            This method can only be used with an **SMTP** server configured.
        """
        forwarded_message = self.__build_message(msg.text, to_addrs, cc_addrs, bcc_addrs, is_forwarded=True,
                                                 use_html=use_html)
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
        self._smtp_mail.send_message(forwarded_message)

    def __build_message(self, text_content: str, to_addrs: List[str], cc_addrs: List[str] = None,
                        bcc_addrs: List[str] = None, attachments: List[str] = None,
                        is_forwarded=False, use_html=False) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self._user_email

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

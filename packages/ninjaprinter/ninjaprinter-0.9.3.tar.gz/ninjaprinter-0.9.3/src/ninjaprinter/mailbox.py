import logging
import imaplib
import os
import smtplib
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import imap_tools
from mako.lookup import TemplateLookup

logger = logging.getLogger(__name__)

class LoginError(Exception):
    """Exception raised for errors during login."""

    def __init__(self, message):
        super().__init__(message)


class MailBox():
    """Object used to interact with a mailbox using smtp/imap, e.g. retrieving and sending email."""

    def __init__(self, *, imap_url: str, smtp_url: str, smtp_port: int):
        self.imap_url = imap_url
        self.smtp_url = smtp_url
        self.smtp_port = smtp_port
        self.username = None
        self.smtp = None
        self.imap = None

    def connect(self, username: str, password: str) -> None:
        """Connect to the imap and smtp hosts using the provided username and password."""
        # IMAP: connect to mailbox for receiving emails
        self.username = username
        try:
            self.imap = imap_tools.MailBox(self.imap_url).login(username, password)
            logger.debug("connected to imap host")
        except (imaplib.IMAP4.error, Exception) as err:
            raise LoginError(f"Error during login with imap mail host on {self.imap_url}") from err

        # SMTP: connect to mailbox for sending emails
        try:
            self.smtp = smtplib.SMTP_SSL(self.smtp_url, self.smtp_port)
            self.smtp.login(username, password)
            logger.debug("connected to smtp host")
        except (smtplib.SMTPAuthenticationError, Exception) as err:
            self.imap.logout()
            raise LoginError(f"Error during login with smtp mail host on {self.smtp_url}") from err

    def disconnect(self) -> None:
        """Close the connections with the imap and smtp hosts."""
        self.imap.logout()
        self.smtp.quit()

    def send_mail(self, template: str, to: str, subject: str, data: dict) -> bool:
        """Compose and send mail message based on active connection with smtp host, original mail 
        message and print status of attachments. Returns whether message was sent successfully."""
        # Message elements
        dir_path = os.path.dirname(os.path.abspath(__file__))
        template_lookup = TemplateLookup(directories=["templates/", f"{dir_path}/templates/"])
        message = template_lookup.get_template(template).render(data=data)
        sender = self.username
        time = strftime("%Y-%m-%d %H:%M:%S")
        msg = MIMEMultipart('alternative')
        msg["From"] = self.username
        msg["To"] = to
        msg["Subject"] = f"{template_lookup.get_template('subject.txt').render()}: {subject} ({time})"
        msg.attach(MIMEText(message, 'html'))

        # Send message
        try:
            self.smtp.sendmail(sender, to, msg.as_string())
            logger.info(f"sent email to {to}")
        except Exception as err:
            logger.error(f"raised during sending of email: {err}")
            return False
        return True

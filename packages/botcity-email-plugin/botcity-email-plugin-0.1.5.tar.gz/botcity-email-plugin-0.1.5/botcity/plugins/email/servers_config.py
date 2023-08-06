from enum import Enum


class MailServers(str, Enum):
    """
    The class with the enumerated servers that have default settings available
    Usage: MailServers.<SERVER_NAME>
    """
    GMAIL = "gmail"
    OUTLOOK = "outlook"


DEFAULT_SERVERS_CONFIG = {
    "gmail": {
        "imap_server": "imap.gmail.com",
        "imap_port": 993,
        "imap_tls_ssl": False,
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "smtp_tls_ssl": True
    },

    "outlook": {
        "imap_server": "imap-mail.outlook.com",
        "imap_port": 993,
        "imap_tls_ssl": False,
        "smtp_server": "smtp-mail.outlook.com",
        "smtp_port": 587,
        "smtp_tls_ssl": True
    }
}

import time
import threading
from collections import OrderedDict
import re
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback


class SMTP_EMailer(object):
    """
    Asynchronous email sender.

    mailer = SMTP_EMailer(...)
    msg = mailer.create_message("to@address, "my subject", "message body")
    mailer.send(msg)

    When messages are sent, a background thread is created, and this thread will persist until there are no more
    messages for some period of time.
    """

    def __init__(self, host, port, user, pwd, sender, logger: callable=None):
        """
        :param host:        Host name of mail sender.
        :param port:        Port for mail send interface.
        :param user:        Username for authentication.
        :param pwd:         Password for authentication.
        :param sender:      Email address of sender.
        :param logger:      Method for reporting emails sent, failed, etc..  Takes one argument, a {}.
        """
        self.host, self.port, self.user, self.pwd, self.sender = host, port, user, pwd, sender
        self.logger = logger
        self.running = False
        self.run_lock = threading.RLock()
        self.queue = []
        # after all messages have been sent, we wait a bit to see if more come in
        self.wait_for_more_messages = 2
        # timeout for SMTP server connection
        self.connection_timeout = 60

    def create_message(self, to=None, subject=None, body=None, attachments=None):
        """
        Build an object that holds a message.  You can fill in the fields in the call, or after, on the returned
        object.
        :param to:          Target email address (string), or a list of email strings, or a comma-delimited string.
        :param subject:     Subject line.
        :param body:        Plaintext body of email, or an array with plaintext and html versions.
        :param attachments: A {} of name->content, or an iteration of tuples with (name,content,mimeType).
        """
        msg = EMail(to, subject, body, sender=self.sender)
        if attachments:
            if isinstance(attachments, dict):
                for name, content in attachments.items():
                    msg.attach(name, content)
            else:
                for spec in attachments:
                    name, content = spec[:2]
                    mime_type = spec[2] if len(spec) >= 3 else None
                    msg.attach(name, content, mime_type)
        return msg

    def _connect(self):
        """
        Connect to the server.
        """
        conn = smtplib.SMTP(host=self.host, port=self.port, timeout=self.connection_timeout)
        conn.starttls(keyfile=None, certfile=None)
        conn.login(self.user, self.pwd)
        return conn

    def _send(self, conn, msg):
        try:
            conn.sendmail(from_addr=self.sender, to_addrs=msg.to, msg=msg.prepare())
            for n in msg.notify:
                n(msg, None)
            if self.logger:
                self.logger({"send_email": {"to": msg.to}})
        except Exception as err:
            if self.logger:
                self.logger({"send_email_failed": {"to": msg.to, "err": repr(err), "trace": traceback.format_exc()}})
            for n in msg.notify:
                n(msg, err)
            raise

    def _run_loop(self):
        conn = self._connect()
        while True:
            with self.run_lock:
                if not self.queue:
                    self.running = False
                    break
            while self.queue:
                msg = self.queue.pop(0)
                try:
                    self._send(conn, msg)
                except Exception:
                    pass
            time.sleep(self.wait_for_more_messages)
        conn.quit()

    def _ensure_connection(self):
        """
        Open the connection to the remote SMTP server, if a connection is not already open.
        """
        def runner():
            try:
                self._run_loop()
            except Exception as err:
                if self.logger:
                    self.logger({"email_connection_failed": {"err": repr(err), "trace": traceback.format_exc()}})
            finally:
                self.running = False
        with self.run_lock:
            if not self.running:
                self.running = True
                t = threading.Thread(target=runner, name="smtp_emailer")
                t.start()

    def send(self, messages):
        """
        Send asynchronously.
        Adds a message (or messages) to the queue and makes sure a thread/connection are running to send it.
        """
        if not isinstance(messages, list):
            messages = [messages]
        if not messages:
            return
        for message in messages:
            assert isinstance(message, EMail)
            self.queue.append(message)
        self._ensure_connection()

    def send_now(self, messages):
        """
        Send a message (or messages) immediately.
        """
        if not isinstance(messages, list):
            messages = [messages]
        if not messages:
            return
        conn = self._connect()
        for msg in messages:
            assert isinstance(msg, EMail)
            self._send(conn, msg)
        conn.quit()


class MockMailer(object):
    def __init__(self, from_addr):
        self.from_addr = from_addr
        self.messages = []

    def create_message(self, to, subject, body, attachments=None):
        return EMail(to, subject, body, sender=self.from_addr)

    def send(self, messages):
        if not isinstance(messages, list):
            messages = [messages]
        for msg in messages:
            self.messages.append({"to": msg.to, "subject": msg.subject, "body": msg.body})
            # notify of send
            for n in msg.notify:
                n(msg, None)

    def send_now(self, messages):
        self.send(messages)


class NullMailer(object):
    def create_message(self, to, subject, body, attachments=None):
        return EMail(to, subject, body, sender="na@na.na")

    def send(self, messages):
        """ placeholder """

    def send_now(self, messages):
        """ placeholder """


class EMail(object):
    """
    Holds content of an email.
    """
    def __init__(self, to=None, subject=None, body=None, sender=None):
        """
        :param to:  Target email address.  Can contain multiple emails delimited by comma (whitespace ok too).
        :param sender: Return email address.
        :param subject: Subject line.
        :param body:  Either a string, for a plain text email, or a tuple of two strings, with the plaintext
          and HTML versions respectively.
        """
        self.to = split_emails(to)
        if not self.to:
            raise ValueError("missing recipient email")
        self.subject = subject
        self.body = body
        self.sender = sender
        self.attachments = OrderedDict()
        self.more = {}
        self.notify = []

    def reply_to(self, v):
        self.more["Reply-To"] = v

    def send_notification(self, notifier: callable):
        """
        Add a notification listener.  It will be called with the email, and None or an exception.
        """
        self.notify.append(notifier)

    def _common_setup(self, msg):
        msg["Subject"] = self.subject
        msg["From"] = self.sender
        if isinstance(self.to, str):
            msg["To"] = self.to
        else:
            msg["To"] = ", ".join(self.to)
        for k, v in self.more.items():
            msg[k] = v

    def prepare(self):
        if isinstance(self.body, str) and not self.attachments:
            msg = MIMEText(self.body)
            self._common_setup(msg)
        else:
            msg = MIMEMultipart('alternative')
            self._common_setup(msg)
            body = self.body
            if isinstance(body, str):
                body = [body]
            text = body[0]
            part1 = MIMEText(text, 'plain')
            msg.attach(part1)
            if len(body) > 1:
                html = body[1]
                part2 = MIMEText(html, 'html')
                msg.attach(part2)
            for name, ct in self.attachments.items():
                content, mime_type = ct
                part_n = MIMEApplication(self._read_content(content), Name=name)
                if mime_type:
                    part_n["Content-Type"] = mime_type
                    part_n["Content-Disposition"] = 'attachment; filename="%s"' % name
                msg.attach(part_n)
        return msg.as_string()

    def attach(self, name, content, mime_type="text/plain"):
        self.attachments[name] = (content, mime_type)

    def _read_content(self, content):
        if isinstance(content, str):
            return content
        if isinstance(content, bytes):
            try:
                # this should pass through binary
                return content.decode("iso-8859-1")
            except UnicodeEncodeError:
                # can't be represented as binary, so encode
                return content.decode("utf-8")
        if hasattr(content, "read"):
            return content.read()
        return str(content)


def split_emails(to):
    if isinstance(to, (str, bytes)):
        out = re.split(r'[,\s]+', to)
    elif to:
        out = []
        for e in to:
            out += split_emails(e)
    else:
        return []
    return [x for x in out if x]


"""  sample test code
if __name__ == "__main__":
    cfg = {
        "user": "***",
        "pwd": "***",
        "host": "email-smtp.us-west-2.amazonaws.com",
        "port": 587,
        "sender": "admin@mydomain.com"
    }
    emailer = SMTP_EMailer(**cfg)
    msg = emailer.create_message("***", "testing email", "testing")
    emailer.send_now(msg)
    print("ok")
"""


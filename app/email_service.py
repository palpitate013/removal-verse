import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Create server object with SSL option
        server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

        # Perform operations via server
        server.login(self.username, self.password)
        server.sendmail(self.username, to_email, msg.as_string())
        server.quit()

# Example usage:
# email_service = EmailService('smtp.example.com', 465, 'your_email@example.com', 'your_password')
# email_service.send_email('recipient@example.com', 'Subject', 'Email body')

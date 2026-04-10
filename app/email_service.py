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
        try:
            # Create server object with SSL option
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.username, self.password)

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(self.username, to_email, msg.as_string())
            print(f"Email sent to {to_email} with subject '{subject}'")  # Log email sending

            # Log the email sending
            with open('email_log.txt', 'a') as log_file:
                log_file.write(f"Email sent to {to_email} with subject '{subject}'\n")

            server.quit()
        except smtplib.SMTPException as e:
            print(f"Failed to send email to {to_email}: {str(e)}")
            # Retry logic or additional error handling can be added here
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
        print(f"Email sent to {to_email} with subject '{subject}'")  # Log email sending
        server.quit()

# Example usage:
# email_service = EmailService('smtp.example.com', 465, 'your_email@example.com', 'your_password')
# email_service.send_email('recipient@example.com', 'Subject', 'Email body')

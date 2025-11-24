import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_smtp(recipient: str, subject: str, body: str):
    sender_email = os.getenv("MAIL_FROM")
    sender_password = os.getenv("MAIL_PASSWORD")
    smtp_server = os.getenv("MAIL_SERVER")
    smtp_port = int(os.getenv("MAIL_PORT"))

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient], msg.as_string())
            server.sendmail(sender_email, sender_email, msg.as_string())  # Send a copy to sender
            print(f"Email sent successfully to {recipient}")
            return True
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return False

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail(from_mail_id, to_mail_ids, password, subject, body=None, file_paths=None):
    msg = MIMEMultipart()
    msg['From'] = from_mail_id
    msg['To'] =  ','.join(to_mail_ids)
    msg['Subject'] = subject

    if body:
        msg.attach(MIMEText(body, 'plain'))

    if file_paths:
        for file_path in file_paths:
            filename = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(attachment)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_mail_id, password)
    s.sendmail(from_mail_id, to_mail_ids, msg.as_string())
    s.quit()



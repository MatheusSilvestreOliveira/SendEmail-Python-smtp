import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(email_sender, pw_email_sender, email_recipient, subject, body, host_smtp, host_port, cc_address=None, path_img=None):
    """ Sends an e-mail using the smtplib and mime library

        :param email_sender: sender email address, expected to be a string
        :param pw_email_sender: password for the sender email adress, expected to be a string
        :param email_recipient: recipient email address, expected to be a list
        :param subject: subject of the email, expected to be a string
        :param body: body message of the email, expected to be a string
        :param host_smtp: host of the smtp server, expected to be a string
        :param host_port: port of the smtp server, expected to be an integer
        :param cc_address: CC email address, expected to be a list, optional
        :param path_img: path to imgs for attachment, expected to be a list, optional

    """
    msg = MIMEMultipart()
    msg['from'] = email_sender
    msg['to'] = ','.join(email_recipient)
    msg['subject'] = subject

    if cc_address is not None and len(cc_address) > 0:
        msg['Cc'] = ','.join(cc_address)

    msg_body = MIMEText(body)
    msg.attach(msg_body)

    if path_img is not None and len(path_img) > 0:
        for file in path_img:
            with open(file, 'rb') as img:
                img = MIMEImage(img.read())
                msg.attach(img)

    with smtplib.SMTP(host=host_smtp, port=host_port) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_sender, pw_email_sender)
            smtp.send_message(msg)
        except Exception as e:
            print('E-mail not sent!')
            print('Error: ', e)


# Code below for tests only
if __name__ == '__main__':
    test_email_sender = 'sender@email.com'
    test_pw_email_sender = 'password123'
    test_email_recipient = ['recipient1@email.com', 'recipient2@email.com']
    test_subject = 'Subject of the email'
    test_body = 'This will be the body of the email'
    test_host_smtp = 'smtp-mail.outlook.com'
    test_host_port = 587
    test_cc_address = []
    test_path_img = ['']

    send_email(test_email_sender, test_pw_email_sender, test_email_recipient, test_subject,
               test_body, test_host_smtp, test_host_port, cc_address=test_cc_address, path_img=test_path_img)

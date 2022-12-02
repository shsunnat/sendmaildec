from email.message import EmailMessage
import ssl
import smtplib
import re


def email_check(email):
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True

    else:
        return False


def sendemail(email_sender: 'Enter sender email', email_password: 'Enter your password',
              email_receiver: 'Enter receiver email', subject: 'email subject', body: 'email body',
              file: 'put your file here' = None, is_html=False):
    """
    --------------------------------- Email sender decorator ---------------------------------------
    :param email_sender: Enter sender email
    :type email_sender: string
    :param email_password: Enter sender password
    :type email_password: string
    :param email_receiver:Enter receiver email
    :type email_receiver: string
    :param subject: Enter email subject here
    :type subject: string
    :param body: Enter email body here
    :type body: string
    :param file:enter your file here
    :type file: string
    :param is_html: Sending HTML formatted emails
    :type is_html:Bool
    :return: string
    """

    def dec(function):
        def inner(*args, **kwargs):

            if is_html:
                em = EmailMessage()
                em["From"] = email_sender
                em["To"] = email_receiver
                em["Subject"] = subject
                em.set_content(body, subtype='html')
                context = ssl.create_default_context()
            else:
                em = EmailMessage()
                em["From"] = email_sender
                em["To"] = email_receiver
                em["Subject"] = subject
                em.set_content(body)
                context = ssl.create_default_context()

            if file:
                with open(file, 'rb') as pdf:
                    em.add_attachment(pdf.read(), maintype='application', subtype='octet-stream', filename=pdf.name)

            with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                print("Sent")

            return function(*args, **kwargs)

        return inner

    return dec
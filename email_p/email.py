import email_p.constants as c

class Email:
    def __init__(self):
        self.to = ''
        self.subject = ''

    def send(self):
        print(f'Email has been sent to {self.to}')
        print(f'Subject: {self.subject}')
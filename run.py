from prime_p.prime import Prime
import prime_p.constants as c
from prime_p.aux_functions import *
from email_p.email import Email

def run():
    p = Prime(c.START, c.FINISH)

    prettier = p.prettify()
    
    new_email = Email()
    new_email.to = 'lautaropc2001@gmail.com'
    new_email.subject = f'Prime Numbers execution between {c.START} and {c.FINISH}'
    print(prettier)
    new_email.send()

if( __name__ == '__main__'):
    run()
'''
Make sure less secure apps on the sender's and receiver's email id is ON
Link to that page- https://www.google.com/settings/security/lesssecureapps
'''
import smtplib
import os

def send_email(email_info,name,today,deadline):
    print(email_info,name)
    db_user=os.environ.get('DB_USER')
    db_pass=os.environ.get('DB_PASS')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(db_user, db_pass)

        subject='Freshi Food Expiration Notification'
        body='Your food item ' +name+ ' is going to expire tommorow.' 

        msg=f'Subject:{subject}\n\n{body}'

        smtp.sendmail(db_user,email_info,msg)

'''
To check the working of email on your localhost terminal-- 
Make this changes in above code 
1) Comment line 9 with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
2) Uncomment line 10 with smtplib.SMTP('localhost', 1025) as smtp:
3) comment the lines from smtp.ehlo() till smtp.login
4) Open you terminal and enter this line- 
   python3 -m smtpd -c DebuggingServer -n localhost:1025

Now you can check working of email on your localhost 
without spamming your email inbox
'''
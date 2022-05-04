from sqlalchemy import create_engine
from datetime import *
from send_email import send_email

# Creating a connection with DB
db_string = "postgresql://postgres:freshiapp123@localhost:5432/freshi"
# Example db_string = "postgresql://postgres:mypassword123@localhost:5432/freshi"
db = create_engine(db_string)


#Function to check for notification need
def notifier():
    result_set = db.execute("SELECT name,creator_id,expiration_date,days_before,email FROM food,public.user where food.creator_id=public.user.id order by expiration_Date ASC")
    today=datetime.today()
    print(today)  
    for result in result_set:  
        expiry_date=result[2]
        email_info=str(result[4])
        name=str(result[0])
        days_before=int(result[3])
        deadline=expiry_date-timedelta(days_before) 
        print(deadline)
        if today >= deadline:
            print("Email will be sent")
            send_email(email_info,name,today,deadline)
        else:
            print("Email will not be sent")

notifier()
'''
To automate this script-
 pip install hickory
 Example 1) hickory schedule notify.py --every=10minutes    (every 10 mins schedule)
 Example 2) hickory schedule notify.py --every=day@12:00AM  (every day @12:00AM schedule)
https://github.com/maxhumber/hickory --> to play around with schedule intervals 
'''



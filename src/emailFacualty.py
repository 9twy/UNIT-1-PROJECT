from facultyInfo import searchFaculaty ,searchEmail
from email.message import EmailMessage
import ssl
import smtplib
import os
from colorama import Fore
# EMail passkey yozq hbqh sddw ypel

def emailFaculaty():
    '''enable emailing the faculaty member 
    args :
    none'''
    try:
        doctorName=input("please Enter the name of faculaty member to email: ")
        if searchFaculaty(doctorName):
            print(searchFaculaty(doctorName))
            
            print()
            is_doctor=input("is this who you want to email? (yes or no): ")
            if is_doctor.lower()=='yes' :
                emailSender=os.environ.get('my_email')
                password=os.environ.get('pass_key_gmail')

                emailReciver=searchEmail(doctorName=doctorName)
                if emailReciver=="" or emailReciver==None :
                    raise ValueError(Fore.RED+"Sorry The email not found."+Fore.RESET)
                subject=input("Enter the subject: ")
                body=input("Enter the body of the message: ")
                em=EmailMessage()
                em['From']=emailSender
                em['To']=emailReciver
                em['Subject']=subject
                em.set_content(body)
                context=ssl.create_default_context()
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                        smtp.login(emailSender, password)
                        smtp.sendmail(emailSender,emailReciver,em.as_string())
                        print(Fore.GREEN+"email sent succssfully."+Fore.RESET)
                    
                except Exception as e:
                    print(e)
                    print("Failed to send email")
                
            
            elif is_doctor.lower()=='no':
                pass
            else :
                raise ValueError("just enter either yes or no!")
    except ValueError as v:
            print(v)




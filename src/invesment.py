import pickle
from prettytable import PrettyTable
from clasess import Project,Investor
from email.message import EmailMessage
import ssl
import smtplib
import os
import registration
from colorama import Fore
def showAvaliableProjects():
    '''display the avaliable projects
    takes no args
    return the project object'''
    # table.add_row([counter,user['obj'].getProject().getProjectTitle(),user['obj'].getProject().getProjectCategory(),user['obj'].getProject().getSupercisorName(),user['obj'].getProject().getProjectFile(),user['obj'].getProject().getFundingGoal()],divider=True)
    usersdicts=[]
    table=PrettyTable()
    table.field_names=['no','Project Title','Project Category','Supervisor','Project File','Funding Goal']
    with open('reg.pickle','rb') as file :
        while True:
            try:
                user=pickle.load(file)
                try:
                    if  user['obj'].getClassName()=='Student' :
                        usersdicts.append(user)
                except Exception:
                    pass
            except EOFError:
                break
    for indx , user in enumerate(usersdicts,start=1):
        if user['obj'].getProject():
            table.add_row([indx,user['obj'].getProject().getProjectTitle(),user['obj'].getProject().getProjectCategory(),user['obj'].getProject().getSupercisorName(),user['obj'].getProject().getProjectFile(),user['obj'].getProject().getFundingGoal()],divider=True)
    print(table)
    choise=input(Fore.RESET+"Do you want to invest on one of these projects? (enter yes or no): ")
    if choise.lower() =='yes':

        selection=int(input("please Enter the number of projects above to contact with project owner : "))
        return usersdicts[selection-1]['obj'].getProject()
    elif choise.lower()=='no':
        print(Fore.GREEN+"Returning to Home page.."+Fore.RESET) 
    else :
        raise ValueError (Fore.RED+"Please just Enter yes or no. try again"+Fore.RESET)
def contactStudent(studentEmail,investorEmail):
    '''send email to the user
    args:
    student email :str
    investor email:str
    return none'''
    print("Fill up email content below: ")
    emailSender=os.environ.get('my_email')
    password=os.environ.get('pass_key_gmail')
    subject=input("Enter the subject: ")
    body=input("Enter the body of your message: ")
    tail=input("Enter message tail: ")
    body+=f"\n{tail}"
    em=EmailMessage()
    em['From']=emailSender
    em['To']=studentEmail
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(emailSender, password)
            smtp.sendmail(emailSender,studentEmail,em.as_string())
            print("email sent succssfully.")
    except Exception as e:
        print(e)
        print("Failed to send email")

def investingProjects(userProject:Project,investor:Investor):
    '''pass args to contactStudent function
    args:
    project:Project
    investor:Investor'''
    contactStudent(userProject.getOwner().getEmail(),investor.getEmail())
        

    
    





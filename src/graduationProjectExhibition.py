from clasess import *
import pickle
import registration
import time
from prettytable import PrettyTable
from colorama import Fore
def createProject(currentUser:object):
    '''creates a project in the user object
    args: 
    currentUser:User'''
    usersdicts=[]
    
    projectTitle=input("Enter project Title: ")
    print("Please select a category for your graduation project:")
    categories = Fore.YELLOW+[
        "Software Development",
        "Data Science and Artificial Intelligence",
        "Embedded Systems and IoT",
        "Networking and Cybersecurity",
        "Business and Information Systems"
    ]+Fore.RESET
    for idx, option in enumerate(categories, start=1):
        print(f"{idx}. {option}")
    
    try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(categories):
                categorie= categories[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(categories)}.")
    except ValueError:
            print("Invalid input. Please enter a number.")
    supervisorName=input("Enter supervisor Name: ")

    projectFile=input("Enter the path of your project file: \'accept only .pdf files\' :")
    if not projectFile.endswith('.pdf'):
         raise ValueError("Accecpt only pdf files!")
    fundingGoal=int(input("What is your funding goal in (SR): "))
    with open('reg.pickle','rb') as file:
        while True:
            try:
               usersdicts.append( pickle.load(file))
            except EOFError:
                 break
    #add the project obj to the student obj
    for i in usersdicts:
         if i['email']==currentUser.getEmail():
              i['obj'].addProject(Project(currentUser,projectTitle,categorie,supervisorName,projectFile,fundingGoal))

    with open('reg.pickle','wb') as file:
        for i in usersdicts:
            pickle.dump(i,file)
        print("project added successfully.")

def updateProject(currentUser:object):
    '''update the project information such as project title
    args:
    current user:User'''
    usersdicts=[]
    userEmail=currentUser.getEmail()
    with open ('reg.pickle','rb') as file:
              while True:
                    try:
                        user=pickle.load(file)
                        usersdicts.append(user)
                    except EOFError:
                        break
    for i in usersdicts:
             if i['email']==currentUser.getEmail():
                 if not i['obj'].getProject():
                      raise ValueError (Fore.RED+"You have't add any project!"+Fore.RESET)

    userEmail=currentUser.getEmail()
    options=['update project title','update projct category','change the project file']
    for indx , option in enumerate(options,start=1):
         print(f"{indx}:{option}")
    what_to_update=input("Enter a number of your choise: ")
    if what_to_update=='1':
        newName=input("Enter the new name for the prject: ")
        
        for i in usersdicts:
             if i['email']==currentUser.getEmail():
                  i['obj'].getProject().setProjectTitle(newName)
        with open('reg.pickle','wb') as file:
            for i in usersdicts:
                pickle.dump(i,file)
            print('The project name updated.')
    elif what_to_update=='2':
        print('\n\n')
        print("Please select a category for your graduation project: ")
        categories = [
            "Software Development",
            "Data Science and Artificial Intelligence",
            "Embedded Systems and IoT",
            "Networking and Cybersecurity",
            "Business and Information Systems"
        ]
        for idx, option in enumerate(categories, start=1):
            print(f"{idx}. {option}")
        try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(categories):
                    categorie= categories[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
                print("Invalid input. Please enter a number.")
        usersdicts=[]
        with open ('reg.pickle','rb') as file:
              while True:
                    try:
                        user=pickle.load(file)
                        usersdicts.append(user)
                    except EOFError:
                        break
        for i in usersdicts:
             if i['email']==currentUser.getEmail():
                  i['obj'].getProject().setProjectCategory(categorie)
        with open('reg.pickle','wb') as file:
            for i in usersdicts:
                pickle.dump(i,file)
            print('The project category updated.')
    elif what_to_update=='3':
        newFile=input("Enter the new name for the prject: ")
        usersdicts=[]
        with open ('reg.pickle','rb') as file:
              while True:
                    try:
                        user=pickle.load(file)
                        usersdicts.append(user)
                    except EOFError:
                        break
        for i in usersdicts:
             if i['email']==currentUser.getEmail():
                  i['obj'].getProject().setProjectFile(newFile)
        with open('reg.pickle','wb') as file:
            for i in usersdicts:
                pickle.dump(i,file)
            print('The project File updated.')
         
        




    
    

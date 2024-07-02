import re
import json
import pickle
import maskpass
from clasess import User , Student,FaculatyMember,Investor   
import graduationProjectExhibition
from invesment import showAvaliableProjects
import graduationProjectExhibition
from colorama import Fore, Back, Style
def signUp():
    newUser:dict={}
    while True:
        try:    
            
            name=input("Please Enter your full name (eg. ali ahmed alghamdi): ")
            email=input("please Enter your email: ")
            password=maskpass.askpass("Enter your password: ",mask="•")
            userTypes=['Student','Faculaty member',"Investor"]
            print("Please choose a number.")
            for index , usertype in enumerate(userTypes,start=1):
                 print(f"{index}.{usertype}")
            
            userType=int(input("Enter a number: "))     
            if userType==1:
                newObj=Student(name,email,password)
                newUser.update({'email':newObj.getEmail(),'obj':newObj})
            elif userType==2:
                newObj=FaculatyMember(name,email,password)
                newUser.update({'email':newObj.getEmail(),'obj':newObj})
            elif userType==3:
                 portflioValue=int(input("Please Enter a portflio Value: "))

                 newObj=Investor(name,email,password,portflioValue)
                 newUser.update({'email':newObj.getEmail(),'obj':newObj})
            else:
                 raise ValueError("Please Enter a number between 1-3")
            
            if (newObj.ststus()):
                break
    
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
            print(Fore.RED+"somthing wrong!")
    
    try:
        with open('reg.pickle','ab') as file:
            pickle.dump(newUser,file)
            print(Fore.GREEN+f"Welcome {newObj.getName()} you sign up successfuly."+Fore.RESET)
    except Exception as e:
        print(e)
    if(newObj.ststus()):
         return newObj
    
    

def logIn():
    email=input("Enter your email: ")
    password=maskpass.askpass("Enter your password: ",mask="•")
    with open ('reg.pickle','rb') as file:
        
            try:
                while True:
                    user = pickle.load(file)  
                    if user['email']==email and user['obj'].getPassword()==password:
                        print(Fore.GREEN+f"signed in succssfuly , Welcom {user['obj'].getName().split(' ')[0]}."+Fore.RESET)
                        return user['obj']
                        break
            except ValueError as v:
                    print(v)
                        
            except Exception:
                print(Fore.RED+"incorrect Email or password try again"+Fore.RED)
                    
               

    
def updateUserInfo(currentUser):
    try:
        update=input('Enter what you need to update (name ,email or password ) or enter delete for deleting your account : ')
        if update.lower()=='name':   
            updateName(currentUser.getEmail())
                
        elif update.lower()=='email':
            updateEmail(currentUser.getEmail())    
                
        elif update.lower()=='password':
            updatePassword(currentUser.getEmail())
        elif update.lower()=='delete':
             deleteAccount(currentUser.getEmail())
        else:
             raise ValueError("Please just enter what you need to update!(eg name,email or password)")
    except ValueError as v:
         print(v)

def updateName(userEmail:object)->bool:
    newName=input("enter your name: ")
    usersInfo=[]
    isNameUpdated=False
    with open('reg.pickle','rb') as file:
                while True:
                    try:
                        usersInfo.append(pickle.load(file)) #load singl obj in each loop
                    except EOFError:
                        break
                    except ValueError as v:
                        print(v)

                    except Exception as e:
                        print(e)
                        print('something went wrong! ')
                
                
                try:    
                    for userInfo in usersInfo:
                        if userInfo['email']==userEmail:
                            userInfo['obj'].setName(newName)
                            print("updated succsfluy")
                            isNameUpdated=True
                    if  isNameUpdated==False:
                        raise ValueError("some thing went wrong!, the email not found")
                                


                except ValueError as v:
                        print(v)
    with open('reg.pickle','wb') as file:
            for i in usersInfo:
                pickle.dump(i,file)



 
def updateEmail(userEmail:str):
    usersInfo=[]
    isEmailUpdated=False
    newEmail=input("Enter the new email: ")
    with open('reg.pickle','rb') as file:
            while True:
                try:
                    usersInfo.append(pickle.load(file)) #load singl obj in each loop
                except EOFError:
                    break
                except ValueError as v:
                    print(v)

                except Exception as e:
                    print(e)
                    print('something went wrong! ')
            
            
            try:    
                for userInfo in usersInfo:
                    if userInfo['email']==userEmail:
                        userInfo['obj'].setEmail(newEmail)
                        userInfo['email']=userInfo['obj'].getEmail()
                        print("updated succsfluy")
                        isEmailUpdated=True
                if  isEmailUpdated==False:
                    raise ValueError("some thing went wrong!, the email not found")
                            


            except ValueError as v:
                    print(v)
    with open('reg.pickle','wb') as file:
        for i in usersInfo:
            pickle.dump(i,file)


def updatePassword(userEmail:object):
    usersInfo=[]
    isPasswordUpdated=False
    newPassword=maskpass.askpass("Enter your password: ",mask="•")
    with open('reg.pickle','rb') as file:
                while True:
                    try:
                        usersInfo.append(pickle.load(file)) #load singl obj in each loop
                    except EOFError:
                        break
                    except ValueError as v:
                        print(v)

                    except Exception as e:
                        print(e)
                        print('something went wrong! ')
                
                
                try:    
                    for userInfo in usersInfo:
                        if userInfo['email']==userEmail:
                            userInfo['obj'].setPassword(newPassword)
                            userInfo['email']=userInfo['obj'].getEmail()
                            print("updated succsfluy")
                            isPasswordUpdated=True
                    if  isPasswordUpdated==False:
                        raise ValueError("some thing went wrong!, the email not found")
                                


                except ValueError as v:
                        print(v)
    with open('reg.pickle','wb') as file:
            for i in usersInfo:
                pickle.dump(i,file)


    

def deleteAccount(userEmail:str):
    usersInfo=[]
    isAccountDeleted=False
    Password=maskpass.askpass("Enter your password: ",mask="•")
    with open('reg.pickle','rb') as file:
                while True:
                    try:
                        usersInfo.append(pickle.load(file)) #load singl obj in each loop
                    except EOFError:
                        break
                    except ValueError as v:
                        print(v)

                    except Exception as e:
                        print(e)
                        print('something went wrong! ')
                
                
                try:    
                    for userInfo in usersInfo:
                        if userInfo['email']==userEmail and userInfo['obj'].getPassword()==Password:
                            usersInfo.remove(userInfo)
                            print("deleted successfully. ")
                            isAccountDeleted=True
                    if  isAccountDeleted==False:
                        raise ValueError("some thing went wrong!, the email not found or the password incorrect.")
                                


                except ValueError as v:
                        print(v)
    with open('reg.pickle','wb') as file:
            for i in usersInfo:
                pickle.dump(i,file)
            raise TimeoutError(Fore.GREEN+"Thank you for visiting our system.."+Fore.RESET)
    


import clasess 
import emailFacualty
import facultyInfo 
import graduationProjectExhibition 
import invesment
import registration 
from colorama import Fore, Back, Style
import pyfiglet
# here we run the code..

def register():
    '''detrmine the registration option
    args:
    return user object'''
    print(Fore.CYAN+"\033[4m" + "WELCOME TO RGU SYSTEM."+ "\033[0m")
    while True:
        try:
            signset=["Sign in","Sign up"]
            for index ,option in enumerate(signset,start=1):
                print(Fore.RESET+f"{index}.{option}")
            sign=input(Fore.RESET+"Enter a number of above: ")
            if sign=='1':
                user=registration.logIn()
            elif sign=='2':
                user=registration.signUp()
            else:
                raise ValueError(Fore.RED+"Please Enter a valid number!"+Fore.RESET)
            if user:
                break
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
            
  
    return user
def servicess(user:clasess.User):
 '''base on the type of the user display he's dashboard'''
 
 try:
    if user.getClassName()=="Student":
        studentInterface(user)
    elif user.getClassName()=="Faculaty":
        faculatyInterface(user)
    elif user.getClassName()=="Investor":
        investorInterface(user)
 except ValueError as v:
     print(v)
 except TimeoutError as T:
     print(T)
#  except Exception as e :
#      pass


def studentInterface(currentUser:clasess.Student):
    '''dashboard for the student 
    args:
    user object
    return 
    none'''
    
    while True:
        print("\n\n")
        options=["Search about a faculaty member","Email a faculaty member","publish your graduation project to investments","Update your previous projects","Update account Information","exit"]
        for indx , option in enumerate(options,start=1):
             print(f"{indx}. {option}")
        print()
        try:

            choise=int(input(Fore.MAGENTA+"Enter the number of the service: "+Fore.RESET))
            if choise==1:
                doctorName=input("Enter doctor name in arabic: ")
                if facultyInfo.searchFaculaty(doctorName):
                 print(facultyInfo.searchFaculaty(doctorName))
            elif choise==2:
                emailFacualty.emailFaculaty()
            elif choise ==3:
                graduationProjectExhibition.createProject(currentUser)
            elif choise==4:
                graduationProjectExhibition.updateProject(currentUser)
            elif choise==5:
                registration.updateUserInfo(currentUser)
            elif choise==6:
                break
        except ValueError as v:
            print("Please Try To Enter a digit Number between 1-4")
        except TimeoutError as T:
            print(T)
def faculatyInterface(currentUser:clasess.FaculatyMember):
    '''dashboard for the faculaty member..'''
    while True:
      try:
        options=["Search about a faculaty member","Email a faculaty member","Update account Information","exit"]
        print('\n\n')
        for indx , option in enumerate(options,start=1):
            print(f"{indx}. {option}")
        print('\n')
        choise=int(input(Fore.MAGENTA+"Enter the number of the service: "+Fore.RESET))
        if choise==1:
            doctorName=input("Enter doctor name in arabic (first name and last name): ")
            if facultyInfo.searchFaculaty(doctorName):
                 print(facultyInfo.searchFaculaty(doctorName))
        elif choise==2:
            emailFacualty.emailFaculaty()
        elif choise==3:
            registration.updateUserInfo(currentUser)
        elif choise==4:
            break
        else:
                raise ValueError("Invalid number!")
      except ValueError as v:
          print(v)
      except TimeoutError as T:
            print(T)
      except Exception as e:
          print(e)
          print("somthing went wrong!!")

def investorInterface(currentUser:clasess.Investor):
    '''dashboard for the investor '''
    while True:
      try:
        options=["Search about a faculaty member","Email a faculaty member",'Graduation projects exhibition',"Update account Information","exit"]
        print('\n\n')
        for indx , option in enumerate(options,start=1):
            print(f"{indx}. {option}")
        print('\n')
        choise=int(input(Fore.MAGENTA+"Enter the number of the service: "+Fore.RESET))
        if choise==1:
            doctorName=input("Enter doctor name in arabic (first name and last name): ")
            if facultyInfo.searchFaculaty(doctorName):
                 print(facultyInfo.searchFaculaty(doctorName))
        elif choise==2:
            emailFacualty.emailFaculaty()
        elif choise==3:
            choise=invesment.showAvaliableProjects()
            if choise:
                invesment.investingProjects(choise,currentUser)
        elif choise==4:
            registration.updateUserInfo(currentUser)
        elif choise==5:
            break
        else:
                raise ValueError(Fore.RED+"Invalid number!"+Fore.RED)
      except ValueError as v:
          print(v)
      except TimeoutError as T:
            print(T)
      except IndexError as i:
          print(Fore.RED+"Please Enter a valid number of above projects! "+Fore.RESET)
      except Exception as e:
          print(e)
          print("somthing went wrong!!")
      


        
    


if __name__=="__main__":
    servicess(register())


import clasess 
import emailFacualty
import facultyInfo 
import graduationProjectExhibition 
import invesment
import registration 
from colorama import Fore, Back, Style

def register():
 
    print(Fore.CYAN+"Welcom to RGU System..")
    # try:
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
            
            
    # except ValueError as v :
    #     print(v)
    # except Exception as e:
    #     print("Something went wrong!!")
    return user
def servicess(user:clasess.User):
 
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
                invesment.investingProjects(currentUser)
        elif choise==4:
            registration.updateUserInfo(currentUser)
        elif choise==5:
            break
        else:
                raise ValueError("Invalid number!")
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
    
    







# moreInfo=input("Need more info about the system enter 1 , enter 2 to exit: ")
# if moreInfo=='1':
#     print(Fore.YELLOW+'''

# Our system is designed to facilitate communication between students and faculty members in the academic field. It caters to universities across Saudi cities, enabling students to connect with faculty
# members from institutions like KSU, PNU, and PSAU.
# The system allows students to email faculty members by simply entering the faculty member's name. Additionally, students can retrieve general information about the faculty member.
# Furthermore, the system enables students to add their graduation projects. This provides investors with the opportunity to review the projects and contact the students directly. 
# The system will automatically send an email to the student when an investor expresses interest in their work. The goal of this system is to create a seamless and efficient platform for academic collaboration and networking, benefiting both students and faculty members across the various universities in Saudi Arabia.

#                         ''')
# # elif moreInfo=='2':
# #     break


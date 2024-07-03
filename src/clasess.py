import re
#parent calss
from prettytable import PrettyTable
import pickle
from colorama import Fore





class User:
    
    
    def __init__(self,name,email,password) -> None:            
            self.setName(name)
            self.setEmail(email=email)
            self.setPassword(password)

    def setName(self,name:str):
        if len(name.split(' '))>=3:
            self.__name=name
        else:
            raise ValueError(Fore.Red+"please Enter your full name correctly (eg.ali ahmed alghamdi)"+Fore.RESET)
    def setEmail(self,email:str):
        if re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@[a-z0-9.-]+\.[a-z]{2,}$',email) :
            self.__email=email
        else: 
            raise ValueError("Please Enter your email correctly.")
    def setPassword(self,password:str):
        if " " in password or len(password)<6:
            
            raise ValueError("the password sholud be more than 6 and not containg space.")
        else:
            self.__password=password

        
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def getPassword(self):
        return self.__password
    # def __str__(self) -> str:
    #     return "printiing the toString"
    def ststus(self)->bool:
        if self.__email and self.__name and self.__password :
            return True
        else:
            return False
        







class Student(User):
        
 
        def __init__(self, name, email, password,userType="student") -> None:
            super().__init__(name, email, password)
            self.__pendingrequests=[]
            self.__userType=userType
            self.__project=None
        def addProject(self,projec:object):
            self.__project=projec
        def getProject(self):
            if self.__project:
                return self.__project
            else:
                return None
        def getRequests(self):
            for i in self.__pendingrequests:
               investor= i['investor']
               fundingAmount=i['fundingAmount']
            return f"{investor} has requested to invest {fundingAmount} in the  project."
        def getClassName(self):
            return "Student"
        def showProjects(self):
            try:
                return f"Project Title: {self.getProject().getProjectTitle()} , Project category: {self.getProject().getProjectCategory()} , projectFile: {self.getProject().getProjectFile()}"
            except Exception:
                print("there's no project add.")


            
        def __str__(self):
            return self.getProject()
    




         
class FaculatyMember(User):
    def __init__(self, name, email, password,userType="faculaty_member") -> None:
        super().__init__(name, email, password)
        self.__userType=userType
    def getClassName(self):
            return "Faculaty"






class Admin(User):
    def __init__(self, name, email, password,userType="admin") -> None:
        super().__init__(name, email, password)
        self.__userType=userType




class Investor(User):
    def __init__(self, name, email, password,portfolioValue,userType="investors") -> None:
        super().__init__(name, email, password)
        self.__portfolioValue=portfolioValue
    def getportfolioValue(self):
        self.__portfolioValue
    def getClassName(self):
            return "Investor"
    def investmentRequest(self,project:object,fundingAmount:int):
        if fundingAmount<=self.__portfolioValue:
            project.getOwner().receiveInvestment(self,fundingAmount)
        else:
            print(f"does not have sufficient funds to invest in: {project.getProjectTitle()}")
    def reciveReplay(self,respone:bool,fundingAmount):
        if respone:
            self.__portfolioValue-=fundingAmount
            return "invested successfully"
    def __str__(self):
        return "i am investor"
        



                    

class Project:
    def __init__(self,owner:object,projectTitle:str,projectCategory:str,supervisorName:str,projectFile,funding_goal:int) -> None:
        self.__funding_goal:int=funding_goal
        self.__owner=owner
        self.__projectTitle=projectTitle
        self.__projectCategory=projectCategory
        self.__supervisorName=supervisorName
        self.__projectFile=projectFile
        self.__currentFunding=0
    def getFunding(self):
            return self.__currentFunding
    def setFunding(self,amount):
            self.__currentFunding+=amount
    def getFundingGoal(self):
        return self.__funding_goal
    def getProjectTitle(self):
        return self.__projectTitle
    def getProjectCategory(self):
        return self.__projectCategory
    def getSupercisorName(self):
        return self.__supervisorName
    def getProjectFile(self):
        return self.__projectFile
    def setFundingGoal(self,fundingAmount:int):
        self.__funding_goal
    def setProjectTitle(self,projectTitle):
        self.__projectTitle=projectTitle
    def setProjectCategory(self,projectCategory):
        self.__projectCategory=projectCategory
    def setProjectFile(self,projectFile):
        self.__projectFile=projectFile
    def getOwner(self):
        return self.__owner
    def __str__(self):
        return f"project Name:{self.__projectTitle} , owner: {self.getOwner().getName()}"

    

    



if __name__=="__main__":
    pass
            

    

    


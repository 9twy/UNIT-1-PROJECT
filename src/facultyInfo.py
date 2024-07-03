import json
from bidi.algorithm import get_display
import re
from arabic_reshaper import reshape
from prettytable import PrettyTable
from colorama import Fore, Back, Style

def searchFaculaty(doctorName:str) -> str:
    # doctorName=input("Please Enter the name of the faculaty member ([First Name Last Name]) : ")
    with open('faculatyData/FulldataPsau.json', 'r', encoding='UTF-8') as psauFile:
        psauInfo = json.load(psauFile)
        
    with open ("faculatyData/KsuFull-DATA.json",'r',encoding='UTF-8') as ksuFile:
        ksuInfo=json.load(ksuFile)
    with open("faculatyData/PNUdata.json",'r',encoding="UTF-8") as pnuFile:
        pnuInfo=json.load(pnuFile)
    doctorName=doctorName.split(' ')
    flage=True
    try:
        while flage:
            
                for i in psauInfo:
                    
                        if re.search(f'^.*{doctorName[0]}.*{doctorName[-1]}$',i['Name']) :
                            table=PrettyTable()
                            table.field_names=['University','Full Name','Academic Rank','Department','College']
                            table.add_row([reashpeToArabic('جامعة الامير سطام بن عبدالعزيز'), reashpeToArabic( i['Name']),reashpeToArabic(i['doctor_info'][0]),reashpeToArabic(i['doctor_info'][1]),reashpeToArabic(i['doctor_info'][2])])
                            flage=False
                            if table !=None:
                                return table
                            
                        
                    
                for i in ksuInfo:
                        if re.search(f'^.*{doctorName[0]}.*{doctorName[-1]}$',i['name']) :
                            table=PrettyTable()
                            table.field_names=['University','Full Name','Academic Rank','Department','College']
                            table.add_row([reashpeToArabic('جامعة الملك سعود بن عبدالعزيز'), reashpeToArabic( i['name']),reashpeToArabic(i['degree']),reashpeToArabic(i['major']),reashpeToArabic(i['faculty'])])
                            flage=False
                            if table !=None:
                                return table
                            
                for i in pnuInfo:
                     if re.search(f'^.*{doctorName[0]}.*{doctorName[-1]}$',i['Name']) :
                            table=PrettyTable()
                            table.field_names=['University','Full Name','Academic Rank','Department','College']
                            table.add_row([reashpeToArabic('جامعة الاميرة نورة'), reashpeToArabic( i['Name']),reashpeToArabic(i['Degree']),reashpeToArabic(i['Major']),reashpeToArabic(i['Faculty'])])
                            if table !=None:
                                return table
                if table:
                      raise Exception
                break           
                     
    except Exception as e:
             print(Fore.RED+"Not found. Please try again and enter the first name and last name!"+Fore.RESET)
                

def searchEmail(doctorName:str) -> str:
    # doctorName=input("Please Enter the name of the faculaty member ([First Name Last Name]) : ")
    with open('faculatyData/FulldataPsau.json', 'r', encoding='UTF-8') as psauFile:
        psauInfo = json.load(psauFile)
        
    with open ("faculatyData/KsuFull-DATA.json",'r',encoding='UTF-8') as ksuFile:
        ksuInfo=json.load(ksuFile)
    with open("faculatyData/PNUdata.json",'r',encoding="UTF-8") as pnuFile:
        pnuInfo=json.load(pnuFile)
    doctorName=doctorName.split(' ')
    flage=True
    try:
        while flage:
            
                for i in psauInfo:
                    
                        if re.search(f'^.*{doctorName[0]}.*{doctorName[-1]}$',i['Name']) :
                            return i['email']
                            break
                        
                    
                for i in ksuInfo:
                        if re.search(f'^{doctorName[0]}.*{doctorName[-1]}$',i['name']) :
                            return i['email']
                            break
                for i in pnuInfo:
                     if re.search(f'^{doctorName[0]}.*{doctorName[-1]}$',i['Name']) :
                            return i['Email']
                break           
                     
    except Exception as e:
             print(e)
             print("Not found. Please try again and enter the first name and last name!")
                
            

    
        
        

def reashpeToArabic(txt:str):
    return get_display(reshape(txt))




    


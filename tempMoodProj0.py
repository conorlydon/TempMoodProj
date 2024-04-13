#This program takes a variable in(temperature), cleans out unwanted text such as /r for example
#import csv to print the temperature levels(average, min and max) and also mood level
import csv
#this enables the program to send and receive data. serial uses one or two transmission lines to send and receive data, and that data is continuously sent and received one piece at a time
import serial
#gets the mean of any floats or integers
from statistics import mean
#enables to print the csv in a formatted, easily readable way
import pandas as pd
#take in the temperature using the microbit and microbit code
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
#prompt user to press A if they wish to stop logging data

print("Press A to exit. (may take 5 seconds)")

#opens serial
ser.open()
on = True
#run unless A is pressed
tempList=[]
temperature="" 
#create a loop to take in data from the microbit unless a is pressed
while on:
    """
    # Only take in data if it is not = 999.
    #If equal to 999 break as button a has been pressed to stop the program
    if  temperature =="999":
        break
        # First take in all the data and assign it to this variable
    elif  temperature !="999":
        continue
    """
    data = str(ser.readline())

    #get "second bit" and change temperature from nothing to the temperature in the room
    temperature = data[2:]
        
    #lines 42-46, remove any data that cannot be changed ti=o a numerical value
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("'","")
    temperature = temperature.replace("\\r\\n","") 
    temperature = temperature.replace("\\r","")   
    temperature = temperature.replace("\\n","")
    
    #temperature=float(temperature)
        
#previous code i tried to use but would not work.
#inputs would not be taken in: nothing could be validated as a float
    """
    # Print it to see if any of that above actually worked
    if type(temperature) == float and (temperature)<50:
        tempList.append(temperature)
        print(temperature)
    """
    #if invalid data given, convert to number 0
    if temperature=="":
        data= 0
    #if temperature is F,break
    
    if temperature=="F":
        on = False
        break
    #if temperature is not equal to F put data into list "tempList"
    
    elif temperature!="F" and "F" not in temperature and temperature!="F" :
        temperature=float(temperature)
        #sometimes the temperature would read as unrealistic such as 2323(two readings read as one)
        #this prevents this. 51 chosen as microbit can only read up to 51 degrees celcius
        if temperature<51:
            tempList.append(temperature)
            print(temperature)
        
               
         
print("My list of light values is:",tempList)
#get mean using statistics import and maximum and minimum temperatures using built-in functions min and max

maxTemp=max(tempList)
minTemp=min(tempList)
meanTemp=round(mean(tempList),2)
print("max light is",maxTemp,"min light is",minTemp,"mean light is",meanTemp)
#prompt the user how they feel.

physical_wellbeing = int(input("On a scale of 1-10 from wrecked to ready, how to you physically feel?"))
emotional_wellbeing = int(input("On a scale of 1-10 from sad to happy, how to you emotionally feel?"))
hygiene = int(input("On a scale of 1-10 from filthy to cleansed, how would you rate your hygiene?"))
#get the average of these three variables. that is the users mood
average_mood = mean([physical_wellbeing, emotional_wellbeing, hygiene])

average_mood = round(average_mood,2)

print("Your mood is roughly", average_mood)
read = "temp.csv"#name the temperature comma seperated values
#open the values i found. thonny prompted to use "encoding" to improve the strength of the program
f = open(read, "a", newline='',encoding='UTF-8')
#convert the opened csv to a spreadsheet using functions imported from csv
spreadsheet = csv.writer(f)
#write the average maximum and minimum temperatures. place these next to the average_mood

spreadsheet.writerow([maxTemp, minTemp, meanTemp, average_mood])
#tell the user what has been added to the csv
print("I have added the following data to your database.")
print([maxTemp, minTemp, meanTemp, average_mood])
print("")
#close opened csv
f.close()
#df stands for data frame
df = pd.read_csv('temp.csv')
#replace every new line with color to make the spreadsheet more appealing
styled_df = df.to_string().replace('\n', '\n\033[34m')
#print the data to the user
print(styled_df)



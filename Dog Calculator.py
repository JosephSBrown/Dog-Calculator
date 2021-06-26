##############################################################
##File Name: Dog Age Calculator                             ##
##File Type: Python 3                                       ##
##                                                          ##
##Author: Joseph Brown                                      ##
##Project Type: Independent Project                         ##
##Creation Date: 28 May 2021                                ##
##Last Modification Date:                                   ##
##                                                          ##
##Description:                                              ##
##                                                          ##
##                                                          ##
##Version: 1.11                                             ##
##Version History:                                          ##
##1.11 - Tidied Up Sleeps and Added More to the Results     ##
##1.1 - Added Use of Sleep to Make Program Last for Longer  ##
##1.0 - Basic Calculations of the Age using Input Variables ## 
##############################################################

#Imports
import time

#Phrase Variables for Printing
name_phrase = "Your Dog's Name is: "
age_phrase = "Your Dog's Age in Human Years is: "

#Program Commencement w/ Input Variables
dog_name = input("What is your Dog's Name? ")
human_age = input("What is your Dog's Age in Human Years? ")

#Calculation using Variables
dog_age = int(human_age) * 7
print("Calculating Dog's Age...")
time.sleep(2)
print(" ")
time.sleep(2)
print("We'll Have Your Results Shortly, Please Wait...")
time.sleep(2)

#Final Calculation Presentation/Results
print("Your Results Are Ready...")
time.sleep(1)
print("Displaying Results...")
time.sleep(0.5)
print(" ")
time.sleep(0.5)
print("--Your Final Results--")
print(name_phrase + dog_name)
print(age_phrase + human_age)
print(dog_name + " is", dog_age, "in Dog Years!")
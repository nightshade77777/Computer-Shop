# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:23:52 2022

@author: SHASHANK
"""
from time import sleep 

BASIC_SET = 200
case_total = 0 
ram_total = 0 
main_hdd_total = 0 
new_total = 0 

ssd_total = 0 
second_hdd_total = 0 
optical_drive_total = 0
os_total = 0

case = [
  ["A1", "Compact", 75],
  ["A2", "Tower", 150]
]

ram = [
  ["B1", "8 GB", 79.99],
  ["B2", "16 GB", 149.99],
  ["B3", "32 GB", 299.99]
]

main_hdd = [
  ["C1", "1 TB HDD", 49.99],
  ["C2", "2 TB HDD", 89.99],
  ["C3", "4 TB HDD", 129.99]
]

solid_state_drive = [
  ["D1", "240 GB SSD", 59.99],
  ["D2", "480 GB SSD", 119.99]
]

second_hdd = [
  ["E1", "1 TB HDD", 49.99],
  ["E2", "2 TB HDD", 89.99],
  ["E3", "4 TB HDD", 129.99]
]

optical_drive = [
  ["F1", "DVD/Blue-Ray Player", 50],
  ["F2", "DVD/Blue-Ray Re-writer", 100]
]

operating_system = [
  ["G1", "Standard Version", 100],
  ["G2", "Premium Version", 175]
]

#note 
print("Note: Please type in the ITEM CODE only. Example: A1, B2, C3. ")

print()

#displays options for cases 
print("Options for computer cases are: ") ; sleep(1)
#prints array without brackets and in sep. lines
for i in case:
  for j in i:
    print(j, end = " ")
  print()

print()

#displays ram options
print("Options for RAMs are: ") ; sleep(1)
for x in ram:
  for y in x:
    print(y, end = " ")
  print()


print()

#displays hard disk options
print("Options for main hard disks are: ") ; sleep(1)
for b in main_hdd:
  for a in b:
    print(a, end = " ")
  print()
 
print()

print("Basic set of computer components will cost you 200 AED. It is already added in your total as default. ")

print()

print("Note: Type 'end' to exit. ")

print()

welcome = input("Welcome! Are you interested in taking a look at our items? Enter (y/n): ")

choose_case = ""
choose_ram = ""
choose_main_hdd = ""

while welcome == "y" or welcome == "Y":
  choose_case = input("Please choose which computer case you want to purchase: ")
  choose_ram = input("Please choose which RAM you want to purchase: ")
  choose_main_hdd = input("Please choose main hard disk you want to purchase: ")

  print()
  choose_case = choose_case.upper()
  choose_ram = choose_ram.upper()
  choose_main_hdd = choose_main_hdd.upper()

  if welcome == "n":
    break
  elif welcome == "end":
    welcome == "false"
  break
  
if choose_case == case[0][0]:
  case_total = case[0][2]
  
elif choose_case == case[1][0]:
  case_total = case[1][2]

if choose_ram == ram[0][0]:
  ram_total = ram[0][2]
  
elif choose_ram == ram[1][0]:
  ram_total = ram[1][2]
  
elif choose_ram == ram[2][0]:
  ram_total = ram[2][2]
  
if choose_main_hdd == main_hdd[0][0]:
  main_hdd_total = main_hdd[0][2]
  
elif choose_main_hdd == main_hdd[1][0]:
  main_hdd_total = main_hdd[1][2]
  
elif choose_main_hdd == main_hdd[2][0]:
  main_hdd_total = main_hdd[2][2]

#total price
new_total = case_total + ram_total + main_hdd_total + BASIC_SET

print()

print("Your total is: " + str(new_total))

print()


#additional options
print("Options for Solid State Drives are: ") ; sleep(1)
for v in solid_state_drive:
  for m in v:
    print(m, end = " ")
  print()


print()

print("Options for second hard disk are: ") ; sleep(1)
for zee in second_hdd:
  for peez in zee:
    print(peez, end = " ")
  print()

print()

print("Options for the optical drives are: ") ; sleep(1)
for moo in optical_drive:
  for mee in moo:
    print(mee, end = " ")
  print()

print()

print("Options for the operating systems are: ") ; sleep(1)
for skee in operating_system:
  for skit in skee:
    print(skit, end = " ")
  print()

print()

#TASK 2
#items remaining are: 
#solid state drive, second hdd, #optical drive and operating system 
#need to make for loops to display these

#while additional == yes, keep asking until user types in END

#calculate total price of additional item(s)
#add this price to existing total 

additional_c = input("Would you like to buy additional items? Enter y/n: ")
if additional_c == "y" or additional_c == "Y":
    additional = True
else:
    additional = False
print("Enter 'close' to exit. ") ; sleep(1)
print()

new_item = " "
while (additional==True) and (new_item!="CLOSE"):
    
  new_item = input("Choose an item to purchase: ")
  new_item = new_item.upper()
  
  if new_item == solid_state_drive[0][0]:
    ssd_total += solid_state_drive[0][2]

  elif new_item == solid_state_drive[1][0]:
    ssd_total += solid_state_drive[1][2]

  if new_item == second_hdd[0][0]:
    second_hdd_total += second_hdd[0][2]
  
  elif new_item == second_hdd[1][0]:
   second_hdd_total += second_hdd[1][2]

  elif new_item == second_hdd[2][0]:
   second_hdd_total += second_hdd[2][2]

  if new_item == optical_drive[0][0]:
   optical_drive_total += optical_drive[0][2]

  elif new_item == optical_drive[1][0]:
   optical_drive_total += optical_drive[1][2]

  if new_item == operating_system[0][0]:
    os_total += operating_system[0][2]

  elif new_item == operating_system[1][0]:
    os_total += operating_system[1][2]

additional_total = ssd_total + second_hdd_total + optical_drive_total + os_total

print("Your total of additional items is " + str(additional_total) + " AED. ")

entire_total = additional_total + new_total
print("Your entire total is " + str(entire_total) + " AED. ")

print("Have a nice day! ")
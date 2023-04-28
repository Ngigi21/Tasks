# m=4
# p=4
# m+=p
# print(m)


# Given two integer variables m and p, write expressions that use the assignment operator to perform the following operations:
# a. Add p to m and store the result in m.
# b. Subtract p from m and store the result in m.
# c. Multiply m by p and store the result in m.
# d. Divide m by p and store the result in m.
# e. Calculate the remainder of m divided by p and store the result in m.


# m=4
# p=4
# print(m-p)


# m=4
# p=4
# print(4*4)

# m=4
# p=4
# print(m/p)


m=78
p=98
m+=p
print(m)

# m=78
# p=98
# m-=p
# print(m)


# temp=56.8926
# print(round(temp, 1))


# Questions
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.90 
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.892 
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 


# temp=56.8926
# print(round(temp,4))


# temp=56.8926 #change to 8.926
# string_temp=str(temp)
# first_part=string_temp[3:4]
# second_part=string_temp[4:]
# new_string=first_part+ "." +second_part
# temp=float(new_string)
# print(temp)
# print(type(temp))


# ASK: Create a List of days of the Week. Print the whole list and Print this day.

# Week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# print(week)

# Get values in a section, range or a specific index using colon.
# Figure out as a class what sideA and sideB are in list[sideA : sideB]. 
# Start daysOfTheWeek[0:], daysOfTheWeek[1:] - conclude and write a statement together.
# Start daysOfTheWeek[0:2], daysOfTheWeek[1:5] - Test more scenarios, conclude and write a statement together
# Start daysOfTheWeek[0:-1], daysOfTheWeek[0:-3 ] - conclude and write a statement.


# daysoftheweek=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# daysoftheweek[0:7]

# print("hello,world!")


# week= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# # print(week[0:])
# print(week[1:])
#print(week[0:3])
# # print(week[1:5])
# print(week[0:-1])
# print(week[0:-3])
# print(week[3:-4])


# name= "The kid"
# count= 345
# total=["The kid", 345 ] 
# cumulative=[865,[total, "the weekend "]]
# # print(len(cumulative))

# # print(cumulative[0])
# print(cumulative[1][0])



# total=["The kid", 345 ] 
# today =["Sunday was good", "Saturday was raining", 25.89]
# Weekend=[today + total]
# # print(Weekend)
# # print(total*3)
# #print("Sunday" in today)
# # print(345 in total)
# # print(25.89 in today)
# #print("Sunday was good" in today)
# total[1]="My kid"
# total.remove("My kid")
# print(total)
# # print(total)
# today.append("Hoping Monday will be better")
# print(today)


# trainees = ["John", [2, ["James","Mary"]]]
# print(trainees[1][0])
# print(trainees[1][1][0])
# trainees.append(56)
# print(trainees)
# print(len(trainees))
# trainees[1][0]=8
# print(trainees)
# trainees.remove("John")
# print(trainees)
# # 4. Using a method add the name Mike between James and Mary
# trainees[1][1].insert(1,"mike")
# # 6. Remove John and Mary from the list.
# trainees[0][1].remove("mary")
# print(trainees)
# # length
# print(len(trainees))



# days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
# #1. Find wednesday using an index
# print(days[2])
# #2. Using a function a find the length of the tuple
# print(len(days))
# #3. Replace Thursday with Thur
# #converting tuple into list
# days=list(days)
# print(days)
# #replacing thursday with thurs
# days[3]="thur"
# #converting list to tuple
# days =tuple(days)
# print(days)


# days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
# print(days)
# #remove friday and sunday from the set using methods and add them back to the set
# # days=list(days)
# # print(days)
# # # days[6].remove("friday")
# # # days[0].remove('sunday')
# # days[0].insert("sunday")
# # days(6).insert("friday")
# # days = set(days)
# # print(days)
# print("monday"in days)
# days.remove("friday")
# days.remove("monday")

#variables-str,numbers.bolean
#data structures- list,dicts
#operators- arithmetic,conditional,logical
#If else
#For loop





# x=5
# y=10
# z=x+y
# print(z)


# x="hello word"
# y= x.upper()
# print(y)
# z=x.strip()


# trainees = ["john" , [2, ["james" , "mary"]]]
# trainees[1][1].remove("mary")
# print(trainees)
# trainees.remove("john")
# print(trainees)


#Dictionary
# person= ["location" : "nairobi", "countries" : ["kenya" , "Turkey"]]
# person=["age"]=2
# print(person)["countries"][-1])
# print("countries"in person.keys())s
# print(person.values())
# print(person.items())
# print(person)

# taskList = [23, “Jane”, [“Lesson 23”, 560, {“currency” : “KES”}], 987, (76,”John”)]
# 1. Determining class of taskList using an inbuilt function
# 2. Print KES
# 3. Print 560
# 4. Use a function to determine the length of taskList
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
# For number 5 above we can research the solution online
# 6. Change the name “John” to “Jane” . 
# 7. In the dictionary with the key currency, add another key “amount” with value 9


# taskList = [23, 'Jane', ['Lesson 23', 560, {"currency" : "KES"}], 987, (76,"John")]
# # print(type(taskList))# 1. Determining class of taskList using an inbuilt function
# # print(len(taskList))# 4. Use a function to determine the length of taskList
# print(taskList[2][2]['currency'])
# print(taskList[2][1])# 3. Print 560
# 6. Change the name “John” to “Jane” .
# taskList[4]=list(taskList[4])
# taskList[4][1]="jane"
# taskList[4]=tuple(taskList[4])
# print(taskList[4])
# taskList[2][2]["amount"]=90
# print(taskList)
#remove "Jane"
# taskList.remove('Jane')#remove "Jane"
# print(taskList)
#add "Jane" back
# taskList.insert(1,"Jane")#add "Jane" back
# print(taskList)
# print(str(taskList[3])[::-1])


# ls1=["Mombasa", ["Kitale", ("Eldoret", "Fill"),("Nakuru")]]
# # Replace Fill with Machakos
# #Expected output should be
# #["Mombasa", ["Kitale", ("Eldoret", "Machakos"),("Nakuru")]]
# temp= list(ls1[1][1])
# temp[1]="machakos"
# temp=tuple(temp)
# ls1[1][1]=temp
# print(ls1)
# person= ["location" : "nairobi", "countries" : ["kenya" , "Turkey"]]
# print(type(person))
# # print(person["countries"][0])


# if 6>7:
#  print("Executes when false")
#  print("Executes also when false")
#  print("Executes also when false")
# else:
#  print("Executes when true")
#  print("Executes when true")

#  print("Executes either way")

# if 40<25:
#   print("Executes when true")
#   print("Executes also when false")
# else:
#    print("Executes when true")

# print("Executes either way")


#Take input from a user requesting for marks and check if its either
#>70 is A
#>=60 and <70 is B
#>=50 and <60 is C
#>=40 and <50 is D
#<40 is E

# average_marks=int(input("Enter marks"))
# if average_marks<40:
#     print("E")
# elif average_marks>=40 and average_marks<50: 
#     print("D")
# elif average_marks>=50 and average_marks<60:
#     print("C")
# elif average_marks>=60 and average_marks<70:
#     print("B")
# else:
#     print("A")


# #Take 3 numbers from a user and return the largest of the 3
# #return the largest from the 3
# num1=int(input("enter marks num 1:"))
# num2=int(input('enter marks num 2:'))
# num3=int(input("enter marks num 3:"))
# if num1>num2 and num1>num3:
#  print("num1")
# elif num2>num1 and num2>num3:
#  print("num2")
# elif num3>num1 and num3>num1:
#  print("num3")
# else:
#   print("num1=num2=num3")


# if num1>num2 :   
#     print(num1)
# elif num2>num3:
#      print(num2)
# elif num3>num2:
#     print(num3)
# else:
#     print("num1=num2=num3")

try:
  marks= float(input("enter marks:"))
  if marks < 0 or marks>100:
    print("invalid marks")
  else:
        if marks<40:
          print('E')
        else:
            if marks>=40 or marks<50:
                print("D")
            else:
              if marks>=50 or marks<60:
                  print("C")
              else:
                  if marks>=60 or marks<70:
                    print("B")
                  else:
                    print("A")
# # except:("Ensure what you have entred is a number")
# except Exception as edu:
#    print(edu)


# lsl=list(range(0,10))
# print(lsl)

# # for ken in lsl:
# #     print("now ken is",ken)

# # kenya=tuple(range(0,20))
# # print(kenya)
# # print(list(kenya))
# # for Nairobi in kenya:
# for i in lsl:
#     if 1%2 == 0:
#         print(i)
#     else:
#         pass


# ls2=[("E",40),("A",30),("B",65)]
# total=0
# for i in ls2:
#     total=total+i[1]
#     # print(total)
#     # if i [1] == 30:
#     #     break
    

# avg=total / len(ls2)
# print(total)  



# try:
#     mark=float(input("Enter a mark:"))
#     if mark<0 or mark>100:
#         if marks<40:
#             print("E")
#         else:
#             if mark>40 and mark<50:
#                 print("D")
#             else:
#                 if mark>50 and mark<60:
#                     print("C")
#                 else:
#                     if mark>60 and mark <70:
#                         print("B")
#                     else:
#                         print("A")
      
        

            



                
    
    
 
    
                                   
            
          
            
              
      



    

       
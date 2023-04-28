# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
Basic_salary=float(input("enter basic salary"))
benefits=float(input("enter benefits"))
gross_salary=Basic_salary+benefits
print(gross_salary)

if gross_salary<=5999:
    print(150)
elif gross_salary>=6000 and gross_salary<7999:
    print(300)
elif gross_salary>=12000 and gross_salary<14999:
    print(500)
elif gross_salary>=15000 and gross_salary<19999:
     print(600)
elif gross_salary>=20000 and gross_salary<24999:
     print(750)
elif gross_salary>=25000 and gross_salary<29999:
     print(850)
elif gross_salary>=30000 and gross_salary<34999:
     print(900)
elif gross_salary>=35000 and gross_salary< 39999:
     print(950)
elif gross_salary>=40000 and gross_salary< 44999:
     print(1000)
elif gross_salary>=45000 and gross_salary< 49999:
     print(1100)
elif gross_salary>=50000 and gross_salary<59999:
     print(1200)
elif gross_salary>=60000 and gross_salary<69999:
     print(1300)
elif gross_salary>=70000 and gross_salary< 79999:
     print(1400)
elif gross_salary>=80000 and gross_salary< 89999:
     print(1500)
elif gross_salary>=90000 and gross_salary<99999:
     print(1600)
else:
     print(1700)


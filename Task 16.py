# Continue with the program above, then use the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using THIS LINK:  
Basic_salary=float(input("enter basic salary"))
benefits=float(input("enter benefits"))
gross_salary=Basic_salary+benefits
print(gross_salary)
NSSF=gross_salary*0.06

if gross_salary<=5999:
    print(150)
    print('NSSF=',NSSF)
elif gross_salary>=6000 and gross_salary<7999:
    print(300)
    print('NSSF=',NSSF)
elif gross_salary>=12000 and gross_salary<14999:
    print(500)
    print('NSSF=',NSSF)
elif gross_salary>=15000 and gross_salary<19999:
     print(600)
     print('NSSF=',NSSF)
elif gross_salary>=20000 and gross_salary<24999:
     print(750)
     print('NSSF=',NSSF)
elif gross_salary>=25000 and gross_salary<29999:
     print(850)
     print('NSSF=',NSSF)
elif gross_salary>=30000 and gross_salary<34999:
     print(900)
elif gross_salary>=35000 and gross_salary< 39999:
     print(950)
     print('NSSF=',NSSF)
elif gross_salary>=40000 and gross_salary< 44999:
     print(1000)
     print('NSSF=',NSSF)
elif gross_salary>=45000 and gross_salary< 49999:
     print(1100)
     print('NSSF=',NSSF)
elif gross_salary>=50000 and gross_salary<59999:
     print(1200)
     print('NSSF=',NSSF)
elif gross_salary>=60000 and gross_salary<69999:
     print(1300)
     print('NSSF=',NSSF)
elif gross_salary>=70000 and gross_salary< 79999:
     print(1400)
     print('NSSF=',NSSF)
elif gross_salary>=80000 and gross_salary< 89999:
     print(1500)
     print('NSSF=',NSSF)
elif gross_salary>=90000 and gross_salary<99999:
     print(1600)
     print('NSSF=',NSSF)
else:
     print(1700)



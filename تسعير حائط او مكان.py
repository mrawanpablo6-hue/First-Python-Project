str_lengh=input("Please type lengh:\n")
str_widgh=input("Please type widgh:\n")
str_money=input("How much for 1 meter:\n")
#احول من سترانج الي Floaat
lengh=float(str_lengh)
widgh=float(str_widgh)
Money=float(str_money)
#احسب شكل المستطيل = الطول * العرض
area=lengh*widgh
total=area*Money
print("the total is :"+str(area))
print("Give the guy :""$"+str(total))
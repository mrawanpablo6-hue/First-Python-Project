total_second=int(input("Please type your second:\n"))
minutes=total_second//60
print(f"This course is:",{minutes//60},"hours and",{minutes%60},"minutes and",{total_second%60},"second")
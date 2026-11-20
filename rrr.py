import sys
salary = int(sys.argv[1])

if salary < 20000:
    bonus = salary * 5 / 100

elif salary >= 20000 and salary < 40000:
    bonus = salary * 10 / 100

else:
    bonus = salary * 15 / 100

annual_salary = salary + bonus

print("Your bonus is =", bonus)
print("Your annual salary is =", annual_salary)

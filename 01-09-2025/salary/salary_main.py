#  Driver code

from salary_manger import create_salary,read_all,read_by_salary
from salary_manger import salaries, update, delete_by_salary

create_salary(1000)
create_salary(2000)
create_salary(3000)
create_salary(4000) 
create_salary(8000) 

result_salaries= read_all()
for salary in result_salaries:
    print(salary)
    
print(read_by_salary(3000)) #1
print(read_by_salary(8000)) #3
print(salaries[read_by_salary(5000)]) #-1

update(8000,8500)
print(read_all())

delete_by_salary(2000)
print(read_all())
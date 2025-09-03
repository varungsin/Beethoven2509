import logging 
import pickle

logging.basicConfig(filename='app.log', 
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO)

employees = []  
def create_employee(id, name, job_title, salary, join_date):    
    emp = {
        'id':id, 
        'name': name, 
        'job_title': job_title, 
        'salary': salary, 
        'join_date': join_date
    }
    employees = read_all()
    employees.append(emp)
    with open('employee.dat','rwbb' ) as writer:
        pickle.dump(employees, writer)
    logging.info(f'{name} Employee Created.')
def read_all():
    with open('employee.dat','rb' ) as reader:
        employees = pickle.load(reader)
        if employees == None:
            return []
    return employees
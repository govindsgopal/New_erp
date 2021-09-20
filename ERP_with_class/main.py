from mod_emp import Employee
import emp_search as search
import mod_details as change
employees = []
def menu():
	print("1. Add Employee")
	print("2. Delete Employee")
	print("3. Change employee data")
	print("4. Search Employee")
	print("5. Display")
	print("6. Exit")

def add_employee():
	print("Add Employee")
	emp_id  = int(input("Enter id : "))
	emp_name = input("Enter name : ")
	emp_age = int(input("Enter age : "))
	emp_gender = input("Gender : ")	
	emp_sal= input ("Enter salary : ")
	emp_place = input("Enter place : ")
	emp_joindate = input("Enter joined date : ")		
	emp_prevcomp =input("Enter previous company : ")
	emp_obj = Employee(emp_id,emp_name,emp_age,emp_gender,emp_place,emp_sal,emp_prevcomp,emp_joindate)
	employees.append(emp_obj)

def display_employee():
	if len(employees) == 0:
		pass
	else:
		for i in employees:
			i.display()

def delete_employee():
	emp_id = int(input("Enter the id : "))
	for i in employees:
		if i.emp_id == emp_id :
			employees.pop(employees.index(i))
while True : 
	menu()
	ch = int(input("Enter the choice : "))
	if ch is None:
		print("Enter valid choice :  ")
	elif ch == 1:
		add_employee()
	elif ch == 2:
		delete_employee()
	elif ch == 3:
		change.update_empoyee(employees)
	elif ch == 4:
		search.search_employee_options(employees)	
	elif ch == 5:
		display_employee()
	elif ch == 6:
		break
	else:
		print("Invalid choice")	

from mod_employee import Employee as emp
def update_menu():
	print("Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
	

def update_empoyee(employee):
	emp_id = int(input("Enter employee id"))
	update_menu()
	choice = input("\tEnter the choice")
	
	if choice == "a":
		name = input("\tEnter new name : ")
		emp_obj  = list(filter(lambda a: a.emp_id == emp_id,employee))
		emp_obj[0].set_name(name)
		elif choice == "b":
		age = input("\tEnter new age : ")
		emp_obj  = list(filter(lambda a: a.emp_id == emp_id,employee))
		emp_obj[0].set_age(age)
	elif choice == "c":
		gender = input("\tEnter new gender : ")
		emp_obj  = list(filter(lambda a: a.emp_id == emp_id,employee))
		emp_obj[0].set_gender(gender)
	elif choice == "d":
		sal = input("\tEnter new salary : ")
		emp_obj  = list(filter(lambda a: a.emp_id == emp_id,employee))
		emp_obj[0].set_salary(sal)
	else:
		print("Wrong choice")

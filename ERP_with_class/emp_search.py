def search_menu():
	print("Change employee data")
	print("\ta. search by Name")
	print("\tb. search by age")
	print("\tc. search by gender")
	print("\td. search by salary")
	print("\te. Exit")
	
def search_employee_options(employee):
	search_menu()
	ch = input("\tEnter the choice : ")
	if ch == "a":
		name = input("\tEnter the name to be search : ")
		lst = list(filter(lambda a: a.emp_name == name,employee))
		if len(lst) == 0:
			print("\tNo Employee found")
		else:
			for i in lst:
				print(f"\t{i.emp_name} is found")
	elif ch == "b":
		age = int(input("\tEnter the age to be search : "))
		lst = list(filter(lambda a: a.emp_age == age,employee))
		if len(lst) == 0: 
			print("\tNo Employee found")
		else:
			for i in lst:
				print(f"\t{i.emp_name} => {i.emp_age} is found")
	elif ch == "c":
		gender = input("\tEnter the gender to be search")
		lst = list(filter(lambda a: a.emp_gender == gender,employee))
		if len(lst) == 0:
			print("\tNo Employee found")
		else:
			for i in lst:
				print(f"\t{i.emp_name} => {i.emp_gender}  is found")
	elif ch == "d":
		salary = input("\tEnter the salary to be search : ")
		lst = list(filter(lambda a: a.emp_sal == salary,employee))
		if len(lst) == 0:
			print("\tNo Employee found")
		else:
			for i in lst:
				print(f"\t{i.emp_name} => {i.emp_sal}  is found")
	else:	
		print("\tInvalid choice")

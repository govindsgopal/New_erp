employees = {}
team = {}
def main_menu():
	print ("Choose your option ")
	print ("1.Add Employee")
	print ("2.Delete Employee ")
	print ("3.Search Employee ")
	print ("4.Change employee data ")
	print ("5.Display Employees")
	print ("6.Manage Teams")
	print ("7.Exit ")
def add_emp():
	e_id= input("Enter the employee code")
	if e_id not in employees.keys():
		name = input("Enter the name \t")
		age = input("Enter their age \t")
		J_date = input("Enter their joining date \t")
		sal = input("Enter their current salary \t")
		Pre_emp = input("Enter their previous employeer \t")
		temp = {
				"Name" : name,
				"Age" : age,
				"Joining date" : J_date,
				"Current salary" : sal,
				"Previous employer" : Pre_emp,
		}
		employees[e_id] = temp
	else:
		print ("Wrong employee ID")
def del_emp():
	e_id = input("\n Enter the employee ID to be deleted\t")
	if e_id not in employees.keys():
		print("Wrong employee ID ")
	else:
		del employees[e_id]
def search_emp():
	name = input("Enter the name of the employee\t")
	flag = False
	for i in employees.values():
		if  i["Name"] == name: 
			print (f"{name} is in the employees list")
			print (f' {i["Name"]} | {i["Age"]} | {i["Joining date"]} | {i["Previous employer"]} | {i["Current salary"]}')
			flag = True
			break
	if flag == False:
		print ("Invalid employee ID")
def mod_sub_menu():
	print ("\t\t1.Change the employee name \n")
	print ("\t\t2.Change the employee age \n")
	print ("\t\t3.Change the employee date of joining \n")
	print ("\t\t4.Change the employee salary \n")
	print ("\t\t5.Change the employees previous employer \n")
	print ("\t\t6.Exit \n")

def mod_emp():
	e_id = input("Enter the employee ID to be changed")
	if e_id in employees.keys():
		while True:		
			mod_sub_menu()
			ch = input("Enter your choice \n")
			if ch == "1":
				name = input("Enter the new name  ")
				employees[e_id]["Name"] = name
			elif ch == "2":
				age = input("Enter the new age  ")
				employees[e_id]["Age"] = age
			elif ch == "3":
				j_date = input("Enter the new date of joining  ")
				employees[e_id]["Joining date"] = j_date
			elif ch == "4":
				sal = input("Enter the updated salary  ")
				employees[e_id]["Current salary"] = sal
			elif ch == "5":
				pre_emp = input("Enter the updated previous employee details")
				employees[e_id]["Previous employer"] = pre_emp
			elif ch == "6":
				break
			else:
				print ("Invalid input")
	else:
		print ("invalid employee ID")
def disp_emp():
	
	for e_id,i in employees.items():
		print (f'\t {e_id} | {i["Name"]} | {i["Age"]} | {i["Joining date"]}  | {i["Current salary"]} | {i["Previous employer"]}')
def manage_team_menu():
	print ("\t\t1.Create new team ")
	print ("\t\t2.Display team")
	print ("\t\t3.Modify teams ")
	print ("\t\t4.Delete teams")
	print ("\t\t5.Exit")
def create_team():
	team_name = input("Enter the Team name to be created \t")
	team[team_name] = []
	
def display_team():
	for key,value in team.items():
		names = ""
		for i in value:
			names = names + "|" + employees[i]["Name"]
		print (f'{key} ==> {names}')	
def modify_teams_menu():
	print ("\t\t\t1.Display_members \n")
	print ("\t\t\t2.Add members\n")
	print ("\t\t\t3.Delete members \n")
	print ("\t\t\t4.exit")
def display_team_members(team_name):
	names = ""
	for i in employees[team_name]:
		names = names + "|" + i + "." + employees[i]["Name"]
	print (f'{names}')

def add_members(team_name):

	disp_emp()
	e_id = input("Enter the ID of the Employee to be added to group")
	if e_id in employees.keys():
		team[team_name].append(e_id)
def delete_members(team_name):
	display_team_members(team_name)
	e_id = input("Enter the group member to be deleted")
	if e_id in teams[team_name]:
		teams[team_name].remove(e_id)
	else:
		print ("Wrong employee ID")

def modify_team():
	team_name = input("Enter the team to be modified\t")
	while True:
		modify_teams_menu()
		ch = input("Enter your choice\t")
		if ch == "1" :
			display_team_members(team_name)		

		elif ch == "2":
			add_members(team_name)

		elif ch == "3":
			delete_members(team_name)
		elif ch == "4":
			break
		else:
			print("Invalid input")

def delete_team():
	display_team()
	team_name = input("Enter the team to be delete")
	if team_name in team.keys():
		del team[team_name]
		print ("Group deleted")
	else:
		print("Invalid team name")	

def manage_teams():
	while True:
		manage_team_menu()		
		ch = input("Enter your option")
		if ch == "1" :
			create_team()		

		elif ch == "2":
			display_team()

		elif ch == "3":
			modify_team()
	
		elif ch == "4":
			delete_team()
		elif ch == "5":
			break
		else:
			print("Invalid input")	

while True:
	
	main_menu()
	choice = input("Enter your option \n")

	if choice == "1" :
		add_emp()
		

	elif choice == "2":
		del_emp()

	elif choice == "3":
		search_emp()
		name = input("Enter the name of the employee")

	elif choice == "4":
		mod_emp()

	elif choice == "5":
		disp_emp()

	elif choice == "6":
		manage_teams()

	elif choice == "7":
                break
	else:
                print ("Invalid input")


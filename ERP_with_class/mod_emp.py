from def_user import User

class Employee(User):
	def __init__(self, emp_id = 0, name = "", age = 0, gender = "",place = "",salary = "",previous_company = "",joining_date = ""):
		self.emp_id = emp_id
		self.emp_name = name
		self.emp_age = age
		self.emp_gender = gender
		self.emp_place = place
		self.emp_sal = salary
		self.emp_prevcomp = previous_company
		self.emp_joindate = joining_date
		self.set_username(input("Enter the Username : "))
		self.set_password(input("Enter the Password : "))
		self.role = input("Enter Role : ")
		
	def set_name(self,name):
		self.emp_name = name
		return "Name assigned Successfully"
	def set_age(self,age):
		self.emp_age = age
		return "Age assigned Successfully"
	def set_salary(self,name):
		self.emp_sal = name
		return "Salary assigned Successfully"
	def set_gender(self,name):
		self.emp_gender = name
		return "Gender changed Successfully"
	def display(self):
		print(f"{self.emp_id} | {self.emp_name} | {self.emp_age} | {self.emp_gender} | {self.emp_sal} | {self.get_username()}")



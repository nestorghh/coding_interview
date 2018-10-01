#You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

#For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

#Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

class Employee:
	def __init__(self,id,importance,subordinates):
		self.id = id
		self.importance = importance
		self.subordinates = subordinates

e1=Employee(1,5,[2,3])
e2=Employee(2,3,[])
e3=Employee(3,3,[])

employees =[e1,e2,e3] 


def getImportance(employees,id):

	def dfs(employee,infos):
		importance = employee.importance
		for child in employee.subordinates:
			importance += dfs(infos[child], infos)
		return importance
		
	infos = {}

	for employee in employees:
		infos[employee.id] = employee

	return dfs(infos[id],infos)
	









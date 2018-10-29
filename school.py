class School():

	def __init__(self, school_name):
		self._school_name = school_name
		self.roster = {}

	# def add_student(self, student_name, grade):
	# 	student = {grade: student_name}
	# 	self.roster.update(student)

	def add_student(self, student_name, grade):
		# student = {grade: [student_name]}
		# student = {grade: student_name}
		if grade in self.roster.keys():
			self.roster[grade].append(student_name)
		else:
			self.roster[grade] = []
			self.roster[grade].append(student_name)
	
	def grade(self, grade):
		return self.roster[grade]

	def sort_roster(self):
		
		# new_dict = self.roster.copy()
		# new_dict = dict(map(lambda grade: new_dict[grade] = sorted(new_dict[grade] , new_dict.keys())))

		for grade in self.roster.keys():
			self.roster[grade] = sorted(self.roster[grade])
		
		return self.roster
class Student:
	def __init__(self, name, id): 
		self.name = name
		self.id = id
		self.courses = []
		self.grades = []
	
	def enroll(self, Course):
		self.courses.append(Course)
		self.grades.append(0.0)
		
	def drop(self, Course):
			self.grades.pop(self.courses.index(Course))
			self.courses.remove(Course)
			print("Course successfully removed")
		
	def editName(self,name):
		self.name = name
		
	def grade(self, score, Course):
		self.grades[self.courses.index(Course)] = score
		
	def viewReportCard(self):
		gpa = 0
		totalunits = 0
		for i in range(0,len(self.courses)):
			print("Course: " + self.courses[i].code.ljust(10) + "| Grade: " + str(self.grades[i]))
			gpa+= (self.grades[i] * self.courses[i].units)
			totalunits += self.courses[i].units
		gpa/=totalunits
		print("GPA: " + str(gpa))
		
	def enrolledIn(self, course):
		exists = False
		for i in range(0, len(self.courses)):
			if(self.courses[i].code == course):
				exists = True
				break
		return exists
		
	hasCourses = lambda self: True if (len(self.courses)!= 0) else False
			
		
		
class Course:
	def __init__(self, code, units):
		self.code = code
		self.units  = units
		'''self.students = []
		
	def addStudent(self, Student): 
		self.students.append(Student)
		
	def removeStudent(self, Student):
		self.students.remove(Student)'''
		
def idExists(num):
	exists = False
	for i in range(0, len(allStudents)):
		if(allStudents[i].id ==  num):
			exists = True
	return exists
	
def courseExists(num):
	exists = False
	for i in range(0, len(allCourses)):
		if(allCourses[i].code == num):
			exists = True
	return exists
	
			
def editStudentMenu(s):
	opt2 = -1
	while(opt2 != 0):
		print("\n\n-EDIT STUDENT MENU-")
		print("1 - Change name")
		print("0 - Return to Student Menu")
		opt2 = int(input("Option: "))
		if(opt2 == 1):
			newName = raw_input("New name: ")
			s.editName(newName)
			print("Editing Successful")
		elif(opt2 == 0):
			print("Returning to Student Menu...")
			
def courseMenu():
	opt1 = -1
	while(opt1 != 0):
		print("\n\n--COURSE MENU--")
		print("1 - Add Course")
		print("2 - Remove Course")
		print("3 - Edit Course")
		print("0 - Back to Main Menu")
		opt1 = int(input("Option: "))
		if(opt1 == 1):
			while(True):
				newCode = raw_input("Unique 7 character Course code: ")
				if(len(newCode) != 7):
					print("Please input exactly 7 characters for your course code")
				elif(courseExists(newCode)):
					print("Code is already being used by another course")
				else:
					tempUnits = int(input("Enter number of units: "))
					allCourses.append(Course(newCode, tempUnits))
					print("Successful course creation")
					break
		elif(opt1 == 2):
			tempCode = raw_input("Enter code of course to remove: ")
			if(courseExists(tempCode)):
				for i in range(0, len(allCourses)):
					if(allCourses[i].code == tempCode):
						for j in range(0, len(allStudents)):
							allStudents[j].drop(allCourses[i])
						allCourses.remove(allCourses[i])
						print("Course successfully removed")
						break
			else:
				print("Course does not exist")
		elif(opt1 == 3):
			tempCode = raw_input("Enter code of course to edit: ")
			if(courseExists):
				for i in range(0, len(allCourses)):
					if(allCourses[i].code == tempCode):
						allCourses[i].units = raw_input("Enter new number of units")
		elif(opt1 == 0):
			print("Returning to main menu...")
		else:
			print("Invalid input.")
					
						
			
		
def studentMenu():
	opt1 = -1
	while(opt1 != 0):
		print("\n\n--STUDENT MENU--")
		print("1 - Add Student")
		print("2 - Remove Student")
		print("3 - Edit Student")
		print("0 - Back to Main Menu")
		opt1 = int(input("Option: "))
		if(opt1 == 1):
			newName = raw_input("Name: ")
			while(True):
				newID = int(input("8 character ID: "))
				if(len(str(newID)) != 8):
					print("Please input exactly 8 characters for your ID")
				elif(idExists(newID)):
					print("ID already exists. Please choose another")
				else:
					break
			newStudent = Student(newName, newID)
			allStudents.append(newStudent)
			print("Student successfully added")
		elif(opt1 == 2):
			if(len(allStudents) == 0):
				print("No students to remove")
			else:
				tempID = int(input("ID of Student to remove: "))
				found = False
				for i in range(0, len(allStudents)):
					if(allStudents[i].id ==  tempID):
						'''for j in range(0, len(allCourses)):
							allCourses.removeStudent(allStudents[i])
						'''
						found = True
						allStudents.remove(allStudents[i])
						print("Removal Successful")
						break
				if(not found):
					print("Student not found")
		elif(opt1 == 3):
			if(len(allStudents) == 0):
				print("No students to edit")
			else:
				found = 0
				tempID = int(input("ID of Student to edit: "))
				for i in range(0, len(allStudents)):
					if(allStudents[i].id ==  tempID):
						editStudentMenu(allStudents[i])
						found = 1
						break
				if(found==0):
					print("Student not found")
		elif(opt1 == 0):
			print("Returning to Main Menu...")
		else:
			print("Invalid input. Try again!")

def enrollmentMenu(thisStudent):
	opt1 = -1
	while(opt1 != 0):
		print("\n\n--ENROLLMENT MENU--")
		print("1 - Enroll in a course")
		print("2 - Drop a course")
		print("3 - Set grade")
		print("4 - View Report Card")
		print("0 - Exit")
		opt1 = int(input("Option: "))
		if(opt1==1):
			newCourse = raw_input("Enter the code of the course you want to enroll in: ")
			if(courseExists(newCourse) and not thisStudent.enrolledIn(newCourse)):
				for i in range(0, len(allCourses)):
					if(allCourses[i].code == newCourse):
						thisStudent.enroll(allCourses[i])
						print("Successfully enrolled in " + allCourses[i].code)
						break
			else:
				print("Course does not exist/Already enrolled in the course")
		elif(opt1==2):
			removeCourse = raw_input("Enter the code of the course to drop: ")
			if(courseExists(removeCourse) and thisStudent.enrolledIn(removeCourse)):
				for i in range(0, len(thisStudent.courses)):
					if(thisStudent.courses[i].code == removeCourse):
						thisStudent.drop(thisStudent.courses[i])
						break
			else:
				print("Course does not exist")
		elif(opt1==3):
			gradeCourse = raw_input("Enter the code of the course you want to grade: ")
			if(courseExists(gradeCourse) and thisStudent.enrolledIn(gradeCourse)):
				grade = float(input("Enter the grade you got: "))
				if(grade>=0 or grade<=4):
					for i in range(0, len(thisStudent.courses)):
						if(thisStudent.courses[i].code == gradeCourse):
							thisStudent.grade(grade, thisStudent.courses[i])
							print("Course successfully graded")
							break
				else:
					print("Invalid grade")
			else:
				print("Student is not enrolled in this course/course does not exist")
		elif(opt1==4):
			if(thisStudent.hasCourses()):
				thisStudent.viewReportCard()
			else:
				print("Not enrolled in any courses")
		elif(opt1==0):
			print("Returning to Main Menu...")
		else:
			print("Invalid input")

def displayAllStudents():
	print("\nAll Students:")
	for i in range(0, len(allStudents)):
		print("Name: " + allStudents[i].name.ljust(20) + "| ID: " + str(allStudents[i].id))
		
def displayAllCourses():
	print("\nAll Courses:")
	for i in range(0, len(allCourses)):
		print("Course: " + allCourses[i].code.ljust(10) + "| Units: " + str(allCourses[i].units))
		
def mainMenu():
	opt = -1
	while(opt != 0):
		print("\n\n---MAIN MENU---")
		print("1 - Student Menu")
		print("2 - Course Menu")
		print("3 - View ALL Students")
		print("4 - View ALL Courses")
		print("5 - Enrollment Menu")
		print("0 - Exit")
		opt = int(input("Option: "))
		if(opt == 1):
			studentMenu()
		elif(opt == 2):
			courseMenu()
		elif(opt == 3):
			displayAllStudents()
		elif(opt == 4):
			displayAllCourses()
		elif(opt == 5):
			if(len(allStudents) == 0):
				print("There are no students. Add students first. ")
			else:
				student = int(input("Enter ID of student: "))
				if(idExists(student)):
					for i in range(0, len(allStudents)):
						if(allStudents[i].id == student):
							print("\nEnrollment menu for " + allStudents[i].name)
							enrollmentMenu(allStudents[i])
							break
				else:
					print("Student does not exist")
		elif(opt==0):
			print("Exiting program...")
		else:
			print("Invalid input. Try  again!")
	
	
	
	
allStudents = []
allCourses = []

mainMenu()

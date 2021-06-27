#Uncomment Desired Statements
class school:
    numOFStudents = 4 #class variable
    numOFTeachers = 2 #class variable
    numOFClass = 1 #class variable

#object initialization & printing
schoolClass = school() #This schoolCLass object will inherit all variables of school Class
schoolClass.name ="Github School"
#print(schoolClass.name)

print(schoolClass.numOFClass)# schoolCLass took class variable ".numOFClass and print it"
print(school.numOFStudents) #Directly access class variable
print(school.numOFClass) #Directly access class variable | same value as variable called by object

# The __dict__ Method
print(school.__dict__) #Print all variables of School (There are so many)
print(schoolClass.__dict__) #Print all variables of schoolClass (There are only 2)
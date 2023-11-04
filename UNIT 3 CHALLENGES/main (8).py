class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name 
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
      sorted_students = sorted(student_list, 
                          key=lambda student:student.cgpa,
                          reverse=True)
      return sorted_students
students= [
      student("jack","a124",10),
      student("hendry",'a125',9.6),
      student('joel','a126',6.3),
      student('lional','a127',8.6),
      
      
]

sorted_students = sort_students(students)

for student in sorted_students:

   print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name,

     student.roll_number, student.cgpa))
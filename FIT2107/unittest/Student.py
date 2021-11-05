class Student:
   def __init__(self, firstName, familyName, grade):
       self.givenName = firstName
       self.familyName = familyName
       self.grade = grade

   def letter_grade(self):
       '''Return the letter grade from the numerical mark
       for this student according to the standard Monash scale'''
       if self.grade >= 80:
          return "HD"
       elif self.grade >=70:
          return "D"
       elif self.grade >=60:
          return "C"
       elif self.grade >=50:
          return "P"
       else:
          return "N"

   def pass_subject(self):
       '''Return true if the student has received a passing grade for
       this subject'''
       return self.letter_grade() != "N"

   def result_summary(self):
        return self.firstName + " " + self.familyName + " " + str(self.grade) + " " + self.letter_grade()

class Unit:
   def __init__(self, students):
       self.students = students

   def fail_report(self):
       for student in students:
           if not student.pass_subject():
               self.print(student.result_summary())

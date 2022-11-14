from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(1000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(100))
    first_name=db.Column(db.String(30))
    notes=db.relationship('Note')

class student(db.Model,UserMixin):
    UID=db.Column(db.Integer,primary_key=True)
    
    Full_Name=db.Column(db.String(50))
    Mothers_Name=db.Column(db.String(20))
    Fathers_Name=db.Column(db.String(20))
    Phone_No=db.Column(db.Integer)
    Address=db.Column(db.String(200))
    DOB=db.Column(db.DateTime)
    Age=db.Column(db.Integer)
    Fees=db.Column(db.Integer)
    Fees_Status=db.Column(db.String(20))
    Attendance=db.Column(db.Float)
    CGPA=db.Column(db.Float)
    Year_of_Graduation=db.Column(db.Integer)
    Branch=db.Column(db.String(20))

    college_email=db.Column(db.String(30))
    college_password=db.Column(db.String(100))
    student_course=db.relationship('Takes')
#primaryjoin="student.UID==takes.UID"
    #FOREIGN KEY (Branch) REFERENCES Department(Dept_Name)
    def get_id(self):
        return (self.UID)

class staff(db.Model,UserMixin):
    Teacher_Code=db.Column(db.String(5),primary_key = True)
    Full_Name=db.Column(db.String(50))
    Mothers_Name=db.Column(db.String(20))
    Fathers_Name=db.Column(db.String(20))
    Phone_Number=db.Column(db.Integer)
    Address=db.Column(db.String(100))
    DOB=db.Column(db.DateTime)
    email=db.Column(db.String(30))
    teacher_password=db.Column(db.String(20))
    Salary=db.Column(db.Integer)
    Qualification=db.Column(db.String(20))
    Experience=db.Column(db.Integer)
    Attendance=db.Column(db.Float)
    Dept_Name=db.Column(db.String(40), db.ForeignKey('Department.Dept_Name'))
    Course_Code=db.Column(db.String(6), db.ForeignKey('courses.Course_Code'))
    
    def get_id(self):
        return (self.Teacher_Code)

class Courses(db.Model):
    Course_Name=db.Column(db.String(30))
    Course_Code=db.Column(db.String(6),primary_key=True)
    Sem_No=db.Column(db.Integer)
    Credits=db.Column(db.Integer)
    Syllabus=db.Column(db.String(100))
    Duration=db.Column(db.Integer)
    Students_enrolled=db.Column(db.Integer)
    course_taken=db.relationship('Takes',back_populates="takes_course")
    def get_id(self):
        return (self.Course_Code)
#primaryjoin="courses.Course_Code==takes.Course_Code"
class Takes(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    UID=db.Column(db.Integer,db.ForeignKey('student.UID'))
    Course_Code=db.Column(db.String(6),db.ForeignKey('courses.Course_Code'))
    grades=db.Column(db.Float)
    takes_course=db.relationship('Courses',back_populates="course_taken")

class Department(db.Model):
    Dept_Name=db.Column(db.String(40), primary_key=True)
    Avg_Package=db.Column(db.Float)
    Floor_Occupied=db.Column(db.Integer)
    SubCommittees=db.Column(db.String(50))
    def get_id(self):
        return (self.Dept_Name)
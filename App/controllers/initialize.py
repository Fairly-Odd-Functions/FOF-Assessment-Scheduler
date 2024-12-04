from datetime import datetime, date
from flask import jsonify
from App.controllers.courseAssessment import add_course_assessment
from App.database import db
from App.models import Admin, Staff, Course, Programme, CourseProgramme, Assessment, Semester, CourseOffering
from App.models.courseAssessment import ClashRules, CourseAssessment

def initialize():
    try:
        db.drop_all()
        db.create_all()

        # Create Default Admin User
        bob = Admin(firstName="Bob", lastName="Bobberson", password="bobpass", email="bob.bobberson@mail.com")

        # Create Default Staff User
        rick = Staff(firstName="Rick", lastName="Rickson", password="rickpass", email="rick.rickson@mail.com")

        # #TESTING CODE: Add Staff Course
        # from datetime import date
        # from App.models import Course, Semester
        # course = Course(courseCode="COMP911", courseTitle="Intro to Mental Health", courseCredits="0", courseDescription="Help Me", courseLevel="1")        
        # semester = Semester(semesterName="Semester 1", academicYear="2024/2025", startDate=date(2024, 10, 12), endDate=date(2025, 10, 12))
        # db.session.add(course)
        # db.session.add(semester)
        # db.session.commit()

        # TESING CODE : List Semester Courses 
        # from datetime import date
        # from App.models import Semester, Course, CourseOffering
        # semester = Semester(semesterName="Semester 1", academicYear="2024/2025", startDate=date(2024, 10, 12), endDate=date(2025, 10, 12))
        # course = Course(courseCode="JAY1212", courseTitle="Introduction To Jalene", courseCredits="9000", courseDescription="Whompy Whomp", courseLevel="Expert")
        # db.session.add(semester)
        # db.session.add(course)
        # course_offering = CourseOffering(semesterName="Semester 1", courseCode="JAY1212", academicYear="2024/2025", totalStudentsEnrolled=100)
        # db.session.add(course_offering)

        # TESING CODE : List Programme Courses
        # from App.models import Programme, Course, CourseProgramme
        # programme = Programme(programmeTitle="B.Sc. Jalene Armstrong", programmeDescription="Whomp Whomp Whompy Whomp")
        # course = Course(courseCode="JAY1212", courseTitle="Introduction To Jalene Armstrong", courseCredits="9000", courseDescription="Whompy Whomp", courseLevel="Expert")
        # db.session.add(programme)
        # db.session.add(course)
        # programme_course = CourseProgramme(programmeID=1, courseCode=course.courseCode,)
        # db.session.add(programme_course)
        
        # TESTING CODE: Create A Course, Add Assessment To Course
        # from datetime import date
        # from App.models import Course, Semester,Assessment,courseAssessment
        # course = Course(courseCode="COMP911", courseTitle="Intro to Mental Health", courseCredits="0", courseDescription="Help Me", courseLevel="1")        
        # semester = Semester(semesterName="Semester 1", academicYear="2024/2025", startDate=date(2024, 10, 12), endDate=date(2025, 10, 12))
        # assessment = Assessment(assessmentTitle="CourseWork#1", assessmentType="Midterm", startDate=date(2024, 10, 12), dueDate=date(2024, 10, 12))
        # db.session.add(assessment)
        # db.session.add(course)
        # db.session.add(semester)
        # db.session.commit()

        # Create The Programme, Semester & Courses | Add Them To The Database
        programme = Programme(programmeTitle="B.Sc. Test Programme", programmeDescription="Test Description")
        db.session.add(programme)
        db.session.commit()

        semester = Semester(semesterName="Semester 1", academicYear="2024/2025", startDate=date(2024, 10, 12), endDate=date(2025, 10, 12))
        db.session.add(semester)
        db.session.commit()

        course1 = Course(courseCode="COMP101", courseTitle="Intro to Mental Health", courseCredits="0", courseDescription="Help Me", courseLevel="1")
        db.session.add(course1)
        db.session.commit()

        course2 = Course(courseCode="COMP102", courseTitle="Intro to Mental Health", courseCredits="0", courseDescription="Help Me", courseLevel="1")
        db.session.add(course2)
        db.session.commit()

        # Add The Courses To The Programme Then To The Semester
        programme_course1 = CourseProgramme(programmeID=programme.programmeID, courseCode=course1.courseCode)
        db.session.add(programme_course1)
        db.session.commit()

        programme_course2 = CourseProgramme(programmeID=programme.programmeID, courseCode=course2.courseCode)
        db.session.add(programme_course2)
        db.session.commit()

        semester_course1 = CourseOffering(courseCode=course1.courseCode, semesterID=semester.semesterID, totalStudentsEnrolled=120)
        db.session.add(semester_course1)
        db.session.commit()

        semester_course2 = CourseOffering(courseCode=course2.courseCode, semesterID=semester.semesterID, totalStudentsEnrolled=100)
        db.session.add(semester_course2)
        db.session.commit()

        # Create The Assessments
        assessment1 = Assessment(assessmentTitle="Coursework Exam", assessmentType="COURSEWORK")
        db.session.add(assessment1)
        db.session.commit()

        assessment2 = Assessment(assessmentTitle="Quiz 1", assessmentType="QUIZ")
        db.session.add(assessment2)
        db.session.commit()

        assessment3 = Assessment(assessmentTitle="Final", assessmentType="FINAL")
        db.session.add(assessment3)
        db.session.commit()

        course_assessment1 = CourseAssessment(
                                courseCode=course1.courseCode, 
                                assessmentID=assessment1.assessmentID,
                                startDate=datetime.strptime("2024-10-10", "%Y-%m-%d"),
                                endDate=datetime.strptime("2024-10-10", "%Y-%m-%d"),
                                startTime=datetime.strptime("09:00", "%H:%M").time(),
                                endTime=datetime.strptime("10:00", "%H:%M").time(),
                                clashRule=ClashRules.ASSESSMENT_TYPE
                            )
        db.session.add(course_assessment1)
        db.session.commit()

        db.session.add(rick)
        db.session.add(bob)
        db.session.commit()

    except Exception as e:
        print(f"Error: {e}")
        return jsonify(error="An Error Occurred While Initializing Database"), 500
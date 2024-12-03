import os, csv
from App.database import db
from App.models import Admin
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required
from App.controllers import *
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
# IMPORTS TO CLEAN UP

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

# * - PPC [Previous Project's Code :D]

"""
Users [8]
Written By
"""
# 01 : Register Staff
@admin_views.route('/registerStaff', methods=['POST'])
@jwt_required(Admin)
def register_staff_action():
    pass
    
# 02 : Create Admin
@admin_views.route('/createAdmin', methods=['POST'])
@jwt_required(Admin)
def create_admin_action():
    pass

# 03 : Get All Staff Users
@admin_views.route('/allStaff', methods=['GET'])
@jwt_required(Admin)
def list_all_staff_action():
    pass

# 04 : Get All Admin Users
@admin_views.route('/allAdmin', methods=['GET'])
@jwt_required(Admin)
def list_all_admin_action():
    pass

# 05 : Update Admin
@admin_views.route('/updateAdmin', methods=['POST'])
@jwt_required(Admin)
def update_admin_action():
    pass

# 06 : Remove Admin
@admin_views.route('/removeAdmin', methods=['POST'])
@jwt_required(Admin)
def remove_admin_action():
    pass

# 07 : Update Staff
@admin_views.route('/updateStaff', methods=['POST'])
@jwt_required(Admin)
def update_staff_action():
    pass

# 08 : Remove Staff
@admin_views.route('/removeStaff', methods=['POST'])
@jwt_required(Admin)
def remove_staff_action():
    pass

"""
Course [2]
Written By
"""

# 01 : Add Course *
@admin_views.route('/addCourse', methods=['POST'])
@jwt_required(Admin)
def add_course_action():
    if request.method == 'POST':
        courseCode = request.form.get('course_code')
        title = request.form.get('title')
        description = request.form.get('description')
        data = request.form
        level = request.form.get('level')
        semester = request.form.get('semester')
        numAssessments = request.form.get('numAssessments')
        course = add_Course(courseCode,title,description,level,semester,numAssessments)
        pass

# 02 : Update Course *
@admin_views.route('/updateCourse', methods=['POST'])
@jwt_required(Admin)
def update_course_action():
    if request.method == 'POST':
        courseCode = request.form.get('code')
        title = request.form.get('title')
        description = request.form.get('description')
        level = request.form.get('level')
        semester = request.form.get('semester')
        numAssessments = request.form.get('assessment')
        # programme = request.form.get('programme')

        delete_Course(get_course(courseCode)) # Woah that's extreme
        add_Course(courseCode, title, description, level, semester, numAssessments)
        flash("Course Updated Successfully!") 
    pass


"""
Semester [2]
Written By
"""

# 01 : Add Semester *
@admin_views.route('/addSemester', methods=['POST'])
@jwt_required(Admin)
def add_semester_action():
    # if request.method == 'POST':
        # semBegins = request.form.get('teachingBegins')
        # semEnds = request.form.get('teachingEnds')
        # semChoice = request.form.get('semester')
        # maxAssessments = request.form.get('maxAssessments') #used for class detection feature
        # add_sem(semBegins,semEnds,semChoice,maxAssessments)
    pass

# 02 : Update Semester
@admin_views.route('/updateSemester', methods=['POST'])
@jwt_required(Admin)
def update_semester_action():
    pass


"""
ProgrammeCourse [2]
Written By
"""

# 01 : Add Programme Course
@admin_views.route('/addProgrammeCourse', methods=['POST'])
@jwt_required(Admin)
def add_programme_course_action():
    pass

# 02 : Remove Programme Course
@admin_views.route('/removeProgrammeCourse', methods=['POST'])
@jwt_required(Admin)
def remove_programme_course_action():
    pass


"""
CourseOffering [3]
Written ByKatoya Ottley
Task: 10.3.2. Implement API Views for Admin (CourseOffering)
"""

# 01: Add Course Offering
@admin_views.route('/addCourseOffering', methods=['POST'])
@jwt_required(Admin)
def add_offering_action():
    try:
        data = request.get_json()
        courseCode = data.get("courseCode")
        semesterID = data.get("semesterID")
        totalStudentsEnrolled = data.get("totalStudentsEnrolled")

        if not courseCode or not semesterID or not totalStudentsEnrolled:
            return jsonify(error= "All Fields are Required To Add Course Offering"), 400

        newCourseOffering = add_course_offering(courseCode, semesterID, totalStudentsEnrolled)
        if newCourseOffering is None:
            return jsonify(error = "Failed To Add Course Offering or Course Offering Already Exists."), 400

        message = f'Course: {newCourseOffering.courseCode} for Semester ID {newCourseOffering.semesterID}  with {newCourseOffering.totalStudentsEnrolled} Number of Students Was Added Successfully!'
        return jsonify(message=message), 201
    
    except Exception as e:
        print (f"Error While Adding Course Offering: {e}")
        return jsonify(error = "An Error Occurred While Adding Course Offering"), 500

# 02 : Remove Course Offering
@admin_views.route('/removeCourseOffering', methods=['POST'])
@jwt_required(Admin)
def remove_offering_action():
    try:
        data = request.get_json()
        courseCode = data.get("courseCode")
        semesterID = data.get("semesterID")

        if not courseCode or not semesterID:
            return jsonify(error= "All Fields are Required To Remove Course Offering"), 400

        removeCourseOffering = remove_course_offering(courseCode, semesterID)
        if removeCourseOffering is None:
            return jsonify(error = "Failed To Remove Course Offering or Course Offering Does Not Exists."), 400

        message = f'Course: {removeCourseOffering.courseCode} for Semester ID {removeCourseOffering.semesterID} Was Removed Successfully!'
        return jsonify(message=message), 201
    
    except Exception as e:
        print (f"Error While Removing Course Offering: {e}")
        return jsonify(error = "An Error Occurred While Removing Course Offering"), 500

''' No Controller Present
# 03 : Update Course Offering
@admin_views.route('/updateCourseOffering', methods=['POST'])
@jwt_required(Admin)
def update_offering_action():
    pass
'''
# 04 : List of Courses For A Specific Semester
@admin_views.route('/listCourse', methods=['GET'])
@jwt_required(Admin)
def list_semester_course_action():
    try:
        data = request.get_json()
        semesterName = data.get("semesterName")
        academicYear = data.get("academicYear")

        if not semesterName or not academicYear:
            return jsonify(error= "All Fields are Required To Add Course"), 400

        listOfSemesterCourse = list_courses_for_semester(semesterName, academicYear)
        if listOfSemesterCourse is None:
            return jsonify(error = "Failed To List Semester Courses or Courses Do Not Exists."), 400

        message = f'Course for : {listOfSemesterCourse.semesterName} For the Academic Year {listOfSemesterCourse.academicYear} Was Listed Successfully!'
        return jsonify(message=message), 201
    
    except Exception as e:
        print (f"Error While Listing Semester Courses: {e}")
        return jsonify(error = "An Error Occurred While Listing Semester Course"), 500

# 05:  List Of A Course Offering For An Academic Year
@admin_views.route('/listCourse', methods=['GET'])
@jwt_required(Admin)
def list_semester_course_action():
    try:
        data = request.get_json()
        courseCode = data.get("courseCode")
        academicYear = data.get("academicYear")

        #if not is_valid_course_code(courseCode):
        #    return jsonify(error = "Invalid Course Code, Please Try Again"), 400

        if not courseCode or not academicYear:
            return jsonify(error= "All Fields are Required To Add Course"), 400

        listOfAcademicYearCourse = get_course_offerings(courseCode, academicYear)
        if listOfAcademicYearCourse is None:
            return jsonify(error = "Failed To List Course For Academic Year Courses or Course Do Not Exists."), 400

        message = f'Course for : {listOfAcademicYearCourse.courseCode} For the Academic Year {listOfAcademicYearCourse.academicYear} Was Listed Successfully!'
        return jsonify(message=message), 201
    
    except Exception as e:
        print (f"Error While Listing Course For The Academic Year: {e}")
        return jsonify(error = "An Error Occurred While Listing Course For The Academic Year"), 500


"""
CourseStaff [3]
Written By
"""
# 01 : Add Course Staff
@admin_views.route('/addCourseStaff', methods=['POST'])
@jwt_required(Admin)
def add_course_staff_action():
    pass

# 02 : Remove Course Staff
@admin_views.route('/removeCourseStaff', methods=['POST'])
@jwt_required(Admin)
def remove_course_staff_action():
    pass

# 03 : Update Course Staff
@admin_views.route('/updateCourseStaff', methods=['POST'])
@jwt_required(Admin)
def update_course_staff_action():
    pass

"""
Programme [3]
Written By
"""

# 01 : Add Programme
@admin_views.route('/addProgramme', methods=['POST'])
@jwt_required(Admin)
def add_programme_action():
    pass

# 02 : Remove Programme
@admin_views.route('/removeProgramme', methods=['POST'])
@jwt_required(Admin)
def remove_programme_action():
    pass

# 03 : Update Programme
@admin_views.route('/updateProgramme', methods=['POST'])
@jwt_required(Admin)
def update_programme_action():
    pass
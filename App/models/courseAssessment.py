import enum
from App.database import db

class ClashRules(enum.Enum):
    DEGREE = 'degree'
    STUDENT_OVERLAP = 'student_overlap'
    ASSESSMENT_TYPE = 'assessment_type'

class CourseAssessment(db.Model):
    __tablename__ = 'courseAssessment'

    # Attributes
    courseAssessmentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assessmentID = db.Column(db.Integer, db.ForeignKey('assessment.assessmentID'), nullable=False)
    courseCode = db.Column(db.String(9), db.ForeignKey('course.courseCode'), nullable=False)
    startDate = db.Column(db.Date, nullable = True)
    endDate = db.Column(db.Date, nullable = True)
    startTime = db.Column(db.Time, nullable = True)
    endTime = db.Column(db.Time, nullable = True)
    clashRule = db.Column(db.Enum(ClashRules), nullable=True)

    # Relationships
    course = db.relationship('Course', backref='course_assessments')
    assessment = db.relationship('Assessment', backref='assessment_courses')

    def __init__(self, courseCode, assessmentID, startDate, endDate, startTime, endTime, clashRule=None):
        self.courseCode = courseCode
        self.assessmentID = assessmentID
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.clashRule = clashRule

    def get_json(self):
        return {
            "courseAssessmentID": self.courseAssessmentID,
            "courseCode": self.courseCode,
            "assessmentID": self.assessmentID,
            'startDate': self.startDate.strftime('%Y-%m-%d') if self.startDate else None,
            'startTime': self.startTime.strftime('%H:%M') if self.startTime else None,
            'endDate': self.endDate.strftime('%Y-%m-%d') if self.endDate else None,
            'endTime': self.endTime.strftime('%H:%M') if self.endTime else None,
            "clashRule": self.clashRule.name if self.clashRule else None
        }

    def __str__(self):
        return f"CourseAssessment(ID={self.courseAssessmentID}, Course={self.courseCode}, Assessment={self.assessmentID})"

    def __repr__(self):
        return (
            f"CourseAssessment(courseAssessmentID={self.courseAssessmentID}, "
            f"courseCode={self.courseCode}, assessmentID={self.assessmentID}, "
            f"startDate={self.startDate.strftime('%Y-%m-%d') if self.startDate else None}, endDate={self.endDate.strftime('%Y-%m-%d') if self.endDate else None},"
            f"startTime={self.startTime.strftime('%H:%M') if self.startTime else None}, endTime={self.endTime.strftime('%H:%M') if self.endTime else None})"
            f"clashRule={self.clashRule.name if self.clashRule else None}"
        )
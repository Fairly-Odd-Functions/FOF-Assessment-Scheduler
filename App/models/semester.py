from App.database import db

class Semester(db.Model):
    __tablename__='semester'
    
    semesterID = db.Column(db.Integer, primary_key= True, autoincrement=True)
    semesterTitle = db.Column(db.String(120),nullable = False)
    startDate = db.Column(db.Date,nullable=False)
    endDate = db.Column(db.Date,nullable=False)
    courses = db.relationship('Course',backref='semester', lazy=True)
    # semNum = db.Column(db.Integer,nullable=False)
    # maxAssessments = db.Column(db.Integer,nullable=False)

def __init__(self, semesterTitle, startDate, endDate):
    self.semesterTitle = semesterTitle
    self.startDate = startDate
    self.endDate = endDate
    # self.semNum = semNum
    # self.maxAssessments = maxAssessments

def to_json(self):
    return{
        "SemesterID":self.semesterID,
        "SemesterTitle":self.semesterTitle,
        "startDate":self.startDate,
        "endDate":self.endDate
        
    }
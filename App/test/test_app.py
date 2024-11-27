import os, tempfile, pytest, logging, unittest

from App.main import create_app
from App.database import db, create_db
#from App.views.auth import login
from App.models import Admin, Staff, User 
from App.controllers import ( #Admin Controller
    create_admin,
    get_all_admin_users,
    get_all_admin_users_json,
    update_admin,
    delete_admin,
    get_admin_by_email,
    get_all_admins,
)
from App.controllers import ( #Staff Controller
    register_staff,
    add_course_staff,
    add_multiple_courses_to_staff,
    get_staff_courses,
    update_staff,
    delete_staff,
    get_staff_by_email,
    get_all_staff,
    remove_staff_from_course,
    is_staff_assigned_to_course,
    get_staff_with_courses,
)
from App.controllers import ( #User Controller
    create_user,
    get_all_admin_users,
    get_all_staff_users,
    get_all_admin_users_json,
    get_all_staff_users_json,
    validate_Staff,
    validate_Admin,
    get_user,
    get_userID,
)

LOGGER = logging.getLogger(__name__)

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

'''
    Unit Tests
'''

class AdminUnitTest(unittest.TestCase):
    
    #UNIT TEST - #1: Create Admin
    def test_unit_01_create_admin(self):
        admin = Admin ("Jane", "Doe", "janepass", "jane.doe@gmail.com")
        assert admin.email == "jane.doe@gmail.com"

        #print("Admin Info:", admin) //Testing Output

    
    #UNIT TEST - #2: Get All Admin Users
    def test_unit_02_get_all_admin_users(self):
        adminUser1 = Admin ("John", "Doe", "johnpass", "john.doe@gmail.com")
        adminUser2 = Admin ("Katie", "White", "katiepass", "katie.white@gmail.com")

        '''Testing Output
        db.session.add(adminUser1)
        db.session.add(adminUser2)
        db.session.commit()
        '''

        admins = get_all_admin_users()    

        '''Testing Output
        print("Admins: ", admins)

        assert len(admins) == 2
        assert admins[0].email == "john.doe@gmail.com"
        assert admins[1].email == "katie.white@gmail.com"
        '''

       
       



    
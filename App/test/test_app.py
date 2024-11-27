import os, tempfile, pytest, logging, unittest

from App.main import create_app
from App.database import db, create_db
#from App.views.auth import login
from App.models import User 
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

@pytest.fixture(autouse=True, scope="function")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.session.remove()
    db.drop_all()

'''
    Unit Tests
'''

class UserUnitTest(unittest.TestCase):

    #UNIT TEST - #19: Create User
    def test_unit_19_create_user(self):
        user = create_user("Hope", "Ice", "hopepass", "hope.ice@gmail.com", "staff" )
        assert user.email == "hope.ice@gmail.com"

        #print("User Info:", user) #Testing Output
    

    #UNIT TEST - #20: Get All Admin Users
    def test_unit_20_get_all_admin_users(self):
        user = create_user("Jake", "Kim", "jakepass", "jake.kim@gmail.com", "admin")
        assert user.email == "jake.kim@gmail.com"

        user = create_user("Laim", "Mike", "liampass", "liam.mike@gmail.com", "admin" )
        assert user.email == "liam.mike@gmail.com"

        admins = get_all_admin_users()    

        #Testing Output
        print("Admin Users: ", admins)

        assert len(admins) == 2
        assert admins[0].email == "jake.kim@gmail.com"
        assert admins[1].email == "liam.mike@gmail.com"
        
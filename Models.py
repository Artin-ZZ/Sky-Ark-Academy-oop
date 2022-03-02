# For creating Database tables
from Database import Database

# models For Creating Database Tabels and etc.
class Models(Database):
    def __init__(self) -> None:
        # Inherit the parent
        super().__init__()
        
        #or ==> Database.__init__(self)
        
        # Create required tables
        self.Students()
        #self.Grades()
        self.Professors()
        self.Departments()
        self.Courses()
        self.Tickets()
        
    # Create students table
    def Students(self):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
              id INTEGER NOT NULL PRIMARY KEY,
              full_name VARCHAR(60) NOT NULL,
              age INTEGER NOT NULL,
              phone_number INTEGER NOT NULL UNIQUE, 
              student_id VARCHAR(255) NOT NULL UNIQUE,
              identity_id INTEGER NOT NULL UNIQUE,
              last_grade FLOAT NOT NULL,
              description TEXT NOT NULL,
              read_student BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # # Grades model
    # def Grades(self):
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS grades (
    #           id INTEGER NOT NULL PRIMARY KEY,
    #           student_id INTEGER NOT NULL,
    #           grade REAL NOT NULL DEFAULT 0.00,
    #           lesson TEXT NOT NULL,
    #           FOREIGN KEY (student_id) REFERENCES students (id)
    #         );
    #     """
    #     return self.query(sql)
    
    # Create Professors table
    def Professors(self):
        sql = """
            CREATE TABLE IF NOT EXISTS professors (
                id INTEGER NOT NULL PRIMARY KEY,
                full_name VARCHAR(60) NOT NULL,
                identity_id INTEGER NOT NULL UNIQUE,
                professor_id VARCHAR(255) NOT NULL UNIQUE,
                phone_number INTEGER NOT NULL UNIQUE,
                age INTEGER NOT NULL,
                read_professor BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # Create Departments Table
    def Departments(self):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER NOT NULL PRIMARY KEY,
                department_name VARCHAR(255) NOT NULL,
                department_story INTEGER NOT NULL,
                cls_number INTEGER NOT NULL,
                dep_courses TEXT NOT NULL,
                description TEXT NOT NULL,
                read_department BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # Course Regestration
    def Courses(self):
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
              id INTEGER NOT NULL PRIMARY KEY,
              cs_name VARCHAR(255) NOT NULL,
              cs_number INTEGER NOT NULL UNIQUE,
              cs_prof VARCHAR(255) NOT NULL,
              read_course BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    # Create Contact Us Table
    def Tickets(self):
        sql = """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER NOT NULL PRIMARY KEY,
                email VARCHAR(100) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                user_type VARCHAR(100) NOT NULL,
                user_id INTEGER NOT NULL,
                ticket_token TEXT NOT NULL UNIQUE,
                read_ticket BOOLEAN DEFAULT False
            );
        """
        return self.query(sql)
    
    
    # Insert new student into database
    def create_students(self, full_name, student_id, identity_id, age, phone_number, last_grade, description):
        sql = """
            INSERT INTO students (full_name, student_id, identity_id, age, phone_number, last_grade, description)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        data = [full_name, student_id, identity_id, age, phone_number, last_grade, description]
        if self.query(sql, data):
            return student_id
    
    
    # Search Student By Id
    def fetch_student(self, student_id):
        sql = """
            SELECT * FROM students
            WHERE student_id = ?;
        """
        data = [student_id]
        
       # Student exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # Student not exists
        else:
            return False

    # Search Student And Return All Students
    def fetch_students(self):
        sql = """SELECT * FROM students;"""

        # Student exists
        if self.query(sql).fetchall():
            return self.query(sql).fetchall()

        # Student not exists
        else:
            return False
    # Student Status for Delete
    def student_status(self, student_id):
        sql = """
            SELECT * FROM students 
            WHERE student_id = ?;
        """
        data = [student_id]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_student']

        else:
            return -1

    # Delete A Students From Data Base
    def student_delete(self, student_id):
        sql = """
            DELETE FROM students
            WHERE student_id = ?;
        """
        data = [student_id]

        if self.query(sql, data):
            return True
        else:
            return False

    # Insert new Professor into database
    def create_professors(self, full_name, professor_id, identity_id, phone_number, age):
        sql = """
            INSERT INTO professors (full_name, professor_id, identity_id, phone_number, age)
            VALUES (?, ?, ?, ?, ?);
        """
        data = [full_name, professor_id, identity_id, phone_number, age]
        if self.query(sql, data):
            return professor_id

     # Search professors By Id
    def fetch_professor(self, professor_id):
        sql = """
            SELECT * FROM professors
            WHERE professor_id = ?;
        """
        data = [professor_id]

       # professor exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # professor not exists
        else:
            return False

    # Search professors And Return All professors
    def fetch_professors(self):
        sql = "SELECT * FROM professors;"

        # professor exists
        if self.query(sql).fetchall():
            return self.query(sql).fetchall()

        # professor not exists
        else:
            return False

    # Professor Status for Delete
    def professor_status(self, professor_id):
        sql = """
            SELECT * FROM professors 
            WHERE professor_id = ?;
        """
        data = [professor_id]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_professor']

        else:
            return -1


    # Delete A Professor From Database
    def professor_delete(self, professor_id):
        sql = """
            DELETE FROM professors
            WHERE professor_id = ?;
        """
        data = [professor_id]

        if self.query(sql, data):
            return True
        else:
            return False
    # Insert new departments into database
    def create_departments(self, department_name, department_story, cls_number, dep_courses, description):
        sql = """
            INSERT INTO departments (department_name, department_story, cls_number, dep_courses, description)
            VALUES (?, ?, ?, ?, ?);
        """
        data = [department_name, department_story, cls_number, dep_courses, description]
        if self.query(sql, data):
            return department_name

     # Search departments By Name
    def fetch_department(self, department_name):
        sql = """
            SELECT * FROM departments
            WHERE department_name = ?;
        """
        data = [department_name]

       # department exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # department not exists
        else:
            return False

    # Search departments And Return All departments
    def fetch_departments(self):
        sql = "SELECT * FROM departments;"

        # department exists
        if self.query(sql).fetchall():
            return self.query(sql).fetchall()

        # department not exists
        else:
            return False

    # Department Status for Delete
    def department_status(self, department_name):
        sql = """
            SELECT * FROM departments 
            WHERE department_name = ?;
        """
        data = [department_name]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_department']

        else:
            return -1


    # Delete A Department From Database
    def department_delete(self, department_name):
        sql = """
            DELETE FROM departments
            WHERE department_name = ?;
        """
        data = [department_name]

        if self.query(sql, data):
            return True
        else:
            return False

    # Insert new Course into database
    def create_courses(self, cs_name, cs_number, cs_prof):
        sql = """
            INSERT INTO courses (cs_name, cs_number, cs_prof)
            VALUES (?, ?, ?);
        """
        data = [cs_name, cs_number, cs_prof]
    
        if self.query(sql, data):
            return cs_number


     # Search courses By Course Number
    def fetch_course(self, cs_number):
        sql = """
            SELECT * FROM courses
            WHERE cs_number = ?;
        """
        data = [cs_number]

       # course exists
        if self.query(sql, data).fetchone():
            return self.query(sql, data).fetchone()

        # course not exists
        else:
            return False

    # Search courses And Return All courses
    def fetch_courses(self):
        sql = "SELECT * FROM courses;"

        # course exists
        if self.query(sql).fetchall():
            return self.query(sql).fetchall()

        # course not exists
        else:
            return False

    # Course Status for Delete
    def course_status(self, cs_number):
        sql = """
            SELECT * FROM courses 
            WHERE cs_number = ?;
        """
        data = [cs_number]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_course']

        else:
            return -1

    # Delete A Course From Database
    def course_delete(self, cs_number):
        sql = """
            DELETE FROM courses
            WHERE cs_number = ?;
        """
        data = [cs_number]

        if self.query(sql, data):
            return True
        else:
            return False

    # Insert new Ticket into database + Shows Contact us info
    def create_ticket(self, email, subject, description, user_type, user_id, ticket_token):
        sql = """
            INSERT INTO tickets (email, subject, description, user_type, user_id, ticket_token)
            VALUES (?, ?, ?, ?, ?, ?);
        """
        data = [email, subject, description, user_type, user_id, ticket_token]

        if self.query(sql, data):
            return ticket_token
    
    
    # Tickets Status In Database
    def ticket_status(self, ticket_token):
        sql = """
            SELECT * FROM tickets 
            WHERE ticket_token = ?;
        """
        data = [ticket_token]
        if len(self.query(sql, data).fetchall()) == 1:
            return self.query(sql, data).fetchone()['read_ticket']

        else:
            return -1


    # Show All Tickets In Database
    def show_tickets(self):
        sql = "SELECT * FROM tickets;"

        # ticket exists
        if self.query(sql).fetchall():
            return self.query(sql).fetchall()

        # ticket not exists
        else:
            return False

    # Process Tickets In Database
    def ticket_process(self, ticket_token):
        sql = """
            UPDATE tickets SET read_ticket = True
            WHERE ticket_token = ?;
        """
        data = [ticket_token]

        if self.query(sql, data):
            return True
        else:
            return False

    # Delete Tickets From Database
    def ticket_delete(self, ticket_token):
        sql = """
            DELETE FROM tickets
            WHERE ticket_token = ?;
        """
        data = [ticket_token]

        if self.query(sql, data):
            return True
        else:
            return False
        
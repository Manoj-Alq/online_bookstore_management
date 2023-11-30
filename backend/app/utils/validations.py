import re

class Validations:

        def email_validations(self, email):
            EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$")
            if EMAIL_REGEX.match(email):
                return True
            else:
                return False
            
        def password_validation(Self, password):
            PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
            if PASSWORD_REGEX.match(password):
                return True
            else: False
        
        def phoneNumber_validation(self,phoneNumber):
            pattern = re.compile(r"^\d{10}$")
            if pattern.match(phoneNumber):
                return True

        def empty_validation(self, obj):
            for key, value in obj:
                if value == "":
                    return True
                
        def empty_key_validation(self, obj):
            for key, value in obj:
                if value == "":
                    return key
                
        def login_validation(Self,user):
            if user.is_active == True:
                return True
            else:
                return False
            
        def User_delete_validation(self, user):
            if user.is_deleted == True:
                return True
            else:
                return False
        
        def None_validation(self,*args):
            for i in args:
                if i == None:
                    return True
        def duplication_username_validate(self,db,model,key):
                db_data = db.query(model).filter(model.username == key).first()
                if db_data:
                    return True
                
        def duplication_email_validate(self,db,model,key):
                db_data = db.query(model).filter(model.email == key).first()
                if db_data:
                    return True
                
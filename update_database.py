from firebase import firebase as fb
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import constants
import json

class update_database:

    data_map ={}
    checker = 'N'
    childrens =''

    print constants.BASE_URL
    base_url =constants.BASE_URL
    cred =credentials.Certificate(constants.MY_CERTIFICATE_PATH)
    firebase_admin.initialize_app(cred, {'databaseURL': '{your database url}'})
    child_node = raw_input("Get Refrence: ")
    #Set firebase database reference
    ref = db.reference(constants.BASE_URL + child_node)

    def __init__(self):
        self.initDatabase()
        

    def initDatabase(self):

        #Ask if the user want to add child to the node
        answer = raw_input("Do you want to add child? (Y/N) ")
        grand_child = ''
        last_child =''
        
        while answer == "Y":
            if grand_child != '':
                #Grand child is not null so continue
                last_child += grand_child +"/"
                self.childrens = last_child
                print self.childrens
                answer = raw_input("Do you want to add child? (Y/N) ")
            grand_child = raw_input("Firebase Child: ")

        if answer == "N":
            self.set_data_to_pass()
            
                
    def set_data_to_pass(self):
        if self.checker !='A':
            self.checker = raw_input("Press \"A\" key to add more. Other key to discontinue: ")
            while self.checker =='A':
                if self.checker =='A':
                    self.data_map[raw_input("Key: ")] = raw_input("Value: ")
                    print self.data_map
                    self.checker = raw_input("- \"A\" to add more children:" +
                                             "\n- \"S\" to send to database: " + "\n- Other keys to jump: ")
                    
                if self.checker == 'S':
                    self.update(self.ref, self.data_map)

        
    def update(self, ref, json_data):
        dbRef = None

        #If the children is none, pass it to the initial reference
        if self.childrens == '':
            dbRef =ref
        else:
            #Add more children
            dbRef = ref.child(self.childrens)
        dbRef.update(json_data)
        print json_data
update_database()

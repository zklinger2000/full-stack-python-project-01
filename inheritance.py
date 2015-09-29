class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)
        print("Number of toys: " + str(self.number_of_toys))        
        
billy = Parent("Cyrus", "blue")
#print(billy.last_name)
billy.show_info()

miley = Child("Cyrus", "Blue", 5)
#print(miley.last_name)
#print(miley.number_of_toys)
miley.show_info()

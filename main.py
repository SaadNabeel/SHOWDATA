class Student:
    def __init__(self, name, city, student_id, grade):
        self.name = name
        self.city = city
        self.student_id = student_id
        self.grade = grade
        self.marks = None 

    def getdata(self):
       
        try:
            self.marks = int(input(f"Enter marks for {self.name}: "))
        except ValueError:
            print("Please enter a valid number for marks.")
            self.getdata()  

    def showdata(self):
       
        print("\nStudent Details:")
        print("Name: {self.name}")
        print("City: {self.city}")
        print("ID: {self.student_id}")
        print("Grade: {self.grade}")
        print("Marks: {self.marks if self.marks is not None else 'No marks entered'}")


s1 = Student("Ali", "New York", 101, "A")
s2 = Student("Saad", "Los Angeles", 102, "B")
s3 = Student("Hamza", "Chicago", 103, "A")
s4 = Student("Dawood", "London", 104, "B")


s1.getdata()
s2.getdata()
s3.getdata()
s4.getdata()


s1.showdata()
s2.showdata()
s3.showdata()
s4.showdata()

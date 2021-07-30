class student:
    def __init__(self,roll,section):
        self.roll=roll
        self.section=section
    def ann(self):
        print("roll no is", self.roll ,self.section)
obj=student(13,'a')
obj1=student(69,'b')
obj.ann()
obj1.ann()
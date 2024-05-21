class parent:
    def __init__(self,name,message):
        self.name=name
        self.message=message
       
        

    def pprint(self):   
        print(f"the name iss {self.name} and the messagge is {self.message} are  ")
class child(parent):
    def __init__(self,name,message):
         self.name=name
         self.message=message
         

    def sound(self):
   
        print(f"the name is {self.name} and the messagge is {self.message}  & ")

  
v=child("manas","How are you")#it go to parent class
v.sound()
v.pprint()
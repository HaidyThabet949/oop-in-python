class animal:
    def __init__(self,_name,_color,_age):
        self.name=_name
        self.color=_color
        self.age=_age
        #print(self.name,self.color,self.age)
        print('the name of animal is ',self.name)
        print('the color of animal is ',self.color)
        print('the age of animal is ',self.age,' years old')
        
class lion(animal):
    def __init__(self,_name,_color,_age):
        super().__init__(_name,_color,_age)
    def Action(self):
        print('lion can run and eat meat')

class elephant(animal):
    def __init__(self,_name,_color,_age):
        super().__init__(_name,_color,_age)
    def Action(self):
        print("elephant can't run and eat plants")

class anotherAnimal(animal):
    def __init__(self,_name,_color,_age):
        super().__init__(_name,_color,_age)
        
        
def menu():
    print('1-lion')
    print('2-elephant')
    print('to another option enter another number')
    

menu()



option=int(input('enter your option:'))


if option==1:
    Lion=lion('lion','yellow',7)
    Lion.Action()

elif option==2:
    Elephant=elephant('elephant','gray',10)
    Elephant.Action()
else:
    anotherName=input('enter animal name:')
    anotherColor=input('enter animal color:')
    anotherage=input('enter animal age:')
    anAction=input('enter animal action:')
    anAnimal=anotherAnimal(anotherName,anotherColor,anotherage)
    print(anotherName,anAction)


    
    
    
    
    
    
    
    
    
    
    
    
    
class Cat(object):
    '''A Cat with name, and greets each other.'''

    def __init__(self, name):
        '''A new cat with name value name.'''
        self.name = name

    def greet(self, another_name):
        '''Print the name of the cat with greeting.'''
        print (f"Hello! I am {self.name}! Nice to meet you {another_name}! Let's together purr at the human, so that they shall give us food!")
        
Hercules = Cat("Hercules")
Hercules.greet("Tim")

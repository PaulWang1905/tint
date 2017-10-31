import time
class Robot:
    """Represents a robot, with a name."""
    
    #A class variable , counting the number of robots.
    population = 0

    def __init__(self,name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))
        #When this person is created, the robot
        #adds to the population
        Robot.population += 1
    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0 :
             print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))
    def say_hi(self):
            print("hi,my master calls me {}".format(self.name))
    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("we have {:d} robots.".format(cls.population))
droid1 = Robot ("R2-D2")
time.sleep(10)
droid1.say_hi()
time.sleep(1)
Robot.how_many()
time.sleep(1)
droid2 = Robot ("C-3P0")
time.sleep(8)
droid2.say_hi()
time.sleep(1)
Robot.how_many()
time.sleep(1)
print("\nRobots can do some work here.\n")
print("The robots are working.\n")
        
time.sleep(30)
print("Robots have finished their work. So let`s destroy them")
droid1.die()
time.sleep(5)
droid2.die()
time.sleep(5)
Robot.how_many()




class Height:

    """A class which encapsulates a persons height."""

    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches
        self.centimeters = 0

    
    def cm(self):
        self.centimeters = round((self.feet * 30.48) + (self.inches * 2.54), 2)
        return self.centimeters
    
        
    def __gt__(self, other):

        if not self.centimeters:

            if self.feat > other.feat:
                return True
            
            if self.feat == other.feat:
                if self.inches > other.inches:
                    return True
                else:
                    return False
            else:
                return False
        
        else:
            if self.centimeters > other.centimeters:
                return True
            else:
                return False

  
    def __add__(self, other):

        new_height_feet = self.feet + other.feet
        new_height_inches = self.inches + other.inches

        new_person = Height(new_height_feet, new_height_inches)

        return new_person


    def __str__(self):

        if self.centimeters == 0:

            return f"{self.feet} {self.inches}"

        else:

            return f"{self.centimeters}" 

# microwave.py

class SimpleMicrowave:
    def __init__(self, ID):
        self.state = False
        self.ID = ID 

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False
    
    def get_state(self):
        return self.state
    
    def get_ID(self):
        return self.ID

class AdvancedMicrowave:
    def __init__(self, ID):
        self.state = False
        self.ID = ID 

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False
    
    def get_state(self):
        return self.state
    
    def get_ID(self):
        return self.ID

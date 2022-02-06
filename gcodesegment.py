class GCodeSegment():
    def __init__(self, code, number, x, y, z, raw):
        self.code = code
        self.number = number 
        self.raw = raw
        self.x = x
        self.y = y
        self.z = z

        self.has_cords = (self.x is not None or self.y is not None or self.z is not None)

        if self.has_cords:
            if self.x == None:
                self.x = 0
            if self.y == None:
                self.y = 0
            if self.z == None:
                self.z = 0
            
        if self.has_cords:
            print (f'\t{self.code} {self.number} ({self.x}, {self.y}, {self.z})')
        else:
            print (f'\t{self.code} {self.number}')

        
    
    def command(self):
        return self.code + self.number
    
    def get_cords(self):
        return (self.x, self.y, self.z)
    
    def has_cords(self):
        return self.has_cords
    
    def get_cord(self, cord):
        cord = cord.upper()

        if cord == 'X':
            return self.x
        elif cord == 'Y':
            return self.y
        elif cord == 'Z':
            return self.z
# created By Dan Stefen (mousymous)

class mealtime_:
    
    def __init__(self):
        self.buff = input("What time is it? ")
        self.time= ""
        self.hour= ""
        self.minute= ""
        self.mode= ""
    
    def getMode(self):
        if 'a.m.' in self.buff or 'A.M' in self.buff:
            self.mode = 'A.M.'
        elif 'p.m' in self.buff or 'P.M' in self.buff:
            self.mode= 'P.M.'
    
    def convertToInt(self):
        for char in self.buff:
            try:
                if isinstance(int(char), int):
                    self.time= self.time+ char
            except:
                continue
            
    def sliceTime(self):
        if len(self.time) == 3:
            self.hour = self.time[:1]
        else:
            self.hour = self.time[:2]
            
        self.minute = self.time[-2:]
        
    def displayTime(self):
        print(f"Hour: {self.hour}")
        print(f"Minute: {self.minute}")
        print(f"Mode: {self.mode}")

myClass = mealtime_()
myClass.getMode()
myClass.convertToInt()
myClass.sliceTime()
myClass.displayTime()

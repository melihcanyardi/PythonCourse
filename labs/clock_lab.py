class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
        if len(str(self.hour)) < 2:
            return f"0{self.hour}:{self.minutes}"
        elif len(str(self.minutes)) < 2:
            return f"{self.hour}:0{self.minutes}"
        elif len(str(self.hour)) < 2 and len(str(self.minutes)) < 2:
            return f"0{self.hour}:0{self.minutes}"
        else:
            return f"{self.hour}:{self.minutes}"
    
    def __add__(self,minutes):
        self.minutes += minutes
        self.hour += (self.minutes // 60)
        self.minutes %= 60
        if self.hour >= 24:
            self.hour //= 24
    
    def __sub__(self,minutes):
        self.minutes -= minutes
        if self.minutes < 0:
            self.hour += (self.minutes // 60)
        self.minutes %= 60
        if self.hour >= 24:
            self.hour //= 24
        elif self.hour < 0:
            self.hour += 24
    
    def __eq__(self, other):
        return f"{self.hour}:{self.minutes}" == other
    
    def __ne__(self, other):
        return f"{self.hour}:{self.minutes}" != other
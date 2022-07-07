class Vehicle:
    def __init__(self, name, speed, marginTime, travelDistance):
        self._name = name
        self._speed = speed
        self._marginTime = marginTime
        self._travelDistance = travelDistance

    def get_name(self):
        return self._name
    
    def get_speed(self):
        return self._speed
    
    def get_marginTime(self):
        return self._marginTime

    def get_travelDistance(self):
        return self._travelDistance
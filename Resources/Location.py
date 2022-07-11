class Location:
    def __init__(self, name, baseDistance, accessability, tag):
        self._name = name
        self._baseDistance = baseDistance
        self._accessability = accessability
        self._tag = tag

    def get_name(self):
        return self._name
    
    def get_baseDistance(self):
        return self._baseDistance
    
    def get_accessability(self):
        return self._accessability
    
    def get_tag(self):
        return self._tag
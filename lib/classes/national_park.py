from .trip import Trip

class NationalPark:

    def __init__(self, name):
        self.trips = []
        if isinstance(name, str):
            self._name = name

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        name

    def add_trip(self, trip):
        self.trips.append(trip)

    def trips(self):
        return self._trips

    def nationalparks(self):
        return list(set(map(lambda trip: trip.national_park, self._trips)))
        pass

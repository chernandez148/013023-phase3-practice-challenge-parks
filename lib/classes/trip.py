
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if isinstance(start_date, str):
            self.start_date = start_date
        if isinstance(end_date, str):
            self.end_date = end_date

            visitor.add_trip(self)

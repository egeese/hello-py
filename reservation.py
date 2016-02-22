from datetime import datetime, timedelta
class Table(object):
    number = 0
    seats = 4
    occupied_seats = 0
    def __init__(self, number, seats, hour_start, duration):
        self.number = number
        self.seats = seats
        self.hour_start = hour_start
        self.hour_end = hour_start + duration
    @property
    def free_seats(self):
        return self.seats - self.occupied_seats

    @property
    def has_free(self, time, seats):
        if self.seats - self.occupied_seats >= seats:
            return True
        else:
            return False


class Reservations(object):
    def __init__(self, tables):
        self.tables = tables

    def make_reservation(self, seats, date, time_start, time_end):
        pass

from datetime import datetime
from.models import *


def comparedate(d1, d2):
    if d1 > d2:
        return True
    return False


def Checkfreeslot(d1, d2):
    d1=datetime(d1)
    d2=datetime(d2)
    s = Booking.objects.all()
    n = s.count()
    if n == 0:
        return True
    else:
        for i in s:
            if i.startdate > d2:
                
                return True
                
            if i.startdate < d1:
                if i.enddate < d1:
                    return True
                return False
            if i.startdate > d2:
                return true
        return False


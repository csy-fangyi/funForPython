# -*- coding: utf-8 -*-

import datetime


def now():
    return datetime.datetime.now()


def dateTstr(_d, _format):
    return _d.strftime(_format)


def strTdate(_str, _format):
    return datetime.datetime.strptime(_str, _format)


now = now()
print(now, dateTstr(now, '%Y-%m-%d %H:%M:%S'))

d = strTdate('2015-04-07 19:11:21', '%Y-%m-%d %H:%M:%S')
print(d)

year = datetime.timedelta(days=365)
ten_years = year * 10
nine_years = ten_years - year
print(ten_years, year, nine_years)

d1 = strTdate('2015-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = strTdate('2015-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print(delta.days)

delta = datetime.timedelta(days=7)
n_days = now + delta
print(n_days.strftime('%Y-%m-%d %H:%M:%S'))

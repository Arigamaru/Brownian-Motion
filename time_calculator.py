def add_time(origin, added, day=None):
    time1 = origin.split()
    hour1, minute1 = map(int, time1[0].split(':'))
    argument = time1[1].strip()
    time2 = added.split()
    hour2, minute2 = map(int, time2[0].split(':'))
    countminutes = minute1 + minute2
    additionalhour = 0

    if countminutes >= 60:
        additionalhour = countminutes // 60
        countminutes = countminutes % 60

    totalhours = hour1 + hour2 + additionalhour
    totalminutes = countminutes
    totalhourdays = totalhours
    extradays = totalhourdays // 24
    
    if totalhours >= 12:
        if totalhours > 12:
            totalhours %= 12
            if totalhours == 0:
                totalhours = 12
            extradays += 1
        argument = 'PM' if argument == 'AM' else 'AM'
        
    if argument == 'PM':
        extradays -= 1

    if extradays == 1:
        extradays_txt = ' (next day)'
    elif extradays > 1:
        extradays_txt = f' ({extradays} days later)'
    else:
        extradays_txt = ''

    if day:
        d_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        dindex = d_week.index(day.capitalize())
        n_dindex = (dindex + extradays) % 7
        week = ', ' + d_week[n_dindex]
    else:
        week = ''

    newtime = f"{totalhours:02d}:{totalminutes:02d} {argument}{week}{extradays_txt}"

    return newtime

test = [
    ("3:00 PM", "3:10", None),
    ("11:30 AM", "2:32", "Monday"),
    ("11:43 AM", "00:20", None),
    ("10:10 PM", "3:30", None),
    ("11:43 PM", "24:20", "tueSday"),
    ("6:30 PM", "205:12", None)
]

for origin, added, day in test:
    result = add_time(origin, added, day)
    print(result)

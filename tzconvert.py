import datetime
import pytz

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
timezones = [pytz.timezone('US/Eastern'),
             pytz.timezone('Europe/Amsterdam'),
             pytz.timezone('Asia/Baghdad'),
             pytz.timezone('Europe/Warsaw'),
             pytz.timezone('Africa/Accra'),
             pytz.timezone('America/Argentina/Buenos_Aires')
             ]

def converter(d, t):
    
    full = datetime.datetime.combine(d, pytz.timezone('US/Pacific').localize(t))
    frmtd_strs = []
    print(full.strftime(fmt))
    for i in timezones:
        time_str = full.astimezone(i).strftime(fmt)
        place_str = i.__class__.__name__.split('/')[1]
        frmtd_strs.append('That time in {} is {}'.format(place_str, time_str))

    return frmtd_strs

d = datetime.date(year=2016, month=10, day=6)
t = datetime.time(hour=6, minute=17)

for i in converter(d, t):
    print(i)
        
    
    

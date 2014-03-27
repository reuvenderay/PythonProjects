import datetime


def time_calc2(time, meg_past, meg_left):
    #time in minutes
    hours_left = ((time/meg_past)*meg_left)/60
    hour = int(hours_left)
    minute = int(round((hours_left - hour) * 60))
    cur_hour = int(str(datetime.datetime.now().time())[0:2])
    cur_min = int(str(datetime.datetime.now().time())[3:5])
    cur_time = cur_hour*60 + cur_min
    eta = hour * 60 + minute + cur_time
    min_done = eta % 60
    hour_done = (eta - min_done)/60
    while hour_done > 12:
        hour_done -= 12
    print "Time left %i:%s" % (hour, str(minute).zfill(2))
    print "process will finish at %i:%s" % (hour_done, str(min_done).zfill(2))

time_calc2(60.0, 1690-215,215.0 )
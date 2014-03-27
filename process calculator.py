import datetime


def time_calc(time, percent, passed=0):
    #takes above arguments And returns time left and when process will finish
    #time - enter how much time has passed on the timer
    #percent - enter what percent the process is up to(even if passed!=0)
    #passed - if timer was started late, enter what percent it was started at.
    #otherwise leave passed blank

    percent_left = 100 - percent
    hours_left = ((time/(percent-passed))*percent_left)/60
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

if __name__ == "__main__":
    time_calc(20,10)
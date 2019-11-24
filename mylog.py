import datetime

def format_time(t):
    return f'{t.seconds:2}.{t.microseconds:06}'

def log(message):
    '''
    prints a line with:
        elapsed time since this function was first called
        elapsed time since this function was previously called
        message

    Elapsed times are shown in seconds with microsecond resolution
    although one does not know what the accuracy is.
    '''

    global time_of_first_call
    global time_of_previous_call

    now = datetime.datetime.now()
    try:
        time_of_first_call
    except NameError:
        time_of_first_call = now
        time_of_previous_call = now

    time_since_first_call = now - time_of_first_call
    time_since_previous_call = now - time_of_previous_call
    print(
        format_time(time_since_first_call),
        format_time(time_since_previous_call),
        message,
    )

    time_of_previous_call = now

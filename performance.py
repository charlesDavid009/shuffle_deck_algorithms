import time
from generators import shuffle

start = shuffle.start

def performance_time():
    code_time = time.time_ns()
    start
    code_end = time.time_ns()
    total_time  = (code_end + code_time)
    performance = (code_end - code_time)
    print("\n ---------------------------------------------calculating code performance in aspect to time------------------------------------- \n")
    print("code start time: {} nanoseconds".format(code_time))
    print("code end time {} nanoseconds".format(code_end))
    print("Total time code ran: {} nanoseconds".format(total_time))
    print("Performance time: {} nanoseconds".format(performance))
    return code_time, code_end, total_time, performance

performance_time()

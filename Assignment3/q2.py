import datetime

def current_datetime():
    #return datetime.date.today()
    return datetime.datetime.now()
    #return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #return datetime.datetime.now().strftime("%A,%Y-%m-%d %H:%M:%S")
    #return datetime.datetime.now().strftime("%A,%B %d,%Y  %H:%M:%S")

def current_day():
    return datetime.datetime.now().strftime("%A")
if __name__ == "__main__":
    print(current_datetime())
    print(current_day())

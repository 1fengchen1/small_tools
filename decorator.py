import time

def out_wrapper(func):
    def inner_wrapper():
        start_time = time.time()
        result = func()
        stop_time = time.time()
        print('Used time {}'.format(stop_time-start_time))
        return result
    return inner_wrapper()

@out_wrapper
def test1():
    time.sleep(1)
    print('I am {test1} !')
    return 'test1 return'

x = test1()
print(x)
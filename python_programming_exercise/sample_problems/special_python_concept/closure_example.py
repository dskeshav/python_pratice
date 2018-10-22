# Closure: " A closure is a record storing a function together with 
# an enviornment : a mapping associating each free variable of the
# function with the value or storage location to which the name was 
# bound when the closure was created. A closure, unlike a plain function,
# allows the function to access those captured varible through the 
# closure's reference to them even when the function is invoked outside 
# their scope."

def outer_func(msg):
    message=msg

    def inner_func():
        print(message)

    return inner_func


hi_func=outer_func('Hi')
hello_func=outer_func("hello")

hi_func()
hello_func()


########################
# Closure is an inner function that rembers and has access to varibles in the local scope in which it is created even after outer function is executed
print("########################")

import logging
logging.basicConfig(filename="closure_example.log",level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger=logger(add)
sub_logger=logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)
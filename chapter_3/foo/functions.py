def foo():
    print "Hello world"
    print "Have a nice day"

foo()

print foo

print type(foo)

def bar():
    foo()
    foo()

bar()

print bar

print type(bar)

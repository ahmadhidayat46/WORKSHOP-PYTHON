# .. if Statements
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# .. for Statements
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# ..The range() Function
for i in range(5):
    print(i)

a = list(range(5, 10))
print(a)
b = list(range(0, 10, 3))
print(b)
c = list(range(-10, -100, -30))
print(c)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

a = range(10)
print(a)
b= sum(range(4))  # 0 + 1 + 2 + 3
print(b)

# ..break and continue Statements, and else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#.. pass Statements
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass:
    pass

def initlog(*args):
    pass   # Remember to implement this!

# ..match Statements
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 402:
            return "Something's wrong with the internet"
        case 401 | 403 | 404:
            return "Not allowed"
print(http_error(400))  
print(http_error(404)) 
print(http_error(418))  
print(http_error(402))  
print(http_error(403)) 
print(http_error(500))  

# point is an (x, y) tuple
def match_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
    match_point((0, 0))  
    match_point((0, 5)) 
    match_point((3, 0))  
    match_point((2, 4))  
    match_point((1, 2, 3))  

class Point:
    x: int
    y: int
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case point():
            print("Not a point")
        case Point(1, var):
            print(f"x=1 dan y={var}")
        case Point(1, y=var):
            print(f"x=1 dan y={var}")
        case Point(x=1, y=var):
            print(f"x=1 dan y={var}")
        case Point(y=var, x=1):
            print(f"x=1 dan y={var}")
        case _:
            print("Tidak cocok dengan pola yang ada")

class Point:
    x: int
    y: int
def where_is(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

class Point:
    x: int
    y: int
point = Point(3, 3)
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

# ..Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Now call the function we just defined:
fib(2000)
fib
f = fib
f(100)
fib(0)
print(fib(0))

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
f100 = fib2(100)    # call it
print(f100) 

# ..Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
result = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
print("Hasil: ", result)

i = 5
def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# ..Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='Vooooom')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
parrot()                                              # required argument missing
parrot(voltage=5.0 , state='dead')                    # non-keyword argument after a keyword argument
parrot(110, voltage=220)                              # duplicate value for the same argument
parrot(actor='John Cleese')                           # unknown keyword argument

def function(a):
    pass
function(0, a=0)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")

# ..Special parameters
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)
f(1, 2, 3, kwd1='foo', kwd2='bar')

# ..Function Examples
def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
standard_arg(2)
standard_arg(arg=2)
pos_only_arg(1)
# pos_only_arg(arg=1)
# kwd_only_arg(3)
kwd_only_arg(arg=3)
# combined_example(1, 2, 3)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)

def foo(name, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})

def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})

# ..Recap
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """
    Fungsi ini menerima dua argumen posisi, satu argumen posisi atau kata kunci,
    dan dua argumen kata kunci.
    """
    print(f"pos1 = {pos1}")
    print(f"pos2 = {pos2}")
    print(f"pos_or_kwd = {pos_or_kwd}")
    print(f"kwd1 = {kwd1}")
    print(f"kwd2 = {kwd2}")
# Contoh 1: Semua argumen diberikan sebagai argumen posisi/kata kunci
f(1, 2, 3, kwd1=4, kwd2=5)
# Contoh 2: argumen posisional dan argumen kata kunci dicampur
f(1, 2, pos_or_kwd=3, kwd1=4, kwd2=5)
# Contoh 3: Semua argumen diberikan sebagai argumen kata kunci
f(pos1=1, pos2=2, pos_or_kwd=3, kwd1=4, kwd2=5)
# Contoh 4: Memasukkan argumen posisi setelah argumen kata kunci
f(pos1=1, pos2=2, kwd1=4, kwd2=5, pos_or_kwd=3)

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
def concat(*args, sep="/"):
    return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# ..Unpacking Argument Lists
list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))           # call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#  ..Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))     
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#.. Documentation Strings
def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)

# ..Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
f('spam')
    

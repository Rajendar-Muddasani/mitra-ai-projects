# Python Basics Cheatsheet
## Source for PDF generation via scripts/generate_cheatsheets.py

---

## Data Types
| Type | Example | Notes |
|---|---|---|
| int | x = 42 | Unlimited precision |
| float | x = 3.14 | IEEE 754 double |
| str | x = "hello" | Immutable |
| bool | x = True | Subclass of int |
| list | x = [1, 2, 3] | Mutable, ordered |
| tuple | x = (1, 2, 3) | Immutable, ordered |
| dict | x = {"a": 1} | Key-value, ordered (3.7+) |
| set | x = {1, 2, 3} | Unique, unordered |
| None | x = None | Null value |

## Control Flow
```python
# if/elif/else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# for loop
for item in [1, 2, 3]:
    print(item)

# while loop
while n > 0:
    n -= 1

# break, continue, pass
for x in range(10):
    if x == 5: break
    if x % 2 == 0: continue
    print(x)
```

## Functions
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Lambda
square = lambda x: x**2

# *args and **kwargs
def func(*args, **kwargs):
    print(args, kwargs)

# Type hints
def add(a: int, b: int) -> int:
    return a + b
```

## List Comprehensions
```python
squares   = [x**2 for x in range(10)]
evens     = [x for x in range(10) if x % 2 == 0]
flat      = [x for row in matrix for x in row]
dict_comp = {k: v for k, v in items.items() if v > 0}
set_comp  = {x**2 for x in range(10)}
gen_expr  = (x**2 for x in range(10))  # generator
```

## String Operations
```python
s = "Hello, World!"
s.lower()          # "hello, world!"
s.upper()          # "HELLO, WORLD!"
s.strip()          # remove whitespace
s.split(",")       # ["Hello", " World!"]
s.replace("o","0") # "Hell0, W0rld!"
f"Name: {name}"    # f-string formatting
s.startswith("He") # True
",".join(["a","b"]) # "a,b"
```

## File I/O
```python
# Read
with open("file.txt", "r") as f:
    content = f.read()      # entire file
    lines   = f.readlines() # list of lines

# Write
with open("out.txt", "w") as f:
    f.write("hello\n")

# Append
with open("log.txt", "a") as f:
    f.write("new line\n")

# JSON
import json
data = json.loads(json_string)
json.dump(data, open("out.json", "w"), indent=2)
```

## Error Handling
```python
try:
    result = int("abc")
except ValueError as e:
    print(f"Error: {e}")
except (TypeError, KeyError) as e:
    print(e)
else:
    print("No error")  # runs if no exception
finally:
    print("Always runs")

# Raise
raise ValueError("Must be positive")
```

## Common Built-ins
```python
len([1,2,3])           # 3
type(42)               # <class 'int'>
isinstance(x, int)     # True/False
range(start, stop, step)
enumerate(["a","b"])   # (0,"a"), (1,"b")
zip([1,2], ["a","b"])  # (1,"a"), (2,"b")
sorted([3,1,2])        # [1, 2, 3]
sorted(items, key=lambda x: x.score, reverse=True)
map(str, [1,2,3])      # ["1","2","3"]
filter(lambda x: x>0, [-1,1,2])
any([False, True])     # True
all([True, True])      # True
min([3,1,2]), max([3,1,2])
sum([1,2,3])           # 6
abs(-5)                # 5
round(3.14159, 2)      # 3.14
```

## Dictionary Operations
```python
d = {"a": 1, "b": 2}
d["c"] = 3          # add/update
d.get("x", 0)       # safe get with default
d.pop("a")          # remove and return
d.keys()            # dict_keys(["b","c"])
d.values()          # dict_values([2,3])
d.items()           # (key,value) pairs
d.update({"d": 4})  # merge
{**d, "e": 5}       # spread merge
```

## AI Learning Prompts
1. Explain Python list comprehensions with 5 real examples
2. What's the difference between a list and a tuple?
3. Show me Python file I/O for CSV, JSON, and text
4. What are Python decorators and when to use them?
5. How does Python's GIL affect multi-threading?

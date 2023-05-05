# Python initiation

**Priscilla Joly - 3iS school**

```bash
    python3 --version
    #Python 3.10.8
```

## Utilities

[Python documentation](https://www.python.org/)

Docstring : Apprendre Python de A à Z (YouTube - 7h)

## Time to learn basics on Python

### Execute a Python script

```bash
    python3 fileName.py
```

## Project

Create a Hangman's game !

- Print and prompt
- Generate a random number 
- Select a random word in array 
- Create and use functions 
- Create and use variables
- Work with : string and array
- Array loop _(while, for)_
- Condition _(if, else if, else)_
- Import libraries

### Conditions in Python

- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

Print text with `print()` :
```python
print("Hello World !") # Hello World !
```

Prompt in terminal with `input()` :
```python
response = input("What's your name ?") # Priscilla
print(response) # Priscilla
```

```python
name = "Priscilla"
print(f"Bonjour {name}") # Bonjour Priscilla
```

Get length of an array with `len()`  : 
```python
array = [1]
item = 1
size = len(array)
print(size) # 1
```

Add item in an array with `.append()` : 
```python
array = []
item = 1
array.append(item)
print(array) # [1]
```
Remove item in an array at index `.pop()` :
```python
array = [1, 2, 3]
array.pop(1)
print(array) # [1, 3]
```

Create a condition (if, else if and else)
**Compare strings**
```python
string = 'STOP'
if string == "STOP" or string == "stop" :
    # Do something
if string =="STOP" and string == "stop":
    # Do something
elif string == "toto":
    # Do something
else :
    # Do something
```

**Compare two numbers**
```python
nombre_a = 0
nombre_b = 2

if nombre_a != nombre_b:
    print("nombre_a et nombre_b sont différents")
```

**Compare a true/false condition**
```python
win = False

if not win:
    print("Not a winner")
else:
    print("A winner")
```

Create a loop

### Excercism

You can find my Python training on [Excercism](https://exercism.org/profiles/SekmSet)

### Deploy Dockerfile

```bash
    # Build in local
    docker build -f Dockerfile . -t test
    
    # Build and deploy in GCP
    docker build . -t  eu.gcr.io/deploy-276111/equideow_script:latest
    docker push eu.gcr.io/deploy-276111/equideow_script:latest
```
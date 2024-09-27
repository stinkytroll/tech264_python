## if statement
The if statement is used for conditional execution. It evaluates a condition and executes a block of code if the 
condition is true. 

### Example: 

```
x = 10

if x = 10:
    print("X is 10")
```

### Output:

 ```
x is 10
```

## elif statement
The elif statement allows you to check multiple conditions. It follows an if statement and can be used to specify 
additional conditions if the initial condition is false.

### Example:

```
x = 10

if x < 5:
    print("x is less than 5")
elif x < 15: 
    print("x is less than 15") 
```

### Output:

 ```
x is less than 15
```

## else statement
The else statement is used to execute a block of code when all preceding conditions in the if and elif 
statements are false.

### Example:

```
x = 10

if x < 5:
    print("x is less than 5")
elif x > 15: 
    print("x is greater than 15") 
else: 
    print("x is between 5 and 15")
```

### Output:

 ```
x is between 5 and 15
```

## while Loop
A while loop repeatedly executes a block of code as long as a specified condition is true.

### Example:

```
count = 0

while count < 5:
    print(count)
    count += 1
    
print("kaboom")
```

### Output:

 ```
0
1
2
3
4
kaboom
```

## for Loop
A for loop is used to iterate over a sequence (like a list, tuple, string, or any iterable). It executes a block of 
code for each item in the sequence.

### Example:

```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
### Output:

 ```
apple
banana
cherry
```

## Nested loops
Nested loops combine different loops together. 

### Example:

```
outer_count = 3

while outer_count > 0:
    print(f"Outer loop iteration: {outer_count}")
    
    for inner_count in range(2): 
        print(f"  Inner loop iteration: {inner_count}")

    outer_count -= 1
```

### Output:

```
Outer loop iteration: 3
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 2
  Inner loop iteration: 0
  Inner loop iteration: 1
Outer loop iteration: 1
  Inner loop iteration: 0
  Inner loop iteration: 1
```
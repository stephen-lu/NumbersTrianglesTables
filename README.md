# NumbersTrianglesTables
 (was, once upon a time, _Leon's Loopy Lab_) (who is Leon?? Is he really Kris' cousin?)
 
## Java:

* Read each of the following `README` files and complete each of the asks.
    * [README-NumberUtilities.md](./README-NumberUtilities.md)
    * [README-TriangleUtilities.md](./README-TriangleUtilities.md)
    * [README-TableUtilities.md](./README-TableUtilities.md)
    
## Loops. `for` and `while` loops

In Java, for and while loops are used for repetitive execution of a block of code.

A for loop is used when the number of iterations is known beforehand. It consists of three parts: initialization, condition, and increment/decrement. The initialization part is executed only once at the beginning of the loop. The condition part is checked before each iteration, and if it is true, the loop body is executed. The increment/decrement part is executed at the end of each iteration. Here is an example of a for loop:

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

This loop will print the numbers from 0 to 9.

A while loop is used when the number of iterations is not known beforehand, and the loop continues until a certain condition is met. The condition is checked at the beginning of each iteration, and if it is true, the loop body is executed. Here is an example of a while loop:

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
```

This loop will also print the numbers from 0 to 9.
Now, one of my favorite `while` loops is

```java
while (true) {
    System.out.println("I'm stuck in an infinite loop!");
}

// yes, infinite loops are a thing
```

or even this one...
```java
while (playerOne.isAlive() && playerTwo.isAlive()) {
    playerOne.attack(playerTwo);
    playerTwo.attack(playerOne);
}
```

Which you should be able imagine is deep inside some game somewhere.

ANY for loop in Java can be substituted with a `while` loop. The following two loops are equivalent:

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
```

But notice how you have to layout the initialization of the `i` variable and also do the incrementing of `i` inside the loop. This is because the `for` loop does this for you. But `while` loops do not.

## One of the things to note about this lab

The description of th eloops and what they produce is somewhat vague. (Welcome to software coding). So, you will have to make some decisions about what the loops should do. And, you will have to make sure that your loops do what you think they should do. Be carefule with where they start and where they end. And, be careful with what they do inside the loop.

Think it thru, what should each method do? What should it return? What should it print? What should it not print? What should it not return? What should it not do?

This can be a tricky lab. But, it is also a very important lab. You will be using loops for the rest of your life. So, get good at them now.


## Python

* Complete the following Python utilities that mirror the Java functionality:
    * NumberUtilities - Number generation and manipulation functions
    * TriangleUtilities - ASCII triangle generation functions  
    * TableUtilities - Multiplication table generation functions

## Loops. `for` and `while` loops in Python

In Python, for and while loops are used for repetitive execution of a block of code.

A for loop is typically used to iterate over a sequence (like a list, string, or range). Python's for loop is different from Java's - it's more like a foreach loop. Here's an example:

```python
for i in range(10):
    print(i)
```

This loop will print the numbers from 0 to 9.

A while loop continues until a certain condition is met. The condition is checked at the beginning of each iteration:

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

This loop will also print the numbers from 0 to 9.

Python also supports infinite loops:

```python
while True:
    print("I'm stuck in an infinite loop!")
```

Or conditional loops in a game context:

```python
while player_one.is_alive() and player_two.is_alive():
    player_one.attack(player_two)
    player_two.attack(player_one)
```

### Python NumberUtilities Functions

Implement these functions that return concatenated strings of numbers:

```python
def get_even_numbers(start, stop):
    """Return concatenated string of even numbers from start to stop (exclusive)"""
    # Example: get_even_numbers(5, 20) returns "681012141618"
    
def get_odd_numbers(start, stop):
    """Return concatenated string of odd numbers from start to stop (exclusive)"""
    # Example: get_odd_numbers(5, 20) returns "5791113151719"
    
def get_square_numbers(start, stop, step):
    """Return concatenated string of squared numbers from start to stop with step"""
    # Example: get_square_numbers(5, 15, 5) returns "25100"
    
def get_range(start, stop, step=1):
    """Return concatenated string of numbers from start to stop with step"""
    # Example: get_range(5, 11) returns "5678910"
    # Example: get_range(5, 20, 5) returns "51015"
    
def get_exponentiations(start, stop, step, exponent):
    """Return concatenated string of numbers raised to exponent"""
    # Example: get_exponentiations(5, 20, 5, 2) returns "25100225"
```

### Python TriangleUtilities Functions

Implement these functions that return ASCII triangle patterns:

```python
def get_row(width):
    """Return string of asterisks with specified width"""
    # Example: get_row(10) returns "**********"
    
def get_small_triangle():
    """Return 4-row triangle string"""
    # Returns:
    # *
    # **
    # ***
    # ****
    
def get_large_triangle():
    """Return 10-row triangle string"""
    # Returns triangle with rows 1-10
    
def get_triangle(n):
    """Return n-row triangle string"""
    # Example: get_triangle(3) returns triangle with 3 rows
```

### Python TableUtilities Functions

Implement these functions that return formatted multiplication tables:

```python
def get_small_multiplication_table():
    """Return 4x4 multiplication table string"""
    # Returns formatted 4x4 table
    
def get_large_multiplication_table():
    """Return 10x10 multiplication table string"""  
    # Returns formatted 10x10 table
    
def get_multiplication_table(width):
    """Return width x width multiplication table string"""
    # Example: get_multiplication_table(3) returns:
    #   1 |  2 |  3 |
    #   2 |  4 |  6 |
    #   3 |  6 |  9 |
```

### Python Implementation Notes

- Use string concatenation or join() for building result strings
- Use range() function for numeric loops
- Python uses snake_case naming convention
- No explicit type declarations needed
- Use f-strings or format() for string formatting in tables
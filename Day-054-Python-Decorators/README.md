# Day 54 – Python Decorators and Function Execution Time

## 📖 Overview

This project is part of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.

On Day 54, I learned about Python Decorators and how they can be used to extend the functionality of existing functions without modifying their original code.

I developed a function execution time calculator using Python decorators and the `time` module. The program measures how long different functions take to execute by recording their start and end times.

A custom decorator called `speed_calc_decorator` is created to wrap around existing functions. It uses a nested wrapper function, `*args`, and `**kwargs` to execute the original function and calculate its execution time.

The project demonstrates function decorators, nested functions, higher-order functions, variable arguments, function wrapping, and performance measurement.

## 🎯 Objectives

- Understand the concept of Python decorators.
- Learn how to pass functions as arguments to other functions.
- Create custom decorators to extend existing function functionality.
- Understand nested functions and closures.
- Use wrapper functions to execute additional code before and after a function.
- Learn how `*args` and `**kwargs` work.
- Use the `time` module to measure execution time.
- Calculate the time taken by a function to execute.
- Apply decorators using the `@decorator_name` syntax.
- Compare the execution time of two functions.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **time Module** – Retrieving the current time and measuring function execution duration.
- **Decorators** – Extending the functionality of existing functions.
- **Nested Functions** – Defining functions inside other functions.
- **Higher-Order Functions** – Passing functions as arguments and returning functions.

## 📚 Concepts Practiced

| **Concept**            | **Description**                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| Functions as Arguments | Passing one function as an argument to another function.                                          |
| Higher-Order Functions | Functions that accept other functions as arguments or return functions.                           |
| Decorators             | Adding extra functionality to an existing function without modifying its original implementation. |
| Nested Functions       | Defining a function inside another function.                                                      |
| Wrapper Functions      | Wrapping an original function to execute additional operations before or after it.                |
| Closures               | Allowing an inner function to access variables from its enclosing function.                       |
| `*args`                | Accepting any number of positional arguments.                                                     |
| `**kwargs`             | Accepting any number of keyword arguments.                                                        |
| `return`               | Returning values from functions.                                                                  |
| `@decorator_name`      | Applying a decorator to a function using Python decorator syntax.                                 |
| `time.time()`          | Getting the current time in seconds since January 1, 1970.                                        |
| Execution Time         | Calculating the duration required by a function to complete execution.                            |
| `__name__`             | Accessing the name of a function.                                                                 |
| Function Wrapping      | Executing the original function through a wrapper function.                                       |
| Loops                  | Repeating an operation multiple times to perform a computational task.                            |

## ⚙️ How It Works

**Import Time Module:** Imports Python's built-in `time` module to access the current system time.

**Create the Decorator:** Defines a custom function called `speed_calc_decorator` that accepts another function as an argument.

**Define Wrapper Function:** Creates a nested function called `wrapper_function` that accepts `*args` and `**kwargs`, allowing it to handle different types and numbers of arguments.

**Record Start Time:** Uses `time.time()` to record the time immediately before the original function executes.

**Execute Original Function:** Calls the original function using `func(*args, **kwargs)` and stores its return value.

**Record End Time:** Calls `time.time()` again after the original function finishes executing.

**Calculate Execution Time:** Subtracts the start time from the end time to calculate the total execution duration.

**Return Execution Details:** Returns a formatted string containing the original function's name and its execution time.

**Apply Decorator:** Uses `@speed_calc_decorator` above both `fast_function()` and `slow_function()` to automatically wrap them with the decorator.

**Execute Functions:** Calls both decorated functions to calculate and display their execution times.

## 💻 Key Implementation Details

### 1. Importing the Time Module

```python
import time
```

Imports Python's built-in time module.

The `time.time()` function returns the current time in seconds since January 1, 1970 (Unix epoch).

This function is used to record timestamps before and after executing another function.

### 2. Creating the Custom Decorator

```python
def speed_calc_decorator(func):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        return (
            f"{func.__name__} run speed: "
            f"{end_time - start_time}"
        )

    return wrapper_function
```

Defines a custom decorator named `speed_calc_decorator`.

- `func` – Receives the original function that needs to be decorated.
- `wrapper_function()` – A nested function that adds execution time measurement functionality.
- `*args` – Accepts any number of positional arguments.
- `**kwargs` – Accepts any number of keyword arguments.
- `start_time` – Stores the time before executing the original function.
- `func(*args, **kwargs)` – Executes the original function.
- `end_time` – Stores the time after the original function finishes.
- `end_time - start_time` – Calculates the total execution time.
- `func.__name__` – Retrieves the name of the original function.
- `return wrapper_function` – Returns the wrapper function so it can replace the original function.

### 3. Understanding the Wrapper Function

```python
def wrapper_function(*args, **kwargs):
    start_time = time.time()

    result = func(*args, **kwargs)

    end_time = time.time()
```

The wrapper function controls the execution of the original function.

It performs three main operations:

1. Records the starting time.
2. Executes the original function.
3. Records the ending time.

The wrapper function allows additional functionality to be added without changing the original function's code.

### 4. Measuring Function Execution Time

```python
start_time = time.time()

result = func(*args, **kwargs)

end_time = time.time()

execution_time = end_time - start_time
```

Uses `time.time()` to capture two timestamps.

The difference between these timestamps represents the time taken by the function to execute.

For example, if a function starts at 10.5 seconds and finishes at 12.5 seconds, its execution time is 2 seconds.

### 5. Returning the Function Name and Execution Time

```python
return (
    f"{func.__name__} run speed: "
    f"{end_time - start_time}"
)
```

Uses an f-string to display the original function's name and the time taken to execute it.

The `__name__` attribute retrieves the name of the function passed to the decorator.

The calculated execution time is included in the returned string.

### 6. Creating the Fast Function

```python
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
```

Defines a function called `fast_function()` and applies the custom decorator using `@speed_calc_decorator`.

The for loop executes one million iterations.

During each iteration, `i * i` calculates the square of the current value of `i`.

This creates a computational task whose execution time can be measured by the decorator.

### 7. Creating the Slow Function

```python
@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i * i
```

Defines another function called `slow_function()`.

It performs the same calculation as `fast_function()` and is decorated using the same decorator.

Both functions execute similar workloads, allowing their execution times to be measured and compared.

**Note:** In this particular implementation, both functions perform identical operations, so neither is intentionally slower than the other. Their measured times may differ slightly because of system activity and execution conditions.

### 8. Calling the Decorated Functions

```python
fast_function()
slow_function()
```

Calls both decorated functions.

Because the decorator is applied using `@speed_calc_decorator`, Python executes the corresponding wrapper functions instead of directly calling the original functions.

Each wrapper records the start time, executes the original function, calculates the execution duration, and returns the execution details.

## 📂 Project Structure

```text
Day-054-Python-Decorators/
│
├── main.py
└── README.md
```

**main.py** – Contains the custom speed calculation decorator and the two functions used to measure execution time.

**README.md** – Documents the project's functionality, technologies, and implementation details.

## 🔐 Important Notes

- The project uses Python's built-in `time` module, so no external library installation is required.
- The `@speed_calc_decorator` syntax automatically applies the decorator to the function.
- The decorator works with functions that accept positional and keyword arguments because of `*args` and `**kwargs`.
- Both functions perform the same computational operation.
- Execution times may vary depending on system performance and background processes.
- The `result` variable stores the original function's return value, although it is not used in the current implementation.
- The decorator currently returns execution information as a string rather than returning the original function's result.
- For more accurate function metadata preservation, Python provides `functools.wraps`.

## 🧠 What I Learned

- Understanding Python decorators and their purpose.
- Passing functions as arguments to other functions.
- Creating higher-order functions.
- Working with nested functions and closures.
- Understanding how wrapper functions work.
- Using `*args` and `**kwargs` to handle flexible function arguments.
- Applying decorators using the `@` syntax.
- Measuring execution time using the `time` module.
- Understanding the difference between a function and its returned wrapper.
- Accessing function metadata using `__name__`.
- Adding functionality to existing functions without modifying their original code.
- Understanding how decorators can be used for performance measurement and code optimization.

## 🚀 Future Improvements

- Use `functools.wraps` to preserve the original function's name and metadata.
- Return the original function's result along with execution time.
- Add support for functions with different positional and keyword arguments.
- Compare functions performing different computational tasks.
- Use `time.perf_counter()` for more precise execution time measurements.
- Create a reusable decorator that logs execution time to a file.
- Add exception handling to ensure timing information can be recorded even if a function raises an exception.
- Display execution time in milliseconds for easier readability.

## 🔑 Key Takeaway

This project strengthened my understanding of Python decorators and higher-order functions. I learned how decorators can extend the functionality of existing functions without modifying their original implementation.

By creating a custom execution time calculator, I gained practical experience with nested functions, wrapper functions, closures, `*args`, `**kwargs`, and the `time` module.

It also helped me understand how decorators can be used in real-world Python applications for performance monitoring, logging, authentication, and code reuse.

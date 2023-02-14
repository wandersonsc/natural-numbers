## Sum of Natural Numbers 

This function calculates the sum of the first n natural numbers, which are the positive integers 1, 2, 3, ..., `n`. The function takes a single argument n, which specifies the number of natural numbers to be summed.
## Get the code.

1. Get the code:

```
git clone https://github.com/wandersonsc/natural-numbersn
```

2. Run it! Assuming you have Python setup.


```sh
pip3 install -r requirements.txt
```


## How it works

The function has a base case, which is when `n <= 1`. In this case, the function returns `n`, since the sum of the first 1 natural number is 1.

If `n > 1`, the function returns `n + natural_numbers(n - 1)`. Which makes a recursive call to the natural_numbers function, with `n - 1` as the argument. The recursive call calculates the sum of the first `n - 1` natural numbers, and this sum is added to `n` to give the sum of the first `n` natural numbers.

This line of code is executed repeatedly for each recursive call to the function, until the base case is reached and the function returns the final sum of the first `n` natural numbers.


```python
   def sum_natural_numbers(n):
       if n <= 1:
          return 
       return n + sum_natural_numbers(n - 1)



```


## Testing

To run the tests.

```sh
pytest

```

```python
 def test_sum_natural_numbers():
    """ Test the natural number fuction """

    n = 10
    assert sum_natural_numbers(n) == 55

```

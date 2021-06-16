# Exercise 5: TBD

Implement a function that sorts a list of numbers, so odd numbers are moved to the left and even numbers to the right:

```python
test_numbers = [int(x%7*5/2) for x in range(20)]

def odd_even_sort(l):
    # TODO: implement, return a list with odd numbers from input on left and even numbers from input on right
    raise NotImplementedError

def test(func, input):
    output = list(func(input))
    # same numbers in two lists
    t1 = sorted(output) == sorted(input)
    # odd-even criteria
    modlist = [int(x%2) for x in output]
    first_one = modlist.index(1)
    t2 = set([x%2 for x in output[:first_one]]) == {0}
    t3 = set([x%2 for x in output[first_one:]]) == {1}
    if t1 and t2 and t3:
        print('Congratulations')
    else:
        print('Try again:', t1, t2, t3)

test(odd_even_sort, test_numbers)
```

Post your answer on [Github Gist](https://gist.github.com/) or [paste bin](https://paste.ubuntu.com/).

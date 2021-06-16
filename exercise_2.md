# Exercise 2: check if string is a palindrome

Implement a function that checks whether a string is a palindrome:

```python
test_strings = [
  'kolmivaihekilowattituntimittari',
  'kalenterivuosi',
  'saippuakivikauppias',
  'liikekannallepanotarkastuskierros',
  'kuusikymmentä'
]

def is_palindrome(s):
  # TODO: implement, return True or False
  return s == s[::-1]


def test(func, input):
    t1 = [int(func(s)) for s in input] == [0,0,1,0,0]
    if t1:
        print('Congratulations')
    else:
        print('Try again')

test(is_palindrome, test_strings)
```

Post your answer on [Github Gist](https://gist.github.com/) or [paste bin](https://paste.ubuntu.com/).

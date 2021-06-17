# Exercise 2: check if string is a palindrome

```
 ,_,    ,_,    ,_,
(.,.)  (O,O)  (.,.)
(   )  (   )  (   )
-"-"----"-"----"-"-
```

Implement a function that checks whether a string is a [palindrome](https://en.wikipedia.org/wiki/Palindrome).

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
  raise NotImplementedError


def test(func, input):
    t1 = [int(func(s)) for s in input] == [0,0,1,0,0]
    if t1:
        print('Congratulations')
    else:
        print('Try again')

test(is_palindrome, test_strings)
```

Share your answers in a private [Github Gist](https://gist.github.com/) or use [Cryptobin](https://cryptobin.co/).

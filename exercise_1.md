# Exercise 1: find distinct characters in a string

```
    .      .
    _\/  \/_
     _\/\/_
 _\_\_\/\/_/_/_
  / /_/\/\_\ \
     _/\/\_
     /\  /\
     '      '
```

Implement a function that returns a collection of distinct characters in a string.

```python
test_string = 'The quick brown fox jumps over the lazy dog twice!'

def get_distinct_characters(s):
    raise NotImplementedError

def test(func, input):
    t1 = sorted(list(func(input))) == sorted([' ', '!', 'T', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    if t1:
        print('Congratulations')
    else:
        print('Try again')

test(get_distinct_characters, test_string)
```

Share your answers in a secret [Github Gist](https://gist.github.com/) or use [Cryptobin](https://cryptobin.co/).

# Exercise 5: crack the PIN-code

```
     _________
    / ======= \
   / __________\
  | ___________ |
  | | -       | |
  | |         | |
  | |_________| |________________________
  \=____________/                        )
  / """"""""""" \                       /
 / ::::::::::::: \                  =D-'
(_________________)
```

Implement a function that cracks a PIN-code hash. You know that the original PIN has four digits and that it was hashed using the SHA-256 hashing algorithm.

```python
sha256_hexdigest = 'bc009cb0995a6810ea16db57aebd7f7c65d7fac419be4c1f16ed6bc3b58d5359'

def crack_sha256(hexdigest):
    # TODO: implement, return PIN code as four-digit integer, e.g. 1234
    raise NotImplementedError

def test(func, input):
    output = func(input)
    if output == 8068:
        print('Congratulations')
    else:
        print('Try again')

test(crack_sha256, sha256_hexdigest)
```

Share your answers in a private [Github Gist](https://gist.github.com/) or use [Cryptobin](https://cryptobin.co/).

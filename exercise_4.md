# Exercise 4: count words on a webpage

```
 __     __     __     __     __     __    
/\ \  _ \ \   /\ \  _ \ \   /\ \  _ \ \   
\ \ \/ ".\ \  \ \ \/ ".\ \  \ \ \/ ".\ \  
 \ \__/".~\_\  \ \__/".~\_\  \ \__/".~\_\
  \/_/   \/_/   \/_/   \/_/   \/_/   \/_/
```

Implement a function that counts words on a webpage. Your function must download the source for the webpage and return the same count as the Linux command `wc -w`.

> Bonus points: implement the function so that it ignores HTML markup.

```python
test_url_1 = 'https://raw.githubusercontent.com/skipperkongen/codechallenge-serotina-kudos/main/page_raw.txt'
test_url_2 = 'https://raw.githubusercontent.com/skipperkongen/codechallenge-serotina-kudos/main/page_markup.html'

def count_words_web(url):
    # TODO: implement, return integer, number of words on webpage
    raise NotImplementedError

def test(func, input):
    t1 = func(input[0]) == 69
    t2 = func(input[1]) == 69
    if t1 and t2:
        print('Congratulations, you cracked the bonus question!')
    elif t1:
        print('Congratulations!')
    else:
        print('Try again:', t1, t2)

test(count_words_web, [test_url_1, test_url_2])
```

Share your answers in a secret [Github Gist](https://gist.github.com/) or use [Cryptobin](https://cryptobin.co/).

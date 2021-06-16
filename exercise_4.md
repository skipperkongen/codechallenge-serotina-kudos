# Exercise 4: count words on a webpage

Implement a function that counts words on a webpage. Your function must download the source for the webpage and return the same count as the Linux command `wc -w`.
Bonus points: implement the function so that it ignores HTML markup.

```python
test_url_1 = 'https://raw.githubusercontent.com/skipperkongen/codechallenge-serotina-kudos/main/page_raw.txt'
test_url_2 = 'https://raw.githubusercontent.com/skipperkongen/codechallenge-serotina-kudos/main/page_markup.html'

def count_words_web(url):
    # TODO: implement, return integer, number of words on webpage
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

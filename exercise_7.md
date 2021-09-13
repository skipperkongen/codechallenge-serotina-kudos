# Exercise 7: Uncles & Aunts

```
  ,--.
 //^\\\   ,;;;,                        .
((-_-))) (-_- ;                       /_\
 )))(((   >..'.    .:.     .--.      |SSt|
((_._ )  /.   .|  :-_-;   /-_-))
_))A ((_//| S ||  ,`-'.   ))-((
`(    )`' |___|),;, C \\_/,`I ))
  \  /    | | |`' |___(/-'|___()  ,-.
   )(     | | |   | | |   | | |  (-_-)    _____
  /__\    |_|_|   |_|_|   |_|_|  (\I/\.__|A|R|T|
  `''     `-'-'   `-'-'   `-'-'  `'-`'   `o' `o'
```

Write a function that returns the uncles and aunts of input person. An uncle is
the sibling or half-sibling of one of your parents.

```python

def get_uncle_and_aunt_ids(id, people):
    raise NotImplementedError

people = [
    {"id": 1, "name": "Peter", "parent_ids": []},
    {"id": 2, "name": "Jamela", "parent_ids": []},
        {"id": 8, "name": "Konstantin", "parent_ids": [1, 2]},
    {"id": 3, "name": "Beth", "parent_ids": []},    
        {"id": 9, "name": "Thor", "parent_ids": [1, 3]},
        {"id": 10, "name": "Freja", "parent_ids": [1, 3]},
            {"id": 17, "name": "Agnes", "parent_ids": [10, 13]},
            {"id": 18, "name": "Agnar", "parent_ids": [10, 13]},
    {"id": 4, "name": "Ali", "parent_ids": []},
    {"id": 5, "name": "Ahlam", "parent_ids": []},
        {"id": 11, "name": "Sophia", "parent_ids": [4,5]},
            {"id": 19, "name": "Helga", "parent_ids": [9,11]},
            {"id": 20, "name": "Aisha", "parent_ids": [9,11]},
        {"id": 12, "name": "Aaliyah", "parent_ids": [4,5]},
            {"id": 21, "name": "Emi", "parent_ids": [12,15]},
            {"id": 22, "name": "Osamu", "parent_ids": [12,15]},
        {"id": 13, "name": "Abbas", "parent_ids": [4,5]},
        {"id": 14, "name": "Adil", "parent_ids": [4,5]},
    {"id": 6, "name": "Hanako", "parent_ids": []},
    {"id": 7, "name": "Isamu", "parent_ids": []},
        {"id": 15, "name": "Hideki", "parent_ids": [6,7]},
        {"id": 16, "name": "Haruna", "parent_ids": [6,7]},
            {"id": 23, "name": "Athena", "parent_ids": [8, 16]},
            {"id": 24, "name": "Yukiko", "parent_ids": [8, 16]},
]

assert set(get_uncle_and_aunt_ids(17, people)) == {9, 11, 12, 14}
```

Share your answers in a secret [Github Gist](https://gist.github.com/) or use [Cryptobin](https://cryptobin.co/).

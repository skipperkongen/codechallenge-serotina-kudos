def flat_list(nested_list):
    return [y for x in nested_list for y in x]

def get_uncle_and_aunt_ids(id, people):
    person = [x for x in people if x['id'] == id][0]
    parents = [x for x in people if x['id'] in person['parent_ids']]
    parent_ids = [x['id'] for x in parents]
    grandparent_ids = flat_list([x['parent_ids'] for x in parents])
    uncles_and_aunts = [x for x in people if set(x['parent_ids']).intersection(grandparent_ids) and x['id'] not in parent_ids]
    return [x['id'] for x in uncles_and_aunts]

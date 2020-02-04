def read_file(path):
    """
    (str) -> (set)
    Return set of lines from file
    """
    lst = []
    with open(path, mode='r', encoding='utf-8') as f:
        for word in f:
            word = word.replace('\n', '')
            '''word = word.split('\t')'''
            word = word.replace('\t', ' ')
            lst.append(word)
    lst.pop(0)
    return set(lst)


def votes_dict(lines_set, num_v):
    """
    (set, int) -> (dict)
    Return dict from set of lines if number of votes > num_v
    """
    res = {}
    for elem in lines_set:
        if elem[13] == ' ':
            if int(elem[14:]) > num_v:
                res[elem[:9]] = elem[10:13]
        else:
            if int(elem[15:]) > num_v:
                res[elem[:9]] = elem[10:14]
    return res


def films_id(n, dict_votes):
    """
    (int, dict) -> (set)
    Return set of n films id with the highest rating
    """
    val_lst = []
    res = []
    for key in dict_votes:
        val_lst.append(dict_votes[key])
    val_lst.sort()
    for i in range(n):
        for key in dict_votes:
            if dict_votes[key] == val_lst[(-1) - i]:
                if key not in res:
                    res.append(key)
    if len(res) > n:
        d = len(res) - n
        for i in range(d):
            res.pop(-1)
    return set(res)


def write_films_id(set_films_id):
    """
    (set) -> Note
    Write films id to file
    """
    text = open('films_id.txt', 'w')
    for elem in set_films_id:
        text.write(elem + '\n')


def find_films_id(n=10, num_v=10**6):
    """
    (int, int) -> None
    """
    write_films_id(films_id(n, votes_dict(read_file('data.tsv'), num_v)))

find_films_id()
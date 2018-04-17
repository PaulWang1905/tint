a = [1,2,3]
squares = [x**2 for x in a]
squares_a = map(lambda x: x **2,a)
print(squares)
print(list(squares_a))
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)


# using dict and set
ranks = {'ghost':1,'habanero':2,'cayenne':3}
rank_dict = {rank: name for name, rank in ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

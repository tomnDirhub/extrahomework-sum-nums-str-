def calc_sum_srtucture(struct):
    sum = 0
    if isinstance(struct, int) or isinstance(struct, float):
        sum += struct
    elif isinstance(struct, str):
        sum += len(struct)
    elif isinstance(struct, str):
        sum += int(struct)
    elif isinstance(struct, list) or isinstance(struct, tuple) or isinstance(struct, set):
        for i in struct:
            sum += calc_sum_srtucture(i)
    elif isinstance(struct, dict):
        for key, item in struct.items():
            sum += calc_sum_srtucture(key)
            sum += calc_sum_srtucture(item)
    return sum





data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calc_sum_srtucture(data_structure)
print(result)


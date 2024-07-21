# module3hard.py Дополнительное практическое задание по модулю: "Подробнее о функциях."


def calculate_strukture_sum(a):
    sum_ = 0
    for i in a:
        if isinstance(i, str):
            sum_ += len(i)
            continue
        if isinstance(i, int or float):
            sum_ += i
            continue
        if isinstance(i,list):
            sum_ += calculate_strukture_sum(i)
            continue
        if isinstance(i, tuple):
            sum_ += calculate_strukture_sum(i)
            continue
        if isinstance(i,dict ):
            sum_ += calculate_strukture_sum(i.items())
            continue
        if isinstance(i, set):
            sum_ += calculate_strukture_sum(i)
            continue
    return sum_




data_structure = [
    2,
    6,
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_strukture_sum(data_structure)
print(result)

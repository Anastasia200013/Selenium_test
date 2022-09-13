def avg(ranks):
    assert len(ranks) != 0, 'Список ranks не должен быть пустым'
    return round(sum(ranks)/len(ranks), 2)

ranks = []
print("Среднее значение:", avg(ranks))


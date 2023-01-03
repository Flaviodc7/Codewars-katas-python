def cakes(rec, avai):
    array_quantity = []
    if len(rec) > len(avai):
        return 0
    for key in rec:
        if key in avai:
            array_quantity.append(int(avai[key] / rec[key]))
        else:
            return 0
    return min(array_quantity)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available)


# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

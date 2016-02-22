def median(lst):
    """

    :rtype: float
    """
    lst = sorted(lst)
    med = None
    l = len(lst)
    if l % 2 == 0:
        if l == 1:
            med = lst[0]
        else:
            med_l = len(lst) / 2 - 1
            med = float((lst[med_l]) + lst[med_l + 1]) / 2
    else:
        med_l = abs(len(lst) / 2) +1
        med = lst[med_l]
    return med


print median([4, 5, 5, 4])
print median([4, 5, 6, 5, 4])


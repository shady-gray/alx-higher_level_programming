#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        n = []
        m = []
        k = 1
        n_total = 0
        m_total = 0
        for tup in my_list:
            for a in tup:
                k *= a
            n.append(k)
            k = 1
            m.append(tup[1])

        for a in n:
            n_total = n_total + a
        for b in m:
            m_total = m_total + b
        average = n_total / m_total

        return average

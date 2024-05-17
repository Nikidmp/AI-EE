import random
import bisect


graph2 = {0: [1, 2, 3, 12, 14, 15],
          1: [0, 2, 4, 7, 8, 13, 14, 15],
          2: [0, 1, 3, 4, 5],
          3: [0, 2, 5, 12],
          4: [1, 2, 5, 6, 8, 9],
          5: [2, 3, 4, 6, 10, 12],
          6: [4, 5, 9, 10],
          7: [1, 8, 13],
          8: [1, 4, 7, 9, 11, 13],
          9: [4, 6, 8, 10, 11],
          10: [5, 6, 9, 11, 12],
          11: [8, 9, 10, 12, 13, 14],
          12: [0, 3, 5,  10, 11, 14, 15],
          13: [1, 7, 8, 11, 14],
          14: [0, 1, 11, 12, 13, 15],
          15: [0, 1, 14],
          }

# ----------------------------------------------------------------

# random first list
rand_l = []
for i in range(200):
    row = [0] * 16
    rand_l.append(row)


def mutation(rand_list):
    m_rate = 0.1
    for mut1 in range(len(rand_list)):
        if random.random() < m_rate:
            for mut2 in range(len(rand_list[i])):
                rand_list[mut1][mut2] = random.randint(1, 4)
    return rand_list


def count_score(rand_list):
    # list with the score of every row of rand_list
    score = [0] * 200

# rand_list contains 20 rows
    for r2 in range(len(rand_list)):
        for km, vm in graph2.items():
            for v5 in vm:
                if rand_list[r2][km] != rand_list[r2][v5]:
                    score[r2] += 1
    for s in range(len(score)):
        score[s] //= 2

    # print("score=", score)
    return score


def roulette(lista):
    roulette_list = [lista[0]]
    for rlt in range(1, len(lista)):
        roulette_list.append(lista[rlt]+roulette_list[rlt-1])
    return roulette_list


def select_parent(lista, summ, rlt):
    par_l = []
    for pr in range(len(lista)):
        rn = random.randint(0, summ)
        # print("random numbers", rn)
        r2 = bisect.bisect_left(rlt, rn)
        par_l.append(r2)
    return par_l


def couple_nodes(parent_list, random_list):
    node_list = []
    for prn in parent_list:
        node_list.append(random_list[prn])
    return node_list


def child_meth(node_lista):
    ch_list = []
    # range 4
    for ch in range(0, len(node_lista), 2):
        q1 = node_lista[ch][:8] + node_lista[ch+1][-8:]
        q2 = node_lista[ch+1][:8] + node_lista[ch][-8:]
        ch_list.append(q1)
        ch_list.append(q2)
    return ch_list


def partial_update(random_list):
    for u1 in range(len(random_list)):
        if random.random() < 0.3:
            for u2 in range(16):
                r_int = random.randint(1, 4)
                random_list[u1][u2] = r_int
    return random_list


# ---------Main program-----------

# First Random solution
max_sc = 0
# fill rand_l with random values-only for first time
for i in range(200):
    for j in range(16):
        rand_int = random.randint(1, 4)
        rand_l[i][j] = rand_int

# ------------------------------------------------

for t in range(1000):
    rand_l = mutation(rand_l)

    # count score for the elements of list
    scr = count_score(rand_l)
    sum_l = sum(scr)

    for sc in range(len(scr)):
        if scr[sc] > max_sc:
            max_sc = scr[sc]
            th = scr.index(max_sc)
            best_choice = rand_l[th]

    # roulette algorithm
    rl = roulette(scr)
    # print(rl)

    # parent is the list that contains rows-parents
    parent = select_parent(rand_l, sum_l, rl)
    # print("parent=", parent)
    nodes = couple_nodes(parent, rand_l)
    rand_l.clear()
    rand_l = []
    rand_l = child_meth(nodes)
    rand_l = partial_update(rand_l)

print("max score= ", max_sc)
print("best choice=", best_choice)


def insertion_sort(G, l=1):
    for i in range(1, len(G)):
        h = i
        
        while G[h] < G[h - l] and h - l >= 0:
            G[h], G[h - l] = G[h - l], G[h]
            h -= l

    return G


def shell_sort(G):
    P = [1]
    k = 0

    while P[-1] < j:
        P.append(4**(k + 1) + (3*(2**k)) + 1)
        k += 1
    P.pop()

    while j > 1:
        j = P.pop()
        G = insertion_sort(G, j)

    return G


def selection_sort(G):
    for i in range(len(G)):
        m = i
        for j in range(i+1, len(G)):
            if G[j] < G[m]:
                m = j

        G[i], G[m] = G[m], G[i]

    return G
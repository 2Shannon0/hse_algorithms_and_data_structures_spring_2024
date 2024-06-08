def exchange(kit, sum):
    razmen = []
    for i in range(len(kit) - 1, -1, -1):
        while sum >= kit[i]:
            sum -= kit[i]
            razmen.append(kit[i])
    if sum != 0:
        return []
    return razmen

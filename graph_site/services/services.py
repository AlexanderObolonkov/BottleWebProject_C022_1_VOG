def kruskal_algorithm(graph: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    sorted_graph = sorted(graph, key=lambda x: x[0])
    connected_vertices = set()  # список соединенных вершин
    isolated_groups = {}  # словарь списка изолированных групп вершин
    skeleton = []  # список ребер остова

    for r in sorted_graph:
        if r[1] not in connected_vertices or r[2] not in connected_vertices:  # проверка для исключения циклов в остове
            if r[1] not in connected_vertices and r[2] not in connected_vertices:  # если обе вершины не соединены, то
                isolated_groups[r[1]] = [r[1], r[2]]  # формируем в словаре ключ с номерами вершин
                isolated_groups[r[2]] = isolated_groups[r[1]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not isolated_groups.get(r[1]):  # если в словаре нет первой вершины, то
                    isolated_groups[r[2]].append(r[1])  # добавляем в список первую вершину
                    isolated_groups[r[1]] = isolated_groups[r[2]]  # и добавляем ключ с номером первой вершины
                else:
                    isolated_groups[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
                    isolated_groups[r[2]] = isolated_groups[r[1]]

            skeleton.append(r)  # добавляем ребро в остов
            connected_vertices.add(r[1])  # добавляем вершины в множество U
            connected_vertices.add(r[2])

    for r in sorted_graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[2] not in isolated_groups[r[1]]:  # если вершины принадлежат разным группам, то объединяем
            skeleton.append(r)  # добавляем ребро в остов
            gr1 = isolated_groups[r[1]]
            isolated_groups[r[1]] += isolated_groups[r[2]]  # объединим списки двух групп вершин
            isolated_groups[r[2]] += gr1

    return skeleton


def kruskal_algorithm2(graph: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    sorted_graph = sorted(graph, key=lambda x: x[2])
    connected_vertices = set()  # список соединенных вершин
    isolated_groups = {}  # словарь списка изолированных групп вершин
    skeleton = []  # список ребер остова

    for r in sorted_graph:
        if r[0] not in connected_vertices or r[1] not in connected_vertices:  # проверка для исключения циклов в остове
            if r[0] not in connected_vertices and r[1] not in connected_vertices:  # если обе вершины не соединены, то
                isolated_groups[r[0]] = [r[0], r[1]]  # формируем в словаре ключ с номерами вершин
                isolated_groups[r[1]] = isolated_groups[r[0]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not isolated_groups.get(r[0]):  # если в словаре нет первой вершины, то
                    isolated_groups[r[1]].append(r[0])  # добавляем в список первую вершину
                    isolated_groups[r[0]] = isolated_groups[r[1]]  # и добавляем ключ с номером первой вершины
                else:
                    isolated_groups[r[0]].append(r[1])  # иначе, все то же самое делаем со второй вершиной
                    isolated_groups[r[1]] = isolated_groups[r[0]]

            skeleton.append(r)  # добавляем ребро в остов
            connected_vertices.add(r[0])  # добавляем вершины в множество U
            connected_vertices.add(r[1])

    for r in sorted_graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[1] not in isolated_groups[r[0]]:  # если вершины принадлежат разным группам, то объединяем
            skeleton.append(r)  # добавляем ребро в остов
            gr1 = isolated_groups[r[0]]
            isolated_groups[r[0]] += isolated_groups[r[1]]  # объединим списки двух групп вершин
            isolated_groups[r[1]] += gr1

    return skeleton


if __name__ == '__main__':
    """
    БЫЛО: [(вес, откуда, куда), ...]
    СТАЛО: [(откуда, куда, вес), ...]
    i[0] = i[2]
    i[1] = i[0]
    i[2] = i[1]
    """
    some_graph = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
                  (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]
    abcd_graph = [(1, 2, 13), (1, 3, 18), (1, 4, 17), (1, 5, 14), (1, 6, 22),
                  (2, 3, 26), (2, 5, 22), (3, 4, 3), (4, 6, 19)]
    print(kruskal_algorithm(some_graph))
    print(kruskal_algorithm2(abcd_graph))

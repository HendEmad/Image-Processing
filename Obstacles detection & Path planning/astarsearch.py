def astar(m, startPoint, endPoint):
    print("Maze: ")
    print(m)
    # input images dimensions
    width, height = 10, 10
    # Start point
    x_start, y_start = startPoint
    # End point
    x_end, y_end = endPoint
    # node = [parentNode, x_start, y_start, heuristic_value(g), cost_value(h)]
    node = [None, x_start, y_start, 0, abs(x_end - x_start) + abs(y_end - y_start)]
    closeList = [node]
    openList = {}
    openList[y_start * width + x_start] = node
    k = 0
    while closeList:
        node = closeList.pop(0)
        x = node[1]
        y = node[2]
        l = node[3] + 1
        k += 1

        # Find neighbours
        if k != 0:
            neighbours = ((x, y+1), (x, y-1), (x+1, y), (x-1, y))
        else:
            neighbours = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

        for neighbour_x, neighbour_y in neighbours:
            if neighbour_x == x_end and neighbour_y == y_end:
                path = [(x_end, y_end)]
                while node:
                    path.append((node[1], node[2]))
                return list(reversed(path))
        if 0 <= neighbour_x < width and 0 <= neighbour_y < height and m[neighbour_y][neighbour_x] == 0:
            if neighbour_y * width + neighbour_x not in openList:
                nn = (node, neighbour_x, neighbour_y, 1, 1 + abs(neighbour_x - x_end)+abs(neighbour_y - y_end))
                openList[neighbour_y * width + neighbour_x] = nn

                nni = len(closeList)
                closeList.append(nn)
                while nni:
                    i = (nni - 1) >> 1
                    if closeList[i][4] > nn[4]:
                        closeList[i], closeList[nni] = nn, closeList[i]
                        nni = 1
                    else:
                        break
    return []
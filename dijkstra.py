def dijkstra(labirinto):

    inicio = (labirinto.rows, labirinto.cols)
    fronteira = []
    naoVisitados = {n:float('inf') for n in labirinto.grid}
    naoVisitados[inicio] = 0
    visitados = {}
    
    dijkstraPath = {}

    while naoVisitados:
        vertice = min(naoVisitados, key = naoVisitados.get)
        visitados[vertice] = naoVisitados[vertice]

        if vertice == labirinto._goal:
            break

        for d in 'EWNS':
            if labirinto.maze_map[vertice][d] == True:
                if d == 'E':
                    vizinho = (vertice[0],vertice[1]+1)
                elif d == 'W':
                    vizinho = (vertice[0], vertice[1]-1)
                elif d == 'S':
                    vizinho = (vertice[0]+1, vertice[1])
                elif d == 'N':
                    vizinho = (vertice[0]-1, vertice[1])

                if vizinho in visitados:
                    continue

                tempDist =  naoVisitados[vertice] + 1
                
                for hurdle in fronteira:
                    if hurdle[0] == vertice:
                        tempDist += hurdle[1]

                if tempDist < naoVisitados[vizinho]:
                    naoVisitados[vizinho] = tempDist
                    dijkstraPath[vizinho] = vertice

        naoVisitados.pop(vertice)
    
    fwdPath = {}
    cell = labirinto._goal

    while cell != inicio:
        fwdPath[dijkstraPath[cell]] = cell
        cell = dijkstraPath[cell]
    
    return fwdPath
            
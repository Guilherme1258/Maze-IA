import random

def bestFirst(labirinto):
    inicio = (labirinto.rows, labirinto.cols)
    fronteira = []
    nosVisitados = []
    fronteira.append(inicio)

    bestFirstPath = {}

    while fronteira != []:
        fronteira.sort(key=lambda x: heuristica(x, labirinto._goal))  # Ordena a fronteira com base na heurística

        vertice = fronteira.pop(0)
        nosVisitados.append(vertice)

        if vertice == labirinto._goal:
            print("Objetivo encontrado")
            break

        movimentos = ["E", "S", "N", "W"]
        random.shuffle(movimentos)

        for d in movimentos:
            if labirinto.maze_map[vertice][d] == True:
                if d == 'E':
                    vizinho = (vertice[0], vertice[1] + 1)
                if d == 'W':
                    vizinho = (vertice[0], vertice[1] - 1)
                if d == 'N':
                    vizinho = (vertice[0] - 1, vertice[1])
                if d == 'S':
                    vizinho = (vertice[0] + 1, vertice[1])

                if vizinho not in nosVisitados and vizinho not in fronteira:
                    fronteira.append(vizinho)
                    bestFirstPath[vizinho] = vertice

    fwdPath = {}
    cell = labirinto._goal

    while cell != inicio:
        fwdPath[bestFirstPath[cell]] = cell
        cell = bestFirstPath[cell]

    return fwdPath

def heuristica(posicao, destino):
    return abs(posicao[0] - destino[0]) + abs(posicao[1] - destino[1])
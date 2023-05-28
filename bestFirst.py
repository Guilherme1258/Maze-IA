from math import sqrt

def getVizinhos(celula, labirinto):
    return  

def bestFirst(labirinto):
    fronteira = []
    caminhos = []
    celulasVisitadas = []
    statusLabirinto = []

    destino = labirinto.getDestino()

    fronteira.append(labirinto.getPosicaoInicio())

    while fronteira != []:
        # Imprime Fronteira
        statusLabirinto.append(labirinto.getLabirintoPlot(posicoes=fronteira, cores=(0, 255, 127)))

        celula = fronteira.pop(0) # Selecionando o primeiro elemento da lista
        celulasVisitadas.append(celula)
        caminhos.append(celula)

        if celula == labirinto.getDestino():
            print("Objetivo", celula, "encontrado")
            # caminhoEncontrado = selecionaCaminho(caminhos, labirinto.getDestino())
            # statusLabirinto.append(labirinto.getLabirintoPlot(posicoes=caminhoEncontrado, cores=(0, 0, 255)))
            return statusLabirinto

        else:
            vizinhos = getVizinhos(celula, labirinto)
            for vizinho in vizinhos:
                if vizinho not in celulasVisitadas:
                    fronteira.append(vizinho)
                
                    # Ordena a fronteira de acordo com a heuristica de menor distância entre os vizinhos e o destino
                    fronteira.sort(key=lambda x: sqrt(abs(pow(x[0] - destino[0], 2)) + abs(pow(x[1] - destino[1], 2)))) # distancia euclidiana

    print("Objetivo nao existente no grafo")
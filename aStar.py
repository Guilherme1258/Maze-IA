def AStar(labirinto):
    fronteira = []
    caminhos = []
    celulasVisitadas = []
    statusLabirinto = []

    fronteira.append(labirinto.getPosicaoInicio())

    while fronteira != []:
        # Imprime Fronteira
        statusLabirinto.append(labirinto.getLabirintoPlot(posicoes=fronteira, cores=(0,255,127)))

        celula = fronteira.pop(0) # Selecionando o primeiro elemento da lista
        celulasVisitadas.append(celula)
        caminhos.append(celula)

        if celula == labirinto.getDestino():
            print("Objetivo", celula, "encontrado")
            caminhoEncontrado = selecionaCaminho(caminhos, labirinto.getDestino())
            statusLabirinto.append(labirinto.getLabirintoPlot(posicoes=caminhoEncontrado, cores=(0,0,255)))
            return statusLabirinto

        else:
            for vizinho in getVizinhos(celula, labirinto):
                if vizinho not in celulasVisitadas:
                    fronteira.append(vizinho)
                    
                    fronteira.sort(key=lambda x: abs(x[0]-labirinto.getDestino()[0])+abs(x[1]-labirinto.getDestino()[1]))

    print("Objetivo nao existente no grafo")
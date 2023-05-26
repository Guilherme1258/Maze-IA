from pyamaze import maze, agent, COLOR, textLabel
from random import randint
from bfs import *
from dfs import *
from dijkstra import *
# from bestFirst import *
# from aStar import *
#import matplotlib.pyplot as plt


def execucaoMaze(tamanho = 30, possibilidadeCaminhos = 100, algoritmo = str):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m = maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent = possibilidadeCaminhos)
    
    # Inclusao dos agentes no ambiente
    agentBfs = agent(m, footprints = True, color = COLOR.red, filled = True)
    agentDfs = agent(m, footprints = True, color = COLOR.cyan, filled = True)
    agentDijkstra = agent(m, footprints = True, color = COLOR.black, filled = True)
    agentBestFirst = agent(m, footprints = True, color = COLOR.blue, filled = True)
    agentAStar = agent(m, footprints = True, color = COLOR.green, filled = True)
    

    path1 = bfs(m)
    path2 = dfs(m)
    path3 = dijkstra(m)
    # path4 = bestFirst(m)
    # path5 = aStar(m)
    

    m.tracePath({agentBfs:path1, 
                agentDfs:path2,
                agentDijkstra:path3})
    m.run()



if __name__ == '__main__':
    execucaoMaze(tamanho = 50)
    # execucaoMaze(tamanho=100, algoritmo="dfs")
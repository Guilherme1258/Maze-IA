'''
' Ana Laura         20.2.4091
' Eder Bragança     20.2.4011
' Luísa Calegari    20.2.4101
' Selio Guilherme   20.2.4107
' Thiago Cecote     20.2.4016
'''


from pyamaze import maze, agent, COLOR, textLabel
from random import randint
from bfs import *
from dfs import *
from dijkstra import *
from bestFirst import *
from aStar import *
import tkinter as tk

def create_label(canvas, text, x, y, color):
    label = tk.Label(canvas, text=text, bg="white", fg=color, font=("Helvetica", 12, "bold"), bd=5, relief="solid",
                     padx=8, pady=4, highlightbackground=color)
    label.place(x=x, y=y)
    return label

def execucaoMaze(tamanho = 30, possibilidadeCaminhos = 100, algoritmo = str):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m = maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent = possibilidadeCaminhos)
    
    # Inclusao dos agentes no ambiente
    agentBfs = agent(m, footprints = True, color = COLOR.red, filled = True)
    agentDfs = agent(m, footprints = True, color = COLOR.cyan, filled = True)
    agentDijkstra = agent(m, footprints = True, color = COLOR.black, filled = True)
    agentBestFirst = agent(m, footprints = True, color = COLOR.green, filled = True)
    agentAStar = agent(m, footprints = True, color = COLOR.yellow, filled = True)
    
    legenda_labels = []
    legenda_labels.append(create_label(m._canvas, "BFS", 1010, 940, "red"))
    legenda_labels.append(create_label(m._canvas, "DFS", 1070, 940, "cyan"))
    legenda_labels.append(create_label(m._canvas, "Dijkstra", 1130, 940, "black"))
    legenda_labels.append(create_label(m._canvas, "Best First", 1220, 940, "green"))
    legenda_labels.append(create_label(m._canvas, "A*", 1330, 940, "yellow"))

    path1 = bfs(m)
    path2 = dfs(m)
    path3 = dijkstra(m)
    path4 = bestFirst(m)
    path5 = aStar(m)
    

    m.tracePath({agentBfs:path1, 
                agentDfs:path2,
                agentDijkstra:path3, 
                agentBestFirst:path4,
                agentAStar:path5})
    m.run()

    for label in legenda_labels:
        label.destroy()


if __name__ == '__main__':
    execucaoMaze(tamanho = 50)
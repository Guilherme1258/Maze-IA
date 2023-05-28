from pyamaze import maze,agent,textLabel
from queue import PriorityQueue

def h(cell1,cell2):
    x1,y1 = cell1
    x2,y2 = cell2

    return abs(x1-x2) + abs(y1-y2)

def aStar(labirinto):
    inicio = (labirinto.rows,labirinto.cols)
    g_score = {cell:float('inf') for cell in labirinto.grid}
    g_score[inicio] = 0
    f_score = {cell:float('inf') for cell in labirinto.grid}
    f_score[inicio] = h(inicio,labirinto._goal)

    open = PriorityQueue()
    open.put((h(inicio, labirinto._goal), h(inicio,labirinto._goal), inicio))#
    aPath = {}

    while not open.empty():
        currCell = open.get()[2]

        if currCell == labirinto._goal:
            break
        
        for d in 'ESNW':
            if labirinto.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0],currCell[1]+1)
                if d == 'W':
                    childCell = (currCell[0],currCell[1]-1)
                if d == 'N':
                    childCell = (currCell[0]-1,currCell[1])
                if d == 'S':
                    childCell = (currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell]+1
                temp_f_score  = temp_g_score+h(childCell, labirinto._goal)

                if temp_f_score  < f_score[childCell]:
                    g_score[childCell] =  temp_g_score
                    f_score[childCell] =  temp_f_score 
                    open.put((temp_f_score,h(childCell,labirinto._goal),childCell))
                    aPath[childCell] = currCell
    fwdPath = {}
    cell = labirinto._goal

    while cell != inicio:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath

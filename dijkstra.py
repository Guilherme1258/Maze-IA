def dijkstra(labirinto):

    start=(labirinto.rows, labirinto.cols)

    # hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in labirinto.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==labirinto._goal:
            break
        for d in 'EWNS':
            if labirinto.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=labirinto._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[labirinto._goal]
            
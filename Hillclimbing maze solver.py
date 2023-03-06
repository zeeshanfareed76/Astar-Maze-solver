import math
class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state 
        self.parent = parent 
        self.actions = actions 
        self.totalCost = totalCost 
        self.heuristic = heuristic 

def hillClimbing():
    initialState = 'A' 
    goalState = 'O2'

    graph = {'A': Node('A', None, [('B',1), ('I',1)], (9,0), 0),
             'B': Node('B', None, [('A',1) , ('C',1 ), ('J',1) ] , (9,1), 0),
             'C': Node('C', None, [('B',1), ('D',1)] , (9,2), 0), 
             'D': Node('D', None, [('C',1), ('K',1)] , (9,3), 0), 
             'E': Node('E', None, [('F',1), ('M',1)], (9,5), 0), 
             'F': Node('F', None, [('E',1), ('G',1)], (9,6), 0), 
             'G': Node('G', None, [('F',1), ('H',1)], (9,7), 0), 
             'H': Node('H', None, [('G',1), ('N',1), ('P',1)], (9,8), 0), 
             'I': Node('I', None, [('A',1), ('J',1),('Q',1)], (8,0), 0), 
             'J': Node('J', None, [('B',1), ('I',1), ('R',1)], (8,1), 0), 
             'K': Node('K', None, [('D',1), ('L',1)], (8,3), 0), 
             'L': Node('L', None, [('K',1), ('T',1), ('M',1)], (8,4), 0), 
             'M': Node('M', None, [('E',1), ('L',1), ('U',1)], (8,5), 0), 
             'N': Node('N', None, [('H',1), ('O',1), ('V',1)], (8,8), 0), 
             'O': Node('O', None, [('P',1), ('N',1)], (8,9), 0), 
             'P': Node('P', None, [('O',1), ('H',1)], (9,9), 0), 
             'Q': Node('Q', None, [('I',1), ('R',1), ('W',1)], (7,0), 0), 
             'R': Node('R', None, [('J',1), ('S',1), ('Q',1)], (7,1), 0), 
             'S': Node('S', None, [('X',1), ('R',1)], (7,2), 0), 
             'T': Node('T', None, [('L',1), ('U',1)], (7,4), 0), 
             'U': Node('U', None, [('M',1), ('T',1), ('Z',1)], (7,5), 0), 
             'V': Node('V', None, [('N',1)], (7,8), 0), 
             'W': Node('W', None, [('Q' ,1), ('C1',1)], (6,0), 0), 
             'X': Node('X', None, [('Y',1), ('S',1)], (6,2), 0), 
             'Y': Node('Y', None, [('D1',1), ('X',1)], (6,3), 0),
             'Z': Node('Z', None, [('U',1), ('A1',1), ('F1',1)], (6,5), 0),
             'A1': Node('A1', None, [('Z',1), ('B1',1), ('G1',1)], (6,6), 0),
             'B1': Node('B1', None, [('A1',1) , ('H1',1 ) ] , (6,7), 0),
             'C1': Node('C1', None, [('W',1), ('K1',1)] , (5,0), 0), 
             'D1': Node('D1', None, [('Y',1), ('E1',1), ('M1',1)] , (5,3), 0), 
             'E1': Node('E1', None, [('D1',1), ('F1',1)], (5,4), 0), 
             'F1': Node('F1', None, [('Z',1), ('E1',1), ('G1',1)], (5,5), 0), 
             'G1': Node('G1', None, [('A1',1), ('F1',1), ('H1',1)], (5,6), 0), 
             'H1': Node('H1', None, [('B1',1), ('G1',1), ('I1',1), ('N1',1)], (5,7), 0), 
             'I1': Node('I1', None, [('H1',1), ('J1',1)], (5,8), 0), 
             'J1': Node('J1', None, [('I1',1)], (5,9), 0), 
             'K1': Node('K1', None, [('C1',1)], (4,0), 0), 
             'L1': Node('L1', None, [('M1',1), ('P1',1)], (4,2), 0), 
             'M1': Node('M1', None, [('D1',1), ('L1',1)], (4,3), 0), 
             'N1': Node('N1', None, [('H1',1), ('R1',1)], (4,7), 0), 
             'O1': Node('O1', None, [('P1',1)], (3,1), 0), 
             'P1': Node('P1', None, [('O1',1), ('L1',1)], (3,2), 0), 
             'Q1': Node('Q1', None, [('R1',1), ('X1',1)], (3,6), 0), 
             'R1': Node('R1', None, [('N1',1), ('S1',1), ('Y1',1), ('Q1',1)], (3,7), 0), 
             'S1': Node('S1', None, [('Z1',1), ('R1',1), ('T1' ,1)], (3,8), 0), 
             'T1': Node('T1', None, [('S1',1), ('A2',1)], (3,9), 0), 
             'U1': Node('U1', None, [('B2',1)], (2,0), 0), 
             'V1': Node('V1', None, [('W1',1), ('E2',1)], (2,4), 0), 
             'W1': Node('W1', None, [('V1' ,1), ('X1',1), ('F2',1)], (2,5), 0), 
             'X1': Node('X1', None, [('Y1',1), ('Q1',1), ('W1',1), ('G2',1)], (2,6), 0), 
             'Y1': Node('Y1', None, [('R1',1), ('X1',1), ('Z1',1), ('H2',1)], (2,7), 0),
             'Z1': Node('Z1', None, [('S1',1), ('Y1',1), ('A2',1), ('I2',1)], (2,8), 0),
             'A2': Node('A2', None, [('T1',1), ('Z1',1), ('J2',1)], (2,9), 0),
             'B2': Node('B2', None, [('U1',1) , ('C2',1 ) ] , (1,0), 0),
             'C2': Node('C2', None, [('B2',1), ('D2',1), ('K2',1)] , (1,1), 0), 
             'D2': Node('D2', None, [('C2',1)] , (1,2), 0), 
             'E2': Node('E2', None, [('V1',1), ('F2',1)], (1,4), 0), 
             'F2': Node('F2', None, [('W1',1), ('E2',1), ('G2',1), ('L2',1)], (1,5), 0), 
             'G2': Node('G2', None, [('X1',1), ('F2',1), ('H2',1), ('M2',1)], (1,6), 0), 
             'H2': Node('H2', None, [('Y1',1), ('G2',1), ('I2',1), ('N2',1)], (1,7), 0), 
             'I2': Node('I2', None, [('H2',1), ('J2',1),('Z1',1)], (1,8), 0), 
             'J2': Node('J2', None, [('A2',1), ('I2',1), ('O2',1)], (1,9), 0), 
             'K2': Node('K2', None, [('C2',1)], (0,1), 0), 
             'L2': Node('L2', None, [('F2',1), ('M2',1)], (0,5), 0), 
             'M2': Node('M2', None, [('G2',1), ('N2',1), ('L2',1)], (0,6), 0), 
             'N2': Node('N2', None, [('H2',1), ('M2',1)], (0,7), 0), 
             'O2': Node('O2', None, [('J2',1)], (0,9), 0)
             }

    parentNode=initialState 
    parentCost = math.sqrt((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])**2+ (graph[goalState].heuristic[1] -  graph[initialState].heuristic[1])**2) 
    explored=[] 
    solution=[] 
    minChildCost = parentCost - 1 
    while parentNode!=goalState: 
        bestNode=parentNode 
        minChildCost=parentCost 
        explored.append(parentNode) 
        for child in graph[parentNode].actions: 
            if child[0] not in explored:
                 childCost = math.sqrt((graph[goalState].heuristic[0] - graph[child[0]].heuristic[0])**2 +(graph[goalState].heuristic[1]  - graph[child[0]].heuristic[1])**2) 
                 if childCost<minChildCost: 
                    bestNode=child[0] 
                    minChildCost=childCost 
        if bestNode==parentNode: 
            break 
        else:
            parentNode=bestNode 
            parentCost=minChildCost 
            solution.append(parentNode) 
    sol_cor=[0]*len(solution)
    sol_cost=[0]*len(solution)
    for i in range(len(solution)):
        sol_cor[i]=graph[solution[i]].heuristic
        sol_cost[i]= math.sqrt((graph[goalState].heuristic[0] - graph[solution[i]].heuristic[0])**2 +(graph[goalState].heuristic[1]  - graph[solution[i]].heuristic[1])**2) 
    return sol_cor, sol_cost, solution

sol_cor, sol_cost, solution = hillClimbing() 

print("Cordinate | Cost | Node")
for i in range(len(sol_cost)):
    print(str(sol_cor[i])+"    | "+str(round(sol_cost[i], 2))+"   | "+str(solution[i]))

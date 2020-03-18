# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).



# Imports Utility(for stacks and queues) time (for slowing down the program - test) and Directions ( to create the route )
import util
import time
from game import Directions
path = {'South': Directions.SOUTH, 'North': Directions.NORTH,
            'West': Directions.WEST, 'East': Directions.EAST}

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves     that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Depth First Search 
    """

    tupStore,isVisit = util.Stack(),set()  # isVisit = store coordinates that are visited -- tupStore = stores a tuple with the current coordinate and list of directions
    
    tupStore.push((problem.getStartState(), [])) # push start state and empty list
    while not tupStore.isEmpty(): # loops till it ran out of routes
        temp = tupStore.pop()   
        pos,answer = temp[0],temp[1]

        if problem.isGoalState(pos): return answer # returns result if goal is found
        if pos not in isVisit: # moves onto unvisited routes then add direction to the list
            isVisit.add(pos)
            for x in problem.getSuccessors(pos):
                if x[0] not in isVisit: tupStore.push((x[0], answer + [path[x[1]]]))

def breadthFirstSearch(problem):
    """
    Similar to Depth First but used Queue instead of Stack
    """
    
    tupStore,isVisit = util.Queue(),set()
    
    tupStore.push((problem.getStartState(), []))
    while not tupStore.isEmpty():
        temp = tupStore.pop()
        pos,answer = temp[0],temp[1]

        if problem.isGoalState(pos): return answer
        if pos not in isVisit:
            isVisit.add(pos)
            for x in problem.getSuccessors(pos):
                if x[0] not in isVisit: tupStore.push((x[0], answer + [path[x[1]]]))

def uniformCostSearch(problem):
    """
    Uniform Cost:
    Similar to Depth First but used Priority Queue instead of Stack and add a cost function1
    """

    tupStore,isVisit = util.PriorityQueue(),set()
    
    tupStore.push((problem.getStartState(), []),0)
    while not tupStore.isEmpty():
        temp = tupStore.pop()
        pos,answer = temp[0],temp[1]

        if problem.isGoalState(pos): return answer
        if pos not in isVisit:
            isVisit.add(pos)
            for x in problem.getSuccessors(pos):
                if x[0] not in isVisit:
                    cost = problem.getCostOfActions(answer + [path[x[1]]]) #cost function
                    tupStore.push((x[0], answer + [path[x[1]]]),cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Similar to uniform Cost but added the heuristic function
    """
    tupStore,isVisit = util.PriorityQueue(),set()
    
    tupStore.push((problem.getStartState(), []),0)
    while not tupStore.isEmpty():
        temp = tupStore.pop()
        pos,answer= temp[0],temp[1]

        if problem.isGoalState(pos): return answer
        if pos not in isVisit:
            isVisit.add(pos)
            for x in problem.getSuccessors(pos):
                if x[0] not in isVisit:
                    cost = problem.getCostOfActions(answer + [path[x[1]]])
                    tupStore.push((x[0], answer + [path[x[1]]]),cost + nullHeuristic(x[0],problem)) #null heuristic


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

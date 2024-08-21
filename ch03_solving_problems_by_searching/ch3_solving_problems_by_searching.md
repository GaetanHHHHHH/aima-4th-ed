# Chapter 3: Solving Problems by Searching

---

- goal: planning ahead to find a sequence of actions leading to a goal
    - *problem-solving agent* doing *search*
- agents must represent the world
    - problem-solving agents: atomic representations (states of the world are wholes with no internal structure)
    - planning agents: factored or structured representations of states
- characteristics of the simplest environment used in this chapter: episodic, single agent, fully observable, deterministic, static, discrete, known
    - informed 🆚 uninformed algorithms
    - asymptotic complexity (*O(n)*)

# 3.1 Problem-Solving Agents

- ~~unknown environment (actions taken at random)~~ 🆚 agents with access to information
- four phase problem-solving process
    1. **goal formulation**
    2. **problem formulation**
    3. **search**: find a sequence of actions that reach the goal (ie a **solution**)
    4. **execution**
- in our defined environment (fully observable, deterministic, known), the solution to any problem is a **fixed sequence of actions**
    - solution is guaranteed to reach the goal ⇒ no need for additional percepts after the search phase
    - **open-loop system (**🆚 closed-loop system when the loop between agent and env is not breached)
        - in a closed loop, a branching strategy can be used (scenarios in function of the current percept)

## Search problems and solutions

- formal definition of a **search problem**
    - **state space** - set of possible states of the environment
        - can be represented as a graph
    - **initial state**
    - **goal states**
    - **actions** - given a state $s$, we have a finite set of actions applicable $ACTIONS(s)$
    - t**ransition model** - describes what an action does ($RESULT(s,a)$ for doing action $a$ in $s$)
    - **action cost function** - cost of applying actions $a$ in state $s$ to reach state $s’$ ($ACTION-COST(s,a,s’)$)
        - we assume that action costs are additive
    - **path** - sequence of actions
    - **solution** - path from initial to goal states
        - an optimal solution has the lowest path cost of all

## Formulating problems

- we use **models** (abstract mathematical representations) and **abstractions** (less detailed representations)
    - we need to be careful when selecting what should/shouldn’t be abstracted away
        - *validity*: all abstract solutions can be elaborated into a solution in the detailed world
        - *usefulness*: abstractions make carrying out actions easier
        
        ⇒ we remove as much details as possible while retaining validity and ensuring usefulness
        

# 3.2 Example Problems

- standardized 🆚 real-world problems
    - **standardized problem**: used to illustrate or exercise problem-solving methods, used as benchmarks for performance
    - **real-world problem**: actually answering a problem people have

### Standardized problems

- **grid world** - 2d rectangle array of square cells
    - vacuum world
        - absolute movement actions 🆚 egocentric actions (relative to agent’s viewpoint)
    - sokoban puzzle, sliding-tile puzzle, etc
- infinite state spaces: eg Knuth conjecture

## Real-world problems

- route-finding problem
- touring problems: set of locations to be visited
    - traveling salesperson problem (TSP): every city must be visited with as low a cost possible
- VLSI layout: positioning of components and connections on chips
    - cell layout (components grouped into cells that perform a function)
    - channel routing (finding specific routes for each wire on the chip)
- robot navigation
- automatic assembly sequencing: feasibility → optimization
    - protein design

# 3.3 Search Algorithms

- search algorithm: takes a search problem and returns a solution or a failure
    - search tree superimposed on the state-space graph
    - node(s) = state
        - *expanding* nodes: considering $ACTIONS$ for that state and using $RESULT$ to see where they lead
        - *generating* new nodes (parent and child nodes)
        - search 🟰 choosing which node to expand next
            - *frontier* of the search tree: unexpended nodes
                - *separates* two regions: expended states 🆚 states not reached
            - state who has a node ⇒ *reached*
    - edge = action
    - root = initial state
- state space 🆚 search tree
    - state space: set of states linked by actions leading to transition in the world
    - search tree: paths between states

## Best-first search

- choose a node with a minimum value returned by an *evaluation function $f(n)$*
    - if goal state: return it
    - else: expand the next minimum valued node on the frontier

## Search data structures

- used to keep track of the tree
- a *node* is represented using four components:
    - $node.STATE$
    - $node.PARENT$
    - $node.ACTION$
    - $node.PAST-COST$  (from initial state to current; also written as $g(node)$)
- the *frontier* is represented by a **queue** with following available operations:
    - $IS-EMPTY(frontier)$
    - $POP(frontier)$
    - $TOP(frontier)$
    - $ADD(node,frontier)$
- three kinds of queues:
    - *priority queue*: pop node with min cost according to an evaluation funct, used for b**est-first search**
    - FIFO queue: used for **breadth-first search**
    - LIFO queue: also known as *stack*, used for **depth-first search**
- reached states stored in a **lookup table** (eg hash table) with key-value pairs of the form *state-node*

## Redundant paths

- repeated states, cycles and loopy paths: *algos that cannot remember the past are doomed to repeat it*
    - a cycle is a special case of repeated state
        - it represents a worst way to end up at the same place (higher cost, no bigger benefit)
- how do we remember the past?
    - **graph search** (look for redundant paths, eg best-first search) 🆚 **tree-like search** (no check)
    - options
        - remember all previously reached states (used for **best-first search**)
            - advised when there are a lot of redundant paths and when the table of reached states can fit in memory
        - don’t remember anything
            - advised when its impossible to have redundant paths (assembly eg)
        - compromise between the two
            - check for cycles but not redundant paths

## Measuring problem-solving performance

- criteria available
    - **completeness** (guaranteed to return a solution/failure?)
        - finite 🆚 infinite state spaces
            - in finite state spaces, completeness is achieved if we keep track of paths and cut out the cycles
            - in infinite state spaces, we need to be *systematic*
    - **cost optimality** (returned solution has the lowest path cost?)
    - t**ime complexity** (how long does it take?)
    - **space complexity** (how much memory is needed?)
        - how do we measure time and space complexity?
            - **graph** as an *explicit data structure*
                - complexity measured as: size of the state-space graph = $|V| + |E|$
                    - $|V|$ is the number of vertices (state nodes)
                    - $|E|$ is the number of edges (distinct state/action pairs)
            - *implicit state spaces*
                - complexity measured in terms of:
                    - $d$ (**depth**, or nb of actions in an optimal solution)
                    - $m$ (maximal nb of actions in any path)
                    - $b$ (**branching factor**, or nb of successors of a node to be considered)

# 3.4 Uninformed Search Strategies

- algo is given no clue how close a state is to the goal (🆚 *informed agent*)

## Breadth-first search

- expand root node → all his successors → all theirs → etc
    - equivalent to best-first search where $f(n)$ is the depth of the node (ie nb of actions to reach it)
- getting additional efficiency
    - FIFO queue
    - **early test goal**: we can check wether a node is a solution when *generating* the node, not when popping it from the queue
- efficiency
    - cost optimal when all actions have the same cost
    - complete
    - nb of nodes generated = $1+b+b^2+b^3+...+b^d$ = $O(b^d)$
    - time and space complexity are $O(b^d)$
    - biggest problem: memory requirement (*in general, exponential-complexity search problems cannot be solved by uninformed search*)

## Dijkstra’s algorithm or uniform-cost search
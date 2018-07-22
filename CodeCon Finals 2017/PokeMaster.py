#Problem        : PokeMaster
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

"""
WARNING: this code has been written AFTER the contest has ended. It means the solution
has not been submitted and there is no guarantee it is the actual working solution.
"""

import sys

N = int(input())

class Node:
        def __init__(self, value, next=None, prev=None):
                self.value = value
                self.next = next
                self.prev = prev
        def __str__(self):
                return str(self.value)

# -------------------------------------------------- #

class List:
        def __init__(self):
                self.__head = None
                self.__tail = None
                self.__length = 0

        def __setitem__(self, index, value):
                if type(index) != type(0):
                        raise TypeError
                if index < 0 or index >= self.__length:
                        raise IndexError
                counter = 0
                walker = self.__head
                while counter < index:
                        walker = walker.next
                        counter += 1
                walker.value = value

        def __getitem__(self, index):
                if type(index) != type(0):
                        raise TypeError
                if index < 0 or index >= self.__length:
                        raise IndexError
                counter = 0
                walker = self.__head
                while counter < index:
                        walker = walker.next
                        counter += 1
                return walker.value

        def __len__(self):
                return self.__length

        def __str__(self):
                items = []
                walker = self.__head
                while walker:
                        items.append(str(walker.value))
                        walker = walker.next
                return ' '.join(items)

        def insert(self, index, value): # add element at given index
                if type(index) != type(0):
                        raise TypeError
                if index < 0 or index > self.__length:
                        raise IndexError
                node = Node(value)
                if self.__length == 0:
                        self.__head = self.__tail = node
                elif index == 0:
                        node.next = self.__head
                        self.__head.prev = node
                        self.__head = node
                elif index == self.__length:
                        node.prev = self.__tail
                        self.__tail.next = node
                        self.__tail = node
                else:
                        walker = self.__head
                        for i in range(index-1):
                                walker = walker.next
                        node.prev = walker
                        node.next = walker.next
                        walker.next.prev = node
                        walker.next = node
                self.__length += 1

        def remove(self, value):                # remove element and return it (None if not found)
                if self.__head == None:
                        return None
                walker = self.__head
                follower = None
                while walker:
                        if walker.value == value:
                                if self.__length == 1:
                                        self.__head = self.__tail = None
                                elif follower == None:
                                        self.__head = walker.next
                                        self.__head.prev = None
                                elif walker.next == None:
                                        self.__tail = follower
                                        self.__tail.next = None
                                else:
                                        follower.next = walker.next
                                        walker.next.prev = follower
                                self.__length -= 1
                                return value
                        follower = walker
                        walker = walker.next
                return None

        def clear(self):                        # clear list
                self.__head = self.__tail = None
                self.__length = 0

        def push_back(self, value):             # push element to last position
                self.insert(self.__length, value)

        def pop_back(self):                     # pop element from last position and return it (None if list is empty)
                if self.__length == 0:
                        return None
                value = self.__tail.value
                self.__tail = self.__tail.prev
                if self.__tail == None:
                        self.__head = None
                else:
                        self.__tail.next = None
                self.__length -= 1
                return value

        def push_front(self, value):            # push element to first position
                self.insert(0, value)

        def pop_front(self):                            # pop element from first position and return it (None if list is empty)
                if self.__length == 0:
                        return None
                value = self.__head.value
                self.__head = self.__head.next
                if self.__head == None:
                        self.__tail = None
                else:
                        self.__head.prev = None
                self.__length -= 1
                return value

        def first(self):                        # return first element
                if self.__head == None:
                        return None
                return self.__head.value

        def last(self):                         # return last element
                if self.__tail == None:
                        return None
                return self.__tail.value

        def index(self, value):         # return index of first occurence of 'value', -1 if not found
                walker = self.__head
                pos = 0
                while walker:
                        if walker.value == value:
                                return pos
                        walker = walker.next
                        pos += 1
                return -1

        def count(self, value):         # return the number of occurences of 'value'
                walker = self.__head
                counter = 0
                while walker:
                        if walker.value == value:
                                counter += 1
                        walker = walker.next
                return counter

        def isempty(self):
                return not bool(self.__length)

class Queue:
        def __init__(self):
                self.__queue = List()

        def __len__(self):
                return len(self.__queue)

        def __str__(self):
                return str(self.__queue)

        def clear(self):                        # clear queue
                self.__queue.clear()

        def enqueue(self, value):       # enqueue element
                self.__queue.push_front(value)

        def dequeue(self):                      # dequeue element and return it (None if queue is empty)
                return self.__queue.pop_back()

        def front(self):                        # return front element
                return self.__queue.last()

        def isempty(self):
                return self.__queue.isempty()
                
# ----------------------- #

class Pokemon:
        def __init__(self, name, health, attack, defense):
                self.name = name
                self.health = health
                self.attack = attack
                self.defense = defense

myPok = []
for n in range(N):
        pok = input().split()
        pok[1] = float(pok[1])
        pok[2] = float(pok[2])
        pok[3] = float(pok[3])
        myPok.append(Pokemon(pok[0], pok[1], pok[2], pok[3]))
        
hisPok = []
for n in range(N):
        pok = input().split()
        pok[1] = float(pok[1])
        pok[2] = float(pok[2])
        pok[3] = float(pok[3])
        hisPok.append(Pokemon(pok[0], pok[1], pok[2], pok[3]))

# lo stato e' un dizionario che dato un numero ritorna una coppia di pokemon che combattono in posizione i-esima
initial_state = {}
for n in range(N):
        initial_state[n] = [myPok[n], hisPok[n]]
# l'azione e' l'indice del pokemon da mandare in battaglia
action = [k for k in range(N)]

# @param state = lo stato corrente
# @return una lista di azioni possibili
def get_possible_actions(state):
        actions = []
        for k in state:
                if state[k][0] != None and state[k][1] != None:
                        actions.append(k)
        return actions

# @param = lo stato corrente
# @param action = l'azione da eseguire
# @return il nuovo stato
def next_state(state, action):
        myPok = state[action][0]
        hisPok = state[action][1]
        
        myAttack = myPok.attack*(1-hisPok.defense)
        hisAttack = hisPok.attack*(1-myPok.defense)
        
        while myPok.health > 0 and hisPok.health > 0:
                hisPok.health -= myAttack
                if hisPok.health > 0:
                        myPok.health -= hisAttack
        
        if myPok.health > 0:
                i = action
                while (i-1) in state:
                        state[i][1] = state[i-1][1]
                        i -= 1
                state[i][1] = None
        else:
                i = action
                while (i-1) in state:
                        state[i][0] = state[i-1][0]
                        i -= 1
                state[i][0] = None
        return state

# @param state = lo stato corrente
# @return valore booleano che dice se lo stato e' finale
def goal_test(state):
        myPokNone = True
        for k in state:
                if state[k][0] != None:
                        myPokNone = False
                        break
        
        hisPokNone = True
        for k in state:
                if state[k][1] != None:
                        hisPokNone = False
                        break
                
        return myPokNone or hisPokNone

# @param state = lo stato corrente
# @return il costo dello stato
def get_cost(state):
        cost = 0
        for k in state:
                if state[k][0] != None:
                        cost += 1
        return cost



class TreeNode:
        def __init__(self, state, parent, action, cost):
                self.state = state
                self.parent = parent
                self.action = action
                self.cost = cost

def stampa(curr):
        for k in curr:
                if curr[k][0] != None:
                        print(curr[k][0].name, curr[k][0].health)
                else:
                        print("none")
                if curr[k][1] != None:
                        print(curr[k][1].name, curr[k][1].health)
                else:
                        print("none")
        print()

import copy

# @param initial_state = lo stato iniziale
# @return un nodo contenente lo stato finale, il percorso si ottiene facendo backtracking
def tree_search(initial_state):
        root = TreeNode(initial_state, None, None, get_cost(initial_state))
        open_list = Queue()
        open_list.enqueue(root)
        
        solutions = []
        
        while not open_list.isempty():
                curr = open_list.dequeue()
                #stampa(curr.state)
                # qui ritorno il primo risultato buono che trovo
                # si puo' cambiare facendo che per esempio ritorna una lista di stati finali possibili
                if goal_test(curr.state):
                        #print("stato finale")
                        #stampa(curr.state)
                        solutions.append(curr.cost)
                for action in get_possible_actions(curr.state):
                        new_state = next_state(copy.deepcopy(curr.state), action)
                        new_parent = curr
                        new_action = action
                        new_cost = get_cost(new_state)
                        new_node = TreeNode(new_state, new_parent, new_action, new_cost)
                        open_list.enqueue(new_node)
                        
        return max(solutions)
        
ans = tree_search(initial_state)
print(ans)

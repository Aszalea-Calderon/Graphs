"""
Simple graph implementation
"""
from collections import deque

## If you need a quick queue class, make this boi!
class Queue(deque):
    def enqueue(self, value):
        self.append(value)  # this appends adds to the tail
    def dequeue(self):
        return self.popleft()  # this returns what is on the far left and returns it. Popleft is from the import from deque.


class Stack(deque):
    def push(self, value):
        self.append(value)



class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # A set is like a list but it cannot have duplicates.


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("v1 or v2, Not in graph") # Throw kills an excution of a program. in  javascript.


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex. # this takes its time searching more fully. # Que # deque
        #Que takes from the start and adds to the end
        """
        q= Queue()  # this will take all the nodes that we need to visit
        q.enqueue(starting_vertex)
        visited = set()  ## this is going to have all the nodes that we visit  #Set is a list of UNIQUE ELEMENTS
        while len(q) > 0:  # while the queue is NOT empty.
            vertex = q.dequeue()  ## take it off the start.
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)  # For every neighbor in our vertex we will add them to the q.


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex. # this is more eager checking the next thing it is connected to. # Stack
        # This will take from the end and add to the end,
        """
        stack=Stack()
        stack.push(starting_vertex)
        visited = set()
        while len(stack)>0:
            vertex = stack.pop()  ## This will return the top of the stack, this is the last, or top element. The most recently added element.
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if not visited:
            visited= set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex]) # This is holding a collection of lists, the sub-lists hold a collection of vertex
        visited = set()
        while len(q) > 0:
            path = q.dequeue()  ## This will return the first sublist.. or least recently added sublist
            vertex= path[-1]  # this is taking the last node in path.
            if vertex not in visited:  # if we have not visited, as stated before
                if vertex == destination_vertex:  # this be it
                    return path  # yay!
                visited.add(vertex)  # otherwise add the vertex
                for next_vertex in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    q.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while len(stack) > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path= list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if not visited:
            visited = set()
        if not path:
            path = []
        visited.add(starting_vertex)
        path.append(starting_vertex)
        if starting_vertex is destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path= self.dfs_recursive(neighbor,destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''

    print("bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft:")
    graph.dft(1)
    print("dft_recur:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Bfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('dfs')
    print(graph.dfs(1, 6))
    print('dfs_recursion')
    print(graph.dfs_recursive(1, 6))

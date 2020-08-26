"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    # EDGE:  denotes a relationship or linkage between two v's

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # v ==  vertex
        # the v's have to be present in order for there to be an edge
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # make a queue
        # enqueue our starting node
        # make a set ot track if we've been here before

        # while our queue isn't empty

        # dequeue whatever's at the front of our line, this is our current_node

        # if we haven't visited this node yet,
        # mark as visited
        # get its neighbors
        # for each of the neighbors add to the queue

        # import from util
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            # take the vertex out, get it ready
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)

                # ready to append
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # make a stack data structure
        # push on our starting node

        # make a set to track if we've been here before so we dont visit twice
        # while our stack isn't empty

        # pop off whatever's on top, this is current_node
        # if we haven't visited this vertex before, mark as visited
        # get neighbor
        # for each of the neighbors, add to stack

        # s = Stack(1)
        # s = Stack(2)
        # visited = set(1, 2, 4, 7)
        # current_node = 1

        # neighbors = [2]  # push onto stack

        s = Stack()
        s.push(starting_vertex)

        visited = set()
        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)

                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            # add to visited
            visited.add(starting_vertex)
            # debug
            print(starting_vertex)

            for next_vertex in self.get_neighbors(starting_vertex):
                # pass in next_vertex and visited set for traversal history
                self.dft_recursive(next_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        # Create an empty se tto track visited verticies

        # while the queue is not empty:
        # current vertext PATH (dequeue from queue)
        # set the current vertex to the LAST element of the PATH

        # Check if the current vertext has not been visited:
        # CHEK IF THE CURRENT VERTEX IS DESTINATION
        # IF IT IS, STOP AND RETURN

        # Mark the current vertex as visited
        # Add the current vertex to a visited_set

        # Queue up NEW paths with each neighbor:
        # take current path
        # append the neighbor to it
        # queue up new PATH

        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path
                # add to visited if not foudn
                else:
                    visited.add(v)

                for next_v in self.get_neighbors(v):
                    # make copy
                    new_path = path.copy()
                    new_path.append(next_v)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            if v not in visited:
                visited.add(v)

                if v == destination_vertex:
                    return path
                else:
                    for next_vertex in self.get_neighbors(v):
                        new_path = path.copy()
                        new_path.append(next_vertex)
                        s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            # search found
            return path

        for next_vertex in self.get_neighbors(starting_vertex):

            if next_vertex not in visited:

                # recur with new path
                new_path = self.dfs_recursive(
                    next_vertex, destination_vertex, visited, path
                )

                # check for new_path if yes, return it to outer scope
                if new_path:
                    return new_path

        # couldn't find? escape?
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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

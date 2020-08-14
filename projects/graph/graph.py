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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        #Add a directed edge to the graph.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, vertex_id):
        #Get all neighbors (edges) of a vertex.

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        
        #Print each vertex in breadth-first order
        #beginning from starting_vertex.
        
        q = Queue()
        q.enqueue(starting_vertex)
   
        visited = []

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited.append(v)

                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
        for e in visited:
            print(e)
        # print(visited)


    def dft(self, starting_vertex):
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        s = Stack()
        s.push(starting_vertex)

        visited = []

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.append(v)

                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
        for e in visited:
            print(e)
        # print(visited)

    def dft_recursive(self, starting_vertex, visited = set()):
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        # This should be done using recursion.
        if len(visited) == 0:
            visited.add(starting_vertex)
            print(starting_vertex)
        s = self.get_neighbors(starting_vertex)

        while s:
            v = s.pop()
            
            if v not in visited:
                visited.add(v)

                print(v)   
                self.dft_recursive(v, visited)


        

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breath-first order.

        # create an empty queue and enqueue PATH To the Starting Vertex ID
        q = Queue()
        q.enqueue((starting_vertex,))
        # create a set to store visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first PATH
            v = q.dequeue()
            # grab the last vertex from the Path
            cur = v[len(v)-1]

            # is this vertex the target?
            if cur == destination_vertex:
                # return the path
                return v
                
            # check if the vertex has not been visited
            elif cur not in visited:
                # mark it as visited
                visited.add(cur)
                # then add A Path to its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(cur):
                    # make a copy of the path
                    copy = list(v)
                    # append the neighbor to the back of the path
                    copy.append(next_vertex)
                    # enqueue out new path
                    q.enqueue(copy)
 
        return None

       

    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.

                
        s = Stack()
        s.push((starting_vertex,))
        visited = set()

        while s.size() > 0:
            v = s.pop()
            cur = v[len(v)-1]

            if cur == destination_vertex:
                return v
                
            elif cur not in visited:
                visited.add(cur)
                for next_vertex in self.get_neighbors(cur):
                    copy = list(v)
                    copy.append(next_vertex)
                    s.push(copy)
 
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set()):
        if isinstance(starting_vertex, list):
            s = self.get_neighbors(starting_vertex[len(starting_vertex)-1])
            path = starting_vertex
        else:
            s = self.get_neighbors(starting_vertex)
            path = [starting_vertex,]

        while s:
            v = s.pop()

            if v == destination_vertex:
                return [*path, v]
                    
            elif v not in visited and not v == destination_vertex:
                visited.add(v)
                check = self.dfs_recursive([*path,v],destination_vertex, visited)
                if check:
                    return check
            

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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))

class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Vértices iguais %d e %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Vértices removidos %d e %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __len__(self):
        return self.size

    def toString(self,lenght):
        print("   ", end="")
        for i in range(lenght):
            print("   ", end=" ")
            print(i, end="   ")
        print("")
        k=0
        for row in self.adjMatrix:
            print(k,end="")
            k=k+1
            for val in row:
                print("   ", end="")
                print('{:4}'.format(val),end=" ")
            print("")

def main():
    g = Graph(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);

    print("-------------------------- Tamanho do Grafo --------------------------")
    print("                             ",g.__len__());
    print("----------------------------------------------------------------------")
    print("------------------- Imprimindo Matriz de Adjacência ------------------")
    g.toString(g.__len__())
    print("----------------------------------------------------------------------")
    
if __name__ == '__main__':
    main()

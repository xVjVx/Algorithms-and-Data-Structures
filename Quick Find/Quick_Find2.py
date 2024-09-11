class UnionFind:
    def _init_(self,size):
        self.vetor = [0] * size
        for i in range(size):
            self.vetor[i] == i 

    def count(self):
        count = 0
        for i in range(len(self.vetor)):
            if self.vetor[i] == i:
                count +=1
        return count

    def find (self,site):
        return self.vetor[site]        

    def connected (self,site1,site2):
        return self.find(site1) == self.find(site2)

    def union(self,site1,site2):
        root1 = self.find(site1)
        root2 = self.find(site2)
        if root1 == root2:
            return 
        self.vetor[root1] = root2
        print(self.vetor)

def main():
    size = int(input("size: "))
    uf = UnionFind(size)
    nTest = int(input("numero de testes: "))
    while (nTest>0):
        site1 = int(input("site1: "))
        site2 = int(input("site2: "))
        print(uf.find(site1))
        print(uf.connected(site1, site2))
        uf.union(site1, site2)
        print(uf.connected(site1, site2))
        print(uf.count())
        nTest-=1
        
if __name__ == "_main_":
    main()
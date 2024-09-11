class WheightedQuickUnion:
    def __init__(self, size):
        self.id = []
        for i in range(size):
            self.id.append(i)
        self.component_size = [1] * size

    def count(self):
        return len(set(self.id))
    
    def find(self, site):
        while site != self.id[site]:
            site = self.id[site]
        return site
    
    def connected(self, site1, site2):
        if self.find(site1) == self.find(site2):
            return True
        return False
        
    def union(self, site1, site2):
        root_site1 = self.find(site1)
        root_site2 = self.find(site2)

        if root_site1 == root_site2:
            return
        
        if self.component_size[root_site1] < self.component_size[root_site2]:
            self.id[root_site1] = root_site2
            self.component_size[root_site2] += self.component_size[root_site1]
        else:
            self.id[root_site2] = root_site1
            self.component_size[root_site1] += self.component_size[root_site2]

def main():
    size = int(input())
    uf = WheightedQuickUnion(size)
    nTest = int(input())

    while (nTest>0):
        site1 = int(input())
        site2 = int(input())
        print(uf.find(site1))
        print(uf.connected(site1, site2))
        uf.union(site1, site2)
        print(uf.connected(site1, site2))
        print(uf.count())
        nTest-=1

if __name__ == '__main__':
    main()
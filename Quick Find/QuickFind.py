class QuickFind:
    def __init__(self, size):
        self.id = []
        for i in range(size):
            self.id.append(i)

    def count(self):
        return len(set(self.id))
    
    def find(self, site):
        return self.id[site]
    
    def connected(self, site1, site2):
        if self.id[site1] == self.id[site2]:
            return True
        return False
        
    def union(self, site1, site2):
        site1_id = self.id[site1]
        site2_id = self.id[site2]
        
        for i in range(len(self.id)):
            if self.id[i] == site1_id:
                self.id[i] = site2_id

def main():

    size = int(input())
    qf = QuickFind(size)
    nTest = int(input())

    while (nTest > 0):
        site1 = int(input())
        site2 = int(input())
        print(qf.find(site1))
        print(qf.connected(site1, site2))
        qf.union(site1, site2)
        print(qf.connected(site1, site2))
        print(qf.count())
        nTest-=1

if __name__ == '__main__':
    main()
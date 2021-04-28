from collections import defaultdict
N = 3 
trust = [[1,3],[2,3]]

def findJudge(n, trust):
        graph = defaultdict(list)
        new = defaultdict(list)

        for i in range(len(trust)):

            # graph is dictionary of peoples who trust judge 
            graph[trust[i][1]].append(trust[i][0])
            # new is dictionary of peoples trusted by judge (i.e. it should be 0)
            new[trust[i][0]].append(trust[i][1])


        for i in range(1,n+1):
            if len(graph[i]) == n-1 and len(new[i]) == 0:
                return i
        return -1

print(findJudge(N, trust))
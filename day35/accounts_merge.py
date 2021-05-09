from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False]*len(accounts)
        graph = defaultdict(list)
        res = []

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                graph[email].append(i)

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for edge in graph[email]:
                    dfs(edge, emails)

        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(id):
            res = imp[id]
            for k in sub[id]:
                res += dfs(k)
            return res

        imp = {}
        sub = {}

        for employee in employees:
            imp[employee.id] = employee.importance
            sub[employee.id] = employee.subordinates
        return dfs(id)

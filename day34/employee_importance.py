
def getimp(emp, id):
    return emp[id][0] + sum([getimp(emp, x) for x in emp[id][1]])


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {}
        for e in employees:
            emp[e.id] = [e.importance, e.subordinates]
        # print(emp)
        return getimp(emp, id)

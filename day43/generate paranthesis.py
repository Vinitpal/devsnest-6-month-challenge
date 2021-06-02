class Solution:
    def generateParenthesis(self, n: int):
        final = []
        
        # op - opening, cl - closing
        def solve(ans, op, cl):
            if op == 0 and cl == 0:
                final.append(ans)
                return
        
            if op == cl:
                solve(ans + "(", op-1, cl)
                print(op, cl, ans)
            elif op < cl and op > 0:
                solve(ans + "(", op-1, cl)
                solve(ans + ")", op, cl-1)
            else:
                solve(ans + ")", op, cl-1)
            
        solve("", n, n)
        return final
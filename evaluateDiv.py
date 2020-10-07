class Solution:
    from collections import defaultdict
    def calcEquation(self,equations,values,queries):
        from collections import defaultdict

        lookup = defaultdict(dict)

        for [n,d], v in list(zip(equations,values)):
            lookup[n][d]=v
            lookup[d][n]=1/v


        def dfs(query):
            src, dest = query

            if not src in lookup:
                return -1

            stack, visited = [(src,1)], set()

            while stack:
                curr, m = stack.pop()
                visited.add(curr)

                if curr==dest:
                    return m

                for nxt, _m in lookup[curr].items():
                    if nxt not in visited:
                        stack.append((nxt, m*_m))
            return -1

        return list(map(dfs,queries))



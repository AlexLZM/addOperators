def addOperators(self, num: str, target: int) -> List[str]:
    n = len(num)
    def dfs(l, expr, cur, last_add, res):
        '''
        l : digits used so far
        expr: current expression string
        cur: current expression value
        last_add: last 'equivalent' added value to reverse one operateion
        res: list for valid strings
        '''
        if l == n:
            if cur == target:
                res.append(expr)
            return
        for i in range(l + 1, n + 1):
            if i == l + 1 or num[l] != "0": # prevent new digit start with 0
                s, x = num[l:i], int(num[l:i]) # string to add, value to update
                if last_add == None: # get first operand
                    dfs(i, s, x, x, res)

                else: # update new string expresion and new value
                    dfs(i, expr+"+"+s, cur + x, x, res)
                    dfs(i, expr+"-"+s, cur - x, -x, res)

                    # handle '*' operation, example: add '*3' to '1+2'
                    original = cur - last_add # reverse one operation '1+2' -> '1'
                    new_add = last_add * x   # new value to add: '2*3'
                    new_value = original + new_add # '1+2*3'
                    dfs(i, expr+"*"+s, new_value, new_add, res)

    res = []
    dfs(0, '', 0, None, res)
    return res

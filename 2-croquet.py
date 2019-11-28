def openOrSenior(data):
    result = []
    for par, age in data:
        state = ('Open', 'Senior')[par > 54 and age > 7]
        result.append(state)
    return result


print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))

assert openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]) == ['Open', 'Senior', 'Open', 'Senior']
assert openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]) == ['Open', 'Open', 'Senior', 'Open']
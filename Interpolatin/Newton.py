class Newton:
    pointsX = []
    pointsY = []

    def __init__(self, x, y):
        self.pointsX = x
        self.pointsY = y

    def get_brackets(self):
        brackets = []
        brackets.append(self.pointsY)
        for i in range(0, len(self.pointsX) - 1):
            current_bracket = []
            for k in range(0, i+1):
                current_bracket.insert(k, 0)
            for j in range(i+1, len(self.pointsX)):
                previous_bracket = brackets[i]
                value = (previous_bracket[j] - previous_bracket[j - 1]) / (self.pointsX[j] - self.pointsX[j - i - 1])
                current_bracket.insert(j, value)
            brackets.insert(len(brackets), current_bracket)
        return brackets

    def get_function(self):
        fn = ""
        term = ""
        brackets = self.get_brackets()

        for i in range(0, len(brackets)):
            term = ""
            for j in range(0, i):
                term += "(x - " + str(self.pointsX[j]) + ")" + " * "
            term += str(brackets[i][i])
            fn += term
            if i != len(brackets) - 1:
                fn += " + "
        return fn


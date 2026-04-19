class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        operandos = [] #length 2
        result = 0
        for i in range(0, len(tokens)):
            char= tokens[i]
            if char in operators:
                a = operandos.pop();
                b = operandos.pop(); 
                match char: 
                    case "+":
                        result = a + b;
                    case "-":
                        result = b - a;
                    case "*":
                        result = a * b;
                    case "/": 
                        result = math.trunc(b / a)
                operandos.append(result);
            else:
                if len(operandos) == 0:
                    result = int(char) 
                operandos.append(int(char))
        return int(result);
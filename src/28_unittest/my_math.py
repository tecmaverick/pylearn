class MyMath:
    def add(self, fno: int, sno: int) -> int:
        return fno + sno

    def substract(self, fno:int, sno:int) -> int:
        return fno - sno

    def multiply(self, fno: int, sno: int) -> int:
        return fno * sno

    def divide(self, fno: int, sno: int) -> int:
        if sno == 0:
            raise ZeroDivisionError()

        return fno / sno

    def demo(self) -> None:
        supported_operators = {"+": self.add,
                               "-": self.substract,
                               "*": self.multiply,
                               "/": self.divide}

        provided_operator = None
        operand1 = None
        operand2 = None
        result = None

        value:str = input("enter the expression to evaluate (Example: 2*2)")

        for char in value:
            if char in supported_operators.keys():
                provided_operator = char
                operands = value.split(char)
                if len(operands) == 2:
                    operand1 = int(operands[0].strip()) if operands[0].strip().isnumeric() else None
                    operand2 = int(operands[1].strip()) if operands[1].strip().isnumeric() else None

                break

        if provided_operator is not None and \
                operand1 is not None and \
                operand2 is not None:

            ops = supported_operators[provided_operator]
            result = ops(operand1, operand2)

        print(f"result is {result}")



#
# m = MyMath()
# result = m.demo()
# print(result)
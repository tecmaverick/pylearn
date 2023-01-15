class MyMatrix:
    def __init__(self, matrix):
        if type(matrix) != list:
            raise Exception("Matrix must be lst list")

        self.__matrix = matrix

    def get_metrix(self):
        return self.__matrix

    def __add__(self, matrixObj):
        if type(matrixObj) != MyMatrix:
            raise Exception("Matrix must be lst list")

        matrix1 = self.get_metrix()
        matrix2 = matrixObj.get_metrix()

        result = []

        # Rows
        for rowIndex in range(len(matrix1)):
            tempList = []
            # Columns
            for colIndex in range(len(matrix1[rowIndex])):
                firstMatrixVal = matrix1[rowIndex][colIndex]
                secondMatrixVal = matrix2[rowIndex][colIndex]
                tempList.append(firstMatrixVal + secondMatrixVal)

            result.append(tempList)

        return result


mx1 = [[4, 8], [3, 7]]
mx2 = [[1, 0], [5, 2]]

m1 = MyMatrix(mx1)
m2 = MyMatrix(mx2)

mx3 = m1 + m2
print(mx3)

def diagonalDifference(arr):
    # Write your code here
    firstDifference = []
    secondDifference = []

    def getDiagonal(inicio, difference):
        inicio = inicio
        for i in range(len(arr)):
            if inicio >= 0:
                difference.append(arr[i][inicio])
                print(inicio)
                inicio+= 1
            else:
                difference.append(arr[i][inicio])
                inicio-= 1

        return difference

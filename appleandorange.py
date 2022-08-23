def countApplesAndOranges(s, t, a, b, apples, oranges):
    resultApples = []
    resultOranges = []
    totalApples = 0
    totalOranges = 0
    def functionDrop(fruits, rang, result):
        for i in fruits:
            #print("i:",i,"rang:",rang)
            result.append(i+rang)
        return result

    resultApples = functionDrop(apples, a, resultApples)
    resultOranges = functionDrop(oranges, b, resultOranges)
    
    def functionResult(fruit, resultFruit):
        for i in fruit:
            if s <= i <= t:
                resultFruit= resultFruit+1

        return resultFruit
        
    print(functionResult(resultApples, totalApples))
    print(functionResult(resultOranges, totalOranges))

            

def bonAppetit(bill, k, b):
    nums = 0
    for i in range(len(bill)):
        if i != k:
            nums += bill[i]
                        
    if nums // 2 == b:
        print("Bon Appetit")
    else:
        print(b - (nums//2))
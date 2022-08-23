def hurdleRace(k, height):
    
    result = 0
    maximum = max(height)
    
    if maximum - k < 0:
        result = 0
    else:
        result = maximum - k
    return result
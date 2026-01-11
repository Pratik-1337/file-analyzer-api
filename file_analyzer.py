def analyze_file(filename):

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"

    sum = 0
    count = 0
    product = 1
    min_val = None
    max_val = None

    for line in lines:
        try:
            number = int(line.strip())
            sum = sum + number
            count = count + 1
            product = product*number

            if min_val == None or min_val>number:
                min_val = number
            
            if max_val == None or max_val<number:
                max_val = number
        except ValueError:
            pass

    if count == 0:
        return None
    
    average = sum/count
    return {
    "count": count,
    "average": average,
    "min": min_val,
    "max": max_val,
    "product": product,
            }

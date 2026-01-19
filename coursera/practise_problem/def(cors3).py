def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:   # ✅ loop until start reaches stop
            return_string += str(start)   # ✅ add current number
            if start > stop:
                return_string += ","      # ✅ add comma if not last
            start -= 1                    # ✅ decrement
    else:
        return_string = "Counting up: "
        while start <= stop:   # ✅ loop until start reaches stop
            return_string += str(start)   # ✅ add current number
            if start < stop:
                return_string += ","      # ✅ add comma if not last
            start += 1                    # ✅ increment
    return return_string


print(counter(1, 10))  # "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))   # "Counting down: 2,1"
print(counter(5, 5))   # "Counting up: 5"

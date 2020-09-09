def berechnen(cash):
    ergTen = 0
    mod5 = cash%5 
    if mod5 == 0:
        ergFive = int(cash/5)
        return {
                "two": 0,
                "five": ergFive,
                "ten": ergTen
                } 
    elif mod5 != 0:
        rest = mod5
        ergFive = int(cash/5)
        if rest%2 == 0:
            ergTwo = int(rest/2)
            return{
                "two":ergTwo, 
                "five":ergFive,
                "ten":ergTen
            }
        else:
            if ergFive > 1:
                new_ergFive = ergFive-1               
                rest = mod5 + (ergFive-new_ergFive)*5
                if rest%2 == 0:
                    ergTwo = int(rest/2)
                    return{
                    "two":ergTwo, 
                    "five":new_ergFive,
                    "ten": ergTen
                    }    

# change 2 
def OptimizationOne(b):
    value_two = b["two"]
    value_five = b["five"]
    value_ten = b["ten"]
    while value_two >= 5:
        value_two -= 5
        value_ten += 1
    return {
            "two": value_two, 
            "five": value_five,
            "ten": value_ten
            }
        

def OptimizationTwo(b):
    value_two = b["two"]
    value_five = b["five"]
    value_ten = b["ten"]
    while value_five >= 2:
        value_five -= 2
        value_ten += + 1
    return {
        "two": value_two, 
        "five": value_five,
        "ten": value_ten
        }

print(OptimizationTwo(OptimizationOne(berechnen(4))))               



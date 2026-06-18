def get_starting_number():
    num="-"
    while not num.isnumeric() or int(num)<1:
        num=input("How many bottles of beer on the wall?")
    if num.isnumeric():
        return int(num)

def sing(number):
    for i in range(number):
        if number==1:
            print(f"{number} bottle of beer on the wall, {number} bottle of beer.")
        else:
            print(f"{number} bottles of beer on the wall, {number} bottles of beer.")
        number-=1
        i+=1
        if number==0:
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        elif number==1:
            print(f"Take one down, pass it around, {number} bottle of beer on the wall.")    
        else:
            print(f"Take one down, pass it around, {number} bottles of beer on the wall.")    
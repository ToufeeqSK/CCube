#Pattern Recogniser:
def find_pattern(string):
    length= len(string)
    
    # Iterate over all possible patterns
    for i in range(1, length // 2 + 1):
        pattern = string[:i]
        repeats = length // i
        if pattern * repeats == string:
            print("Pattern Found")
            print("Pattern:", pattern)
            print("Repeats:", repeats)
            return
    
    print("Pattern Not Found")

# Test the function
input_string = input("Enter a string: ").split(",")
find_pattern(input_string)


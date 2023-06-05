#Pattern Recogniser:
'''num_list_1=[]
num_list_2=[]
length=num_list_2
n=int(input("Enter the range of the list:"))
for i in range(n):
    p=int(input())
    num_list_1.append(p)
print("The list:",num_list_1)
for j in num_list_1:
     if j not in num_list_2:
        num_list_2.append(j)
     for i in range(1, length // 2 + 1):
        pattern = num_list_2[:i]
        repeats = length // i
        if pattern * repeats == num_list_1:
            print("Pattern Found")
            print("Pattern:", pattern)
            print("Repeats:", repeats)
'''
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


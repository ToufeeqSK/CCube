#Color Classifier
print("Enter the value for classifying the color")
red_color_value=int(input("Enter any integer value for red: "))
blue_color_value=int(input("Enter any integer value for blue: "))
green_color_value=int(input("Enter any integer value for green: "))
if(red_color_value>blue_color_value and red_color_value>green_color_value):
    print("The color category: Red")
elif(blue_color_value>red_color_value and blue_color_value>green_color_value):
    print("The color category: Blue")
else:
    print("The color category: Green")


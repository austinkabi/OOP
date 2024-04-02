string_input=input("Enter a string:  ")
string_input=string_input.replace("","").lower()
reversed_string=string_input[::-1]
if reversed_string==string_input:
    print("The string is palindrome")
else:
    print("The string is NOT palindrome")

 
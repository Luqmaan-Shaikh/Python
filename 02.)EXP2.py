str1 = input("Enter Str1: ")
str2 = input("Enter Str2: ")
# Concatinating 2 Strings
str3 = str1 + str2

print(str3)

# String Slicing

print(f"From 0th index: {str3[0:]}")
print(f"To 5-1th index: {str3[:5]}")
print(f"From 5th index: {str3[5:]}")
print(f"From 0th index in interval of 2 (Alternate letters): {str3[0: : 2]}")

# Reversing String

print(f"Reversed String: {str3[::-1]}")

print(f"To Upper: {str3.upper()}")
print(f"Is upper: {str3.isupper()}")
print(f"To lower: {str3.lower()}")
print(f"Is lower: {str3.islower()}")
print(f"First Letter: {str3.title()}")
print(f"Swap Cases of Letter: {str3.swapcase()}")
print(f"Max alphabet: {max(str3)}")
print(f"Length of String: {len(str3)}")

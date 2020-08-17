user_input_string_1 = input("Enter a String: ")
print(user_input_string_1)
upper_case_count = 0
lower_case_count = 0
i = 0
while i < len(user_input_string_1):
    if user_input_string_1[i].isupper() == True:
        upper_case_count = upper_case_count + 1
        #print("Upper Count Incremented")
    if user_input_string_1[i].islower() == True:
        lower_case_count = lower_case_count + 1
        #print("Lower Count Incremented")
    i = i + 1
print("UpperCase: ", upper_case_count)
print("LowerCase: ", lower_case_count)

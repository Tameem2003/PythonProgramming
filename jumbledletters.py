print("Press 1 to  a encrypt a word")
print("Press 2 to convert an encrypted word ")
choice = int(input("Enter your choice"))
if choice == 1:
    user_input = input("Enter a word")
    str_len = len(user_input)
    for i in range(0,str_len):
        print(chr((ord(user_input[i]))+1))
elif choice == 2:
    user_input = input("Enter a jumbled word")
    str_len = len(user_input)
    for i in range(0,str_len):
        print(chr((ord(user_input[i]))-1))
else:
    print("Invalid choice")

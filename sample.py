num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
supply_transaction_name="STRX-1456210299"
str_only = supply_transaction_name[0:5]
transaction_number = (supply_transaction_name[5:])
last_4_transaction_number = int(transaction_number)
print(last_4_transaction_number)
last_4_transaction_number = last_4_transaction_number + 1
last_4_transaction_number = str(last_4_transaction_number)
length = len(last_4_transaction_number)
print(length)
if(length==5):
    supply_transaction_name_new = str_only + "00000" + last_4_transaction_number
elif(length==6):
    supply_transaction_name_new = str_only + "0000" + last_4_transaction_number
elif(length==7):
    supply_transaction_name_new = str_only + "000" + last_4_transaction_number
elif (length == 8):
    supply_transaction_name_new = str_only + "00" + last_4_transaction_number
elif(length==9):
    supply_transaction_name_new = str_only + "0" + last_4_transaction_number
elif(length==10):
    supply_transaction_name_new = str_only + last_4_transaction_number
print(supply_transaction_name_new)
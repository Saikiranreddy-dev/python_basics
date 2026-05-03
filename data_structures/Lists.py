# Lists
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months[0])  # January
print(months[2]) 
print(months[-1]) #negitive indexing
print(months[-2])
print(len(months)-1)
print(months[len(months)-1]) #last element
# List slicing
q3=months[6:9] #start index is inclusive and end index is exclusive
print(q3)
first_half=months[:6] #start index is 0 by default
second_half=months[6:] #end index is len(months) by default
print(first_half)
print(second_half)
greetings ='''Hello 

there, how are you?'''
print(len(months))
print(len(greetings)) #length of string

#membership operators [in,not in] which list and strings follow
print("January" in months) #True
print("Jan" in months) #False
print("Jan" not in months) #True
print("Hello" in greetings) #True
print("     " in greetings) #True
print("     " not in greetings) #False

# mutable ordered unordered and immutable
# list can be mutable and ordered but strings are immutable and ordered
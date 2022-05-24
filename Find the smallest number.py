# None ist ein leeres Objekt. Es hat keinen Datentyp!
# Man kann auch None verwenden, um die größte Nummer zu finden
smallest_so_far = None
print('Before:')
for the_num in [9, 41, 12, 3, 74, 5]:
    if smallest_so_far is None: 
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After:' , smallest_so_far)
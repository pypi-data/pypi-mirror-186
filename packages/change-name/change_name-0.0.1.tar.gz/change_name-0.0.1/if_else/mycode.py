def change_name(n):
    
    b   = n[-3:]
    if b == 'ing':
        print(n + 'ly')
    else:
        print(n + 'ing')
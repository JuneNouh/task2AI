lines=1
maxlines=9

while lines<=maxlines:
    # print the leading spaces, the left part and the right side of the tree
    print((maxlines-lines)*' '+ lines*'*'+(lines-1)*'*')
    lines+=1

print('     ########')
    

def print_big(letter):
    alpabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    alpabet = alpabet.split(",")
    book = {}
    for k, v in enumerate(alpabet):
        book[v] = k
    file = open(
        "Letters.txt", "r")
    lines = file.readlines()
    choise = lines[book[letter]*5:book[letter]*5 + 5]
    print(''.join(choise))

print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')
print_big('f')
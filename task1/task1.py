import sys 
n = int(sys.argv[1])
m = int(sys.argv[2])
st = 1
while True:
    print(st, end='')
    st = 1+(st+m-2)%n
    if st == 1:
        break
print()

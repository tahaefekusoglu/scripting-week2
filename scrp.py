A = [['a', 'b', 'c', 'd'],
     ['g', 'h', 'm'],
     ['s', 't', 'm']
     ]

B= ['yahya', 'hamza', 'musa', 'ali']



print(len(A))
print(len(B))

def irem(arr):
    counter = 0
    try:
        while True:
            print(B[counter])
            counter += 1

    except:
        pass
    return counter

def rsi(value):
    if value < 20:
        print('Buy stock-------')
    elif value > 80:
        print('-------Sell stock')
    else:
        print('Hold On')



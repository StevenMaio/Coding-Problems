from random import randint

def rand5():
    return randint(1,5)

'''
    This one does so using a binomail distribution
'''
def rand7_bin():
    r = 1
    for i in range(6):
        r += int(rand5()/3)

    return r

def main():
    result = rand7_bin()

    print('{}'.format(result))

if __name__ == '__main__':
    main()

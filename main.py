def main():
    print('Please enter number:')
    x = input()
    if(x=='21'):
        for i in range(1,21):
            if(int(i)%3==0 and int(i)%5==0):
                 print('fizzbuzz')
            if(int(i)%3==0):
                print('fizz')
            if(int(i)%5==0):
                print('buzz')
            if(int(x)%7==0):
                print('bang')
            else:
                print(i)
    if(x=='35'):
        print('this is easter egg')
        for i in reversed(range(1,35)):
            if(int(i)%3==0 and int(i)%5==0):
                 print('fizzbuzz')
            if(int(i)%3==0):
                print('fizz')
            if(int(i)%5==0):
                print('buzz')
            if(int(x)%7==0):
                print('bang')
            else:
                print(i)
        return
    if(int(x)%3==0 and int(x)%5==0):
        print('fizzbuzz')
    if(int(x)%3==0):
        print('fizz')
    if(int(x)%5==0):
        print('buzz')
    if(int(x)%7==0):
        print('bang')

if __name__ == '__main__':
    main()

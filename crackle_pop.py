if __name__ == "__main__":
    for i in range(1, 100, 1):
        if i % 5 == 0 and i % 3 == 0: 
            print 'CracklePop'
        elif i % 3 == 0:
            print 'Crackle'
        elif i % 5 == 0:
            print 'Pop'
        else:
              print i

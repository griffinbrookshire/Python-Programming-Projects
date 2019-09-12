"Dynamic Programming approach to finding factorials extra quickly. The program 'learns' the factorial of inputs you have already tried by keeping the answers in a table -> trading space for time."

while 1:
    
    print '\n\"q\" to quit, Find factorial of? '
    response = raw_input()
    if response == 'q' :
        exit(1)
    n = int(response)
    
    factTable = {}

    def factorial(n):
        try:
            return factTable[n]
        except KeyError:
            if n == 0:
                factTable[0] = 1
                return 1
            else:
                factTable[n] = n * factorial(n-1)
                return factTable[n]

    print 'The factorial of ', n, ' is ', factorial(n)

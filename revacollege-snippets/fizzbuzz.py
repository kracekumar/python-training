import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
        if number % 15 == 0:
            print "FizzBuzz"
        elif number % 3 == 0:
            print "Fizz"
        elif number % 5 == 0:
            print "Buzz"
        else:
            print number

    else:
        print "python filename.py 23 is the format"

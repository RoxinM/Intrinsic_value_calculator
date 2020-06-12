def getFloat(s):
    while True:
        try:
            x = float(input("Enter "+s+": "))
            if x < 0:
                print("Error: Use a positive whole # or decimal")
                continue
            break
        except KeyboardInterrupt:
            exit(0)
        except:
            print("Error: use a whole # or decimal")
    return x


def getString(s):
    while True:
        try:
            x = input("Enter "+s+": ")
            if type(x) != str:
                print("Error: Input must be string")
                continue
            break
        except KeyboardInterrupt:
            exit(0)
        except:
            print("Error: enter a string")
    return x


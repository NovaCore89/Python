


def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1,var2


def compute(var1,var2):
    go = True
    while go:
        var1,var2 = getInfo()
        try:  
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1,var2,var3)) 
        except ValueError:
            print("You did not provide a numeric value!".format(e))
        except:
            print("Oops, you provided an invalid input. The program will close now.")
 




if __name__ == "__main__":
    getInfo()
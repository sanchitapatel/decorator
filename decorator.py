def decoretor(fun):
    def wrappar():
        print("start")
        fun()
        print("stop")
    return wrappar

@decoretor
def original_fun():
    print("this is write")

original_fun()


import threading
import time

def sqrt(num):
    for n in num:
        time.sleep(0.6)
        print("the sqrt is ",n*n)

def cube(num):
    for n in num:
        time.sleep(0.6)
        print("the cube is ",n*n*n)

ar=[4, 5, 6, 7, 2]

t=time.time()

th1=threading.Thread(target=sqrt, args=(ar, ))
th2=threading.Thread(target=cube, args=(ar, ))
th1.start()
th2.start()
th1.join()
th2.join()
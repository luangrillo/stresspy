import multiprocessing

def threadingPrimes():
    numb=1
    while numb==numb:
        numb+=numb
        if numb > 1:
            for x in range(2, numb):
                if(numb%x)==0:
                    break

if __name__ == "__main__":
    cpuThreads=multiprocessing.cpu_count()
    print("Burning " + str(cpuThreads) + " threads of this machine.\nCtrl+c for exit..")
    for x in range(0, cpuThreads):
        multiprocessing.Process(target=threadingPrimes).start()

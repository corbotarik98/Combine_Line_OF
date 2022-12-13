import os
import time
import threading
import time


def thread_function(timei, line, folder):
    os.system("sed -i -e 's/^/"+timei+"    /' " + folder +
              "/postProcessing/linesample/"+timei+'/'+line)
    os.system('cat '+folder+'/postProcessing/linesample/' +
              timei+'/'+line+' >> '+folder+'/combined/'+line)


def main(folder):
    tim = time.time()

    os.system('ls '+folder+'/postProcessing/linesample > times'+folder)
    #os.system('rm -rf combined')
    os.system('mkdir '+folder+'/combined')

    f = open("times"+folder, "r")
    times_ = f.readlines()

    times = []

    for line in times_:
        times.append(line.strip('\n'))

    times.sort(key=float)
    os.system("rm times"+folder)

    # print(times)

    #mylist = ["a", "b", "a", "c", "c"]
    #mylist = list(dict.fromkeys(mylist))

    os.system('ls '+folder+'/postProcessing/linesample/' +
              times[0]+' > samplines')

    f = open("samplines", "r")
    samplines_ = f.readlines()

    samplines = []

    for line in samplines_:
        samplines.append(line.strip('\n'))

    threads = list()

    n = 0
    for timei in times:
        n += 1
        print(folder+": "+str(100*n/len(times)))
        for index in samplines:

            x = threading.Thread(target=thread_function,
                                 args=(timei, index, folder))
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):

            thread.join()

    print(folder+" time: "+str(time.time()-tim))

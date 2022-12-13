import divider
import combine_multi
import combine_final
from multiprocessing import Process, Queue
import os

n_cores = 2


def joiner(core):
    combine_multi.main(core)


if __name__ == "__main__":

    print("DIVIDING")

    print("================")
    print("================")

    division = divider.main(n_cores)

    cores = division[0]

    queue = Queue()

    print("")
    print("")

    print("COMBINING")

    print("================")
    print("================")

    processes = [Process(target=joiner, args=(cores[x],))
                 for x in range(n_cores)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("")
    print("")

    print("FINAL COMBINING")

    print("================")
    print("================")
    combine_final.main(n_cores)

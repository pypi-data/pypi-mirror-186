
def multiprocess_pool(process_func: callable,
                      args: list,
                      num_parallel: int = 20):
    from multiprocessing import Process
    pool = {i: None for i in range(num_parallel)}

    for arg in args:
        while True:
            search = False
            for i in range(num_parallel):
                if (pool[i] is None) or (not pool[i].is_alive()):
                    pool[i] = Process(target=process_func, args=arg)
                    pool[i].start()
                    search = True
                    break
            if search:
                break

    for i in range(num_parallel):
        if pool[i] is not None:
            pool[i].join()



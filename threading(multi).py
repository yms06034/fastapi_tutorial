from multiprocessing import Process

import multiprocessing as mp
import time

class SubProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
        
    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")
        

# def sub_process(name):
#     print("[sub] start")
#     print(name)
#     cp = mp.current_process()
#     print(f"[sub] pid : {cp.pid}")
#     print("[sub] end")
    
if __name__ == "__main__":
    print("[main] start")
    p = SubProcess(name='balang')
    p.start()
    time.sleep(1)
    # p.join()
    if p.is_alive:
        p.terminate()
    print("[main] end")
    


## 추가 공부
# threading간의 data 처리 (lock)
# process 간의 data 전송 (queue, pipe)
# multiprocessing, multithreading 간의 속도 비교
# 운영체제와 메모리
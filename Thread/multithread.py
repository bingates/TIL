import threading

# th1 -> 0~249
# th2 -> 250~499
def thread_main(li, i):
    for idx in range(offset*i, offset*(i+1)):
        li[idx]*=2

num_elem = 1000
num_thread = 4
offset = num_elem//num_thread

li=[i+1 for i in range(num_elem)]

threads=[]

for i in range(num_thread):
    th=threading.Thread(target=thread_main, args=(li,i))
    threads.append(th)

for th in threads:
    th.start() # 쓰레드를 시작해

for th in threads:
    th.join() # 쓰레드가 모두 돌동안 기다려

print(li)
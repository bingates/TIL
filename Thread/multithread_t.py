import threading

g_count=0

def thread_main():
    global g_count

    # 임계영역 (critical section) : 공유 자원에 접근해서 값을 수정 하려는 코드
    lock.acquire() # 1. mutual exclusion
    for _ in range(100000):
        g_count+=1
    lock.release() # 2. mutual exclusion

threads=[]

# lock 객체 생성
lock=threading.Lock() # 3. mutual exclusion

for _ in range(50):
    threads.append(threading.Thread(target=thread_main))

for th in threads:
    th.start() # 스레드를 시작해

for th in threads:
    th.join() # 스레드가 모두 돌동안 기다려

print('g_count : {}',format(g_count))

# race condition 경쟁조건 => mutual exclusion 상호배제
# 공유 자원(전역변수) 의  여러 스레드가 한번에 접근후 수정 하려 할때 이런 문제가 발생함
# thread safe : 여러 스레드가 한번에 공유 자원에 접근 하더라고 문제가 발생하지 않는다 -> mutual exclusion
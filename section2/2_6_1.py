from multiprocessing import Process, Queue, current_process
import time
import os

"""

Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe
keyword - Queue, pipe, Communication between processes
"""


# 프로세스 통신 구현 queue

# 실행 함수
def worker(identifier, base_num, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(base_num):
        sub_total += 1

    # Produce
    q.put(sub_total)

    print('Process ID: {}, Process Name: {}, ID: {}, Sum: {}'.format(process_id, process_name, identifier, sub_total))
    print('Result: {}'.format(sub_total))


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()

    print("Parent process ID : {}".format(parent_process_id))

    # 프로세스 리스트 선언
    processes = list()

    # 시작 시간
    start_time = time.time()

    # Queue 선언
    q = Queue()

    for i in range(5):
        # 생성
        p = Process(name=str(i), target=worker, args=(i, 1000000, q))

        # 배열에 담기
        processes.append(p)

        # 프로세스 시작
        p.start()

    # Join
    for process in processes:
        process.join()

    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))

    # 종료 플래그
    q.put('exit')

    total = 0

    # 대기
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()

    print('Main-Processing Total Count = {}'.format(total))
    print('Main-Processing Done!')


if __name__ == '__main__':
    main()

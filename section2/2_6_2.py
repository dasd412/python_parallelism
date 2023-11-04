from multiprocessing import Process, Pipe, current_process
import time
import os

"""

Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe
keyword - Queue, pipe, Communication between processes
"""


# 프로세스 통신 구현 Pipe

# 실행 함수
def worker(identifier, base_num, conn):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(base_num):
        sub_total += 1

    # Produce
    conn.send(sub_total)
    conn.close()

    print('Process ID: {}, Process Name: {}, ID: {}, Sum: {}'.format(process_id, process_name, identifier, sub_total))
    print('Result: {}'.format(sub_total))


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()

    print("Parent process ID : {}".format(parent_process_id))

    # 시작 시간
    start_time = time.time()

    # Pipe 선언
    parent_conn, child_conn = Pipe()

    p = Process(name=str(1), target=worker, args=(1, 1000000, child_conn))

    # 프로세스 시작
    p.start()

    # Join
    p.join()

    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))

    print()
    print('Main-Processing Total Count = {}'.format(parent_conn.recv()))  # Consume
    print('Main-Processing Done!')


if __name__ == '__main__':
    main()

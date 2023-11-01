from multiprocessing import Process, current_process
import os
import time
import random

"""

Parallelism with Multiprocessing - multiprocessing(2) - Naming
keyword - Naming, parallel processing

"""


def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name

    result = n * n

    print(f'Process ID: {process_id}, Process Name: {process_name}')
    print(f'Result of {n} square: {result}')


if __name__ == "__main__":
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()

    print(f'Parent process ID: {parent_process_id}')

    # 프로세스 리스트 선언
    processes = []

    # 프로세스 생성 및 실행
    for i in range(1, 10):
        # 생성
        t = Process(name=str(i), target=square, args=(i,)) # 프로세스에 네이밍을 부여하여 식별하기 쉽게 함!

        # 배열에 담기 (join하려고 담음)
        processes.append(t)

        t.start()

    for process in processes:
        process.join()

    print('Main-Processing Done!')

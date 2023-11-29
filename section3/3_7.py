import time
import os
from multiprocessing import current_process, Array, Manager, Process, freeze_support

"""

Concurrency , Cpu Bound , I/O Bound - CPU Bound(2) - Multiprocessing

keyword :CPU Bound

"""


# CPU-Bound Multiprocessing 예제

def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name

    # 프로세스 정보 출력
    print(f"Process ID : {process_id}, Process Name : {process_name}")

    total_list.append(sum(i * i for i in range(number)))


def main():
    numbers = [3_000_000 + x for x in range(30)]
    print(numbers)

    # 프로세스 리스트 선언
    processes = []

    # 프로세스 공유 매니저
    manager = Manager()

    # 프로세스 공유 리스트
    total_list = manager.list()

    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers:
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))

        processes.append(t)

        t.start()

    # Join
    for process in processes:
        process.join()

    print()

    print(f"Total list {total_list}")
    print(f"Sum: {sum(total_list)}")

    print()

    print(f"Duration : {time.time() - start_time} seconds")


if __name__ == '__main__':
    main()

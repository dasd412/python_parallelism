from multiprocessing import Process, current_process
import os

"""

Parallelism with Multiprocessing - multiprocessing(4) - Sharing state
keyword - Memory sharing, array, value
"""


# 프로세스 메모리 공유 예제 (공유 x)

def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print(current_process().name, "data", v)


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()

    # 출력
    print("Parent process ID : {}".format(parent_process_id))

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 메모리 공유 변수
    share_value = 0

    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))

        processes.append(p)

        p.start()

    for p in processes:
        p.join()

    # 최종 프로세스 부모 변수 확인 (공유가 안 되어 있으므로 최종 값 = 0)
    print("Final Data (share_value) : {}".format(share_value))


if __name__ == '__main__':
    main()

from multiprocessing import Process, current_process, Value, Array
import os

"""

Parallelism with Multiprocessing - multiprocessing(4) - Sharing state
keyword - Memory sharing, array, value
"""


# multiprocessing.Value : 프로세스 사이에서 공유할 수 있는 단일 값을 저장하는데 사용
# multiprocessing.Array : 프로세스 사이에서 공유할 수 있는 배열을 저장하는데 사용

# 프로세스 메모리 공유 예제 (공유 o)

def generate_update_number(v: Value):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v.value)


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()

    # 출력
    print("Parent process ID : {}".format(parent_process_id))

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 메모리 공유 변수를 Value로 지정. 이 때, i는 int를 의미. multiprocessing 패키지는 타입을 엄격하게 지정함.
    share_value = Value('i', 0)
    # from multiprocess import shared_memory 사용 가능 (파이썬 3.8 이상)
    # from multiprocess import Manager 사용 가능
    # share_numbers=Array('i', range(10))

    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))

        processes.append(p)

        p.start()

    for p in processes:
        p.join()

    # 최종 프로세스 부모 변수 확인 (공유가 되어 있으므로 최종 값 = 450)
    print("Final Data (share_value) : {}".format(share_value))


if __name__ == '__main__':
    main()

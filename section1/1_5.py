import logging
from concurrent.futures import ThreadPoolExecutor
import time

"""

멀티 스레딩 - ThreadPoolExecutor

keyword : Many Threads, concurrent.futures, ThreadPoolExecutor

"""

"""

그룹 스레드
(1) Python 3.2 이상 표준 라이브러리 사용
(2) concurrent.futures 모듈 사용
(3) with 사용으로 생성 , 소멸 라이플 사이클 관리 용이
(4) 디버깅하기가 난해함
(5) 대기 중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화
"""


# ThreadPoolExecutor를 이용하면, 로우레벨로 구현할 필요 없이 스레드를 편리하게 사용할 수 있다.

def task(name):
    logging.info("Sub-Thread-starting : %s", name)

    result = 0

    for i in range(10001):
        result += i

    logging.info("Sub-Thread %s : finishing result : %d", name, result)

    return result


def main():
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread-end: before creating and running thread")

    # 실행 방법 1 (중복 코드로 무식하게 하는 법)
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    # executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(task, ("First",))
    # task2 = executor.submit(task, ("Second",))
    #
    # # 결괏값이 있을 경우
    # print(task1.result())
    # print(task2.result())

    # 실행 방법 2 (우아한 방법)
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['first', 'second', 'third'])

        # 결과 확인
        print(list(tasks))


if __name__ == '__main__':
    main()

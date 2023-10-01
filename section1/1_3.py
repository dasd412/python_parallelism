"""

멀티 스레딩 - 스레드 기본

키워드 - Threading basic

"""

import logging
import threading
import time


# 스레드 실행 함수
def thread_func(name: str):
    logging.info("Sub-Thread %s : starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s : finishing", name)  # 스레드는 한 번 일을 시작하면, 부모 스레드가 종료되어도 계속해서 일을 수행한다.


# 메인 스레드 영역
if __name__ == "__main__":
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread-start: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))

    logging.info("Main-Thread-start: before running thread")

    # 서브 스레드 시작
    x.start()  # 이 구간부터 메인 스레드, 서브 스레드 모두 실행되는 중

    # 주석 전후 결과 확인
    # x.join()  # 서브 스레드가 종료될 때까지 메인 스레드가 대기한다.

    logging.info("Main-Thread-start: wait for the thread to finish")

    logging.info("Main-Thread-start: all done")

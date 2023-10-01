"""

멀티 스레딩 - Daemon, Join

키워드 - DaemonThread, Join
"""

"""

DaemonThread 

(1). 백그라운드에서 실행
(2). 메인 스레드 종료 시 즉시 종료
(3). 주로 백그라운드 무한 대기 상태로 실행하는 프로그램을 작성할 때 사용 (ex. 서버 또는 JVM 가비지 컬렉, 문서 프로그램 중 자동 저장 기능)
(4). 일반 스레드는 작업 종료 시까지 실행
"""
import logging
import threading
import time


# 스레드 실행 함수
def thread_func(name: str, d):
    logging.info("Sub-Thread %s : starting", name)

    for i in d:
        print(i)

    logging.info("Sub-Thread %s : finishing", name)  # 스레드는 한 번 일을 시작하면, 부모 스레드가 종료되어도 계속해서 일을 수행한다.


# 메인 스레드 영역
if __name__ == "__main__":
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread-start: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)

    logging.info("Main-Thread-start: before running thread")

    # 서브 스레드 시작
    x.start()  # 이 구간부터 메인 스레드, 서브 스레드 모두 실행되는 중
    y.start()

    # DaemonThread 확인. 일반 스레드는 default로 Daemon이 False이다.
    print(x.daemon)

    # DaemonThread 이후 join()을 호출하는 것은 좋지 않다.
    # x.join()
    # y.join()

    # DaemonThread 는 다음 구문 안에서 많이 실행됨.
    # while True:
    #     pass

    logging.info("Main-Thread-start: wait for the thread to finish")

    logging.info("Main-Thread-start: all done")

import concurrent.futures
import logging
import queue
import random
import threading
import time

"""

멀티 스레드 - prod vs cons using Queue
keyword : 생산자 / 소비자 패턴 (Producer / Consumer Pattern)

"""

"""

Producer / Consumer Pattern
(1) 멀티 스레드 디자인 패턴의 정석
(2) 서버 측 프로그래밍의 핵심
(3) 주로 허리 역할

Python Event 객체
(1) Flag 초기값 (0)
(2) set() -> 1 , clear() -> 0, wait() => 1 일때 리턴, 0 일때 대기, isSet() -> 현 플래그 상태 리턴

"""


def producer(queue, event):
    """네트워크 대기 상태라 가정 (서버)"""
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    """응답 받고 소비하는 것으로 가정 or DB 저장"""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())

    logging.info("Consumer received event. Exiting")


if __name__ == '__main__':
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")

    # 큐의 사이즈가 중요 (maxsize가 핵심! 무작정 크게 하는 것도 안 좋음.)
    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # with context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)  # 생산자 스레드
        executor.submit(consumer, pipeline, event)  # 소비자 스레드

        # 생상자 스레드와 소비자 스레드는 pipeline을 활용해서 통신하게 됨.

        # 실행 시간 조정 (with context 바깥으로 하면, 스레드 무한 실행됨)
        time.sleep(0.1)

        logging.info("Main : about to set event")

        # 생산자 스레드와 소비자 스레드 종료
        event.set()

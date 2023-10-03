import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    # 공유 변수 (value)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()  # Lock 객체 생성

    # 변수 업데이트 함수 (함수이므로 스택 영역에 생성됨)
    def update(self, x):
        logging.info("Thread %s: starting update", x)

        # Mutex & Lock 등 동기화가 필요한 지점

        # # Lock 획득 (방법 1)
        # self._lock.acquire()
        # logging.info("Thread %s has lock", x)
        # local_copy = self.value  # 스택 영역에 local_copy 변수 생성
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        #
        # logging.info("Thread %s about to release lock", x)
        #
        # # lock 반환
        # self._lock.release()

        # Lock 획득 (방법 2) - 더 쉬운 방법임.
        with self._lock:
            logging.info("Thread %s has lock", x)

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info("Thread %s about to release lock", x)

        logging.info("Thread %s: finishing update", x)


if __name__ == '__main__':
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")

    store = FakeDataStore()

    logging.info("Testing update. Starting value is %d.", store.value)

    # with Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third', 'Fourth']:
            executor.submit(store.update, n)

    logging.info("Testing update. Ending value is %d.", store.value)

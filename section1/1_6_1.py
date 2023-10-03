import logging
from concurrent.futures import ThreadPoolExecutor
import time

"""

멀티 스레딩 - Lock, Deadlock

keyword : Lock, Deadlock, Race Condition, Thread Synchronization

"""

"""

용어 설명
(1) 세마포어 (Semaphore) : 프로세스 간 공유된 자원에 접근 시 문제 발생 가능성
    -> 한 개의 프로세스만 접근 처리 고안 (경쟁 상태 예방)

(2) 뮤텍스 (Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 -> 경쟁 상태 예방
(3) 락 (Lock) : 상호 배제를 위한 잠금(lock) -> 데이터 경쟁 예방
(4) 데드락 (Deadlock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상태 (교착 상태)
(5) Thread Synchronization (스레드 동기화)을 통해서 안정적으로 동작하게 처리한다. (동기화 메소드, 동기화 블록)
(6) 세마포어와 뮤텍스의 차이점은?
    -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
    -> 뮤택스 개체는 단일 스레드가 리소스 또는 중요 섹선을 소비하게 허용
    -> 세마포어는 리소스에 대한 제한된 수의 동시 액세스를 허용
"""


class FakeDataStore:
    # 공유 변수 (value)
    def __init__(self):
        self.value = 0

    # 변수 업데이트 함수 (함수이므로 스택 영역에 생성됨)
    def update(self, x):
        logging.info("Thread %s: starting update", x)

        # Mutex & Lock 등 동기화가 필요한 지점
        local_copy = self.value  # 스택 영역에 local_copy 변수 생성
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info("Thread %s: finishing update", x)


if __name__ == '__main__':
    # Logging format 설정
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")

    store = FakeDataStore()

    logging.info("Testing update. Starting value is %d.", store.value)

    # with Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    # FakeDataStore의 update()가 동기화가 제대로 안 되있어서 원하는 결괏값이 안나옴.
    logging.info("Testing update. Ending value is %d.", store.value)

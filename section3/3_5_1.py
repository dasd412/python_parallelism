import requests
import concurrent.futures
import threading
import time

"""

Concurrency , Cpu Bound , I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing 

keyword : I/O Bound, requests, threading

"""

# I/O Bound 예제

# 각 스레드에 생성되는 객체 (각 스레드마다 독립적으로 메모리를 할당받는 객체) <- 독립된 네임 스페이스
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


# 실행 함수 1 (다운로드)
def request_site(url):
    # 세션 획득
    session = get_session()

    # 세션 확인
    with session.get(url) as response:
        print(f'session : {session} [Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}')


# 실행 함수 2 (요청)
def request_all_sites(urls):
    # 멀티 스레드 실행
    # 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def main():
    # 테스트 URLS
    urls = ['https://www.jython.org',
            'http://olympus.realpython.org/dice',
            'https://realpython.com'] * 3

    # 실행시간 측정
    start_time = time.time()

    # 실행 (동기 방식)
    request_all_sites(urls)

    # 실행 시간 종료
    duration = time.time() - start_time

    print()
    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds")
    # Downloaded 9 sites in 1.1982369422912598 seconds


if __name__ == "__main__":
    main()

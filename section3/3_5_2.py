import requests
import multiprocessing
import time

"""

Concurrency , Cpu Bound , I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing 

keyword : I/O Bound, requests, multiprocessing

"""

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행할 때마다 객체 생성은 멀티 프로세스에서 특히 안 좋음
session = None


def set_global_session():
    global session
    if not session:
        session=requests.Session()


# 실행 함수 1 (다운로드)
def request_site(url):
    # 세션 확인
    with session.get(url) as response:
        name=multiprocessing.current_process().name
        print(
            f'name : {name} session : {session} [Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}')


# 실행 함수 2 (요청)
def request_all_sites(urls):
    # 멀티 프로세스 실행
    # 반드시 processes 개수 조절 후 session 객체 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


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
    # Downloaded 9 sites in 1.8933489322662354 seconds


if __name__ == "__main__":
    main()

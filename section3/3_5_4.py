import aiohttp
import asyncio
import time

"""

Concurrency , Cpu Bound , I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing 

keyword : I/O Bound, asyncio

"""


# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 -> async, await 신경써야 함.

# 실행 함수 1 (다운로드)
async def request_site(session, url):
    print(session)
    async with session.get(url) as response:
        print(f'Read {response.content_length} from {url}')


# 실행 함수 2 (요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        print(*tasks)
        print(tasks)

    await asyncio.gather(*tasks, return_exceptions=True)


def main():
    # 테스트 URLS
    urls = ['https://www.jython.org',
            'http://olympus.realpython.org/dice',
            'https://realpython.com'] * 3

    # 실행시간 측정
    start_time = time.time()

    # 실행
    asyncio.run(request_all_sites(urls))

    # 실행 시간 종료
    duration = time.time() - start_time

    print()
    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds")
    # Downloaded 9 sites in 0.0010228157043457031 seconds


if __name__ == "__main__":
    main()

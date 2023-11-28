import time
import asyncio

"""

Concurrency , Cpu Bound , I/O Bound - I/O Bound(2) - Asyncio basic

keyword : asyncio

"""

"""
동시 프로그래밍 패러다임 변화

싱글 코어인 경우 처리향상 미미, 저하 -> 해결책으로 비동기 프로그래밍 등장 -> CPU 연산, DB 연동, API 호출 대기 시간동안 다른 일을 할 수 있게 함.

파이썬 3.4 -> 비동기 (asyncio) 표준 라이브러리 등장

"""


async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print('{} : Calculate {} -> {}'.format(name, i, i * i))
        await asyncio.sleep(1)  # time.sleep()은 동기 메서드임.
    print(f'{name} - {n} : Done')


async def process_async():
    start = time.time()

    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('Two', 2),
        exe_calculate_async('Three', 1)
    ])

    end = time.time()

    print('>>> total execute time : {:.2f}'.format(end - start))


def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print('{} : Calculate {} -> {}'.format(name, i, i * i))
        time.sleep(1)
    print(f'{name} - {n} : Done')


def process_sync():
    start = time.time()

    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)

    end = time.time()

    print('>>> total execute time : {:.2f}'.format(end - start))


if __name__ == '__main__':
    # Sync 실행
    # process_sync()

    # Async 실행
    # 파이썬 3.7 이상
    asyncio.run(process_async())

"""

Parallelism with Multiprocessing - multiprocessing(3) - Process Pool Executor
keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS = ['http://www.daum.net', 'http://www.cnn.com', 'http://naver.com', 'http://ruliweb.com', 'http://python.org',
        'https://www.google.com']


# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    # 프로세스 풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드(실행x)
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        # 실행
        for future in as_completed(future_to_url):
            # Key 값이 Future 객체, Value 값이 URL
            url = future_to_url[future]

            try:
                # 결과
                data = future.result()

            except Exception as exc:
                # 예외 처리
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == '__main__':
    main()

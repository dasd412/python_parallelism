from multiprocessing import Process
import time
import logging

"""

Parallelism with Multiprocessing - multiprocessing(1) - Join , is_alive
keyword - multiprocessing, processing state

"""


def proc_func(name):
    print('Sub-process name start : {}'.format(name))
    time.sleep(3)
    print('Sub-process name end : {}'.format(name))


def main():
    format_str = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")

    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))

    logging.info("Main-Process: before Process start")

    # 프로세스 시작
    p.start()

    logging.info("Main-Process: during Process")

    # # 프로세스 강제 종료시키기
    # logging.info("Main-Process : terminated process")
    # p.terminate()

    logging.info("Main-Process : Joined Process")
    p.join()

    # 프로세스 상태 확인
    logging.info("Main-Process : Sub-Process status : {}".format(p.is_alive()))


if __name__ == "__main__":
    main()

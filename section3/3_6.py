import time

"""

Concurrency , Cpu Bound , I/O Bound - CPU Bound(1) - Synchronous

keyword :CPU Bound

"""


# CPU-Bound 예제

def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    result = []

    for number in numbers:
        result.append(cpu_bound(number))

    return result


def main():
    numbers = [3_000_000 + x for x in range(30)]
    print(numbers)

    start_time = time.time()

    total = find_sums(numbers)

    print()

    print(f"Total list {total}")
    print(f"Sum: {sum(total)}")

    print()

    print(f"Duration : {time.time() - start_time} seconds")


if __name__ == '__main__':
    main()

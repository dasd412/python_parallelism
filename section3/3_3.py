"""

Concurrency , Cpu Bound , I/O Bound , Multiprocessing  vs Multithreading vs Async IO

keyword : Cpu Bound, I/O Bound , Async IO

"""

"""

CPU Bound vs I/O Bound 
    
    CPU Bound
    - 프로세스 진행이 CPU 속도에 의해 제한되는 경우 (ex: 행렬 곱, 고속 연산, 파일 압축, 집합 연산 등)
    - CPU 연산 위주 작업
    
    I/O Bound
    - 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해서 병목 (수행 시간)이 결정됨
    - CPU 성능 지표가 수행시간 단축에 크게 영향을 끼치지 않는다.

메모리 바인딩, 캐시 바운딩

작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요하다.

최종 비교

- Multiprocessing : Multiple processes, 고가용성 (CPU) utilization -> CPU Bound -> 10개 부엌, 10명 요리사, 10개 요리
- Multithreading : Single (Multi) process, Multiple threads, OS decides task switching -> Fast I/O Bound -> 1개 부엌, 10명 요리사, 10개 요리
- AsyncIO : Single process, single thread, cooperative multitasking , tasks cooperatively decide switching -> Slow I/O Bound -> 1개 부엌, 1명 요리사, 10개 요리

"""
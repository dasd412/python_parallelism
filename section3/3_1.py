"""

Concurrency , CPU Bound vs I/O Bound - what is Concurrency
keyword - Concurrency

"""

"""

Concurrency(동시성)
- CPU 가용성 극대화를 위해 Parallelism의 단점 및 어려움을 소프트웨어 (구현)레벨에서 해결하기 위한 방법
- 싱글 코어에 멀티 스레드 패턴으로 작업을 처리
- 동시 작업에 있어서 일정량 처리 후 다음 작업으로 제어권을 넘기는 방식
- 즉, 제어권을 주고 받으며 작업을 처리하는 것을 뜻한다. 병렬적은 아니나 유사한 처리 방식이다.

Concurrency (동시성) vs Parallelism (병렬성)

동시성 : 논리적, 소프트웨어 레벨에서 처리, 싱글 코어에서도 충분히 가능, 멀티 코어 역시 실행 가능, 한 개의 작업 공유 처리,
디버깅 매우 어려움, Mutex, DeadLock

병렬성 : 물리적, CPU 코어가 멀티 코어여야 함, 물리적으로 동시 실행, 멀티 코어에서 구현 가능, 주로 별개의 작업 처리할 때 유용, 
디버깅 어려움, OpenMP, MPI, CUDA

"""

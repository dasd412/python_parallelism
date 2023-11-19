"""

Concurrency , CPU Bound vs I/O Bound - Blocking vs Non-Blocking I/O
keyword - Blocking I/O, Non-Blocking I/O, Sync, Async

"""

"""
Blocking I/O vs Non-Blocking I/O

    Blocking I/O
    - 시스템 콜 요청 시 -> I/O 작업 완료까지 응답을 대기함.
    - 제어권 : I/O 작업 -> 커널 소유 -> 응답 전까지 대기(Blocked) -> 다른 작업 수행 불가
    
    Non-Blocking I/O
    - 시스템 콜 요청 시 -> 커널 I/O 작업 완료 여부 상관 없이 즉시 응답
    - 제어권 : I/O 작업 -> 유저 프로세스 -> 다른 작업 수행 가능 (지속) -> 주기적으로 시스템 콜 통해서 I/O 작업 완료 여부 확인


Sync vs Async
    
    Async : I/O 작업 완료 여부에 대한 Notification는 커널 (호출되는 함수) -> 유저 프로세스(호출하는 함수)
    Sync : I/O 작업 완료 여부에 대한 Notification는 유저 프로세스 (호출하는 함수) -> 커널 (호출되는 함수)
"""

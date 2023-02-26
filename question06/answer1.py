n = int(input('탑의 층 수를 입력하세요: '))


def trace_moving_of_hanoi_tower(height: int, from_pillar: int, to_pillar: int, auxiliary_pillar: int) -> str:
    """_summary_

    Args:
        height (int): 층 수
        from_pillar (int): 이동할 원반이 있는 기둥의 번호
        to_pillar (int): 원반이 옮겨질 목적지 기둥의 번호
        auxiliary_pillar (int): 보조 기둥의 번호

    Returns:
        str: _description_
    """
    if height == 1:
        print(f"from {from_pillar} -> to {to_pillar}")
        return ''
    
    # 시작 기둥의 상위 n-1개의 원반을 보조기둥으로 먼저 옮긴다.
    trace_moving_of_hanoi_tower(height-1, from_pillar, auxiliary_pillar, to_pillar)
    
    # 시작 기둥의 마지막 1개의 원반(=가장 밑의 것)을 목적지 기둥으로 옮긴다.
    print(f"from {from_pillar} -> to {to_pillar}")
    
    # 보조기둥의 n-1개의 원반을 목적지 기둥으로 옮긴다.
    trace_moving_of_hanoi_tower(height-1, auxiliary_pillar, to_pillar, from_pillar)

trace_moving_of_hanoi_tower(n, 1, 3, 2)
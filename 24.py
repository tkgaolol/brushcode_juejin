def solution(n: int, a: list) -> list:
    result = []
    songs = a.copy()  # 创建歌单副本，避免修改原列表
    
    while songs:
        # 播放并移除第一首歌
        result.append(songs.pop(0))
        
        # 如果还有歌曲，将第一首移到末尾
        if songs:
            songs.append(songs.pop(0))
            
    return result

if __name__ == '__main__':
    print(solution(n = 5, a = [5, 3, 2, 1, 4]) == [5, 2, 4, 1, 3])
    print(solution(n = 4, a = [4, 1, 3, 2]) == [4, 3, 1, 2])
    print(solution(n = 6, a = [1, 2, 3, 4, 5, 6]) == [1, 3, 5, 2, 6, 4])
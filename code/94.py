def solution(relations: list[list[str]]) -> bool:
    from collections import defaultdict

    # 创建图和访问状态
    graph = defaultdict(list)
    for relation in relations:
        target = relation[0]
        dependencies = relation[1:]
        graph[target].extend(dependencies)

    visited = set()
    visiting = set()

    def dfs(table):
        if table in visiting:  # 检测循环
            return False
        if table in visited:  # 已访问过的表
            return True

        visiting.add(table)
        for neighbor in graph[table]:
            if not dfs(neighbor):
                return False
        visiting.remove(table)
        visited.add(table)
        return True

    # 检查每个表
    for table in list(graph.keys()):  # Convert to list to avoid modifying during iteration
        if not dfs(table):
            return False

    return True


if __name__ == "__main__":
    # Add your test cases here
    print(solution([["A", "B", "C"], ["B", "D"], ["C", "E"], ["D", "A"]]) == False)
    print(solution([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]]) == True)
    print(
        solution(
            [
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I"],
                ["J", "K", "L", "M", "A"],
                ["N", "O", "P", "Q"],
                ["E", "H", "I", "J"],
                ["R", "S", "T", "U"],
                ["V", "W", "X"],
                ["Y", "Z"],
            ]
        )
        == False
    )

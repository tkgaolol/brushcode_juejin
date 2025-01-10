
def solution(nodes, decorations, tree):
    MOD = 998244353
    # 提取礼物信息和边信息
    gifts = tree[0]
    edges = tree[1:]
    # 确保 gifts 数组的长度与节点数一致
    if len(gifts) < nodes:
        gifts.extend([0] * (nodes - len(gifts)))
    # 记录剪边的数组
    cut_edges = [False] * (nodes- 1)
    # 判断连通分块是否只包含一种礼物的函数
    def is_valid_block(cut_edges):
        # 初始化邻接表
        adj = [[] for _ in range(nodes + 1)]
        for i in range(nodes-1):
            if cut_edges[i] == False:
                u, v = edges[i]
                adj_u_set = set(adj[u])
                for w in adj[v]:
                    if w not in adj_u_set:
                        adj[u].append(w)
                        adj_u_set.add(w)
                adj[u].append(v)
                adj_v_set = set(adj[v])
                for w in adj[u]:
                    if w not in adj_v_set:
                        adj[v].append(w)
                        adj_v_set.add(w)
                adj[v].append(u)
                
        for i in range(nodes):
            # print(gifts[i],adj[i+1])
            if gifts[i]!=0:
                for node in adj[i+1]:
                    #print(gifts[node-1],gifts[i])
                    if gifts[node-1]!=gifts[i] and gifts[node-1]!=0:
                        return False
        return True
    count=0
 
    # 深度优先搜索函数
    def dfs(i, cut_count):
        nonlocal count  # 使用 nonlocal 关键字访问外部作用域的 count 变量
        if cut_count > decorations - 1 or i>=nodes-1:
            return 0
        #如果剪掉这条边
        if cut_count == decorations-1:
            #print(i,cut_count)
            if is_valid_block(cut_edges):
                count+=1
            #print (cut_edges,is_valid_block(cut_edges))
            return 0
 
        cut_edges[i]=True
        dfs(i+1,cut_count+1)
        cut_edges[i]=False
        dfs(i+1,cut_count)
        return 0
    
    # 从根节点开始 DFS
    dfs(0,0)
    
    return count % MOD


if __name__ == "__main__":
    #  You can add more test cases here
    testTree1 = [[1,0,0,0,2,3],[1,7],[3,7],[2,1],[3,5],[5,6],[6,4]]
    testTree2 = [[1,0,1,0,2],[1,2],[1,5],[2,4],[3,5]]

    print(solution(7, 3, testTree1) == 3 )
    print(solution(5, 2, testTree2) == 0 )
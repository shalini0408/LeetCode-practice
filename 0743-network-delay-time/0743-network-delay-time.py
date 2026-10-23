class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for node in range(1,n+1):
            graph[node]=[]
        
        for (source,dest,time) in times:
            graph[source].append((dest,time))

        # shortest = {}

        # def dfs(node, time):
        #     # We've already reached this node faster
        #     if node in shortest and time >= shortest[node]:
        #         return

        #     # Best time found for this node
        #     shortest[node] = time

        #     # Explore neighbors
        #     for neighbor, edge_time in graph[node]:
        #         dfs(neighbor, time + edge_time)

        # dfs(k, 0)

        # # Some node couldn't be reached
        # if len(shortest) != n:
        #     return -1

        # # Last node to receive signal
        # return max(shortest.values())

        heap = [(0,k)]
        visited = set()
        max_time =0
        while heap:
            time,node = heapq.heappop(heap)
            if node in visited:
                continue 
            visited.add(node)
            max_time = time

            for neighbor, edge_time in graph[node]:
                heappush(heap, (time + edge_time, neighbor))
        
        if len(visited)!=n:
            return -1
        return max_time
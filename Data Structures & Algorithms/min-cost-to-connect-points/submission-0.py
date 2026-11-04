import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        graph : Dict[int,List[Tuple[int,int]]] = {i:[] for i in range(n)}

        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                graph[i].append((j,dist))
                graph[j].append((i,dist))
        

        connected = [False] * n
        connected[0] = True
        heap = []
        cnt = n-1
        cost = 0
        
        for vert,dist in graph[0]:
            heapq.heappush(heap,(dist,vert))

        
        while cnt:

            dist,vert = heapq.heappop(heap)

            if connected[vert]:
                continue
            
            connected[vert] = True
            cnt -= 1
            cost += dist

            for v,d in graph[vert]:
                if not connected[v]:
                    heapq.heappush(heap,(d,v))
            

        return cost



        


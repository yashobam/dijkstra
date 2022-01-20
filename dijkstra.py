import heapq
from sqlitedict import SqliteDict
def dijkstra(adj, source, target):
    keys=[]
    for key in adj:
        keys.append(key)
    print(keys)
    INF = ((1<<63) - 1)//2
    pred = { x:x for x in adj }
    dist = { x:INF for x in adj }
    dist[source] = 0
    PQ = []
    heapq.heappush(PQ, [source,dist[source]])

    while(PQ):
        u = heapq.heappop(PQ)  # u is a tuple [u_dist, u_id]
        u_dist = u[1]
        u_id = u[0]
        if u_dist == dist[u_id]:
            #if u_id == target:
            #    break
            print(adj[u_id])
            for v in adj[u_id]:
                print(v in keys)
                if v in keys:
                   v_id = v[0]
                   w_uv = v[1]
                   if dist[u_id] +  w_uv < dist[v_id]:
                       dist[v_id] = dist[u_id] + w_uv
                       heapq.heappush(PQ, [v_id, dist[v_id]])
                       pred[v_id] = u_id
               
    if dist[target]==INF:
        print("There is no path between " + source + " and " + target)
    else:
        st = []
        node = target
        while(True):
            st.append(str(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        print("The shortest path is: " + " ".join(path))
adj=SqliteDict("simplewikitest.sqlite")
'''for i in adj.keys():
    print(str(i))'''
dijkstra(adj,"anarchy","nation")
import math
import sys
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], 
                       max_iterations: int) -> list[tuple[float, float]]:
    #first, we randomly choose k initial centroids
    #then, assign each point to the cluster whose centroid is close via euclidean distance
    #lastly, we then recalculate the centroid of each as the mean of all points assigned to it 
    
    for i in range(max_iterations):
        #first make lists to append to each for each centroid in the list
        cluster_list = []
        for j in range(0,k):
            cluster_list.append([])
            
        #now we loop through the points, check the euclidean distance compared to the centroids, and assign it a sublist
        for point in points:
            # print(f"Doing point {point} on run {i}")
            current_min = sys.maxsize
            current_index = -1
            for index in range(len(initial_centroids)):
                distance = math.dist(point, initial_centroids[index])
                
                if distance < current_min:
                    current_min = distance 
                    current_index = index
            
            #now we assign it
            cluster_list[current_index].append(point) 
            # print(f"Appending the point {point} to the following list: {cluster_list[current_index]}")
            
        #now we can update the centroid of each cluster as the mean of all points assigned to it
        for idx in range(len(initial_centroids)):
            running_sum = tuple(0 for _ in initial_centroids[idx])
            for num in cluster_list[idx]:
                running_sum = tuple(a + b for a, b in zip(running_sum, num))
            
            
            new_tuple = tuple(round(x / len(cluster_list[idx]),4) for x in running_sum) if len(cluster_list[idx]) != 0 else initial_centroids[idx]
            
            initial_centroids[idx] = new_tuple
            
    return initial_centroids
            

print(k_means_clustering([(0, 0, 0), (2, 2, 2), (1, 1, 1), (9, 10, 9), (10, 11, 10), (12, 11, 12)], 2, [(1, 1, 1), (10, 10, 10)], 10))

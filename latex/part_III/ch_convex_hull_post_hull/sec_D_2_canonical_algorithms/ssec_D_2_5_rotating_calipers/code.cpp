int64_t convex_polygon_diameter2(const vector<Point>& hull) {
    int n = hull.size();
    if (n <= 1) return 0;
    if (n == 2) return (hull[1] - hull[0]).norm2();
    
    int64_t max_dist2 = 0;
    int j = 1;
    
    for (int i = 0; i < n; i++) {
        // Advance j to find the furthest point from edge (i, i+1)
        while (true) {
            int next_j = (j + 1) % n;
            Point edge = hull[(i + 1) % n] - hull[i];
            Point to_j = hull[j] - hull[i];
            Point to_next_j = hull[next_j] - hull[i];
            
            // Check if next_j is further from the edge than j
            if ((edge ^ to_next_j) >= (edge ^ to_j)) {
                j = next_j;
            } else {
                break;
            }
        }
        
        // Update maximum distance
        max_dist2 = max(max_dist2, (hull[i] - hull[j]).norm2());
        max_dist2 = max(max_dist2, (hull[(i + 1) % n] - hull[j]).norm2());
    }
    
    return max_dist2;
}
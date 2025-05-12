double convex_polygon_width(const vector<Point>& hull) {
    int n = hull.size();
    if (n <= 2) return 0;
    
    double min_width = 1e18;
    int j = 1;
    
    for (int i = 0; i < n; i++) {
        Point edge = hull[(i + 1) % n] - hull[i];
        double edge_len = edge.norm();
        
        // Find the vertex furthest from edge (i, i+1)
        while (true) {
            int next_j = (j + 1) % n;
            double dist_j = abs((hull[j] - hull[i]) ^ edge) / edge_len;
            double dist_next_j = abs((hull[next_j] - hull[i]) ^ edge) / edge_len;
            
            if (dist_next_j > dist_j) {
                j = next_j;
            } else {
                break;
            }
        }
        
        // Width is the distance from vertex j to edge (i, i+1)
        double width = abs((hull[j] - hull[i]) ^ edge) / edge_len;
        min_width = min(min_width, width);
    }
    
    return min_width;
}
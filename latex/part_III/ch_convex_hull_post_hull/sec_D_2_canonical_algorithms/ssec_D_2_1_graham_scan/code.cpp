vector<Point> graham_scan(vector<Point> points) {
    int n = points.size();
    if (n <= 3) return points;
    
    // Find bottom-most point (and leftmost if tied)
    int bottom = 0;
    for (int i = 1; i < n; i++) {
        if (points[i].y < points[bottom].y || 
           (points[i].y == points[bottom].y && points[i].x < points[bottom].x)) {
            bottom = i;
        }
    }
    swap(points[0], points[bottom]);
    Point pivot = points[0];
    
    // Sort by polar angle with respect to pivot
    sort(points.begin() + 1, points.end(), [&pivot](const Point& a, const Point& b) {
        int64_t cross = (a - pivot) ^ (b - pivot);
        if (cross == 0) {
            // Collinear points: sort by distance
            return (a - pivot).norm2() < (b - pivot).norm2();
        }
        return cross > 0;
    });
    
    // Build hull using stack
    vector<Point> hull;
    hull.push_back(points[0]);
    hull.push_back(points[1]);
    
    for (int i = 2; i < n; i++) {
        while (hull.size() >= 2) {
            Point top = hull.back();
            Point second = hull[hull.size() - 2];
            if (((top - second) ^ (points[i] - second)) <= 0) {
                hull.pop_back();
            } else {
                break;
            }
        }
        hull.push_back(points[i]);
    }
    
    return hull;
}

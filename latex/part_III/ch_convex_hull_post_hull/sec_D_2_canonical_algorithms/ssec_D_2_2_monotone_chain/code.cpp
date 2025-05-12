vector<Point> monotone_chain(vector<Point> points) {
    int n = points.size();
    if (n <= 3) return points;
    
    sort(points.begin(), points.end());
    
    // Build lower hull
    vector<Point> lower;
    for (int i = 0; i < n; i++) {
        while (lower.size() >= 2) {
            int sz = lower.size();
            if (((lower[sz-1] - lower[sz-2]) ^ (points[i] - lower[sz-2])) <= 0) {
                lower.pop_back();
            } else {
                break;
            }
        }
        lower.push_back(points[i]);
    }
    
    // Build upper hull
    vector<Point> upper;
    for (int i = n - 1; i >= 0; i--) {
        while (upper.size() >= 2) {
            int sz = upper.size();
            if (((upper[sz-1] - upper[sz-2]) ^ (points[i] - upper[sz-2])) <= 0) {
                upper.pop_back();
            } else {
                break;
            }
        }
        upper.push_back(points[i]);
    }
    
    // Remove last point of each half because it's repeated
    lower.pop_back();
    upper.pop_back();
    
    // Combine hulls
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}
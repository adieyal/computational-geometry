vector<Point> divide_and_conquer_hull(vector<Point> points) {
    int n = points.size();
    if (n <= 5) {
        // Base case: use Graham scan or brute force for small sets
        return graham_scan(points);
    }
    
    // Sort points by x-coordinate
    sort(points.begin(), points.end());
    
    // Divide
    int mid = n / 2;
    vector<Point> left_points(points.begin(), points.begin() + mid);
    vector<Point> right_points(points.begin() + mid, points.end());
    
    // Conquer
    vector<Point> left_hull = divide_and_conquer_hull(left_points);
    vector<Point> right_hull = divide_and_conquer_hull(right_points);
    
    // Merge - find upper and lower tangent
    return merge_hulls(left_hull, right_hull);
}

vector<Point> merge_hulls(const vector<Point>& left_hull, const vector<Point>& right_hull) {
    int nl = left_hull.size(), nr = right_hull.size();
    if (nl == 0) return right_hull;
    if (nr == 0) return left_hull;
    
    // Find rightmost point of left hull
    int right_l = 0;
    for (int i = 1; i < nl; i++) {
        if (left_hull[i].x > left_hull[right_l].x) right_l = i;
    }
    
    // Find leftmost point of right hull
    int left_r = 0;
    for (int i = 1; i < nr; i++) {
        if (right_hull[i].x < right_hull[left_r].x) left_r = i;
    }
    
    // Find upper tangent
    int upper_l = right_l, upper_r = left_r;
    bool done = false;
    while (!done) {
        done = true;
        while (orientation(right_hull[upper_r], left_hull[upper_l], 
                          left_hull[(upper_l+1)%nl]) >= 0)
            upper_l = (upper_l + 1) % nl;
            
        while (orientation(left_hull[upper_l], right_hull[upper_r], 
                          right_hull[(upper_r-1+nr)%nr]) <= 0) {
            upper_r = (upper_r - 1 + nr) % nr;
            done = false;
        }
    }
    
    // Find lower tangent
    int lower_l = right_l, lower_r = left_r;
    done = false;
    while (!done) {
        done = true;
        while (orientation(left_hull[lower_l], right_hull[lower_r], 
                          right_hull[(lower_r+1)%nr]) >= 0)
            lower_r = (lower_r + 1) % nr;
            
        while (orientation(right_hull[lower_r], left_hull[lower_l], 
                          left_hull[(lower_l-1+nl)%nl]) <= 0) {
            lower_l = (lower_l - 1 + nl) % nl;
            done = false;
        }
    }
    
    // Construct the merged hull
    vector<Point> merged_hull;
    int i = upper_l;
    do {
        merged_hull.push_back(left_hull[i]);
        i = (i + 1) % nl;
    } while (i != lower_l);
    
    i = lower_r;
    do {
        merged_hull.push_back(right_hull[i]);
        i = (i + 1) % nr;
    } while (i != upper_r);
    
    return merged_hull;
}
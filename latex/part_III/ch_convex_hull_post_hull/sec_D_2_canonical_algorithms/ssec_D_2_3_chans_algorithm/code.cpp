vector<Point> chan_algorithm(vector<Point> points) {
    int n = points.size();
    if (n <= 3) return points;
    
    // Try increasing values of m
    for (int m = 3; m <= n; m *= 2) {
        vector<Point> hull = chan_step(points, m);
        if (!hull.empty()) return hull;
    }
    return {};
}

vector<Point> chan_step(vector<Point>& points, int m) {
    int n = points.size();
    vector<vector<Point>> groups;
    
    // Partition into groups of size m
    for (int i = 0; i < n; i += m) {
        vector<Point> group;
        for (int j = i; j < min(i + m, n); j++) {
            group.push_back(points[j]);
        }
        // Compute convex hull of each group
        groups.push_back(monotone_chain(group));
    }
    
    // Gift wrapping on the groups
    Point start = *min_element(points.begin(), points.end(), 
        [](const Point& a, const Point& b) { 
            return a.y < b.y || (a.y == b.y && a.x < b.x); 
        });
    
    vector<Point> hull;
    hull.push_back(start);
    
    Point current = start;
    for (int step = 0; step < m; step++) {
        Point next = groups[0][0];
        
        // Find the next hull point across all groups
        for (const auto& group : groups) {
            Point candidate = find_tangent(current, group);
            if (hull.size() == 1 || 
                ((candidate - current) ^ (next - current)) > 0) {
                next = candidate;
            }
        }
        
        if (next == start) return hull;  // Completed the hull
        hull.push_back(next);
        current = next;
    }
    
    return {};  // Hull has more than m points
}

Point find_tangent(const Point& p, const vector<Point>& hull) {
    int n = hull.size();
    if (n == 1) return hull[0];
    if (n == 2) {
        // Return the more "right" tangent
        return ((hull[0] - p) ^ (hull[1] - p)) < 0 ? hull[0] : hull[1];
    }

    auto is_right_turn = [&](int i, int j) {
        // True if p is to the right of the directed edge hull[i] -> hull[j]
        return ((hull[j] - hull[i]) ^ (p - hull[i])) < 0;
    };

    int low = 0, high = n;
    while (low < high) {
        int mid = (low + high) / 2;
        int prev = (mid - 1 + n) % n;
        int next = (mid + 1) % n;

        bool mid_right = is_right_turn(mid, next);
        bool prev_right = is_right_turn(prev, mid);

        if (!mid_right && prev_right) {
            // Found the tangent
            return hull[mid];
        }
        // If both are right turns, move right
        if (mid_right) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return hull[low % n];
}
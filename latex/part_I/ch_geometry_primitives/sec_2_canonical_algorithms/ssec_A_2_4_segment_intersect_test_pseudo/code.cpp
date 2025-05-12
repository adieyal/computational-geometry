// Assuming PointLL struct and orientation() function are defined
// bool on_segment(PointLL pk, PointLL pi, PointLL pj) from Alg A.2.4

bool on_segment(PointLL pk, PointLL pi, PointLL pj) {
    // Assumes pk, pi, pj are collinear.
    // Check if pk is within the bounding box of pi, pj.
    return (pk.x >= std::min(pi.x, pj.x) && pk.x <= std::max(pi.x, pj.x) &&
            pk.y >= std::min(pi.y, pj.y) && pk.y <= std::max(pi.y, pj.y));
}

bool segments_intersect(PointLL p1, PointLL p2, PointLL p3, PointLL p4) {
    int o1 = orientation(p1, p2, p3);
    int o2 = orientation(p1, p2, p4);
    int o3 = orientation(p3, p4, p1);
    int o4 = orientation(p3, p4, p2);

    // General case
    if (o1 != 0 && o2 != 0 && o3 != 0 && o4 != 0) {
        return (o1 != o2) && (o3 != o4);
    }

    // Special Cases for collinearity / endpoint touching
    if (o1 == 0 && on_segment(p3, p1, p2)) return true;
    if (o2 == 0 && on_segment(p4, p1, p2)) return true;
    if (o3 == 0 && on_segment(p1, p3, p4)) return true;
    if (o4 == 0 && on_segment(p2, p3, p4)) return true;

    return false; // Doesn't fall into any of the above intersection cases
}
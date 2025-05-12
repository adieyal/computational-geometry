// Assuming PointLL struct with long long x, y from ssec:A.5.1
// and a cross product method: p1.cross(p2) = p1.x*p2.y - p1.y*p2.x
#include <iostream> // For PointLL definition if not separate

// struct PointLL { long long x, y; ... PointLL operator-(PointLL o) const { ... } ... };
// long long cross(PointLL a, PointLL b) { return a.x * b.y - a.y * b.x; }
// long long cross(PointLL O, PointLL A, PointLL B) {
//    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
// }

int orientation(PointLL p1, PointLL p2, PointLL p3) {
    // Equivalent to (p2-p1).cross(p3-p1)
    long long val = (p2.x - p1.x) * (p3.y - p1.y) - 
                    (p2.y - p1.y) * (p3.x - p1.x);
    if (val == 0) return 0;  // Collinear
    return (val > 0) ? 1 : -1; // 1 for CCW (Left), -1 for CW (Right)
}
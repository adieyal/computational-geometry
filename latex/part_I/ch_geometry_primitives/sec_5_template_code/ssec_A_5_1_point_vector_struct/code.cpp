#include <cmath>     // For std::sqrt, std::atan2 (for PointD methods)
#include <iostream>  // For operator<< (optional)
#include <algorithm> // For std::min, std::max (for on_segment if included here)

const double PI = std::acos(-1.0); // For angle conversions if needed
const double EPS_DEFAULT = 1e-9;   // Default epsilon for PointD

template <typename T>
struct Point {
    T x, y;

    // Constructors
    Point(T _x = 0, T _y = 0) : x(_x), y(_y) {}

    // Vector operations
    Point operator+(const Point& other) const { return Point(x + other.x, y + other.y); }
    Point operator-(const Point& other) const { return Point(x - other.x, y - other.y); }
    Point operator*(T scalar) const { return Point(x * scalar, y * scalar); }
    // Note: Scalar division might need care for integer T (truncation)
    // Point operator/(T scalar) const { return Point(x / scalar, y / scalar); } // Add if needed

    // Dot and Cross products
    T dot(const Point& other) const { return x * other.x + y * other.y; }
    T cross(const Point& other) const { return x * other.y - y * other.x; }
    // Cross product for three points P, A, B (as P->A x P->B)
    // static T cross(const Point& P, const Point& A, const Point& B) {
    //    return (A - P).cross(B - P);
    // }


    // Magnitude and distance
    T norm_sq() const { return x * x + y * y; } // Squared norm (magnitude squared)
    
    // Methods that might return double even if T is integer
    double norm() const { return std::sqrt(static_cast<double>(norm_sq())); }
    double angle() const { return std::atan2(static_cast<double>(y), static_cast<double>(x)); } // Angle w.r.t positive x-axis

    // Rotation (typically returns Point<double> or needs careful handling for Point<int>)
    // Rotates CCW by 'a' radians around origin.
    Point<double> rotate(double angle_rad) const {
        double s = std::sin(angle_rad);
        double c = std::cos(angle_rad);
        double new_x = static_cast<double>(x) * c - static_cast<double>(y) * s;
        double new_y = static_cast<double>(x) * s + static_cast<double>(y) * c;
        return Point<double>(new_x, new_y);
    }
    // Specific 90-degree rotation (preserves T if T is integer)
    Point rotate90_ccw() const { return Point(-y, x); }
    Point rotate90_cw() const { return Point(y, -x); }

    // Comparison operators
    bool operator<(const Point& other) const { // Lexicographical comparison
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
    bool operator==(const Point& other) const {
        if constexpr (std::is_floating_point_v<T>) {
            return std::abs(x - other.x) < EPS_DEFAULT && std::abs(y - other.y) < EPS_DEFAULT;
        } else {
            return x == other.x && y == other.y;
        }
    }
    bool operator!=(const Point& other) const { return !(*this == other); }

    // Optional: Input/Output
    friend std::istream& operator>>(std::istream& is, Point& p) {
        is >> p.x >> p.y;
        return is;
    }
    friend std::ostream& operator<<(std::ostream& os, const Point& p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }
};

using PointLL = Point<long long>; // Common choice for integer coordinates
using PointD = Point<double>;   // For problems requiring floating point precision

// Example: Orientation function using the Point struct methods
template <typename T>
T orientation_val(const Point<T>& p1, const Point<T>& p2, const Point<T>& p3) {
    return (p2 - p1).cross(p3 - p1);
}

template <typename T>
int orientation_sign(const Point<T>& p1, const Point<T>& p2, const Point<T>& p3) {
    T val = orientation_val(p1, p2, p3);
    if constexpr (std::is_floating_point_v<T>) {
        if (std::abs(val) < EPS_DEFAULT) return 0; // Collinear
    } else {
        if (val == 0) return 0; // Collinear
    }
    return (val > 0) ? 1 : -1; // 1 for CCW, -1 for CW
}
#include <cmath> // For std::abs
#include <algorithm> // For std::max (if using relative EPS)

const double EPS = 1e-9;

// Returns -1 if a < b, 0 if a == b, 1 if a > b
int dcmp(double a, double b) {
    if (std::abs(a - b) < EPS) {
        return 0; // a is "equal" to b
    }
    if (a < b) {
        return -1; // a is less than b
    }
    return 1; // a is greater than b
}

// Usage examples:
// if (dcmp(x, y) == 0) { /* x is approx equal to y */ }
// if (dcmp(x, y) < 0)  { /* x is approx less than y */ }
// if (dcmp(x, y) <= 0) { /* x is approx less than or equal to y */ }
#include <iostream>
#include <math.h>

//using namespace std;

double root(double x, unsigned int n)
{
    // your code goes here
    double lo = 0.0, hi = x;
    double mid = (lo + hi) / 2;
    double x_ = pow(mid, n);
    double efficient = pow(0.001, n);
    while(fabs(x_ - x) > efficient && hi > lo){
        if (x_ - x < - efficient) lo = mid;
        else hi = mid;
        mid = (hi + lo) / 2;
        x_ = pow(mid, n);
    }
    return mid;
}

int main() {
    int x = 3;
    unsigned int n = 2;
    std::cout<< "the "<<n<<"th root of "<<x<<" is "<<root(x, n)<<std::endl;
    return 0;
}

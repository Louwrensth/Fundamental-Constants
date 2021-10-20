#include <cstdio>
#include <math.h>            // Excellent math constants live here
#include <codata_2018.hpp>   // Recommended physical constants since 2018

int main(int argc, const char* argv[])
{
    double electron_mass = codata::electron_mass;
    double PI = M_PI;
    // Double values can have max 15-17 digits of precision (53-bit significand precision)
    // Use G formatting to print as many as needed given the constant's value
    printf("   %10.17G\n", electron_mass);
    printf("   %10.17G\n", PI);
    return 0;
}

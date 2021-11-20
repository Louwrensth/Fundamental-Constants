#include <cstdio>
#include <math.h>            // Excellent math constants live here
#include <codata_2018.hpp>   // Recommended physical constants since 2018

int main(int argc, const char* argv[])
{
    // It is recommended to use your own names for the constants as the CODATA
    // constants have names that are typically long to be descriptive and they
    // sometimes also change in a next publication.
    const double e_mass = codata::electron_mass;
    const double PI = M_PI;
    // Double values can have max ~15.95 digits of precision (53-bit significand precision)
    // Use G formatting to print as many as needed given the constant's value
    printf("   %10.15G\n", e_mass);
    printf("   %10.15G\n", PI);
    return 0;
}

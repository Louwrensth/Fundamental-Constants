#include <stdio.h>
#include <math.h>            // Excellent math constants live here
#include <codata_2018.h>   // Recommended physical constants since 2018

int main(int argc, const char* argv[])
{
    double electron_mass = codata_electron_mass;
    double PI = M_PI;
    // Double values can have max ~15.95 digits of precision (53-bit significand precision)
    // Use G formatting to print as many as needed given the constant's value
    printf("   %10.15G\n", electron_mass);
    printf("   %10.15G\n", PI);
    return 0;
}


# Fundamental Constants

... of physical quantities with the values according to the latest CODATA
recommendation as well as previous recommendations.

Provided as a minimal, zero-dependencies, header-only implementation for use
in any C, C++, or Fortran program.

Sources are generated through Scipy.

Homepage: https://imas.iter.org/
Contact: imas-support@iter.org
Repository: https://git.iter.org/projects/IMAS/repos/fundamental-constants



# Examples

See the examples directory

## C / C++

There are two header values available, one for C/C++ and one for C++ only.

They don't differ very much. The only difference is the C header does not 
use namespaces and the globally defined constants are all prefixed with
`codata_` for clarity and to prevent clashes.

```
#include <stdio.h>
#include <math.h>          // Excellent math constants live here
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
```

## C++ only

If using the `.hpp` header for C++, one uses the `codata` namespace
to access the constant, but the example is otherwise identical to above:

```
#include <cstdio>
#include <math.h>            // Excellent math constants live here
#include <codata_2018.hpp>   // Recommended physical constants since 2018

int main(int argc, const char* argv[])
{
    double electron_mass = codata::electron_mass;
    double PI = M_PI;
    // Double values can have max ~15.95 digits of precision (53-bit significand precision)
    // Use G formatting to print as many as needed given the constant's value
    printf("   %10.15G\n", electron_mass);
    printf("   %10.15G\n", PI);
    return 0;
}
```

## Fortran (2008+)

Because π is not already commonly provide to Fortran via standard library it
is providede here as well for convenience.

The fortran header files are suitable for version 2008 and up because of the use
of `iso_fortran_env` to refer to the defined data type (`real64`).

The constants are found in the `codata` (`mathematical_constants`) module name:

```
include 'mathematical_constants.f90'

include 'codata_2018.f90'

program test_physical_constants
  use codata, only: electron_mass
  use mathematical_constants, only: PI => M_PI
  implicit none

  print *,electron_mass
  print *,PI
  
end program test_physical_constants
```

# Fundamental Constants

Fundamental Constants of Physical Quantities with values according to the
latest CODATA recommendation as well as previous recommendations, are hereby
provided as minimal, zero-dependent, header-only source files for use in any C,
C++, or Fortran program.

Sources are originally generated using SciPy and the results are hardcoded via
a commit. This ensures consistency, provenance, and ease of installation with
dormant dependency on SciPy, until CODATA publishes a new set of recommended
values every four years.

Although hosted as part of IMAS on git.iter.org, this package is expressly not
tied to IMAS and can be freely used anywhere without modification.

Homepage: https://imas.iter.org/ \
Contact: imas-support@iter.org \
Repository: https://git.iter.org/projects/IMAS/repos/fundamental-constants

# Examples

Please see the `examples` directory to find source files of the examples below.

## C / C++

There are two header files available, one for C/C++ and one for C++ only.

They don't differ very much. The only difference is that the C header does not
use namespaces. Instead, the globally defined constants are all prefixed with
`codata_` for clarity and to prevent clashes.

```
#include <stdio.h>
#include <math.h>          // Excellent math constants live here
#include <codata_2022.h>   // Recommended physical constants since 2022

int main(int argc, const char* argv[])
{
    // It is recommended to use your own names for the constants as the CODATA
    // constants have names that are typically long to be descriptive and they
    // sometimes also change in a next publication.
    const double e_mass = codata_electron_mass;
    const double PI = M_PI;
    // Double values can have max ~15.95 digits of precision (53-bit significand precision)
    // Use G formatting to print as many as needed given the constant's value
    printf("   %10.15G\n", e_mass);
    printf("   %10.15G\n", PI);
    return 0;
}
```

## C++ only

If using the `.hpp` header for C++, one uses the `codata` namespace
to access the constant, but the example is otherwise identical to the above:

```
#include <cstdio>
#include <math.h>            // Excellent math constants live here
#include <codata_2022.hpp>   // Recommended physical constants since 2022

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
```

## Fortran (2008+)

The Fortran include files follow the Fortran 2008 standard because of the use
of the `iso_fortran_env` feature providing the kind parameter named `real64`.

Because π is not by default provided to Fortran users via a standard library,
it is provided here for convenience.

The constants are found in the `codata` (`mathematical_constants`) module name:

```
include 'mathematical_constants.f90'  ! Excellent math constant lives here
include 'codata_2022.f90'      ! Recommended physical constants since 2022

program test_physical_constants
  ! It is recommended to use your own names for the constants as the CODATA
  ! constants have names that are typically long to be descriptive and they
  ! sometimes also change in a next publication.
  use codata, only: e_mass => electron_mass
  use mathematical_constants, only: PI => M_PI
  implicit none

  print *,e_mass
  print *,PI
end program test_physical_constants
```

## Legal

IMAS-Python is Copyright 2021-2023, 2026 ITER Organization
It is licensed under [LGPL 3.0](LICENSE.txt).

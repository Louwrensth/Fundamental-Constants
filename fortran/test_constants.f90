include 'mathematical_constants.f90'

include 'physical_constants_2018.f90'

program test_physical_constants
  use physical_constants_2018, only: electron_mass
  use mathematical_constants, only: PI => M_PI
  implicit none

  print *,electron_mass
  print *,PI
  
end program test_physical_constants

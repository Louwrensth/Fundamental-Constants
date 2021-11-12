include 'mathematical_constants.f90'  ! Excellent math constant lives here
include 'codata_2018.f90'      ! Recommended physical constants since 2018

program test_physical_constants
  use codata, only: electron_mass
  use mathematical_constants, only: PI => M_PI
  implicit none

  print *,electron_mass
  print *,PI
  
end program test_physical_constants

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

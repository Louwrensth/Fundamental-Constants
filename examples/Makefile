
# HINT:
# Ensure to have PKG_CONFIG_PATH point to your install dir of fundamental-constants.pc
# e.g. PKG_CONFIG_PATH=$(DESTDIR)$(libdir)/pkgconfig

FC = gfortran
CXX = g++
CFLAGS = `pkg-config fundamental-constants --cflags`
PROGS = test_constants.x test_constants.xx

all: $(PROGS)

check: $(PROGS)
	for PROG in $^ ;do echo ./$$PROG; $$_ || exit 1 ;done

clean:
	$(RM) *.x *.xx *.mod

%.x: %.f90
	$(FC) $(CFLAGS) $< -o $@

%.xx: %.cpp
	$(CXX) $(CFLAGS) $< -o $@

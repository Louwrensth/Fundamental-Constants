
# HINT:
# Ensure to have PKG_CONFIG_PATH point to your install dir of fundamental-constants.pc
# e.g. PKG_CONFIG_PATH=$(DESTDIR)$(libdir)/pkgconfig

FC = gfortran
FCFLAGS = `pkg-config fundamental-constants --cflags`
PROGS = test_constants.x

all: $(PROGS)

check: $(PROGS)
	for PROG in $^ ;do echo ./$$PROG; $$_ || exit 1 ;done

clean:
	$(RM) *.x *.mod

%.x: %.f90
	$(FC) $(FCFLAGS) $< -o $@

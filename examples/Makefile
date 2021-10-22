
# HINT:
# Ensure to have PKG_CONFIG_PATH point to your install dir of fundamental-constants.pc
# e.g. PKG_CONFIG_PATH=$(DESTDIR)$(libdir)/pkgconfig

FC = gfortran
CC = gcc
CXX = g++
CFLAGS = `pkg-config fundamental-constants --cflags`
PROGS = test_constants_f90 test_constants_cpp test_constants_c

all: $(PROGS)

check: $(PROGS)
	for PROG in $^ ;do echo ./$$PROG; $$_ || exit 1 ;done

clean:
	$(RM) *_f90 *_c *_cpp

%_f90: %.f90
	$(FC) $(CFLAGS) $< -o $@

%_c: %.c
	$(CC) $(CFLAGS) $< -o $@

%_cpp: %.cpp
	$(CXX) $(CFLAGS) $< -o $@

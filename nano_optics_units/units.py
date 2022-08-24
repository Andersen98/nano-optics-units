from scipy import constants

meep_unit_length_si = constants.micro
meep_init_time_si = meep_unit_length_si/constants.c
meep_unit_frequency_si = meep_init_time_si**-1


THz = constants.tera*meep_init_time_si
nm = constants.nano/meep_unit_length_si
fs = constants.femto/meep_init_time_si
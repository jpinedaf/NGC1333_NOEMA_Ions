import numpy as np
from astropy.io import fits
from reproject import reproject_interp

file_col = 'HGBS_perseus_hires_column_density_map.fits'
file_temp = 'HGBS_perseus_dust_temperature_map.fits'

file_DCOp = 'NGC1333_DCOp_matched_TdV.fits'

file_col_zoom = 'NGC1333_SE_H2.fits'
file_temp_zoom = 'NGC1333_SE_Tdust.fits'

hd_target = fits.getheader(file_DCOp)

#
hd_target['BUNIT'] = ('cm-2', 'N(H2)')
hd_target['BPA'] = 0.0
hd_target['BMAJ'] = 18.2/3600.
hd_target['BMIN'] = 18.2/3600.
N_H2_rep, footprint = reproject_interp(file_col, hd_target)

fits.writeto(file_col_zoom, N_H2_rep, hd_target, overwrite=True)

hd_target['BUNIT'] = ('K', 'T_dust (SED)')
hd_target['BMAJ'] = 36.1/3600.
hd_target['BMIN'] = 36.1/3600.
Td_rep, footprint = reproject_interp(file_temp, hd_target)

fits.writeto(file_temp_zoom, Td_rep, hd_target, overwrite=True)

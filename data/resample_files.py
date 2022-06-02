import numpy as np
from astropy.io import fits
from reproject import reproject_interp

file_col = 'HGBS_perseus_hires_column_density_map.fits'
file_temp = 'HGBS_perseus_dust_temperature_map.fits'
file_DCOp = 'NGC1333_DCOp_H13COp_ratio_coldens.fits'
file_C18O_TdV = 'NGC1333_C18O_3-2_TdV.fits'
file_C18O = 'NGC1333_C18O_3-2_Ncol.fits'

file_col_zoom = 'NGC1333_SE_H2.fits'
file_temp_zoom = 'NGC1333_SE_Tdust.fits'
file_C18O_zoom = 'NGC1333_SE_C18O.fits'
file_C18O_Td_zoom = 'NGC1333_SE_C18O_Td.fits'
file_C18O_TdV_zoom = 'NGC1333_SE_C18O_TdV.fits'

hd_target = fits.getheader(file_DCOp)

# N_H2, hd_Herschel = fits.getdata(file_col, header=True)

hd_target['BUNIT'] = ('cm-2', 'N(H2)')
hd_target['BPA'] = 0.0
hd_target['BMAJ'] = 18.2/3600.
hd_target['BMIN'] = 18.2/3600.
N_H2_rep, footprint = reproject_interp(file_col, hd_target)

fits.writeto(file_col_zoom, N_H2_rep, hd_target, overwrite=True)

hd_target['BUNIT'] = ('K', 'T_dust (SED)')
hd_target['BMAJ'] = 31.0/3600.
hd_target['BMIN'] = 31.0/3600.
Td_rep, footprint = reproject_interp(file_temp, hd_target)

fits.writeto(file_temp_zoom, Td_rep, hd_target, overwrite=True)

#
#
#
hd_target['BUNIT'] = ('K km s-1', 'Tmb')
hd_target['BMAJ'] = 17.7 / 3600.
hd_target['BMIN'] = 17.7 / 3600.
hd_target['BPA'] = 0.0
TdV_C18O_rep, footprint = reproject_interp(file_C18O_TdV, hd_target)
fits.writeto(file_C18O_TdV_zoom, TdV_C18O_rep, hd_target, overwrite=True)

hd_target['BUNIT'] = ('cm-2', 'N(C18O)')
Tex = 12.0
T_18 = 31.6
N_C18O_rep = 5e12 * Tex * np.exp(T_18/Tex) * TdV_C18O_rep 
fits.writeto(file_C18O_zoom, N_C18O_rep, hd_target, overwrite=True)

# if Tex = Td
hd_target['BUNIT'] = ('cm-2', 'N(C18O)')
# Tex = 12.0
T_18 = 31.6
N_C18O_Td_rep = 5e12 * Td_rep * np.exp(T_18/Td_rep) * TdV_C18O_rep 
fits.writeto(file_C18O_Td_zoom, N_C18O_Td_rep, hd_target, overwrite=True)



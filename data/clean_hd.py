import numpy as np
from astropy.io import fits
key_list = ['NAXIS3', 'PC3_1', 'PC3_2', 'PC1_3', 'PC2_3', 'PC3_3',
            'CTYPE3', 'CRVAL3', 'CDELT3', 'CRPIX3', 'CUNIT3', 'SPECSYS']

file_in = 'NGC1333_DCOp_L09-merged_SDI_TdV.fits'
file_out = 'NGC1333_DCOp_L09-merged_SDI_TdV_fix.fits'

data, hd = fits.getdata(file_in, header=True)
for key_i in key_list:
    hd.remove(key_i)
hd['NAXIS'] = 2
fits.writeto(file_out, np.squeeze(data), hd, overwrite=True)

file_in = 'NGC1333-H13COp_match_TdV.fits'
file_out = 'NGC1333-H13COp_match_TdV_fix.fits'
data, hd = fits.getdata(file_in, header=True)
hd['BUNIT'] = 'K km s-1 '
fits.writeto(file_out, data/1e3, hd, overwrite=True)


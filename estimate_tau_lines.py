import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from radio_beam import Beam
from molecular_columns.common_functions import J_nu
import astropy.units as u

plt.ion()

file_DCOp_Tp = 'data/NGC1333_DCOp_Tp.fits'
file_H13COp_Tp = 'data/NGC1333_H13COp_Tp.fits'

file_DCOp_tau = 'data/NGC1333_DCOp_tau.fits'
file_H13COp_tau = 'data/NGC1333_H13COp_tau.fits'

Tp_DCOp, hd_DCOp = fits.getdata(file_DCOp_Tp, header=True)
Tp_H13COp, hd_H13COp = fits.getdata(file_H13COp_Tp, header=True)

beam_DCOp = Beam.from_fits_header(hd_DCOp)
beam_H13COp = Beam.from_fits_header(hd_H13COp)

freq_DCOp = hd_DCOp['RESTFREQ'] * u.Hz
freq_H13COp = hd_H13COp['RESTFREQ'] * u.Hz

Tp_DCOp_K = (Tp_DCOp * u.Jy).to(u.K, beam_DCOp.jtok_equiv(freq_DCOp))
Tp_H13COp_K = (Tp_H13COp * u.Jy).to(u.K, beam_H13COp.jtok_equiv(freq_H13COp))

tau_DCOp = -np.log(1.0 - Tp_DCOp_K / 
                  (J_nu(Tex=10*u.K, freq=freq_DCOp) - 
                   J_nu(Tex=2.73*u.K, freq=freq_DCOp))).value

tau_H13COp = -np.log(1.0 - Tp_H13COp_K / 
                  (J_nu(Tex=10*u.K, freq=freq_H13COp) - 
                   J_nu(Tex=2.73*u.K, freq=freq_H13COp))).value

hd_DCOp['BUNIT'] = ('', 'opacity')
hd_H13COp['BUNIT'] = ('', 'opacity')
fits.writeto(file_DCOp_tau, tau_DCOp, hd_DCOp, overwrite=True)
fits.writeto(file_H13COp_tau, tau_H13COp, hd_H13COp, overwrite=True)

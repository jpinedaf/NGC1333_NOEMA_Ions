import numpy as np
from astropy.io import fits
from radio_beam import Beam
from molecular_columns.common_functions import J_nu
import astropy.units as u

# import matplotlib.pyplot as plt
# plt.ion()

file_DCOp_Tp = 'data/NGC1333_DCOp_Tp.fits'
file_H13COp_Tp = 'data/NGC1333_H13COp_Tp.fits'
file_C18O_Tp = 'data/NGC1333_C18O_Tp.fits'

file_DCOp_tau = 'data/NGC1333_DCOp_tau.fits'
file_H13COp_tau = 'data/NGC1333_H13COp_tau.fits'
file_C18O_tau = 'data/NGC1333_C18O_tau.fits'

Tp_DCOp, hd_DCOp = fits.getdata(file_DCOp_Tp, header=True)
Tp_H13COp, hd_H13COp = fits.getdata(file_H13COp_Tp, header=True)
Tp_C18O, hd_C18O = fits.getdata(file_C18O_Tp, header=True)

beam_DCOp = Beam.from_fits_header(hd_DCOp)
beam_H13COp = Beam.from_fits_header(hd_H13COp)
beam_C18O = Beam.from_fits_header(hd_C18O)

freq_DCOp = hd_DCOp['RESTFREQ'] * u.Hz
freq_H13COp = hd_H13COp['RESTFREQ'] * u.Hz
freq_C18O = 329.33055250 * u.GHz #hd_C18O['RESTFREQ'] * u.Hz

Tp_DCOp_K = (Tp_DCOp * u.Jy).to(u.K, beam_DCOp.jtok_equiv(freq_DCOp))
Tp_H13COp_K = (Tp_H13COp * u.Jy).to(u.K, beam_H13COp.jtok_equiv(freq_H13COp))

T_ex_DCOp = 10.0 * u.K
T_ex_H13COp = 8.0 * u.K

tau_DCOp = -np.log(1.0 - Tp_DCOp_K / 
                  (J_nu(Tex=T_ex_DCOp, freq=freq_DCOp) - 
                   J_nu(Tex=2.73*u.K, freq=freq_DCOp))).value

tau_H13COp = -np.log(1.0 - Tp_H13COp_K / 
                  (J_nu(Tex=T_ex_H13COp, freq=freq_H13COp) - 
                   J_nu(Tex=2.73*u.K, freq=freq_H13COp))).value

tau_C18O = -np.log(1.0 - Tp_C18O * u.K / 
                  (J_nu(Tex=12.0*u.K, freq=freq_C18O) - 
                   J_nu(Tex=2.73*u.K, freq=freq_C18O))).value

hd_DCOp['BUNIT'] = ('', 'opacity')
hd_H13COp['BUNIT'] = ('', 'opacity')
fits.writeto(file_DCOp_tau, tau_DCOp, hd_DCOp, overwrite=True)
fits.writeto(file_H13COp_tau, tau_H13COp, hd_H13COp, overwrite=True)
fits.writeto(file_C18O_tau, tau_C18O, hd_C18O, overwrite=True)

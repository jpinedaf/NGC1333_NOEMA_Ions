from astropy.io import ascii
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": True,
                     "font.family": "serif",
                     'xtick.direction': 'in',
                     'ytick.direction': 'in',
                     'xtick.minor.size': 3,
                     'xtick.major.size': 6,
                     'ytick.minor.size': 3,
                     'ytick.major.size': 6,})

plt.ion()

file_list = ['data/collected_1e-15.dat',
             'data/collected_1e-16.dat',
             'data/collected_1e-17.dat']

label_list = [r'$\zeta=10^{-15}\, {\rm s^{-1}}$',
              r'$\zeta=10^{-16}\, {\rm s^{-1}}$',
              r'$\zeta=10^{-17}\, {\rm s^{-1}}$']

zeta_list = [1e-15, 1e-16, 1e-17]

plt.close('all')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=1, nrows=4,
                                         figsize=(5, 10), sharex=True)
fig.subplots_adjust(hspace=0.005)
# fig2, ax2 = plt.subplots(figsize=(5, 5))
# fig3, ax3 = plt.subplots(figsize=(5, 5))
# fig4, ax4 = plt.subplots(figsize=(5, 5))

ax4.set_xlim(0.1, 10)
# ax2.set_xlim(0.1, 10)
# ax3.set_xlim(0.1, 10)
# ax4.set_xlim(0.1, 10)

ax1.set_ylim(0, 0.0005)
ax2.set_ylim(0, 0.17)
ax3.set_ylim(0, 6)
ax4.set_ylim(0, 50)

# ax1.set_xlabel(r"time, (Myr)")
# ax2.set_xlabel(r"time, (Myr)")
# ax3.set_xlabel(r"time, (Myr)")
ax4.set_xlabel(r"Time, (Myr)")

ax1.set_ylabel(r"$R_H$")
ax2.set_ylabel(r"$R_D$")
ax3.set_ylabel(r"$\zeta_{out}/\zeta_{in}$")
ax4.set_ylabel(r"$f_D$")

n_H2 = 10**(3.9)

for file_in, label_i, zeta_i in zip(file_list, label_list, zeta_list):
    data = ascii.read(file_in)
    R_D = data['DCO+'] / (data['HCO+'] + 1e-20)
    R_H = data['HCO+'] / (data['CO'] + 1e-10)
    f_D = 1.5e-4 / (data['CO'] + 1e-10)
    time_Myr = data['time']*1e-6
    xe_fd = 2.7e-8 / R_D - 1.2e-6 / f_D
    zeta_out = (7.5e-4 * xe_fd + 4.6e-10/f_D) * xe_fd * R_H * (n_H2)
    # print(data)
    ax1.plot(time_Myr, R_H, label=label_i)
    ax2.plot(time_Myr, R_D, label=label_i)
    ax3.plot(time_Myr, zeta_out / zeta_i, label=label_i)
    ax4.plot(time_Myr, f_D, label=label_i)
# ax3.set_yscale('log')
ax3.legend()
plt.show()
fig.tight_layout()
# fig2.tight_layout()
# fig3.tight_layout()
# fig4.tight_layout()


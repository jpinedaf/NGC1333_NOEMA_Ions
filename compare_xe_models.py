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
color_list = ['#377eb8', '#ff7f00', '#4daf4a']

zeta_list = [1e-15, 1e-16, 1e-17]

plt.close('all')

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(ncols=1, nrows=5,
                                         figsize=(5, 10), sharex=True)
fig.subplots_adjust(hspace=0.01)
t_min = 0.3
ax5.set_xlim(t_min, 10)

ax1.set_ylim(0, 0.0005)
ax2.set_ylim(0, 0.17)
ax3.set_ylim(0, 50)
ax4.set_ylim(0, 6)
ax5.set_ylim(0, 5)

ax5.set_xlabel(r"Time, (Myr)")

ax1.set_ylabel(r"$R_H$")
ax2.set_ylabel(r"$R_D$")
ax3.set_ylabel(r"$f_D$")
ax4.set_ylabel(r"$\zeta_{out}/\zeta_{in}$")
ax5.set_ylabel(r"$X(e)_{out}/X(e)_{in}$")

n_H2 = 10**(3.9)

for file_in, label_i, zeta_i, color_i in zip(file_list, label_list, zeta_list, color_list):
    data = ascii.read(file_in)
    gd_time = (data['time']*1e-6 > t_min)
    R_D = data['DCO+'][gd_time] / (data['HCO+'][gd_time] + 1e-20)
    R_H = data['HCO+'][gd_time] / (data['CO'][gd_time] + 1e-10)
    f_D = 1.5e-4 / (data['CO'][gd_time] + 1e-10)
    time_Myr = data['time'][gd_time]*1e-6
    xe_in = data['e-'][gd_time]

    xe_fd_old = 2.7e-8 / R_D - 1.2e-6 / f_D
    zeta_out_old = (7.5e-4 * xe_fd_old + 4.6e-10 / f_D) * xe_fd_old * R_H * (n_H2)
    # New Olli
    xe_fd = 2.9e-8 / R_D - 2.2e-6 / f_D
    zeta_out = (7.1e-4 * xe_fd + 7.38e-10 / f_D) * xe_fd * R_H * (n_H2)
    
    # print(data)
    ax1.plot(time_Myr, R_H, label=label_i, color=color_i)
    ax2.plot(time_Myr, R_D, label=label_i, color=color_i)
    ax3.plot(time_Myr, f_D, label=label_i, color=color_i)

    ax4.plot(time_Myr, zeta_out / zeta_i, label=label_i, color=color_i)
    ax4.plot(time_Myr, zeta_out_old / zeta_i, ls=":", color=color_i)
    
    ax5.plot(time_Myr, xe_fd / xe_in, label=label_i, color=color_i)
    ax5.plot(time_Myr, xe_fd_old / xe_in, ls=":", color=color_i)

ax5.legend(frameon=False, loc=2)
plt.show()
fig.tight_layout()

fig.savefig('figs/compare_chem_models.pdf', bbox_inches='tight')
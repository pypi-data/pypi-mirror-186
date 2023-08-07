# Lipid bilayer in SAXS/SANS
# Values for layer thickness can be found in
# Structure of lipid bilayers
# John F. Nagle et al. Biochim Biophys Acta. 1469, 159–195. (2000)

# scattering length densities of DPPC for SAXS and SANS can be found in
#  Kučerka et al. Biophysical Journal. 95,2356 (2008)
#  https://doi.org/10.1529/biophysj.108.132662

import jscatter as js
import numpy as np

ffmV = js.ff.multilamellarVesicles
save = 0

Q = js.loglist(0.01, 7, 500)
dd = 1.5
dR = 5
nG = 100
ds = 0.05  # variation of hydrocarbon layer thickness
R = 50
sd = [0.75, 2.8, 0.75]
N = 2

p = js.grace(1.4,1)
p.title('Multilamellar/unilamellar vesicle for SAXS/SANS')
# SAXS
sld = np.r_[420, 290, 420] * js.formel.felectron  # unit e/nm³*fe
sSLD = 335 * js.formel.felectron  # H2O unit e/nm³*fe
saxm = ffmV(Q=Q, R=R, displace=dd, dR=dR, N=N, dN=0, phi=0.2, layerd=sd, ds=ds, layerSLD=sld, solventSLD=sSLD, nGauss=nG)
p.plot(saxm, sy=0, li=[1, 1, 1], le='multilamellar')
saxu = ffmV(Q=Q, R=R, displace=0, dR=dR, N=1, dN=0, phi=0.2, layerd=sd, ds=ds, layerSLD=sld, solventSLD=sSLD, nGauss=100)
p.plot(saxu, sy=0, li=[3, 2, 1], le='unilamellar')
saxu0 = ffmV(Q=Q, R=R, displace=0, dR=dR, N=1, dN=0, phi=0.2, layerd=sd, ds=0, layerSLD=sld, solventSLD=sSLD, nGauss=100)
p.plot(saxu0, sy=0, li=[2, 0.3, 1], le='unilamellar ds=0')
p.text('SAXS', x=0.015, y=0.2, charsize=1.5,color=1)

# SANS
sld=[4e-4, -.5e-4, 4e-4]  # unit 1/nm²
sSLD = 6.335e-4  # D2O
sanm = ffmV(Q=Q, R=R, displace=dd, dR=dR, N=N, dN=0, phi=0.2, layerd=sd, ds=ds, layerSLD=sld, solventSLD=sSLD, nGauss=nG)
p.plot(sanm, sy=0, li=[1, 1, 2], le='multilamellar')
sanu = ffmV(Q=Q, R=R, displace=0, dR=dR, N=1, dN=0, phi=0.2, layerd=sd, ds=ds, layerSLD=sld, solventSLD=sSLD, nGauss=100)
p.plot(sanu, sy=0, li=[3, 2, 2], le='unilamellar')
sanu = ffmV(Q=Q, R=R, displace=0, dR=dR, N=1, dN=0, phi=0.2, layerd=sd, ds=0, layerSLD=sld, solventSLD=sSLD, nGauss=100)
p.plot(sanu, sy=0, li=[2, 0.3, 2], le='unilamellar ds=0')
p.text('SANS', x=0.015, y=50, charsize=1.5,color=2)

p.legend(x=0.8, y=950, boxcolor=0, boxfillpattern=0)
p.subtitle('R=%.2g nm, N=%.1g, layerd=%s nm, dR=%.1g, ds=%.2g' % (R, N, sd, dR, ds))

p.yaxis(label='S(Q)', scale='l', min=2e-6, max=2e3, ticklabel=['power', 0])
p.xaxis(label=r'Q / nm\S-1', scale='l', min=1e-2, max=9, ticklabel=['power', 0])
p.text(r'Correlation peaks\n at 2\xp\f{}N/R', x=0.25, y=0.05, charsize=1.,color=1)
p.text('Guinier range', x=0.03, y=900, charsize=1.)
p.text('Shell form factor ds=0', x=0.2, y=0.2e-4)
p[0].line(0.3, 1e-5, 1.3, 1e-5, 2, arrow=2)
if save: p.save('multilamellar5.png')



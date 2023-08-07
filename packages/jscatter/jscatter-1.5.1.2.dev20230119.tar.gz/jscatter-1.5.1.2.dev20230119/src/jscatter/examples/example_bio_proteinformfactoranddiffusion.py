import jscatter as js
import numpy as np
import scipy.constants as constants

adh = js.bio.fetch_pdb('4w6z.pdb1')
# the 2 dimers in are in model 1 and 2 and need to be merged into one.
adhmerged = js.bio.mergePDBModel(adh)

p = js.grace(1.4, 1)
p.multi(1, 2)

for cc, pdb in enumerate(['3rn3', '3pgk', adhmerged], 1):
    # create universe; M and Z are for wrong named Mg and Zn  in the pdb files
    uni = js.bio.scatteringUniverse(pdb, vdwradii={'M': 1.73, 'Z': 1.7})

    # SANS scattering intensity with conversion to 10g/l mass concentration and 1/cm units
    uni.qlist = np.r_[0.01, 0.1:6:0.03]
    protein = uni.select_atoms('protein')
    Iq = js.bio.nscatIntUniv(protein)
    # molarity for 1g/l concentration
    mol = 1/protein.masses.sum()  # molarity 1g/l
    c = 10 * constants.N_A*mol/1000*1e-14  # conversion from 1/nm² per particle to 1/cm for 10g/l concentration
    p[0].plot(Iq.X, Iq.Y * c, sy=0, li=[1, 3, cc], le=pdb)

    # effective diffusion as seen by NSE in the initial slope of a rigid protein
    D_hr = js.bio.hullRad(uni)
    Dt = D_hr['Dt'] * 1e2  # conversion to nm²/ps
    Dr = D_hr['Dr'] * 1e-12  # conversion to 1/ps
    uni.qlist = np.r_[0.01, 0.1:3:0.06]
    Dq = js.bio.diffusionTRUnivTensor(uni.residues, DTT=Dt, DRR=Dr)
    p[1].plot(Dq.X, Dq.Y/Dq.DTTtrace, sy=[-1, 0.6, cc], le=pdb)

p[0].plot([0, 6], [0.06]*2, sy=0, li=[2,3,1], le='D2O background')
p[0].xaxis(label=r'Q / nm\S-1', min=0, max=6)
p[0].yaxis(label=r'I(Q) / 1/cm', scale='log', min=1e-4, max=2)
p[1].xaxis(label=r'Q / nm\S-1', min=0, max=3)
p[1].yaxis(label=['D(Q)/D(0)', 1.5, 'opposite'], min=0.98, max=1.4)
p[0].legend(x=2, y=0.8)
p[0].title('neutron scattering intensity')
p[1].title('scaled effective diffusion')
p[1].subtitle('transl. diffusion at q=0, increase due to rot. diffusion')

# p.save('bio_protein_formfactor+Diffusion.png')


import jscatter as js
import numpy as np
import tempfile
import os
import pymol2
import matplotlib.image as mpimg


def savepng(u, fname):
    p1 = pymol2.PyMOL()
    p1.start()
    with tempfile.TemporaryDirectory() as tdir:
        name = os.path.splitext(u.filename)[0] + '.pdb'
        tfile = os.path.join(tdir, name)
        u.atoms.write(tfile)
        p1.cmd.load(tfile)
        p1.cmd.rotate('x', 90, 'all')
        p1.cmd.color('red', 'ss h')
        p1.cmd.color('yellow', 'ss s')
        p1.cmd.color('blue', 'ss l+')
        p1.cmd.set('cartoon_discrete_colors',1)
        p1.cmd.png(fname, width=600, height=600, dpi=-1, ray=1)
    p1.stop()

uni=js.bio.scatteringUniverse(js.examples.datapath+'/arg61.pdb', addHydrogen=False)

uni=js.bio.scatteringUniverse('3pgk')
u = uni.select_atoms("protein and name CA")
nm = js.bio.vibNM(u)
moving = nm.animate([6,7,8,9], scale=120)
moving.qlist = js.loglist(0.1, 5, 100)

p = js.mplot(16, 8)
for i, ts in enumerate(moving.trajectory):
    Sq = js.bio.xscatIntUniv(moving.atoms, refreshVolume=False)
    p.Multi(1, 2)
    p[1].axis('off')
    p[0].Plot(Sq, li=[1,2,1], sy=0)
    p[0].Yaxis(label='F(Q) / nm²', scale='log', min=3e-7, max=6e-4)
    p[0].Xaxis(label=r'$Q / nm^{-1}$')
    name = f'test_{i:.0f}.png'
    savepng(moving, name)
    img = mpimg.imread(name)
    p[1].imshow(img)
    # p.savefig(name, transparent=True, dpi=100)
    p.clear()

p.Close()

# in ipython shell using ImageMagic
# %system convert -delay 10 -loop 0  -dispose Background test*.png mode_animation.gif


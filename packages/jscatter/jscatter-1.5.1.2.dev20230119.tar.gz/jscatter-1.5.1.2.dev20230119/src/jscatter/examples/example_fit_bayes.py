import numpy as np
import jscatter as js
import matplotlib.pyplot as plt
import corner

# data to fit
# We use each a subset to speed up the example
i5 = js.dL(js.examples.datapath+'/iqt_1hho.dat')[[3, 5]]

# model
def diffusion(A, D, t, elastic, wavevector=0):
    return A*np.exp(-wavevector**2*D*t) + elastic

# define ln_prior that describes knowledge about the data
# the prior is complemented by the limits
# without prior only the limits are used (uninfomative prior)
# so the prior is optional if you know something about the parameters
def ln_prior(A, D):
    # assuming a normalised Gaussian distribution around the mean of A and D
    # the log of the Gaussian is the log_prior
    # the parameters are arrays for all elements of the dataList or a float for common parameters
    # the 't' is not included as it descibes the .X values, 'elastic' is not used.
    Asig = 0.01  # just a guess for the eample
    Dsig = 0.02  # just a guess for the eample
    lp = -0.5*(np.sum((A-1)**2/Asig**2)) + np.log(2*np.pi*Asig**2*len(A))
    lp += -0.5*(np.sum((D-0.09)**2/Dsig**2)) + np.log(2*np.pi*Dsig**2*len(D))
    return lp

i5.setlimit(D=[0.05, 1], A=[0.5, 1.5])

# do Bayesian analysis with the prior
i5.fit(model=diffusion, freepar={'D': [0.2], 'A': 0.98}, fixpar={'elastic': 0.0},
      mapNames={'t': 'X', 'wavevector': 'q'}, condition=lambda a: a.X<90,
       method='bayes', tolerance=20, bayesnsteps=1000, ln_prior=ln_prior)

i5.showlastErrPlot()

# get sampler chain and examine results removing burn in time 2*tau
tau = i5.getBayesSampler().get_autocorr_time(tol=20)
flat_samples = i5.getBayesSampler().get_chain(discard=int(2*tau.max()), thin=1, flat=True)
labels = i5.getBayesSampler().parlabels

plt.ion()
fig = corner.corner(flat_samples, labels=labels, quantiles=[0.16, 0.5, 0.84], show_titles=True, title_fmt='.3f')
plt.show()
# fig.savefig(js.examples.imagepath+'/bayescorner_withprior.jpg')

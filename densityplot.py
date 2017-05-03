import corner
import numpy as np
import pylab

ndim, nsamples = 2, 10000 #this is the original example
#ndim, nsamples = 2, 50000 #all lines beginning with 'ndim' below the line above are other initial conditions
#ndim, nsamples = 2, 1000000
#ndim, nsamples = 3, 10000
np.random.seed(42)
samples = np.random.randn(ndim * nsamples).reshape([nsamples, ndim])
figure = corner.corner(samples)

pylab.savefig("density_plot") #this is the original example
#pylab.savefig("density_plot_1") #all lines beginning with 'pylab' below the line above this one are saves for
# other initial conditions
#pylab.savefig("dp2")
#pylab.savefig("dp3")

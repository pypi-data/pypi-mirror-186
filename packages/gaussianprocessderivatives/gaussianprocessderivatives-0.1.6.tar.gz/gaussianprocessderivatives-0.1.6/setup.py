# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gaussianprocessderivatives']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.0,<4.0.0', 'numpy>=1.16.0,<2.0.0', 'scipy>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'gaussianprocessderivatives',
    'version': '0.1.6',
    'description': 'Uses Gaussian processes to smooth data and estimate first- and second-order derivatives',
    'long_description': "A Python package for smoothing data and estimating first- and second-order derivatives and their errors.\n\nCovariance functions can either be linear, squared exponential, neural network-like, or squared exponential with a linear trend.\n\nAn example workflow to smooth data (x, y), where the columns of y are replicates, is\n\n>>> import gaussian process as gp\n>>> g= gp.maternGP({0: (-4, 4), 1: (-4, 4), 2: (-4, -2)}, x, y)\n\nThe dictionary sets bounds on the hyperparameters, so that 0: (-4, 4) means that the bounds on the first hyperparameter are 1e-4 and 1e4.\n\n>>> g.info()\n\nexplains what each hyperparameter does.\n\nOnce g is instantiated,\n\n>>> g.findhyperparameters()\n>>> g.results()\n>>> g.predict(x, derivs= 2)\n\noptimises the hyperparameters and determines a smoothed version of the data and estimates the derivatives.\n\nThe results can be visualised by\n\n>>> import matplotlib.pylab as plt\n>>> plt.figure()\n>>> plt.subplot(2,1,1)\n>>> g.sketch('.')\n>>> plt.subplot(2,1,2)\n>>> g.sketch('.', derivs= 1)\n>>> plt.show()\n\nand are available as g.f and g.fvar (smoothed data and error), g.df and g.dfvar (estimate of dy/dx), and g.ddf and g.ddfvar (estimate of d2y/dx2).\n",
    'author': 'Peter Swain',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<3.11',
}


setup(**setup_kwargs)

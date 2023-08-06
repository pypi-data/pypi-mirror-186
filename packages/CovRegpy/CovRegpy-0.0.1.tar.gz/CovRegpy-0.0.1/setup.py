
from setuptools import setup

setup(
  name = 'CovRegpy',
  packages = ['CovRegpy'],
  version = '0.0.1',
  license='gpl-3.0',
  description = 'Regularised covariance regression software project based on Hoff and Niu (2012).',
  long_description = 'Regularised Covariance regression software project based on Hoff and Niu (2012). This package was developed out of research performed by Cole van Jaarsveldt, Gareth W. Peters, Matthew Ames, and Mike Chantler. This package was built entirely using Python 3.7.0 - Python guarantees backwards compatibility which should ensure that this software package functions as expected on all future Python versions.',
  author = 'Cole van Jaarsveldt',
  author_email = 'colevj0303@gmail.com',
  url = 'https://github.com/Cole-vJ/CovRegpy.git',
  download_url = 'https://github.com/Cole-vJ/CovRegpy/archive/refs/tags/0.0.1.tar.gz',
  keywords = ['Portfolio Optimisation', 'Regularised Covariance Regression (RCR)', 'Empirical Mode Decomposition (EMD)', 'Singular Spectrum Analysis (SSA)', 'Singular Spectrum Decomposition (SSD)', 'X11', 'Implicit Factors', 'Risk Premia Parity', 'Risk Parity', 'Long\Short Equity'],
  install_requires=[
          'numpy',
          'seaborn',
	  'group-lasso',
	  'AdvEMDpy',
	  'pandas',
	  'matplotlib',
	  'yfinance',
  	  'mdlp-discretization',
	  'arch',
  	  'notebook',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.7',
  ],
)

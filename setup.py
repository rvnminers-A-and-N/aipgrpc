from distutils.core import setup
setup(
  name = 'evrmorerpc',         
  packages = ['evrmorerpc'],   
  version = '0.2',      
  license='MIT',     
  description = 'Crazy simple AI Power Grid RPC library',
  author = 'JonPizza and Alpha',
  author_email = 'jon@jon.network and rvnminers@gmail.com',
  url = 'https://jon.network and https://cyrpticwizardry.com',
  download_url = 'https://github.com/rvnminers-A-and-N/aipgrpc/archive/refs/tags/v0.2.tar.gz',
  keywords = ['EVR', 'RPC'],
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

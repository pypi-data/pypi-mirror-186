from setuptools import setup

setup(
    name='molaguttal',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/HarshiniAiyyer/molaguttal',
    author='HarshiniAiyyer',
    author_email='kerneldacore@gmail.com',
    license='MIT License',
    packages=['molaguttal'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
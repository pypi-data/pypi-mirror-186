from setuptools import setup

setup(
    name='megaboost',
    version='0.1.1',    
    description='Semi-supervised AutoML library on top of Pytorch',
    url='',
    author='Max Ng',
    author_email='maxnghello@gmail.com',
    license='',
    packages=['megaboost'],
    install_requires=['numpy>=1.19.2',
                        'Pillow>=9.2.0',
                        'scikit_learn>=1.2.0',
                        'torch>=1.12.1',
                        'torchvision>=0.13.1'                   
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.10'
    ],
)
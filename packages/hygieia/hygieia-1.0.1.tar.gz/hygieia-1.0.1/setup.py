from setuptools import setup

setup(
    name='hygieia',
    version='1.0.1',
    packages=['hygieia'],
    license='GNU General Public License v3.0',
    description='Hygieia utilizes feature selection to predict the clinical and genomic basis of disease.',
    long_description=open('README.md').read(),
    install_requires=[
        'pandas',
        'sklearn',
        'matplotlib',
        'seaborn'
    ],
    author='Will DeGroat, Vignesh Venkat, Habiba Abdelhalim, Widnie Pierre-Louis, Dr. Zeeshan Ahmed',
    author_email='zahmed@ifh.rutgers.edu'
)

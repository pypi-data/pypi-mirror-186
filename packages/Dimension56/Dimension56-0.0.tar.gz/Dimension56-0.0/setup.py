from setuptools import setup, find_packages

setup(
    name='Dimension56',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'sklearn'
    ],
    author='Hanzlah Shah',
    author_email='shahhanzlah90@gmail.com',
    description='Package for Dimension Reduction',
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        
    ],
    python_requires='>=3.6,<4.0', 
)

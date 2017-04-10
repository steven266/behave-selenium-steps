from setuptools import setup, find_packages

requirements = [
    "behave>=1.2.4",
    "selenium>=2.0.0",
]

setup(
    name='behave_steps',
    version='0.1.0',
    description='Some useful behave step definitions',
    url='https://github.com/steven266/behave-selenium-steps',
    author='Steven Cardoso',
    author_email='hello@steven266.de',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='behave selenium uat',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements,
)

from setuptools import setup
setup(
    name='sunnyday-calcetto',
    packages=['sunnyday'],
    version='2.0.0',
    author='Denis Vreshtazi(helped by Ardit Sulce)',
    author_email='vreshtazi21@gmail.com',
    url='https://github.com/denisvreshtazi/Weather-Package',
    description='Weather forecast data',
    license='MIT',
    keywords=['weather', 'forecast', 'openweather'],
    install_rquires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Build Tools',
    ],

)


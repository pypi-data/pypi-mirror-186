import setuptools

setuptools.setup(
    name="energypriceapi",
    version="1.0.3",
    url="https://github.com/energypriceapi/energypriceapi-python",

    author="EnergypriceAPI",
    author_email="contact@energypriceapi.com",

    description="Official Python wrapper for energypriceapi.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.9.1'],
    keywords=['currency', 'oilpriceapi', 'oil price', 'foreign exchange rate', 'currency conversion', 'exchangerate', 'rates'],
)

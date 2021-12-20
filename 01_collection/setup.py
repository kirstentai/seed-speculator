import setuptools

setuptools.setup(
    name="scraper",
    version="0.0",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': "scraper=scraper.cli:cli"} #alias scraper

)

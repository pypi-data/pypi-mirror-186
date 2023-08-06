from setuptools import setup, find_packages

setup(
    name = "TOPSIS-GIRIK-102003178",
    version = "1.3.3",
    license = "MIT",
    description = "A Python package to find TOPSIS for multi-criteria decision analysis method",
    long_description = open('readme.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type = "text/markdown",
    author = "Girik Garg",
    author_email = "girikgarg8@gmail.com",
    url = "https://www.github.com/girikgarg8",
    keywords = ['topsis', 'UCS654', 'TIET'],
    packages = ["topsis_python"],
    include_package_data = True,
    install_requires = ['pandas', 'tabulate'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3' 
    ],
     entry_points={
        "console_scripts": [
            "topsis=topsis_python.topsis:main",
        ]
     }
)
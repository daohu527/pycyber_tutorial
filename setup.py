import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycyber_tutorial",
    version="0.0.1",
    author="daohu527",
    author_email="daohu527@gmail.com",
    description="pycyber tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/pycyber_tutorial",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/pycyber_tutorial/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    package_data={
        '': [
            'car_model/*.png',
        ]
    },
    packages=setuptools.find_packages(where="."),
    install_requires=[
        'pycyber',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'cyber_game = pycyber_tutorial.game:main',
        ],
    },
    python_requires=">=3.6",
)

from setuptools import setup, find_packages


setup(
    name="manitex",
    readme = "README.md",
    description = "Generate manifest and bundle for Latex articles",
    version="0.2",
    packages=find_packages(),
    entry_points={'console_scripts': [
            'manitex = manitex.manitex:main',
        ]
    }
)

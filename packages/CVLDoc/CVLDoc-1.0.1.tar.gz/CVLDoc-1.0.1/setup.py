from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "CVLDoc"
VERSION = "1.0.1"

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author="Certora ltd",
        author_email="support@certora.com",
        description=" Utility for reading CERTORA spec files, parse and export their NatSpec comments to JSON files.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords='Certora CVLDoc',
        url="https://github.com/Certora/natspecTools",
        packages=find_packages('src'),
        package_dir={'': 'src'},
        include_package_data=True,
        data_files=[('src/CVLDoc/examples', ['tests/basic_tests/definition_test.spec',
                                             'tests/basic_tests/import_test.spec',
                                             'tests/basic_tests/rules_test.spec',
                                             'tests/basic_tests/full_contract.spec',
                                             'tests/basic_tests/invariant_test.spec',
                                             'tests/basic_tests/use_test.spec',
                                             'tests/basic_tests/function_test.spec',
                                             'tests/basic_tests/methods_test.spec',
                                             'tests/basic_tests/using_test.spec'])],
        install_requires=[
            'cvldoc_parser==1.0.1',
            'inflection'
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 3 - Alpha",
        ],
        python_requires='>=3.7',
        entry_points={
            "console_scripts": [
                "cvldoc=CVLDoc.natspec_to_json:entry_point",
            ],
        },
    )

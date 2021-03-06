from setuptools import Extension, setup, find_packages


try:
    from Cython.Build import cythonize

    use_cython = True
except ImportError:
    use_cython = False

if use_cython:
    sources = [
        "orderbook/orderbook.pyx",
        "orderbook/src/orderbook.cpp",
        "orderbook/src/tree.cpp",
        "orderbook/src/limit.cpp",
        "orderbook/src/order.cpp",
    ]

    ext_modules = cythonize(
        Extension(
            "ghulorderbook",
            sources=sources,
            include_dirs=["orderbook/include/"],
            language="c++",
        ),
        compiler_directives={"embedsignature": True},
    )
else:
    ext_modules = [
        Extension("ghulorderbook", sources=["orderbook/orderbook.cpp"], language="c++")
    ]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    author="Andriy Rossoshynskyy",
    author_email="andriy.rossoshynskyy@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    description="A HFT order book written in C++ with a python wrapper",
    ext_modules=ext_modules,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="ghul-orderbook",
    packages=find_packages(),
    package_data={"": ["src/*", "*.pxd", "*.pyx", "*.cpp", ".h"],},
    python_requires=">=3.6",
    url="https://github.com/arossoshynskyy/ghul-orderbook",
    version="0.0.1",
)

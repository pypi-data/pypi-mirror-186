from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

extensions = [
    Extension("watsoncrdp", ["watson-crdp.pyx"]),
]

try:
    from Cython.Build import cythonize

    extensions = cythonize(extensions, compiler_directives={"language_level": 3})
except ImportError:
    pass


setup(
    name="watsoncrdp",
    version="0.3.0",
    packages=(find_packages()),
    install_requires=[],
    extras_require=dict(dev=["cython",],),
    ext_modules=extensions,
)

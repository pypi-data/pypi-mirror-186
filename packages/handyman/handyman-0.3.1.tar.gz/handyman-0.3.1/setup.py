import io
import os

from setuptools import setup


name = "handyman"
description = "Skit utils package for ML Services"
version = "0.3.1"

package_root = os.path.abspath(os.path.dirname(__file__))

dependencies_filename = os.path.join(package_root, "requirements.txt")
with io.open(dependencies_filename, "r") as dependencies_file:
    dependencies = dependencies_file.readlines()

dependencies = list(map(lambda x: x.strip(), dependencies))
extras = {}

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, "r") as readme_file:
    readme = readme_file.read()

# Only include packages under the 'handyman' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    "handyman", "handyman.crypto", "handyman.events", "handyman.cli", "handyman.exceptions"
]

# Determine which namespaces are needed.
namespaces = ["handyman"]

setup(
    name=name,
    version=version,
    description=description,
    long_description_content_type="text/markdown",
    long_description=readme,
    author="Skit.ai",
    author_email="deepankar@vernacular.ai",
    license="Apache 2.0",
    url="https://gitlab.com/vernacularai/tools/handyman",
    classifiers=[
        "Development Status :: 4 - Beta",   # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.5",
    include_package_data=True,
    zip_safe=False,
)

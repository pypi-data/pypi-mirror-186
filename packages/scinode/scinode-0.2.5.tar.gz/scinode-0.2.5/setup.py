import pathlib
from setuptools import setup, find_packages


def test_suite():
    import unittest

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")
    return test_suite


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="scinode",
    version="0.2.5",
    description="Design computational workflow using nodes.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scinode/scinode",
    author="Xing Wang",
    author_email="xingwang1991@gmail.com",
    license="MIT License",
    classifiers=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": ["scinode=scinode.cli.main:cli"],
        "scinode_node": [
            "built_in = scinode.nodes.built_in:node_list",
            "control = scinode.nodes.control:node_list",
            "python_builtin = scinode.nodes.python_builtin:node_list",
            "numpy_node = scinode.nodes.numpy_node:node_list",
            "node_from_database = scinode.nodes.node_from_database:node_list",
            "test = scinode.nodes.test:node_list",
        ],
        "scinode_socket": [
            "built_in = scinode.sockets.built_in:socket_list",
        ],
        "scinode_property": [
            "built_in = scinode.properties.built_in:property_list",
        ],
    },
    install_requires=[
        "psutil",
        "numpy",
        "scipy",
        "click",
        "dnspython",
        "pymongo",
        "pandas",
        "pyyaml",
        "colorama",
    ],
    package_data={},
    python_requires=">=3.6",
    test_suite="setup.test_suite",
)

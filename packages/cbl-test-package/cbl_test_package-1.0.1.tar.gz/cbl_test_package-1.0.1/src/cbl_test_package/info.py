# a.voss@fh-aachen.de

import platform
import sys
import dataclasses


@dataclasses.dataclass
class PlatformInfo:
    platform: str
    machine: str
    processor: str


def platform_info() -> PlatformInfo:
    return PlatformInfo(platform.platform(), platform.machine(), platform.processor())


@dataclasses.dataclass
class PythonInfo:
    executable: str
    version: str
    implementation: str


def python_info() -> PythonInfo:
    return PythonInfo(sys.executable, platform.python_version(), platform.python_implementation())


@dataclasses.dataclass
class PackageInfo:
    full_name: str
    version: str


def package_info() -> PackageInfo:
    return PackageInfo("cbl_test_package.info", "1.0.1")


if __name__ == "__main__":
    print(f"Platform Info: '{platform_info()}'")
    print(f"Python Info: '{python_info()}'")
    print(f"Package Info: '{package_info()}'")

"""

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://choosealicense.com/licenses/mit/
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps cbl_test_package==1.2.3


python3 -m build  
python3 -m twine upload --repository testpypi dist/* 
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps cbl_test_package@1.2.3 


python3 -m twine upload dist/* 
python3 -m pip install cbl_test_package==1.2.3 
pip install cbl-test-package==1.2.3
pip install cbl-test-package==2.3.4
"""

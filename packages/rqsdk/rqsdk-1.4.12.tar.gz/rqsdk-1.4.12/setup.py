# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import versioneer

version_map = {}
version_map["rqdatac"] = {
    "wcwidth",
    "tabulate",
    "requests",
    "cryptography>=2.9.2, <=36.0.2; python_version > '3.7'",
    "cryptography==2.9.2; python_version <= '3.6'",  # python 3.6.0有点过分,pip更新报错，cryptography版本太高也报错
    "click>=7.0",
    "pyjwt==1.7.1",
    "patsy>=0.5.1",
    "statsmodels>=0.12.1",
    "scipy <= 1.7.3; python_version <= '3.7'",
    "scipy >= 1.8.0; python_version >= '3.8'",
    "numpy>=1.19.5; python_version <= '3.6'",
    "numpy>=1.20.0; python_version == '3.7'",
    "numpy>=1.23.0; python_version >= '3.8'",  # numpy 1.23.0 修改了类型大小
    "pandas >= 0.24.2",
    "python-rapidjson <= 1.5; python_version <= '3.6'",  # rapidjson 1.6 开始不再提供 python 3.6 的 whl 包
    "rqdatac>=2.9.44",
    "rqdatac_fund==1.0.*,>=1.0.18"
}
version_map["rqfactor"] = version_map["rqdatac"] | {
    "ta-lib==0.4.20",
    "rqfactor==1.3.*,>=1.3.1",
}
version_map["rqoptimizer"] = version_map["rqdatac"] | {
    "ecos==2.0.10",
    "scs==2.1.4",
    "cvxpy==1.1.18 ; python_version == '3.6'",
    "cvxpy==1.2.0 ; python_version >= '3.7'",
    "osqp==0.6.2.post5",
    "rqoptimizer==1.2.*,>=1.2.17",
    "rqoptimizer2==1.2.*,>=1.2.17",
}
version_map["rqalpha_plus"] = version_map["rqfactor"] | {
    "rqalpha==4.14.1",
    "rqalpha-mod-option==1.1.*,>=1.1.20",
    "rqalpha-mod-optimizer2==1.0.*, >=1.0.8",
    "rqalpha-mod-convertible==1.2.*,>=1.2.15",
    "rqalpha-mod-ricequant-data==2.3.*,>=2.3.9",
    "rqalpha-mod-rqfactor==1.0.10",
    "rqalpha-mod-spot==1.0.*,>=1.0.9",
    "rqalpha-mod-fund==0.0.11",
    "rqalpha-mod-incremental==0.0.8",
    "rqalpha-plus==4.2.2",
    "rqrisk==1.0.5",
    "h5py>=3.0.0",
    "hdf5plugin",
    "matplotlib",
}

extras_require = {k: list(v) for k, v in version_map.items()}

with open('README.md', encoding="utf8") as f:
    readme = f.read()

with open('HISTORY.md', encoding="utf8") as f:
    history = f.read()

setup(
    name="rqsdk",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Ricequant Native SDK",
    long_description="",
    author="Ricequant",
    author_email="public@ricequant.com",
    keywords="rqsdk",
    url="https://www.ricequant.com/",
    include_package_data=True,
    packages=find_packages(include=["rqsdk", "rqsdk.*"]),
    install_requires=extras_require["rqdatac"],
    python_requires=">=3.6.1",
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "rqsdk = rqsdk:entry_point"
        ]
    },
)

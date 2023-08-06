"""
编译安装文件
"""

# -*- coding: utf-8 -*-
# @File    : setup.py

# 编译配置信息
from setuptools import setup, find_packages

reqs = []

setup(name='earth_brain_engine',
      version="V1.0",
      packages=find_packages(where='./src/'),  # 查找包的路径
      package_dir={'': 'src'},  # 包的root路径映射到的实际路径
      include_package_data=False,
      package_data={'data': []},
      description="Earth Brain Engine Package",
      author='LiuDonggang',
      author_email='1437309904@qq.com',
      url='http://127.0.0.1/geovis_earth_brain_engine/',
      license='MIT',
      install_requires=reqs  # rely on pip package
      )

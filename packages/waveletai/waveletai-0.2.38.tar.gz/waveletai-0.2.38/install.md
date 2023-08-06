### 1. 安装setuptools和whell三方库(已安装跳过)

python -m pip install --user --upgrade setuptools wheel

### 2.build 在setup同级目录下运行打包命令(sdist：达成源码包 dbist_wheel：打成whl包)
python setup.py sdist bdist_wheel

### 3.上传包

#### 3.1 下载twine三方库用于上传包(已安装跳过)

python -m pip install --user --upgrade twine

#### 3.2 上传包到生产环境。需要用到上面生产环境注册的账号。

python -m twine upload dist/*

python -m twine upload --repository testpypi dist/*

#### install
# pip install ./waveletai-0.1.0-py3-none-any.whl

#### 默认上传 minio提供下载使用
# pip install http://aiminio.xiaobodata.com/package/waveletai-0.1.0-py3-none-any.whl
#
# https://pypi.org/classifiers/
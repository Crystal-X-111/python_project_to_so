# 简介
## 该开源代码主要介绍了:
###1 如何将python工程所有python脚本一起通过cython编译成一个so，而不是将每个python脚本一个个都编译成独立的so。
###2 然后将编译好的so以wheel包的形式发布出去。用户只需要执行pip install wheel_package_name.whl就能把所有的依赖和so安装到自己的系统中。
###3 通过这种方式把python工程编译发布，可以有效地保护python源码不被看到。

# wheel包编译
`
./build_wheel
`

# wheel包安装
`
pip3 install maidabu-0.1-py3-none-any.whl
`

# 使用安装后的包
`
python3
from maidabu.main_module import TestModule
testmodule = TestModule()
testmodule.test_2()
testmodule.test_1() 
`



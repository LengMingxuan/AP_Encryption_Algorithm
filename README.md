# AP_Encryption_Algorithm
AP加密算法

![ ](https://img.shields.io/badge/Language-Python-blue?logo=python)  ![GitHub repo size](https://img.shields.io/github/repo-size/LengMingxuan/AP_Encryption_Algorithm?color=red)  ![GitHub last commit](https://img.shields.io/github/last-commit/LengMingxuan/AP_Encryption_Algorithm?logo=Code%20Climate)
### 算法原理
&nbsp;&nbsp;&nbsp;&nbsp;对于输入的字符串首先进行字符打乱，奇数位置上的字符存入l1列表，偶数位置上的字符存入l2列表，然后将l1列表中的字符倒置，与l2列表进行字符串拼接。之后采用移位加密方式再次加密，将每个字符分成两部分分别移位，加密结果长度为原字符串的2倍。
### 用法
#### 加密
```bash
python main.py -e -s "ABCD"
```
#### 解密
```bash
python main.py -d -s ABCD
```
### 举例
&nbsp;&nbsp;&nbsp;&nbsp;需加密的字符串为"`hello world`"，通过字符打乱变为"`el oldrwolh`",再通过移位加密的方式生成加密结果"KGDGPCAGDGLGNHIHAGDGHG"

&nbsp;&nbsp;&nbsp;&nbsp;同理，解密过程输入加密字符串"`KGDGPCAGDGLGNHIHAGDGHG`",解除移位加密，字符串变为"`el oldrwolh`"，再对打乱顺序的字符串复原，结果为"`hello world`"。

### 安全可行性分析

1. 数据

&nbsp;&nbsp;&nbsp;&nbsp;数据在计算机中，其实就是字节串。将被加密的数据，根据某些规则打乱可以进一步干扰，加大破解难度。
即破解者无法通过单一数学运算从中获取原始字符串。

2. 加解密

![](http://www.lengmingxuan.cn/wp-content/uploads/2021/06/ap.png)

3. 安全性

&nbsp;&nbsp;&nbsp;&nbsp;此算法的安全性在于进行了双重加密，在不考虑源码泄露的情形外，较难通过暴力破解得到k、N的值。

## License
![GitHub](https://img.shields.io/github/license/LengMingxuan/AP_Encryption_Algorithm)
<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg"></a>

本项目遵循`MIT license`，方便交流与学习，包括但不限于本项目的衍生品都禁止在损害他人利益情况下进行盈利。如果您发现本项目有侵犯您的知识产权，请与我取得联系，我会及时修改或删除。
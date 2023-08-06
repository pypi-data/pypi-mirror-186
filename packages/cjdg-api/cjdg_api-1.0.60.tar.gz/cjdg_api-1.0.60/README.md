# 超级导购接口

## 版本更新记录
----
|版本号|更新内容|更新时间|
|----|----|----|
|1.0|初始化|20210324|
## 为什么要写这个
- 这个工具用于快速调用超导内外部的接口
- 快速操作一些内部可以进行的操作
- 方便项目管理人员快速处理业务
## 如何使用

`pip install cjdg_api`
|模块|二级模块|三级模块|接口|接口说明|
|----|----|----|----|----|
|cjdg_api||||非公开接口，多数是抓包web分析而来|
|cjdg_open_api||||公开接口需要通过appsecret来使用|
|cjdg_api|pc|||PC端非公开接口|
|cjdg_api|pc|base||PC端基础请求模块，一般不使用，或者只使用其中的token接口|
|cjdg_api|pc|auth||PC端权限模块|
|cjdg_api|app|||移动端非公开接口|

## 可以操作哪些接口

### 开放平台接口

- 接口文档地址：http://env.xxynet.com/confluence/pages/viewpage.action?pageId=8120937

### 其它接口

### 说明

- cjdg_api:表示为超导未公开的接口，表示接口是通过抓包得到的
- cjdg_open_api:表示超导公开对外的接口
- pip install cjdg-api==1.0.26 -i https://pypi.org/simple

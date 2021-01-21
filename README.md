# 一个指定用途的打卡脚本

## 一、关于声明

### 1. 禁止用于破坏性行为

### 2. 别惹事，好好学习

### 3. 自己动手丰衣足食，别想着偷懒

### 4. 切记切记，一定要数据准确

### 5. 造成的不良后果，自行负责

## 二、更新日志

### 2020-11-05

即使如此其他人也要自行对比数据条，因为很多数据互相绑定的，因为单人环境，所以需要多组对比数据条并加以修改代码、测试后使用

### 2020-11-06

1. 修复部分函数传参问题
2. 经测试，全数据打卡已经可用

### 2020-11-07

1. 添加名单全数据表（name_table.json），以文件形式读取全部信息并执行
2. 增加定时任务功能
3. 增加日志功能
4. 添加启动sh文件

### 2020-11-12

1. 拆分部分函数
2. 部分数据打卡功能测试上线

### 2020-11-13

1. 添加每日打卡情况邮件报告功能
2. 优化启动文件

### 2020-11-14

1. 自动设置日志目录
2. 修改邮箱服务器
3. 优化部分逻辑

### 2020-11-16

1. 修复报告邮件发送异常的BUG
2. 测试快速打卡

### 2020-11-19

1. 验证快速打卡新思路

### 2020-11-26

1. 修改路径分隔符为/
2. plugin/zzut路径下加入zzut钉钉打卡链接获取(链接需要在钉钉手机app内打开)

### 2020-11-27

1. 拆分启动与功能部分
2. 添加功能测试文件

### 2020-11-28

1. 初步添加Centos8依赖程序安装脚本

### 2020-11-29

1. 添加关闭服务脚本
2. 添加脚本过程提示

### 2020-12-12

1. 随机分配打卡
2. 扩充启动脚本

### 2020-12-21

1. 捕获运行时异常
2. 提高容错

### 2020-12-22

1. 修复路径错误

### 2021-01-06

1. 删除全数据打卡
2. 添加配合[web]((https://github.com/WindSnowLi/PunchCardWeb))打卡的功能

### 2021-01-13

1. 优化日志存储
2. 修复浏览器驱动未关闭的BUG
3. 优化浏览器启动管理

---

## 三、开始与[web]((https://github.com/WindSnowLi/PunchCardWeb))部分合并

### 2021-01-17

1. 整体重构，优化项目目录
2. 改写部分功能

### 2020-01-19

1. 重构邮件报告提示

# Ventoy – 开源 U 盘启动盘制作工具，支持启动多个系统，还能当普通 U 盘保存文件[Win/Linux]
[小众软件 Ventoy – 开源 U 盘启动盘制作工具，支持启动多个系统，还能当普通 U 盘保存文件❲Win/Linux❳](https://www.appinn.com/ventoy/) 

[Ventoy](https://www.appinn.com/ventoy/) 是一款开源的，用来制作可启动 U 盘的 Windows 工具，使用简单，只需要将多个系统镜像 ISO 文件拷贝至 U 盘，即可自动创建包含多个系统的启动菜单，来安装操作系统。并且该启动 U 盘还能当普通 U 盘使用。@Appinn

![](assets/image_3.jpeg)

感谢 @ [懒洋洋的就趴在那里一动不动动不动动动](https://twitter.com/cryous/status/1253868388067115008) 的推荐。

都说一块 U 盘制作一个系统启动盘， **Ventoy** 最方便的地方就是你可以用它制作一块既能启动 Windows，也能启动 Linux 的启动盘，而且使用非常简单。

目前已测试过支持包括主流 Windows、服务器版 Windows、Debian、Ubuntu、CentOS、RHEL、Deepin，VMware ESXi 等系统 202 个，你要做的，只是下载系统镜像文件，然后直接拷贝进去就好了。 **Ventoy** 会帮助你自动创建启动菜单。

## 下载 Ventoy

首先，需要下载 **Ventoy** ，有 Windows 与 Linux 两个版本，下载地址位于 [GitHub](https://github.com/ventoy/Ventoy/releases) ，有能力的前往下载，青小蛙提供两个国内转运下载地址：

 
![](assets/image_1.png)
 
## 制作启动 U 盘

插入 U 盘之后， **Ventoy** 会自动识别，只需要点击 Install 即可，会两次提醒格式化将会删除 U 盘数据。

如果 **Ventoy** 有更新，点击 Update 更新即可。

![](assets/image_4.jpeg)

Linux 安装方式请参考 [官方文档](https://www.ventoy.net/cn/doc_start.html) 。

### 启动盘依旧是普通 U 盘

Ventoy 最酷的地方，是成为启动 U 盘之后，还可以当普通 U 盘使用，保存普通文件，不影响 Ventoy 功能。

## 复制系统 ISO 镜像文件

制作好的启动 U 盘，表面上看起来还是一块普通 U 盘，文件管理器里什么文件都没有：

![](assets/image_7.jpeg)

实际上，是因为 **Ventoy** 将 U 盘分为了两个分区：

![](assets/image_5.jpeg)

EFI 分区被隐藏，无需理会。

只需要将 ISO 文件拷贝到 U 盘里即可，比如青小蛙就直接将 Ubuntu 和 Windows XP 两个 ISO 系统镜像文件拷贝到了 Ventoy(E:) 盘下：

![](assets/image_2.jpeg)

Ventoy 会自动扫码 U 盘里的所有 ISO 文件，包括子文件夹，但不支持中文文件夹名称。

## 多系统启动

复制好系统镜像之后，直接拿去启动即可。

![](assets/image_6.jpeg)

青小蛙在虚拟机 [PD](https://partner.lizhi.io/appinn/parallels_desktop) 中测试成功，已经识别了两个 ISO 文件。选一个，就可以进入正常的系统安装流程了。

## Ventoy 特点列表：

* 开源、易用
* 快速 （拷贝文件有多快就有多快）
* 直接从 ISO 文件启动，无需解开
* 无差异支持 Legacy + UEFI 模式
* UEFI 模式支持安全启动 （Secure Boot）
* 支持超过 4GB 的 ISO 文件
* 保留 ISO 原始的启动菜单风格（Legacy & UEFI）
* 支持大部分常见操作系统, 已测试 200+ 个 ISO 文件
* 不仅仅是启动，而是完整的安装过程
* 提出 “Ventoy Compatible” 概念
* 支持插件扩展
* 启动过程中支持 U 盘设置写保护
* 不影响 U 盘日常普通使用
* 版本升级时数据不会丢失
* 无需跟随操作系统升级而升级 Ventoy

## 最后

至此，一个系统启动 U 盘、一个普通 U 盘合二为一的 Ventoy 启动盘已经制作完成，想要添加新的系统只需要更新 U 盘里的 ISO 系统镜像文件即可，也不影响当作普通 U 盘保存文件使用，非常方便。

青小蛙要给一个 [精选](https://www.appinn.com/category/featured/) ，Ventoy [官网在这里](https://www.ventoy.net/cn/index.html?ref=appinn) 。

- - - -

[©](http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds) 2019 青小蛙 for [小众软件](http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds) | [加入我们](http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds) | [投稿](https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds) | [订阅指南](http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds)
3659b075e72a5b7b1b87ea74aa7932ff
[点击这里留言、和原作者一起评论](https://www.appinn.com/ventoy/#comments) 收藏0

[https://www.appinn.com/ventoy/](https://www.appinn.com/ventoy/)

Sent with [Reeder](http://reederapp.com)

Sent from my iPad

#博客/小众软件
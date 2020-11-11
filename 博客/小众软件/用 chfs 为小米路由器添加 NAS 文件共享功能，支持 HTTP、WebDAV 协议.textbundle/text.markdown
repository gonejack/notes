# 用 chfs 为小米路由器添加 NAS 文件共享功能，支持 HTTP、WebDAV 协议
[小众软件 用 chfs 为小米路由器添加 NAS 文件共享功能，支持 HTTP、WebDAV 协议](https://www.appinn.com/cutehttpfileserver/) 

[CuteHttpFileServer](https://www.appinn.com/CuteHttpFileServer/) （简称 chfs）是一个免费的文件共享工具，它可以让运行 Windows、Linux、macOS 的设备变成文件服务器，通过 HTTP 网页，或者使用 WebDAV 协议访问共享文件。@Appinn

![](assets/image_2.jpeg)

CuteHttpFileServer（ [官网](http://iscute.cn/chfs) ） 的特性不少：

* 单个文件，核心功能无需其他文件
* 跨平台运行，支持主流平台：Windows，Linux 和 Mac
* 界面简洁，简单易用
* 支持扫码下载和手机端访问，手机与电脑之间共享文件非常方便
* 支持账户权限控制和地址过滤
* 支持快速分享文字片段
* 支持webdav协议

chfs 支持众多 CPU，可以在很多设备上使用，比如路由器、NAS、miniPC 等等，最早 @ **kuyucman** 同学在 [发现频道](https://meta.appinn.net/t/web/8051) 推荐了 chfs，但他的推荐太简单了，并没有引起别人的注意。@ **浪漫酱** 同学就不一样了，他 [分享了](https://meta.appinn.net/t/cutehttpfileserver-chfs-nas-http-webdav/13634) 在小米路由器上使用 chfs 的方法，并实现了自动启动、网页共享文件、WebDAV 协议支持，非常的实用。具体思路是这样的：

1. 小米路由器 R1D 刷开发版，开通 SSH 访问权限
2. 下载对应 chfs，R1D 是 chfs-linux-arm-2.0.zip
3. 配置 chfs（支持用户名密码访问、可配置 https、图片预览等）
4. 设置开机启动
5. 使用

具体教程、配置文件 [见这里](https://meta.appinn.net/t/cutehttpfileserver-chfs-nas-http-webdav/13634) 。

设置完成之后，会看到服务器信息：

![](assets/image_4.jpeg)

然后，就可以在浏览器访问路由器上的 chfs 地址，然后就能看到共享文件列表了：

![](assets/image_1.png)

而如果想要使用 [WebDAV](https://www.appinn.com/tag/webdav/) 协议，只需要在地址后面添加 /webdav 即可，比如 chfs 地址为 http://192.168.1.1:82，那么 WebDAV 地址就是 http://192.168.1.1:82/webdav

如果你愿意并且拥有公网 IP，还可以将这个端口开放给公网，让全世界都可以凭用户名密码访问你的小 NAS 服务器。以及，@浪漫酱 同学还说，他直接将 WebDAV 放到了公网上使用，非常的方便。

如果你也有小米路由器，或者其他型号的路由器（能获取 SSH、知道 CPU 型号），也可以折腾一下 CuteHttpFileServer，这样就能几乎 0 成本完成一个永久在线的文件共享服务，能做很多事情。

![](assets/image_3.png)
chfs 支持众多平台
- - - -

[©](http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds) 2019 青小蛙 for [小众软件](http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds) | [加入我们](http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds) | [投稿](https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds) | [订阅指南](http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds)
3659b075e72a5b7b1b87ea74aa7932ff
[点击这里留言、和原作者一起评论](https://www.appinn.com/cutehttpfileserver/#comments) 收藏0

[https://www.appinn.com/cutehttpfileserver/](https://www.appinn.com/cutehttpfileserver/)

Sent with [Reeder](http://reederapp.com)

#博客/小众软件
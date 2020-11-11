# Windows 程序包管理器：使用 winget 安装 Edge 浏览器[视频]
[小众软件 Windows 程序包管理器：使用 winget 安装 Edge 浏览器❲视频❳](https://www.appinn.com/use-winget-to-install-edge/) 

Windows 程序包管理器是微软刚刚发布的程序包管理器解决方案，包含了一款命令行工具 winget，主要面向开发者和软件提供商，用来搜索、安装、升级、删除和配置特选应用程序集，也就是说以后普通用户只需要敲击几下命令就能安装软件了，省去了传统搜索、下载软件安装包的过程。@Appinn

![](assets/image_1.jpeg)

注意目前的 Windows 程序包管理器和 **winget** 工具均为公共预览版，仅支持 Windows 10。

## 安装 winget

微软 [提供了](https://docs.microsoft.com/zh-cn/windows/package-manager/winget/) 有多种方式安装 winget，青小蛙是通过登记表格之后，在 Windows Store 自动安装。更简单的方式是 [在 GitHub 下载](https://github.com/microsoft/winget-cli/releases) 后直接安装。

建议使用新的 Windows 终端程序 [Windows Terminal](https://www.microsoft.com/zh-cn/p/windows-terminal/9n0dx20hk701#activetab=pivot:overviewtab) 而不是 **命令提示符** cmd，后者有点弱。

## winget 功能

目前 winget 有下列命令:

* **install** 安装指定的应用程序
* **show** 显示关于应用的信息
* **source** 管理应用源
* **search** 查找并显示应用的基本信息
* **hash** 哈希安装程序的帮助程序
* **validate** 验证清单文件
* **-v,–version** 显示工具的版本
* **–info** 显示工具的常规信息

然后，就是测试啦。

## 使用 winget 安装 Edge 开发者版本

这里青小蛙测试通过 winget 安装 Edge 的开发者版本，你就可以对比到与传统安装方式的区别。

1. 搜索程序包 **winget search edge**
2. 获得程序包 ID “Microsoft.EdgeDev”
3. 安装 **winget install Microsoft.EdgeDev**

![](assets/image_2.jpeg)

然后，就完成了 Edge 开发者版本的安装。

青小蛙录制了一段视频发布在 B 站：

大概就是这样了，开发者可以 [提交](https://github.com/microsoft/winget-pkgs/pulls) 自己的软件包给 Windows 程序包管理器，用户就可以通过 winget 安装程序了。感觉未来桌面操作系统的操作方式会越来越接近呀。

附链接：

* [Windows 程序包管理器（预览）](https://docs.microsoft.com/zh-cn/windows/package-manager/)
* [使用 winget 工具安装和管理应用程序](https://docs.microsoft.com/zh-cn/windows/package-manager/winget/)

感兴趣的同学快去试试吧，虽然目前来说还没什么大的卵用。

- - - -

## 相关阅读

* [微软 Edge 浏览器 正式发布 iOS 与 Android 版本](https://www.appinn.com/edge-for-ios-android/)
* [微软正式发布基于 Chromium 的浏览器 the New Microsoft Edge](https://www.appinn.com/the-new-microsoft-edge-base-chromium/)
* [基于 Chromium 的微软 Edge 浏览器泄漏，真香](https://www.appinn.com/chromium-based-microsoft-edge-for-windows/)
* [Muviz Edge – 利用屏幕边缘，可视化听歌❲Android❳](https://www.appinn.com/muviz-edge-for-android/)
* [如何在 Win10 中让 Edge 而非 IE 打开来自 QQ 的链接](https://www.appinn.com/ie-to-edge/)

- - - -

[©](http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds) 2019 青小蛙 for [小众软件](http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds) | [加入我们](http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds) | [投稿](https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds) | [订阅指南](http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds)
3659b075e72a5b7b1b87ea74aa7932ff
[点击这里留言、和原作者一起评论](https://www.appinn.com/use-winget-to-install-edge/#comments) 收藏0

[https://www.appinn.com/use-winget-to-install-edge/](https://www.appinn.com/use-winget-to-install-edge/)

Sent with [Reeder](http://reederapp.com)

#博客/小众软件
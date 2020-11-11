# Stroke – 开源鼠标手势软件[Windows]
[小众软件 Stroke – 开源鼠标手势软件❲Windows❳](https://www.appinn.com/stroke-for-windows/) 

**Stroke** 是一款开源的鼠标手势软件，小巧（主程序 74KB）、速度快，可通过插件扩展功能。@ [Appinn](https://www.appinn.com/stroke-for-windows/)

![](assets/image_1.jpeg)

来自 [发现频道](https://meta.appinn.net/t/topic/18180) ， [Screenote – 全快捷键截图、贴图工具❲Windows❳](https://www.appinn.com/screenote-for-windows/) 的开发者 @ [Poerin](https://meta.appinn.net/u/Poerin) 同学的又一款作品。

Stroke 在 [GitHub](https://github.com/poerin/Stroke) 开源，支持 C# 语言编写脚本，可使用 .NET Framework 及自己编写 dll。初次使用建议先 [阅读操作手册](https://docs.shuax.com/MouseInc/#/) 。

## 主要功能如下：

* 鼠标手势：按住右键滑动即可开始使用。
* 配置细微，可自由修改手势宽度，颜色，识别灵敏度等。
* 支持黑名单，支持特定软件自定义手势，支持复合动作。

### 例子

选中一个网址，画 P 直接打开 ping 命令。
选中文本以后，画 S 直接打开浏览器搜索。

### 高质量截图

这个截图可以保留窗口阴影，半透明（包括 win7 和 win10 的毛玻璃特效）。
可以保留鼠标指针形状，可以加入透明网格特效。按下 Ctrl+PrtSc 可以快速体验。

### 贴图

可以把截图半透明置顶显示在屏幕上，方便参考内容或对比。
鼠标手势画一个四边形（下右上左）即可体验。

### OCR文字识别

鼠标手势画一个四边形（下左上右）即可体验。

### 按键回显

可在屏幕上显示您所有的键盘按键，方便您在录制视频包含按键信息。绝对不要在输入密码的时候打开这个功能！

### 边缘滚动

在屏幕四边滚动滚轮，可以触发特殊操作。
目前有音量调节和程序切换功能。

### 复制增强

选中文字快速按下两次 Ctrl+C 后，会弹出一个快捷操作菜单，可以进行搜索等。

### 快速音量调节

按住 Alt 时，滚动滚轮可以快速调节音量大小。

### 滚轮穿透

可使得滚轮可以直接滚动未激活窗口。
Win10 自带此功能，推荐老系统 Win7 开启。

### 自然滚动

把内容滚动方向改变为随屏幕方向。
保持和 macOS 一致（滚轮反向）。

- - - -

需要管理员权限运行 Stroke，之后就和你想象中的鼠标手势工具一样使用，当然设置起来要…门槛高一些。

![](assets/image_5.jpeg)
运行 Stroke.Configure.exe 配置
@Poerin 同学还提供了一些截图：

![](assets/image_3.gif)

![](assets/image_4.gif)

关于 Stroke 的速度，Poerin 专门做了测试：

- - - -

那么 Stroke 反应有多灵敏呢？从鼠标弹起，开始判别是否在任何动作包中触发了相应的动作，到执行手势完成，我们来看看花了多少时间（13 年买的 i5 笔记本）。
我们在以下两个位置插入记录时间的代码：

![](assets/image_6.png)

测试 5 轮结果如下， [Ticks](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.ticks?view=netframework-4.7.2) 是以 100 纳秒（1 ns = 10^(-9) s）为单位计数的：

Start:637372381902555779
End:637372381902595758
Start:637372381947865912
End:637372381947905872
Start:637372381966984207
End:637372381967024144
Start:637372381983986626
End:637372381984046605
Start:637372382038631758
End:637372382038661736

即 分别得到 39979、39960、39937、59979、29978，即大概是 4毫秒、4毫秒、4毫秒、6毫秒、3毫秒。（1秒 = 1000 毫秒）。

取决于你的使用滚轮的手速和火狐的反应，你可以：

![](assets/image_2.gif)

而关于定制，@Poerin 提供了一个 [百度翻译的脚本](https://meta.appinn.net/t/topic/18180/9?u=qingwa) 。

总之这是一款定制性很高，但门槛也略高的鼠标手势工具，帖子里的信息量很大， 不少同学还推荐里其他手势软件， [欢迎围观](https://meta.appinn.net/t/topic/18180) 。

官网： [https://shuax.com/project/mouseinc/?ref=appinn](https://shuax.com/project/mouseinc/?ref=appinn)

- - - -

## 相关阅读

* [Tabler Icons – 558 个可完全自定义的免费 SVG 图标](https://www.appinn.com/tabler-icons-online/)
* [为什么要使用 Windows 10 的 214 条理由](https://www.appinn.com/why-are-there-214-reasons-to-use-windows-10/)
* [微软的 150 款免费软件❲部分，待更新❳](https://www.appinn.com/ultimate-list-of-free-windows-software-from-microsoft/)
* [8 款漂亮的 Windows 7 主题桌面](https://www.appinn.com/8-windows-7-themes/)
* [Ultimate Windows Tweaker 3.0 for Windows 8 系统微调工具](https://www.appinn.com/ultimate-windows-tweaker-3-0-for-windows-8/)

- - - -

[©](http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds) 2019 青小蛙 for [小众软件](http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds) | [加入我们](http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds) | [投稿](https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds) | [订阅指南](http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds)
3659b075e72a5b7b1b87ea74aa7932ff
[点击这里留言、和原作者一起评论](https://www.appinn.com/stroke-for-windows/#comments) 收藏0

[https://www.appinn.com/stroke-for-windows/](https://www.appinn.com/stroke-for-windows/)

Sent with [Reeder](http://reederapp.com)

#博客/小众软件

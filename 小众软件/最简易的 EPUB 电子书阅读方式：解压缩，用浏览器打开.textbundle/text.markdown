# 最简易的 EPUB 电子书阅读方式：解压缩，用浏览器打开
[小众软件 最简易的 EPUB 电子书阅读方式：解压缩，用浏览器打开](https://www.appinn.com/epub-reader-easy/) 

自从微软把最好的 EPUB 电子书阅读器 edge 砍掉之后，满世界都是寻找 EPUB 阅读器的 [帖子](https://meta.appinn.net/t/edge-epub-pc-epub/11434) ，但似乎大家都不是很满意。直到 @ *[ricoeur](https://meta.appinn.net/u/ricoeur)* 说： [最简易的 epub 阅读方式，解压，浏览器](https://meta.appinn.net/t/epub/15401) 。

![](assets/image_1.jpeg)
Photo by [Anthony Tran](https://unsplash.com/@anthonytran?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/read-book?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)
- - - -

@ **ricoeur** 是这样说的：

自 edge 更新之后，新的 EPUB 阅读工具虽多，但都不如 edge 那种随时能用、用完即抛的感觉。

收费的且不说。

现在做个软件都想着帮你管理文档，不导入没法阅读，还要多平台同步。现在大家天天宅在家里，守着电脑，谁看那个小屏幕，多憋屈。

也许是看不到盈利方向，才没有人做那种简易的阅读器

试了那么多，最后觉得最好用的是，改后缀，直接变成 ZIP 格式，解压，找到网页文档，直接用浏览器阅读，一下子爽了。

下面是青小蛙搜索了一个 EPUB 电子书，解压缩之后的全部文件结构，其中电子书正文在 OEBPS 文件夹内，只需要打开 **xxx_body.html** 文件就能阅读内容了。

.
├── META-INF
│ └── container.xml
├── **OEBPS**
│ ├── GeographyofBli.ncx
│ ├── GeographyofBli_body.html
│ ├── GeographyofBli_copyright.html
│ ├── GeographyofBli_opf.opf
│ ├── GeographyofBli_toc.html
│ ├── cover.xml
│ ├── css
│ │ └── GeographyofBli_style.css
│ └── images
│ ├── Art_P333.jpg
│ ├── GeographyofBli-cover.jpg
│ └── Thumbs.db
└── mimetype

又及：说到底 EPUB 就是个网页文件夹打包，那就还原为网页。浏览器插件固然不错，总要借助，在线的要上网，或许功能多些（ie6 可能不支持 XHTML 格式，我用的是 Firefox75，另外两个浏览器是 edge Chrome版，vivaldi）。如果只是看下，我倒是看好 PC 上的 WPS，WPS 的个人版已经支持 epub，并且可以换底色，改字体，尽管还是不能复制。

我无意争论那个最好，大家提到的我大都尝试过，只是最近弄一个60多兆的 epub 文件，等待打开等的有点烦，才会想起来解压缩这个大招。复制出来（选择复制，是不想要某些无关的图片，而且为后面的处理打下好的基础，其实可以用导入网页文件的方式导入到笔记软件，我用的 mybase），想怎么处理就怎么处理。

- - - -

那么问题来了，你觉得“最好”的 EPUB 阅读器是什么呢？

- - - -

## 相关阅读

* [Neat Reader – 可能是「最独特」的桌面端在线电子书阅读器](https://www.appinn.com/neat-reader/)
* [❲AIR❳Lovely Reader – ePub 电子书阅读器](https://www.appinn.com/lovelyreader-epub-reader-air/)
* [Foxit Reader 3.0 发布，十分出色的 PDF 阅读器](https://www.appinn.com/foxit-reader-30/)
* [福昕阅读器 – 知名 PDF 阅读器](https://www.appinn.com/foxit-pdf-reader-6/)
* [Easy to RSS – 能发现 RSSHub（RSS 生成工具）订阅地址的 RSS 工具 ❲Chrome❳](https://www.appinn.com/easy-to-rss/)

- - - -

[©](http://www.appinn.com/copyright/?utm_source=feeds&amp;utm_medium=copyright&amp;utm_campaign=feeds) 2019 青小蛙 for [小众软件](http://www.appinn.com/?utm_source=feeds&amp;utm_medium=appinn&amp;utm_campaign=feeds) | [加入我们](http://www.appinn.com/join-us/?utm_source=feeds&amp;utm_medium=joinus&amp;utm_campaign=feeds) | [投稿](https://meta.appinn.com/c/faxian/?utm_source=feeds&amp;utm_medium=contribute&amp;utm_campaign=feeds) | [订阅指南](http://www.appinn.com/feeds-subscribe/?utm_source=feeds&amp;utm_medium=feedsubscribe&amp;utm_campaign=feeds)
3659b075e72a5b7b1b87ea74aa7932ff
[点击这里留言、和原作者一起评论](https://www.appinn.com/epub-reader-easy/#comments) 收藏0

[https://www.appinn.com/epub-reader-easy/](https://www.appinn.com/epub-reader-easy/)

Sent with [Reeder](http://reederapp.com)

#博客/小众软件
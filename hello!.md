#  ==Hello 文洋==

###**关于阶段二的笔记**

1. ==git的下载== 我直接在官网打开下载链接的方法行不通（会像打开GitHub一样请求超时🤷‍♂️）

我十分不理解，我在csdn与b站搜索下载方法，最终发现打开 pc.qq腾讯的下载网站可以顺利下载

2. ==本地项目上传到GitHub的远程仓库==  在看了各个博主的方法后我总结的大致思路：

   1. 在本地创建一个版本库（即文件夹），通过`git init`把它变成Git仓库；

   2) 把项目复制到这个文件夹里面，再通过`git add .`把项目添加到仓库；

   3. 再通过`git commit -m "注释内容"`把项目提交到仓库；

   4. 在Github上设置好SSH密钥后，新建一个远程仓库，通过`git remote add origin 远程仓库地址`将本地仓库和远程仓库进行关联；

   5. 最后通过`git push -u origin master`把本地仓库的项目推送到远程仓库（也就是Github）

   

3. ==遇到的困难：==

   + ~~GitHub任基本打不开 ~~~

   + git需使用不熟悉的Linux命令行执行，总是出现各种意料之外的错误^。^<img src="C:\Users\阿ven\AppData\Roaming\Typora\typora-user-images\image-20211102195715265.png" alt="image-20211102195715265" style="zoom: 80%;" /><img src="C:\Users\阿ven\AppData\Roaming\Typora\typora-user-images\image-20211102200036238.png" alt="image-20211102200036238" style="zoom: 67%;" />


 4.  ==终于我解决==了^但没完全解决^   **！！！** （气急败坏下我开通了VPN 进GitHub的速度快得一）
+  解决的part：为了保证至少能远程上传至GitHub==我新建了一个仓库‘try again’==

​     **第一次远程关联该仓库上传是并未成功** 于是我又远程关联了第一个仓库==‘Tasks’==并push结果刷新后

​     **看见了本地项目‘hello.md’出现在了==try again’==** 不知道是时间问题还是什么问题

+ 需解决的part: *** 弄清如何远程传送至第一个仓库‘Tasks’***

  
  
  
  
  ==新发现== 原来我的hello已经发送到仓库==‘Tasks’==了但是 是其中的**master** 分支这是为啥？
  
  （虽然还不知道为什么但离成功又近了一步了^ ^）
  
  破案了master和main是一个仓库的两个分支 我在考虑要不要合并他俩
  
  

​     


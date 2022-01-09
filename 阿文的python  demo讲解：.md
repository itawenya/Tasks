# 阿文的python -demo讲解：

### 图片的套娃

众所周知啊，图片是由一个一个像素组成的，这个思路就是

用图片替代像素，以此来组成图片套娃

那我的目标呢就是用这张作为子图片：

![imgchild.jpg](https://github.com/itawenya/Tasks/blob/main/imgchild.jpg?raw=true)

这张作为父图片：

![imgparent.jpg](https://github.com/itawenya/Tasks/blob/main/imgparent.jpg?raw=true)

不多BB 先上结果![imgout.jpg](https://github.com/itawenya/Tasks/blob/main/imgout.jpg?raw=true)

根据网上讲解的具体原理大致流程是：    


选取父图片→将父图片用PIL中的Img转为灰度（大概？）→用循环将子图片替代    
其中PIL是python的第三方库可以通过 Windows的命令行输入`pip install pil`  
或者在pycharm中的settings里添加  


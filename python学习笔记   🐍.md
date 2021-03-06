



# python学习笔记   🐍

​                                                                                                                                                 ---是阿文呀

### 0️⃣我认为python语言几个鲜明的特点

1. **语法相对简单。**  

   一个很直观的对比，让我们来看看c和python的“hello world”

```c
#include<stdio.h>
int main()
{
printf("Hello World!\n");
}
```

```python
print('Hello world!')
```



2. **python强调缩进的规范以控制类而非大括号{}。** 

```python
   if True:
       print('一般四个空格为一组缩进/TAB键同样的效果')
   else:
     print('假如这样缩进不一就会报错')
```



3. **拥有丰富的内置函数以及第三方库**



###  1️⃣python的基础语法

   （当然有很多，我也不需要全都列举。这里挑一些我觉得有意思的记。）

1. **python的注释： **
   + 单行注释： （#）
   
   + 多行注释： 三个单引号（’‘’）或三个双引号（“”“）



2. **模块的引入：** `import 模块名` 或者 `from 模块名 import 属于前一个大模块的某个小模块`



3. **python的保留字。**与C语言一样指在高级语言中已经定义过的字，使用者不能再将这些字作为变量名或过程名使用。在python中可以通过以下命令查看

```python
import keyword
keyword.kwlist
```



4. **变量的命名。** 变量名必须是大小写英文、数字和’_‘的组合，且不能以数字开头。

（但似乎新版本确实已经的确可以用汉字做变量名了，不推荐使用）



5. **IF条件判断。**

```
b = 2
if b == 2:
	print('你这个2B')
elif b == 1:
	print('python的语句真会偷懒呢')
else:
	print('连else if都要缩写成elif😂')
```

根据python的缩进规则，如果**If** 语句判断是**True**，

就把缩进的语句执行



6. **python中的循环。** 二者的特征呢也很好区分，请看我写的例子：

   + for循环

   ```
   for i in range(10):
   	print('将此内容循环10此并输出这句话')
   ```

   

   + while循环

   ```
   count = 0
   while count <10:
   	print('将此内容循环10此并输出这句话')
   	count += 1
   ```

   一般而言呢for循环是能明确知道要循环多少次的，而

   while循环适合满足情况下不需要知道循环多少次的情况。



### 2️⃣python中的数据类型

 python的基本数据类型一共有6种分别是：

**其中前三种是不可变的！！！**

1. Num（数字）
   + int整型
   + float浮点型
   + bool布尔型  （其中True=1 False=0）
   + complex复数 （形如 1+2j）

2. Str（字符串）
   + 用单引号（‘ ’）或者双引号（” “）
   + 有两种索引方式：从左到右（0开始），从右到左（-1开始）
   + 可以进行切片： str[第一组数字包括起始位置:第二组数字不包括结束位置:第三组数字表示步长]

3. Tuple（元组）

   + 写在小括号内（ ）用逗号隔开，元素类型可以不同

     🛑如果只有一个元素也记得加逗号

   + 同样可以索引切片

4. List（列表）
   + 写在中括号内[ ] 用逗号隔开，元素类型可以不同
   + 同样可以索引切片

5. Sets（集合）
   + 无序且不重复
   + 可以用{ }来创建包含元素的集合，或者用（ ）来创建空元素的集合

6. Dict（字典）
   + 是一个无序的键值对的集合
   + 声明格式： dic={key：value；键：值}



### 3️⃣python的一些内置的操作函数

既然上面刚讲了六大基本数据类型

那我们就以与数据类型相关的函数引入吧

![py.png](https://github.com/itawenya/Tasks/blob/main/py.png?raw=true)

不难发现我们通过函数`str( )`将变量wy从整型变成了字符串并将其付给了变量pp



**在python中有许许多多形如`str()`的不同功能的内置函数实现不同的功能**

<img src="https://github.com/itawenya/Tasks/blob/main/%E5%87%BD%E6%95%B0.png?raw=true" alt="函数.png" style="zoom: 80%;" />



:car:当然这么多函数的用法不需要全都背下来

我们可以通过 `help(这里输入你想知道的函数名)`便可以查看用法:bookmark_tabs:



💢当然除了内置函数我们还可以自己定义函数

```python
def 函数名(参数，可以是多个)：
	这里写函数内容
最后可以有return也可以没有
```



### 4️⃣面向对象程序设计🐘🐘Object-Oriented-Programming

首先我们来看看百度对OOP的概念：

**面向对象程序设计(Object Oriented Programming)作为一种新方法，其本质是以建立模型体现出来的抽象思维过程和面向对象的方法。模型是用来反映现实世界中事物特征的。任何一个模型都不可能反映客观事物的一切具体特征，只能对事物特征和变化规律的一种抽象，且在它所涉及的范围内更普遍、更集中、更深刻地描述客体的特征。通过建立模型而达到的抽象是人们对客体认识的深化。**

然后来记一下名词：

+ 对象（object）：可以对其做事情的一些东西。
+ 类（class）： 一个共享相同结构和行为的对象的集合。定义了一类事情的抽象特点。
+ 封装（encapsulation）： 将数据和操作捆绑在一起，创造出一个信的类型的过程。将接口与实现分离的过程。
+ 继承： 类之间的关系，在这种关系中，一个类共享了一个或多个其他类定义的结构和行为。



接下来是面向对象的三大特征：

+ 封装——类的集合
+ 继承——通用的标准
+ 多态——各式各样



🎃这些概念看起来都十分的抽象，我想到一个联系实际的类比：

类——手机的设计图纸📮

封装——将手机硬件打包好，用户在使用时即可使用现成的。📱

继承——通用的标准，比如充电口，电源开关摁键。🎹

多态——在继承的基础上手机的个性化的特征，比如刘海屏，全面屏，实体home键





### 5️⃣文件操作 

**File**        open（ ）函数常用的形式

就是接受两个参数： open（file，mode=’ ？ ‘）



**文件名（file）**：输入文件路径（绝对或相对路径）

**模式（mode）**：常用的模式 （如果不写默认是只读模式 ’r‘ ）

+ r    以只读模式打开
+ w   创建模式，若文件存在则覆盖旧文件
+ a    可追加模式，新数据会写到文件末尾



当然以上模式是针对文本文件的打开书写，面对视频图像文件需要：

**二进制模式打开** （十分类似，这里的加上的b其实就是’bytes‘字节）

+ rb  2进制以只读模式打开
+ wb 2创建模式，若文件存在则覆盖旧文件
+ ab 2进制可追加模式，新数据会写到文件末尾


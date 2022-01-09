from PIL import Image
#fill_img_with_img: 把imgParent中的每个像素用imgChild代替 两个参数均为PIL图像

def taowa(imgparent,imgchild):
    #创建一个空的图片
    imgsize = (imgparent.width*imgchild.width,imgparent.height*imgchild.height)
    imgout = Image.new('L',imgsize,'white') #48x48

    #用图片代替像素
    for w in range(imgparent.width):
        for h in range(imgparent.height):
            if imgparent.getpixel((w,h)) < 127:
                imgout.paste(imgchild,(w*imgchild.width,h*imgchild.height))
    return imgout

if __name__=="__main__":
    #读取图片文件
    imgparent = Image.open('imgparent.jpg')
    imgparent = imgparent.convert('L')
    imgchild = Image.open('imgchild.jpg')
    imgchild = imgchild.convert('L')
    #生成套娃
    imgout = taowa(imgparent,imgparent)
    imgout = taowa(imgparent,imgchild)
    #结果保存为图片
    imgout.save('imgout.jpg')

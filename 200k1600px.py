from PIL import Image
import os

def compress_images(folder_path, target_size, target_height):
    # 获取文件夹内所有图片文件
    images = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]
    n = 0
    for file_name in images:
        file_path = os.path.join(folder_path, file_name)
        
        # 打开图片
        image = Image.open(file_path)

        # 控制高度
        width, height = image.size
        if height > target_height:
            width = int((target_height / height) * width)
            height = target_height
            image = image.resize((width, height))

        # 设置压缩质量（0-100），100表示无损压缩
        quality = 100
        
        # 压缩图片并保存
        image.save(file_path, optimize=True, quality=quality)

        # 检查文件大小是否满足目标大小
        while os.path.getsize(file_path) > target_size * 1024:
            # 如果文件大小超过目标大小，则进一步降低压缩质量
            quality -= 5
            image.save(file_path, optimize=True, quality=quality)
        n += 1
    print("数量：" + str(n))
    print("压缩完成，按下任意键关闭窗口...")
    input()  # 等待用户输入


# 指定文件夹路径和目标文件大小（以KB为单位）
path = os.getcwd()
size = 200
height = 1600

# 调用函数进行压缩
compress_images(path, size, height)
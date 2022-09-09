import os


exclude_dir = {'编程资料'}


def scan_file(path, level, target):
    filenames = os.listdir(path)  # 返回path目录下的所有文件名称
    for filename in filenames:
        cur_path = path + "/" + filename
        if level == 0:
            cur_path = filename
        if os.path.isdir(cur_path):  # 子文件
            target.write("{blank}- {dir_name}\n".format(blank=' ' * 2 * level, dir_name=filename))
            scan_file(cur_path, level + 1, target)
        elif level != 0 and filename[0] != '.' and filename.endswith('.md'):
            target.write("{blank}- [{filename}]({cur_path})\n".format(blank=' ' * 2 * level, filename=filename,
                                                                      cur_path=cur_path))


# 生成sidebar 文件
def gen_sidebar():
    print("开始生成sidebar文件\n")
    os.chdir('docs')
    with open("_sidebar.md", "w") as f:
        scan_file(".", 0, f)


if __name__ == '__main__':
    gen_sidebar()

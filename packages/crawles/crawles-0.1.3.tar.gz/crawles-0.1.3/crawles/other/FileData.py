class FileData:
    def __init__(self, filename):
        self.filename = filename
        try:
            f2 = open(self.filename, 'r', encoding='utf-8')
            self.file_list = eval(f2.read())
            f2.close()
        except FileNotFoundError:
            f2 = open(self.filename, 'w+', encoding='utf-8')
            f2.write('[]')
            f2.close()
            self.file_list = []

    def add_id(self, video_id):
        """数据的添加"""
        self.file_list.append(video_id)
        self.data_save()

    def select_id(self, video_id):
        """判断id是否存在"""
        if video_id in self.file_list:
            return True
        else:
            return False

    def data_save(self):
        """数据报错"""
        f1 = open(self.filename, 'w+', encoding='utf-8')
        f1.write(str(self.file_list))
        f1.close()


file_data = FileData

if __name__ == '__main__':
    f = FileData('data.txt')
    f.add_id('a')  # 添加id
    f.select_id('a')  # 查询id

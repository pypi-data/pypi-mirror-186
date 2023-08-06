title = '\033[1;33;3m'
code = '\033[1;34;3m'
sub = '\033[1;38;3m#'
end_ = '\033[0m'


class HelpDoc:
    @property
    def data_save(self):
        return f'''{title}crawles.data_save 数据存储{end_}

    {sub}crawles.data_save.image_save 单张图片保存方法 以下代码为使用案例{end_}
        {code}crawles.data_save.image_save(图片的链接，图片的保存位置){end_}
    
    {sub}crawles.data_save.images_save 多张图片保存方法 以下代码为使用案例{end_}
        {code}crawles.data_save.images_save([
                     [图片的链接，图片的保存位置] ,
                     [图片的链接，图片的保存位置] ,
                     [图片的链接，图片的保存位置] ,
                     [图片的链接，图片的保存位置] ,
                    ]){end_}
    
    {sub}crawles.data_save.sql_save mysql保存数据到数据库 以下代码为使用案例{end_}
        {code}db = sql_save.connect(user='root',  # 账号
                              password='000000',  # 密码
                              database='python_mysql',  # 需要连接的数据库名字
                              table='table'  # 需要操作的表)
                              
        # ['url_id', 'url_title', 'url_author'] 为字段名数据 [1, 2, 3] 为需要插入的数据
        db.save(['url_id', 'url_title', 'url_author'], [1, 2, 3])
        db.close()  # 关闭数据库{end_}
    
    
    {sub}crawles.data_save.mongo_save mongo保存数据到数据库 以下代码为使用案例{end_}
        {code}db = mongo_save.connect(host='localhost',  # 主机名 127.0.0.1
                                port=27017,  # 端口
                                database=None,  # 需要连接的数据库名字
                                table=None  # 连接表的名称)'''+'''
    
        dict_data = {'index': 1}
        db.insert_one(dict_data)  # 插入一条数据
        
        list_data = [{'index': 1}, {'index': 2}, {'index': 3}]
        db.insert_many(list_data)  # 插入多条数据
        db.close() # 关闭数据库{end_}'''+f'''
    
    
    {sub}crawles.data_save.csv_save csv_save保存数据到csv文件 以下代码为使用案例{end_}
        {code}csv_obj = csv_save('data.csv', mode='w+')
        csv_obj.head(['1', '2', '3', '4'])  # 写入一条字段数据
        csv_obj.writerow(['a', 'b', 'c', 'd'])  # 写入单条数据
        csv_obj.writerows([['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']])  # 写入多条数据
        csv_obj.close()  # 关闭文件
        # 上下文管理操作示例
        with csv_save('data.csv', mode='w+') as csv_obj:
            csv_obj.head(['1', '2', '3', '4'])  # 写入一条字段数据
            csv_obj.writerow(['a', 'b', 'c', 'd'])  # 写入单条数据
            csv_obj.writerows([['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']])  # 写入多条数据
        csv_obj.close()  # 关闭文件{end_}'''

    @property
    def api(self):
        return f'''{title}crawles.api 请求方法{end_}
        
    {sub}以下请求都具备:
        head_data 数据如果为字符串自动清洗为自动格式/如果没有User-Agent则自动添加
        head_data = 字典数据/字符串文本数据
        # 如果为字符串自动清洗为自动格式/自动判断请求和数据是否传输错误
        params/data = 字典数据/字符串文本数据
        **kwargs(其他爬虫参数都可以正常使用)
    {end_}
        
    {sub}crawles.get get请求{end_}
        {code}url ='https://www.xxxxx.com/'
        head_data = 字典数据/字符串文本数据
        param = 字典数据/字符串文本数据
        crawles.get(url,
                    headers=head_data,
                    params=param,
                    **kwargs(其他爬虫参数)){end_}
     
    {sub}crawles.post post请求{end_}
        {code}url ='https://www.xxxxx.com/'
        head_data = 字典数据/字符串文本数据
        data = 字典数据/字符串文本数据
        crawles.post(url,
                    headers=head_data,
                    data=data,
                    **kwargs(其他爬虫参数)){end_}
    
    {sub}crawles.session_get session_get请求{end_}
        {code}# session_get无需创建对象，可以直接使用
        url ='https://www.xxxxx.com/'
        head_data = 字典数据/字符串文本数据
        param = 字典数据/字符串文本数据
        crawles.session_get(url,
                    headers=head_data,
                    params=param,
                    **kwargs(其他爬虫参数)){end_}
                
    {sub}crawles.session_post session_post请求{end_}
        {code}# session_post无需创建对象，可以直接使用
        url ='https://www.xxxxx.com/'
        head_data = 字典数据/字符串文本数据
        data = 字典数据/字符串文本数据
        crawles.session_post(url,
                    headers=head_data,
                    data=data,
                    **kwargs(其他爬虫参数)){end_}'''

    @property
    def other(self):
        return f'''{title}crawles.other 常用辅助方法{end_}
        
    {sub}crawles.decorator_thread 装饰在函数,可以使函数异步运行{end_}
        {code}@crawles.decorator_thread
        def func(参数):
            time.sleep(3){end_}
              
    {sub}crawles.execjs js函数封装{end_}
        {code}js = execjs('wb.js')
        # 使用js函数
        rest = js.call('func/函数名', '参数1', '参数2', '参数......'){end_}        
             
    {sub}crawles.head_format 格式化请求参数为字符串 api请求都自带了该清洗函数{end_}
        {code}data = ''"             
        type: 0                
        formhash: CDD4E5BDEA    
        ''"
        print(head_format(data)) '''+'''
        结果:{'type': '0', 'formhash': 'CDD4E5BDEA'}'''+f'''
        {end_}
        
    {sub}crawles.head_format 格式化请求参数为字符串 api请求都自带了该清洗函数{end_}
        {code}data = ''"             
        type: 0                
        formhash: CDD4E5BDEA    
        ''"
        print(head_format(data)) '''+'''
        结果:{'type': '0', 'formhash': 'CDD4E5BDEA'}'''+f'''
        {end_}
        
    {sub}crawles.file_data 记录数据使用情况，可以记录视频文件是否已经下载，从而且进行增量获取{end_}
        {code}f = file_data('data.txt')
        f.add_id('a')  # 添加id
        f.select_id('a')  # 查询id
        {end_}
        
    '''

    def __str__(self):
        return f'''{sub}通过‘print(crawles.help_doc.xxxxx)’查看方法使用详情{end_}
{title}help_doc.api                     请求方法{end_}
    {sub}.get                        get请求{end_}
    {sub}.post                       post请求{end_}
    {sub}.session_get                session_get请求{end_}
    {sub}.session_post               session_post请求{end_}

{title}help_doc.data_save               数据存储方法{end_}
    {sub}.data_save.image_save       图片存储{end_}
    {sub}.data_save.sql_save         mysql存储{end_}
    {sub}.data_save.mongo_save       mongodb存储{end_}
    {sub}.data_save.csv_save         csv存储{end_}

{title}help_doc.other                   常用辅助方法{end_}
    {sub}.execjs                     js调用{end_}
    {sub}.decorator_thread           多线程装饰器{end_}
    {sub}.head_format                请求信息格式化字典格式{end_}
    {sub}.file_data                  文件数据记录{end_}

'''

    @staticmethod
    def _colour():
        s = "hello, world"
        print('\033[1;31;3m%s\033[0m' % s)
        print('\033[1;32;3m%s\033[0m' % s)
        print('\033[1;33;3m%s\033[0m' % s)
        print('\033[1;34;3m%s\033[0m' % s)
        print('\033[1;35;3m%s\033[0m' % s)
        print('\033[1;36;3m%s\033[0m' % s)


help_doc = HelpDoc()

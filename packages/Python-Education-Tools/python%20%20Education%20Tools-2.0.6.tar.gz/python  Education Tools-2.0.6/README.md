![Python与数据分析及可视化](https://imgservice.suning.cn/uimg1/b2c/image/gIH3lXgAHfqhSFy_QvLmpQ.jpg_800w_800h_4e)
# Prof.Li's Python Education Tools

## Author: 道法自然  lilluqun@gmail.com

## **模块安装：pip install -U python-education-tools**

* Python Education Tools模块为教材配套工具。模块由作者Prof.Luqun Li团队自主开发 。
* 模块简称“pet工具”。取Python Education Tools 首字母的缩写pet（英文意思：宠物），希望该工具成为大家学习的宠物！。
* 所有工具包的根目录是pet。模块安装后对应的安装包为 pet.data.* 、pet.textbook1.*等。
* 该模块提供了教学相关代码工具、数据生成工具，以及所有教学案例等。
* 模块安装后，可使用一行Python代码获取本书教学案例：import pet.textbook1.codes ，即可将教学案例下载到Windows用户桌面。
* 作者会对模块不断更新，确保为读者提供最佳的代码工具、教学案例与服务。
* 其他教学资源可以参见GitHub：https://github.com/liluqun。


* 今后会根据大家的需求，不断扩充相关教学相关工具和数据集。如果您有好的建议，请发邮件到liluqun@gmail.com联系我。

![hah](https://tse1-mm.cn.bing.net/th/id/OIP-C.1WzofyXU4XlVG1soFYMmpgHaEc?w=273&h=180&c=7&r=0&o=5&dpr=2&pid=1.7)

`````

** Pet相关模块的功能：**

1.提供教材案例下载。
      教材配套的案例下载（运行以下1行Python代码）：
 
      import pet.textbook1.codes
      稍后(一般是瞬间），即可将教学案例下载到Windows桌面，目录为：Python与数据分析及可视化教学案例。
  
2.提供编程之道论述。
      趣谈编程之道（运行以下1行Python代码）：
  
      import pet.this
      与“晦涩难懂的”Python编程之禅import this对应，本模块从中国传统文化，心，术，道三个层次，引用古文阐述编程之道。
      内容大家自己体会，道法自然，道不简则理不明！！Just for Fun！！！（不笑不足以为道!!)

3.提供教材涉及的数据集。
    pet模块提供了如下数据集（字典）：
    datafile_dict = {
    'ip地址分类': 'ip_address.xlsx',
    '研究生初试成绩': 'st.xlsx',
    '上海地铁线路': 'subway.xlsx',
    '北京公交车': 'beijing_bus.xlsx',
    '通识课': '2022tsk.xlsx',
    '优秀毕业论文': '2022pst.xlsx',
    '太乙金华宗旨': 'tyjhzz.txt',
    '微信接龙投票': 'votes.txt',
    'cookie样例': 'sample_cookies.txt',
    '道德经': 'ddj.txt',
    '双色球': 'ssq_22134.xlsx',
    '2022转专业': '2022zzy.xlsx'
}
  通过调用函数：factory.load_data(key='道德经',prompt=True) 获取DataFrame或文本文件
  xlsx格式返回dataframe, txt格式返回字符串
  
  如：factory.load_data(key='上海地铁线路')
  
4.提供随机伪数据集的生成函数：

    from pet.datasets import factory

    以下2个函数可以分别随机生成Series和DataFrame对象数据。
    
    #生成纯净Series数据：
    df=factory.gen_sample_series() #默认生成Series样本数据 40条，姓名，成绩
    
    #生成带噪声的Series数据：
    df = factory.gen_sample_series(number=30, noise=0.1, repeat=2)
    其中：number 为记录数，noise为随机产生None数据概率，repeat为允许重复数据项的最高次数。
    
    #生成纯净DataFrame数据：
    df=factory.gen_sample_dataframe() #默认生成Series样本数据 40条，姓名，成绩
    
    #生成带噪声的DataFrame数据：
    df = factory.gen_sample_dataframe(number=500, noise=.08, repeat=2)
    其中：number 为记录数，noise为随机产生None数据概率，repeat为允许重复数据项的最高次数。
    
    
        '''
5.提供个性化定制随机伪数据集的生成函数：

   factory.gen_sample_dataframe(sample_order=sample_order,
                         number: int = 40,
                         dst=f'{pet_home}/generated_sample_dataframe_{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.xlsx',
                         noise=0,
                         repeat=1):

    即：按照订单格式产生数据。
    sample_order：订单
    number：数量
    dst：数据保存的目录
    noise：噪声，增加None数据字段概率
    repeat：产生重复数据
    ------------------

   sample_orde为产生数据订单格式，样本格式如下：
   
    sample_order = {

    '学号.iid': 220151000,
    '考号.i': [151000, 789000],
    '姓名.n': '',  # ""生成默认的随机名字，也可以设置姓名字符串，['赵钱孙李','微甜地平天下'],
    '性别.c': ['男', '女'],
    '日期.d': ['2020-2-24', '2024-12-31'],
    '时间.t': ['00:00:00', '23:59:59'],
    '年龄.i': [18, 24],
    '政治面貌.c': ['党员', '团员', '群众'],
    '专业.c': ['计算机科学与技术', '人工智能', '软件工程', '自动控制', '机械制造', '自动控制'],
    '学校.c': ['清华大学', '北京大学', '复旦大学', '上海交通大学', '上海师范大学', '中国科技大学', '上海大学'],
    '政治.i': [19, 100],
    '英语.i': [29, 100],
    '英语类别.c': ['英语一', '英语二'],
    '高等数学.i': [30, 140],
    '数学类别.c': ['数学一', '数学二', '数学三'],
    '专业课.i': [30, 150],
    '净收入.f': [30.3, 150.55, 3]}
    
     学号.iid: 代表产生整数学号（字段名称.类型）
        .i:代表整数
        .n: 代表名字
        .c: 代表类别
        .d: 代表日期
        .t: 代表时间
        .f: 代表浮点数
        
   

`````

![hah](https://img.niuqiuyi.com/202210/19/012355471.png)
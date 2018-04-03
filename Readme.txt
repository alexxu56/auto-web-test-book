
一、测试对象：图书管理测试项目nbop-plat-test-app。实现IE页面自动化化测试（待补充Chrome/Firefox）

二、测试设计: 采用Python+Unittest+Selenium实现页面自动化测试
    1、主体结构介绍
       1）casesrc：测试运行入口，测试案例源码
          run.py:主体入口，实现运行测试案例、记录日志、出测试报告等功能。
          testlist.txt:放置要运行的测试案例文件名，文件名以test开头
          SetupIE.py：打开窗口、获取并打开URL
          getBookListInit.py:调用SetupIE，点击图书管理按钮获取图书管理栏目
          AddBook.py:先调用getBookListInit，再进行新增一条图书记录操作。
          DeleteBook.py:先调用getBookListInit，再删除一条图书记录
          UpdateBook.py:先调用getBookListInit，再进行修改一条图书记录操作
          RefreshBook.py:先调用getBookListInit，再进行刷新图书记录操作
         主体功能已完成，测试案例参考基本操作设计，并放入testlist.txt中。待后续补充
       2）common:公共模块源码
	  config.ini：放置URL、timeout、database参数
          ConnetExcel.py:读写excel模块
          elementActionUtile.py:页面元素操作模块
          IEAction.py:IE驱动公共模块、截图模块
          Log.py：日志模块
          ReadConfig.py：读取公共参数config.ini模块
       3）driver：放置浏览器驱动
       4）log/report：运行日志、png截图、测试报告
       5) testData:存放测试数据，
          数据输入datain页：为每个案例设计编号、描述
          数据输出dataout页：记录每个案例运行结果信息，并与期望值比较，得出测试结果。
    2、测试案例设计：
       1）调度方式：使用unittest调度不同场景测试用例。
       2）案例标注：为每个测试用例标准唯一的case id
       3）一个脚本执行多个案例:  在同个场景下，设计可执行连续的测试案例
       4）可重复性：测试用例可重复执行                       

三、框架待持续补充：
    1、补充测试案例、断言
    2、补充database操作
    3、补充浏览器兼容性测试


          

                 









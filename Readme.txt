
һ�����Զ���ͼ����������Ŀnbop-plat-test-app��ʵ��IEҳ���Զ��������ԣ�������Chrome/Firefox��

�����������: ����Python+Unittest+Seleniumʵ��ҳ���Զ�������
    1������ṹ����
       1��casesrc������������ڣ����԰���Դ��
          run.py:������ڣ�ʵ�����в��԰�������¼��־�������Ա���ȹ��ܡ�
          testlist.txt:����Ҫ���еĲ��԰����ļ������ļ�����test��ͷ
          SetupIE.py���򿪴��ڡ���ȡ����URL
          getBookListInit.py:����SetupIE�����ͼ�����ť��ȡͼ�������Ŀ
          AddBook.py:�ȵ���getBookListInit���ٽ�������һ��ͼ���¼������
          DeleteBook.py:�ȵ���getBookListInit����ɾ��һ��ͼ���¼
          UpdateBook.py:�ȵ���getBookListInit���ٽ����޸�һ��ͼ���¼����
          RefreshBook.py:�ȵ���getBookListInit���ٽ���ˢ��ͼ���¼����
         ���幦������ɣ����԰����ο�����������ƣ�������testlist.txt�С�����������
       2��common:����ģ��Դ��
	  config.ini������URL��timeout��database����
          ConnetExcel.py:��дexcelģ��
          elementActionUtile.py:ҳ��Ԫ�ز���ģ��
          IEAction.py:IE��������ģ�顢��ͼģ��
          Log.py����־ģ��
          ReadConfig.py����ȡ��������config.iniģ��
       3��driver���������������
       4��log/report��������־��png��ͼ�����Ա���
       5) testData:��Ų������ݣ�
          ��������datainҳ��Ϊÿ��������Ʊ�š�����
          �������dataoutҳ����¼ÿ���������н����Ϣ����������ֵ�Ƚϣ��ó����Խ����
    2�����԰�����ƣ�
       1�����ȷ�ʽ��ʹ��unittest���Ȳ�ͬ��������������
       2��������ע��Ϊÿ������������׼Ψһ��case id
       3��һ���ű�ִ�ж������:  ��ͬ�������£���ƿ�ִ�������Ĳ��԰���
       4�����ظ��ԣ������������ظ�ִ��                       

������ܴ��������䣺
    1��������԰���������
    2������database����
    3����������������Բ���


          

                 









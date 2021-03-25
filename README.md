# 使用Quizlet创建英语词汇集

#### 1. 使用方法

- 准备：`*.xls`，里面每一列存放一个单词。并修改`main.py`中的`InFilename`

- 生成词汇和释义文件：

  ```shell
  python main.py
  ```

  多线程版：
  ```shell
  python main_mulprocess.py
  ```

- 将生成的文件`eggs.csv`中的内容加入到词汇集。


# python
Python学习笔记

# 第2章 变量和简单数据类型

在Python中使用变量时，需要遵守一些规则和指南。
违法规则将会引发错误，遵循指南可以让代码更容易阅读和理解。
* 变量名只能包含字母、数字和下划线。变量名可以以字母或下划线开头，但不能以数字开头。例如，可将变量命名为`message_1`，但不能命名为`1_message`。
* 变量名不能包含空格，但可以使用下划线分隔单词。例如，变量名`greeting_message`可行，但是变量名`greeting message`会引发错误。
* 不要将Python关键字和函数名用作变量名，例如`print`。
* 变量名应该既短又有描述性。例如，`name`比`n`好，`student_name`比`s_n`好，`name_length`比`length_of_person_name`好。
* 慎用小写字母`l`和大写字母`O`，因为它们可能被人错看成数字`1`和`0`。

Python定义了一些标准类型，用于存储各种类型的数据。
Python有5个标准的数据类型：
* Numbers（数字）
* String（字符串）
* List（列表）
* Tuple（元组）
* Dictionary（字典）
---
title: Mysql 大小写规范
date: 2022-08-31 23:33:58
tags: MySql
categories: 数据库
---

## windows和linux区别

在 SQL 中，关键字和函数名是不区分大小写的，比如 SELECT、WHERE、ORDER、GROUP BY 等关键字，以及 ABS、MOD、ROUND、MAX 等函数名。

但是数据库名，表名，表的别名，变量名在 Linux 和 Windows 环境下是不同的，` windows系统默认大小写不敏感` ，但是 `linux系统默认是大小写敏感`的 。  

## Sql编写建议

+ 关键字和函数名称全部大写；
+ 数据库名、表名、表别名、字段名、字段别名等全部小写；
+ SQL 语句必须以分号结尾。  
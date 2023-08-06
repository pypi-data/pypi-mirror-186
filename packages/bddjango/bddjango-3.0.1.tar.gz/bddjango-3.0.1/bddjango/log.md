# bddjango版本更新


## 相关链接

- [wiki文档地址_内网](https://www.bodexiong.vip/mkdocs/)
- [wiki文档地址_外网](https://wiki-bddjango.readthedocs.io/zh/)
- [pypi项目地址](https://pypi.org/project/bddjango/)
- [查看当前最新版本号](https://pypi.org/search/?q=bddjango)


## 更新信息

# 3.0.0
- 增加`BulkUpdateMixin`
- 统计方法增加`loc_ls`字段
- 精简项目结构
- autocode兼容gbk格式csv等
- 生成代码时使用render来返回html格式

# 3.0.1
- `copy_to`增量上传的同名文件策略改为默认替换
- `auto_wiki`, `auto_code`, `auto_model`界面优化
- 增加`BaseOrmSearchModel`, 进行相关性检索
- 增加前端控制`search_fields_conf`参数
- order_by_order_type_ls对OrderByObject进行兼容
- 在tools中增加`CsrfExemptSessionAuthentication`方法
- migrate出错导致ContentType对应的base_model为None时, 自动删除对应的obj.
- 修复auto_code的'<pk>'在html的<pre>标签中被转义的bug
- tools中增加一个`fake_model.py`
- 修复导出数据外键值为None时报错的bug
- 文件下载类`DownloadFileMixin`

























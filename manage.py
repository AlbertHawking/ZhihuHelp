# -*- coding: utf-8 -*-
# 放置于首位
import os
import sys  # 修改默认编码
import locale #获取原始编码
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(100000)  # 为BS解析知乎上的长答案增加递归深度限制

# 添加包路径
base_path = unicode(os.path.abspath('.').decode(locale.getpreferredencoding()))
sys.path.append(base_path + u'/src/lib')



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhihuhelp.settings")
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

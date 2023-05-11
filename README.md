# DaLiu_prompts_from_file.py

本文件是sd-web-ui的一个脚本文件。

具体的是基于官方自带的prompts_from_file.py文件修改而来。

增加了对sd_model参数的支持，也就是可以自动更换模型。

使用方法和prompts_from_file.py文件一样，--sd_model XXX，放到scripts文件夹中重载前端ui界面生效。

目前由于代码水平有限，不知道如何将模型变换改为ui界面手动变换的形式。

大佬如果知道的话，可以指点一下我，其实是个很简单的功能哈哈，我自己再看看gr的使用和源码吧

# get_prompts_list.py
补充添加的生成不同模型多行prompts的脚本代码，不用放到scripts文件夹

# random_prompts
补充添加的随机组合描述词生成多行prompts的脚本代码，不用放到scripts文件夹

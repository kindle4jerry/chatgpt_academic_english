> **Note**
>
> 2023.5.27 对Gradio依赖进行了调整，Fork并解决了官方Gradio的若干Bugs。请及时**更新代码**并重新更新pip依赖。安装依赖时，请严格选择`requirements.txt`中**指定的版本**： 
> 
> `pip install -r requirements.txt`
>

# <img src="docs/logo.png" width="40" > GPT 学术优化 (GPT Academic)

**如果喜欢这个项目，请给它一个Star；如果你发明了更好用的快捷键或函数插件，欢迎发pull requests**

If you like this project, please give it a Star. If you've come up with more useful academic shortcuts or functional plugins, feel free to open an issue or pull request. We also have a README in [English|](docs/README_EN.md)[日本語|](docs/README_JP.md)[한국어|](https://github.com/mldljyh/ko_gpt_academic)[Русский|](docs/README_RS.md)[Français](docs/README_FR.md) translated by this project itself.
To translate this project to arbitary language with GPT, read and run [`multi_language.py`](multi_language.py) (experimental).

> **Note**
>
> 1.请注意只有**红颜色**标识的函数插件（按钮）才支持读取文件，部分插件位于插件区的**下拉菜单**中。另外我们以**最高优先级**欢迎和处理任何新插件的PR！
>
> 2.本项目中每个文件的功能都在自译解[`self_analysis.md`](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)详细说明。随着版本的迭代，您也可以随时自行点击相关函数插件，调用GPT重新生成项目的自我解析报告。常见问题汇总在[`wiki`](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)当中。[安装方法](#installation)。
> 
> 3.本项目兼容并鼓励尝试国产大语言模型chatglm和RWKV, 盘古等等。支持多个api-key共存，可在配置文件中填写如`API_KEY="openai-key1,openai-key2,api2d-key3"`。需要临时更换`API_KEY`时，在输入区输入临时的`API_KEY`然后回车键提交后即可生效。


 

<div align="center">

功能 | 描述
--- | ---
一键润色 | 支持一键润色、一键查找论文语法错误
一键中英互译 | 一键中英互译
一键代码解释 | 显示代码、解释代码、生成代码、给代码加注释
[自定义快捷键](https://www.bilibili.com/video/BV14s4y1E7jN) | 支持自定义快捷键
模块化设计 | 支持自定义强大的[函数插件](https://github.com/binary-husky/chatgpt_academic/tree/master/crazy_functions)，插件支持[热更新](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)
[自我程序剖析](https://www.bilibili.com/video/BV1cj411A7VW) | [函数插件] [一键读懂](https://github.com/binary-husky/chatgpt_academic/wiki/chatgpt-academic%E9%A1%B9%E7%9B%AE%E8%87%AA%E8%AF%91%E8%A7%A3%E6%8A%A5%E5%91%8A)本项目的源代码
[程序剖析](https://www.bilibili.com/video/BV1cj411A7VW) | [函数插件] 一键可以剖析其他Python/C/C++/Java/Lua/...项目树
读论文、[翻译](https://www.bilibili.com/video/BV1KT411x7Wn)论文 | [函数插件] 一键解读latex/pdf论文全文并生成摘要
Latex全文[翻译](https://www.bilibili.com/video/BV1nk4y1Y7Js/)、[润色](https://www.bilibili.com/video/BV1FT411H7c5/) | [函数插件] 一键翻译或润色latex论文
批量注释生成 | [函数插件] 一键批量生成函数注释
Markdown[中英互译](https://www.bilibili.com/video/BV1yo4y157jV/) | [函数插件] 看到上面5种语言的[README](https://github.com/binary-husky/chatgpt_academic/blob/master/docs/README_EN.md)了吗？
chat分析报告生成 | [函数插件] 运行后自动生成总结汇报
[PDF论文全文翻译功能](https://www.bilibili.com/video/BV1KT411x7Wn) | [函数插件] PDF论文提取题目&摘要+翻译全文（多线程）
[Arxiv小助手](https://www.bilibili.com/video/BV1LM4y1279X) | [函数插件] 输入arxiv文章url即可一键翻译摘要+下载PDF
[谷歌学术统合小助手](https://www.bilibili.com/video/BV19L411U7ia) | [函数插件] 给定任意谷歌学术搜索页面URL，让gpt帮你[写relatedworks](https://www.bilibili.com/video/BV1GP411U7Az/)
互联网信息聚合+GPT | [函数插件] 一键[让GPT先从互联网获取信息](https://www.bilibili.com/video/BV1om4y127ck)，再回答问题，让信息永不过时
公式/图片/表格显示 | 可以同时显示公式的[tex形式和渲染形式](https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png)，支持公式、代码高亮
多线程函数插件支持 | 支持多线调用chatgpt，一键处理[海量文本](https://www.bilibili.com/video/BV1FT411H7c5/)或程序
启动暗色gradio[主题](https://github.com/binary-husky/chatgpt_academic/issues/173) | 在浏览器url后面添加```/?__theme=dark```可以切换dark主题
[多LLM模型](https://www.bilibili.com/video/BV1wT411p7yf)支持，[API2D](https://api2d.com/)接口支持 | 同时被GPT3.5、GPT4、[清华ChatGLM](https://github.com/THUDM/ChatGLM-6B)、[复旦MOSS](https://github.com/OpenLMLab/MOSS)同时伺候的感觉一定会很不错吧？
更多LLM模型接入，支持[huggingface部署](https://huggingface.co/spaces/qingxu98/gpt-academic) | 加入Newbing接口(新必应)，引入清华[Jittorllms](https://github.com/Jittor/JittorLLMs)支持[LLaMA](https://github.com/facebookresearch/llama)，[RWKV](https://github.com/BlinkDL/ChatRWKV)和[盘古α](https://openi.org.cn/pangu/)
更多新功能展示(图像生成等) …… | 见本文档结尾处 ……

</div>


- 新界面（修改`config.py`中的LAYOUT选项即可实现“左右布局”和“上下布局”的切换）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif" width="700" >
</div>


- 所有按钮都通过读取functional.py动态生成，可随意加自定义功能，解放粘贴板
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231975334-b4788e91-4887-412f-8b43-2b9c5f41d248.gif" width="700" >
</div>

- 润色/纠错
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/231980294-f374bdcb-3309-4560-b424-38ef39f04ebd.gif" width="700" >
</div>

- 如果输出包含公式，会同时以tex形式和渲染形式显示，方便复制和阅读
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png" width="700" >
</div>

- 懒得看项目代码？整个工程直接给chatgpt炫嘴里
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="700" >
</div>

- 多种大语言模型混合调用（ChatGLM + OpenAI-GPT3.5 + [API2D](https://api2d.com/)-GPT4）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/232537274-deca0563-7aa6-4b5d-94a2-b7c453c47794.png" width="700" >
</div>

---
# Installation
## 安装-方法1：直接运行 (Windows, Linux or MacOS) 

1. 下载项目
```sh
git clone https://github.com/binary-husky/chatgpt_academic.git
cd chatgpt_academic
```

2. 配置API_KEY

在`config.py`中，配置API KEY等设置，[特殊网络环境设置](https://github.com/binary-husky/gpt_academic/issues/1) 。

(P.S. 程序运行时会优先检查是否存在名为`config_private.py`的私密配置文件，并用其中的配置覆盖`config.py`的同名配置。因此，如果您能理解我们的配置读取逻辑，我们强烈建议您在`config.py`旁边创建一个名为`config_private.py`的新配置文件，并把`config.py`中的配置转移（复制）到`config_private.py`中。`config_private.py`不受git管控，可以让您的隐私信息更加安全。P.S.项目同样支持通过`环境变量`配置大多数选项，环境变量的书写格式参考`docker-compose`文件。读取优先级: `环境变量` > `config_private.py` > `config.py`)


3. 安装依赖
```sh
# （选择I: 如熟悉python）（python版本3.9以上，越新越好），备注：使用官方pip源或者阿里pip源,临时换源方法：python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python -m pip install -r requirements.txt

# （选择II: 如不熟悉python）使用anaconda，步骤也是类似的 (https://www.bilibili.com/video/BV1rc411W7Dr)：
conda create -n gptac_venv python=3.11    # 创建anaconda环境
conda activate gptac_venv                 # 激活anaconda环境
python -m pip install -r requirements.txt # 这个步骤和pip安装一样的步骤
```

<details><summary>如果需要支持清华ChatGLM/复旦MOSS作为后端，请点击展开此处</summary>
<p>

【可选步骤】如果需要支持清华ChatGLM/复旦MOSS作为后端，需要额外安装更多依赖（前提条件：熟悉Python + 用过Pytorch + 电脑配置够强）：
```sh
# 【可选步骤I】支持清华ChatGLM。清华ChatGLM备注：如果遇到"Call ChatGLM fail 不能正常加载ChatGLM的参数" 错误，参考如下： 1：以上默认安装的为torch+cpu版，使用cuda需要卸载torch重新安装torch+cuda； 2：如因本机配置不够无法加载模型，可以修改request_llm/bridge_chatglm.py中的模型精度, 将 AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True) 都修改为 AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
python -m pip install -r request_llm/requirements_chatglm.txt  

# 【可选步骤II】支持复旦MOSS
python -m pip install -r request_llm/requirements_moss.txt
git clone https://github.com/OpenLMLab/MOSS.git request_llm/moss  # 注意执行此行代码时，必须处于项目根路径

# 【可选步骤III】确保config.py配置文件的AVAIL_LLM_MODELS包含了期望的模型，目前支持的全部模型如下(jittorllms系列目前仅支持docker方案)：
AVAIL_LLM_MODELS = ["gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "newbing", "moss"] # + ["jittorllms_rwkv", "jittorllms_pangualpha", "jittorllms_llama"]
```

</p>
</details>



4. 运行
```sh
python main.py
```

5. 测试函数插件
```
- 测试函数插件模板函数（要求gpt回答历史上的今天发生了什么），您可以根据此函数为模板，实现更复杂的功能
    点击 "[函数插件模板Demo] 历史上的今天"
```

## 安装-方法2：使用Docker

1. 仅ChatGPT（推荐大多数人选择）

``` sh
git clone https://github.com/binary-husky/chatgpt_academic.git  # 下载项目
cd chatgpt_academic                                 # 进入路径
nano config.py                                      # 用任意文本编辑器编辑config.py, 配置 “Proxy”， “API_KEY” 以及 “WEB_PORT” (例如50923) 等
docker build -t gpt-academic .                      # 安装

#（最后一步-选择1）在Linux环境下，用`--net=host`更方便快捷
docker run --rm -it --net=host gpt-academic
#（最后一步-选择2）在macOS/windows环境下，只能用-p选项将容器上的端口(例如50923)暴露给主机上的端口
docker run --rm -it -e WEB_PORT=50923 -p 50923:50923 gpt-academic
```

2. ChatGPT + ChatGLM + MOSS（需要熟悉Docker）

``` sh
# 修改docker-compose.yml，删除方案1和方案3，保留方案2。修改docker-compose.yml中方案2的配置，参考其中注释即可
docker-compose up
```

3. ChatGPT + LLAMA + 盘古 + RWKV（需要熟悉Docker）
``` sh
# 修改docker-compose.yml，删除方案1和方案2，保留方案3。修改docker-compose.yml中方案3的配置，参考其中注释即可
docker-compose up
```


## 安装-方法3：其他部署姿势
1. 一键运行脚本。
完全不熟悉python环境的Windows用户可以下载[Release](https://github.com/binary-husky/gpt_academic/releases)中发布的一键运行脚本安装无本地模型的版本，
不建议电脑上已有python的用户采用此方法（在此基础上安装插件的依赖很麻烦）。
脚本的贡献来源是[oobabooga](https://github.com/oobabooga/one-click-installers)。

2. 使用docker-compose运行。
请阅读docker-compose.yml后，按照其中的提示操作即可

3. 如何使用反代URL/微软云AzureAPI。
按照`config.py`中的说明配置API_URL_REDIRECT即可。

4. 远程云服务器部署（需要云服务器知识与经验）。
请访问[部署wiki-1](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9C%E7%A8%8B%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

5. 使用WSL2（Windows Subsystem for Linux 子系统）。
请访问[部署wiki-2](https://github.com/binary-husky/chatgpt_academic/wiki/%E4%BD%BF%E7%94%A8WSL2%EF%BC%88Windows-Subsystem-for-Linux-%E5%AD%90%E7%B3%BB%E7%BB%9F%EF%BC%89%E9%83%A8%E7%BD%B2)

6. 如何在二级网址（如`http://localhost/subpath`）下运行。
请访问[FastAPI运行说明](docs/WithFastapi.md)

---
# Advanced Usage
## 自定义新的便捷按钮 / 自定义函数插件

1. 自定义新的便捷按钮（学术快捷键）
任意文本编辑器打开`core_functional.py`，添加条目如下，然后重启程序即可。（如果按钮已经添加成功并可见，那么前缀、后缀都支持热修改，无需重启程序即可生效。）
例如
```
"超级英译中": {
    # 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
    "Prefix": "请翻译把下面一段内容成中文，然后用一个markdown表格逐一解释文中出现的专有名词：\n\n", 
    
    # 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来。
    "Suffix": "",
},
```
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226899272-477c2134-ed71-4326-810c-29891fe4a508.png" width="500" >
</div>

2. 自定义函数插件

编写强大的函数插件来执行任何你想得到的和想不到的任务。
本项目的插件编写、调试难度很低，只要您具备一定的python基础知识，就可以仿照我们提供的模板实现自己的插件功能。
详情请参考[函数插件指南](https://github.com/binary-husky/chatgpt_academic/wiki/%E5%87%BD%E6%95%B0%E6%8F%92%E4%BB%B6%E6%8C%87%E5%8D%97)。

---
# Latest Update
## 新功能动态

1. 对话保存功能。在函数插件区调用 `保存当前的对话` 即可将当前对话保存为可读+可复原的html文件，
另外在函数插件区（下拉菜单）调用 `载入对话历史存档` ，即可还原之前的会话。
Tip：不指定文件直接点击 `载入对话历史存档` 可以查看历史html存档缓存，点击 `删除所有本地对话历史记录` 可以删除所有html存档缓存。
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/235222390-24a9acc0-680f-49f5-bc81-2f3161f1e049.png" width="500" >
</div>



2. 生成报告。大部分插件都会在执行结束后，生成工作报告
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/227503770-fe29ce2c-53fd-47b0-b0ff-93805f0c2ff4.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504617-7a497bb3-0a2a-4b50-9a8a-95ae60ea7afd.png" height="300" >
<img src="https://user-images.githubusercontent.com/96192199/227504005-efeaefe0-b687-49d0-bf95-2d7b7e66c348.png" height="300" >
</div>

3. 模块化功能设计，简单的接口却能支持强大的功能
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/229288270-093643c1-0018-487a-81e6-1d7809b6e90f.png" height="400" >
<img src="https://user-images.githubusercontent.com/96192199/227504931-19955f78-45cd-4d1c-adac-e71e50957915.png" height="400" >
</div>

4. 这是一个能够“自我译解”的开源项目
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226936850-c77d7183-0749-4c1c-9875-fd4891842d0c.png" width="500" >
</div>

5. 译解其他开源项目，不在话下
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png" width="500" >
</div>

<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/226969067-968a27c1-1b9c-486b-8b81-ab2de8d3f88a.png" width="500" >
</div>

6. 装饰[live2d](https://github.com/fghrsh/live2d_demo)的小功能（默认关闭，需要修改`config.py`）
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236432361-67739153-73e8-43fe-8111-b61296edabd9.png" width="500" >
</div>

7. 新增MOSS大语言模型支持
<div align="center">
<img src="https://user-images.githubusercontent.com/96192199/236639178-92836f37-13af-4fdd-984d-b4450fe30336.png" width="500" >
</div>

8. OpenAI图像生成
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/bc7ab234-ad90-48a0-8d62-f703d9e74665" width="500" >
</div>

9. OpenAI音频解析与总结
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/709ccf95-3aee-498a-934a-e1c22d3d5d5b" width="500" >
</div>

10. Latex全文校对纠错
<div align="center">
<img src="https://github.com/binary-husky/gpt_academic/assets/96192199/651ccd98-02c9-4464-91e1-77a6b7d1b033" width="500" >
</div>


## 版本:
- version 3.5(Todo): 使用自然语言调用本项目的所有函数插件（高优先级）
- version 3.4(Todo): 完善chatglm本地大模型的多线支持
- version 3.3: +互联网信息综合功能
- version 3.2: 函数插件支持更多参数接口 (保存对话功能, 解读任意语言代码+同时询问任意的LLM组合)
- version 3.1: 支持同时问询多个gpt模型！支持api2d，支持多个apikey负载均衡
- version 3.0: 对chatglm和其他小型llm的支持
- version 2.6: 重构了插件结构，提高了交互性，加入更多插件
- version 2.5: 自更新，解决总结大工程源代码时文本过长、token溢出的问题
- version 2.4: (1)新增PDF全文翻译功能; (2)新增输入区切换位置的功能; (3)新增垂直布局选项; (4)多线程函数插件优化。
- version 2.3: 增强多线程交互性
- version 2.2: 函数插件支持热重载
- version 2.1: 可折叠式布局
- version 2.0: 引入模块化函数插件
- version 1.0: 基础功能

gpt_academic开发者QQ群-2：610599535

- 已知问题
    - 某些浏览器翻译插件干扰此软件前端的运行
    - 官方Gradio目前有很多兼容性Bug，请务必使用requirement.txt安装Gradio

## 参考与学习

```
代码中参考了很多其他优秀项目中的设计，主要包括：

# 项目1：清华ChatGLM-6B:
https://github.com/THUDM/ChatGLM-6B

# 项目2：清华JittorLLMs:
https://github.com/Jittor/JittorLLMs

# 项目3：Edge-GPT:
https://github.com/acheong08/EdgeGPT

# 项目4：ChuanhuChatGPT:
https://github.com/GaiZhenbiao/ChuanhuChatGPT

# 项目5：ChatPaper:
https://github.com/kaixindelele/ChatPaper

# 更多：
https://github.com/gradio-app/gradio
https://github.com/fghrsh/live2d_demo
https://github.com/oobabooga/one-click-installers
```

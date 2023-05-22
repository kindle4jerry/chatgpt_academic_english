"""
这是什么？
    这个文件用于函数插件的单元测试
    运行方法 python crazy_functions/crazy_functions_test.py
"""

def validate_path():
    import os, sys
    dir_name = os.path.dirname(__file__)
    root_dir_assume = os.path.abspath(os.path.dirname(__file__) +  '/..')
    os.chdir(root_dir_assume)
    sys.path.append(root_dir_assume)
    
validate_path() # validate path so you can run from base directory
from colorful import *
from toolbox import get_conf, ChatBotWithCookies
proxies, WEB_PORT, LLM_MODEL, CONCURRENT_COUNT, AUTHENTICATION, CHATBOT_HEIGHT, LAYOUT, API_KEY = \
    get_conf('proxies', 'WEB_PORT', 'LLM_MODEL', 'CONCURRENT_COUNT', 'AUTHENTICATION', 'CHATBOT_HEIGHT', 'LAYOUT', 'API_KEY')

llm_kwargs = {
    'api_key': API_KEY,
    'llm_model': LLM_MODEL,
    'top_p':1.0, 
    'max_length': None,
    'temperature':1.0,
}
plugin_kwargs = { }
chatbot = ChatBotWithCookies(llm_kwargs)
history = []
system_prompt = "Serve me as a writing and programming assistant."
web_port = 1024


def test_解析一个Python项目():
    from crazy_functions.解析项目源代码 import 解析一个Python项目
    txt = "crazy_functions/test_project/python/dqn"
    for cookies, cb, hist, msg in 解析一个Python项目(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_解析一个Cpp项目():
    from crazy_functions.解析项目源代码 import 解析一个C项目
    txt = "crazy_functions/test_project/cpp/cppipc"
    for cookies, cb, hist, msg in 解析一个C项目(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_Latex英文润色():
    from crazy_functions.Latex全文润色 import Latex英文润色
    txt = "crazy_functions/test_project/latex/attention"
    for cookies, cb, hist, msg in Latex英文润色(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_Markdown中译英():
    from crazy_functions.批量Markdown翻译 import Markdown中译英
    txt = "README.md"
    for cookies, cb, hist, msg in Markdown中译英(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_批量翻译PDF文档():
    from crazy_functions.批量翻译PDF文档_多线程 import 批量翻译PDF文档
    txt = "crazy_functions/test_project/pdf_and_word"
    for cookies, cb, hist, msg in 批量翻译PDF文档(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_谷歌检索小助手():
    from crazy_functions.谷歌检索小助手 import 谷歌检索小助手
    txt = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=auto+reinforcement+learning&btnG="
    for cookies, cb, hist, msg in 谷歌检索小助手(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_总结word文档():
    from crazy_functions.总结word文档 import 总结word文档
    txt = "crazy_functions/test_project/pdf_and_word"
    for cookies, cb, hist, msg in 总结word文档(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_下载arxiv论文并翻译摘要():
    from crazy_functions.下载arxiv论文翻译摘要 import 下载arxiv论文并翻译摘要
    txt = "1812.10695"
    for cookies, cb, hist, msg in 下载arxiv论文并翻译摘要(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)

def test_联网回答问题():
    from crazy_functions.联网的ChatGPT import 连接网络回答问题
    # txt = "谁是应急食品？"
    # >>        '根据以上搜索结果可以得知，应急食品是“原神”游戏中的角色派蒙的外号。'
    # txt = "道路千万条，安全第一条。后面两句是？"
    # >>        '行车不规范，亲人两行泪。'
    # txt = "You should have gone for the head. What does that mean?"
    # >>        The phrase "You should have gone for the head" is a quote from the Marvel movies, Avengers: Infinity War and Avengers: Endgame. It was spoken by the character Thanos in Infinity War and by Thor in Endgame.
    txt = "AutoGPT是什么？"
    for cookies, cb, hist, msg in 连接网络回答问题(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port): 
        print("当前问答：", cb[-1][-1].replace("\n"," "))
    for i, it in enumerate(cb): print亮蓝(it[0]); print亮黄(it[1])

def test_解析ipynb文件():
    from crazy_functions.解析JupyterNotebook import 解析ipynb文件
    txt = "crazy_functions/test_samples"
    for cookies, cb, hist, msg in 解析ipynb文件(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
        print(cb)


# test_解析一个Python项目()
# test_Latex英文润色()
# test_Markdown中译英()
# test_批量翻译PDF文档()
# test_谷歌检索小助手()
# test_总结word文档()
# test_下载arxiv论文并翻译摘要()
# test_解析一个Cpp项目()
# test_联网回答问题()
test_解析ipynb文件()

input("程序完成，回车退出。")
print("退出。")
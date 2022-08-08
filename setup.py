 # -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name = "nonebot_plugin_covid_19_by_guild",
    version = "1.0",
    packages = setuptools.find_packages(),
    author="bingyue",
    author_email="hello-yiqiu@qq.com",
    description="""疫情小助手 支持查地区 风险地区 境外输入等""",
    url="https://github.com/bingqiu456/nonebot_plugin_covid_19_by_guild",
    install_requires=[
        "aiofiles>=0.8.0",
        "nonebot2>=2.0.0b2",
        "Pillow>=9.1.1",
        "nonebot-adapter-onebot>=2.0.0b1",
        "httpx>=0.23.0",
        "nonebot-plugin-guild-patch>=0.2.0",
    ],
    keywords=["nonebot_plugin_covid_19_by_guild","nonebot","nonebot_plugin"],
    package_data={
        'nonebot_plugin_covid_19_by_guild':['covid_19.txt','123.ttf'],
    }

)

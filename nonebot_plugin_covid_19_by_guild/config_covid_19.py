from nonebot.permission import SUPERUSER
from nonebot import get_driver,on_command
from loguru import logger
from nonebot_plugin_guild_patch import GUILD_SUPERUSER,GuildMessageEvent

global colour
global size
global group_image_covid
colour = get_driver().config.dict().get("covid_19_by_colour","#ccffcc")
group_image_covid = get_driver().config.dict().get("covid_19_by_images",[])
size = get_driver().config.dict().get("covid_19_by_size",20)
global group_covid
group_covid = get_driver().config.dict().get("covid_19_by_guild",[])
if colour ==None:
    logger.warning("covid_19:未配置文转图颜色 默认#ccffcc")
if size==None:
    logger.warning("covid_19:未配置文转图字体大小 默认20")
if group_covid ==[]:
    logger.warning("covid_19:未配置开启群号 默认[]")
if group_image_covid==[]:
    logger.success("covid_19:未配置文转图群组 默认[]")

add_group_123 = on_command("covid_19开启",permission=GUILD_SUPERUSER|SUPERUSER,priority=30)
@add_group_123.handle()
async def _(event:GuildMessageEvent):
    group_covid.append(event.guild_id)
    logger.success(f"covid_19:开启{event.guild_id}成功")
    await add_group_123.finish("covid_19:开启本频道成功")
    
del_group = on_command("covid_19关闭",permission=GUILD_SUPERUSER|SUPERUSER,priority=30)
@del_group.handle()
async def del_group_(event:GuildMessageEvent):
    try:
        group_covid.remove(event.guild_id)
    except(ValueError):
        logger.error("covid_19:此群不存在列表中")
        pass
    else:
        logger.success(f"covid_19:关闭{event.guild_id}成功")
        await del_group.finish("covid_19:关闭本频道成功")

image_group = on_command("疫情文转图开",permission=GUILD_SUPERUSER|SUPERUSER,priority=30)
@image_group.handle()
async def _(event:GuildMessageEvent):
    group_image_covid.append(event.guild_id)
    logger.success(f"covid_19:开启{event.guild_id}成功")
    await image_group.finish("covid_19:开启本频道成功")
    
image_group_off = on_command("疫情文转图关",permission=GUILD_SUPERUSER|SUPERUSER,priority=30)
@image_group_off.handle()
async def del_group_(event:GuildMessageEvent):
    try:
        group_image_covid.remove(event.guild_id)
    except(ValueError):
        logger.error("covid_19:此群不存在列表中")
        pass
    else:
        logger.success(f"covid_19:关闭{event.guild_id}成功")
        await image_group_off.finish("covid_19:关闭本频道成功")
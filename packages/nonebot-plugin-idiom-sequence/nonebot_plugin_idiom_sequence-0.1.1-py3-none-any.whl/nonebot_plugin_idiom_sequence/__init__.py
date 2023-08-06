import os
import json
import random
from pathlib import Path
from nonebot import on_command, on_fullmatch
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER

global groups

groups = {}

files = Path() / os.path.dirname(__file__) / "idiom.json"
idioms = json.loads(files.read_text(encoding='utf-8'))

diamond_path = Path() / 'data' / 'idiom_sequence' / 'data.json'
diamond_path.parent.mkdir(parents = True, exist_ok = True)
diamonds = (
    json.loads(diamond_path.read_text('utf-8'))
    if diamond_path.is_file()
    else {'': 0}
)

def save_diamond() -> None:
    diamond_path.write_text(json.dumps(diamonds), encoding='utf-8')

join = on_command("加入接龙", aliases={"参加接龙"}, priority=1)

@join.handle()
async def join_handle(bot, event: MessageEvent, state: T_State):
    global groups
    gid = str(event.group_id)
    try:
        if len(groups[gid]['players']) == 11:
            groups[gid]['players'].append(str(event.user_id))
            await join.send('加入成功 当前人数: 12/12 可以开始游戏🔱')
        else:
            groups[gid]['players'].append(str(event.user_id))
            await join.send('加入成功 当前人数: ' + str(len(groups[gid]['players'])) + '/12')
    except:
        groups[gid] = {'status': False, 'prev': '', 'prev_abbreviation': '', 'prev_end': '', 'multiples': [], 'players': []}
        groups[gid]['players'].append(str(event.user_id))
        await join.send('加入成功 当前人数: ' + str(len(groups[gid]['players'])) + '/12')

quit = on_command("退出接龙", aliases={"离开接龙"}, priority=1)

@quit.handle()
async def quit_handle(bot, event: MessageEvent, state: T_State):
    global groups
    if (str(event.group_id) not in groups) or groups[str(event.group_id)]['status'] == False:
        if str(event.user_id) in groups[str(event.group_id)]['players']:
            groups[str(event.group_id)]['players'].remove(str(event.user_id))
            await quit.send(f'你已退出接龙, 当前人数: ' + str(len(groups[str(event.group_id)]['players'])) + '/12')
        else:
            await quit.send(f'你未加入接龙, 无法退出')
    else:
        await quit.send(f'本群游戏已开始, 请等待下一局⚜️')

view = on_command("查看接龙", aliases={"接龙列表", '玩家列表'}, priority=1)

@view.handle()
async def view_handle(bot, event: MessageEvent, state: T_State):
    global groups
    if (event.group_id not in groups) or groups[str(event.group_id)]['players'] == 0:
        if len(groups[str(event.group_id)]['players']) == 0:
            await view.send(f'[CQ:at,qq={event.user_id}] 本群暂无玩家, 请先加入接龙')
        else:
            string = '本局玩家列表:'
            for i in groups[str(event.group_id)]['players']:
                string = string + f'\n[CQ:at,qq={i}]'
            await view.finish(Message(f'{string}'))

kick = on_command("踢出接龙", aliases={"禁止接龙"}, priority=1)

@kick.handle()
async def kick_handle(event: MessageEvent, state: T_State, msg: Message = CommandArg(), permission = SUPERUSER):
    global groups
    try:
        segment_list=event.get_message()["at"]
        for i in [segment.data['qq'] for segment in segment_list]:
            if str(i) in groups[str(event.group_id)]['players']:
                groups[str(event.group_id)]['players'].remove(str(i))
                await kick.send(f'你被踢出接龙, 当前人数: ' + str(len(groups[str(event.group_id)]['players'])) + '/12')
            else:
                await kick.send(f'该玩家未加入接龙, 无法踢出')
    except:
        await kick.send(f'操作失败,可能因为没开始或者没权限或者没有at玩家')

def test(gid, word):
    global groups
    for d in idioms:
        if word in d['word']:
            comp = d['pinyin'].split(' ')
            if comp[0] == groups[gid]['prev_end']:
                return {'status': True, 'word': d['word'], 'abbreviation': d['abbreviation'], 'derivation': d['derivation'], 'explanation': d['explanation'], 'pinyin': d['pinyin'], 'example': d['example'], 'end': comp[len(comp) - 1]}
    else:
        return {'status': False}

def info(word):
    for d in idioms:
        if word == d['word']:
            return d
    else:
        return 0

start = on_fullmatch('成语接龙', priority=12, block=True)
@start.handle()
async def start_handle(event: MessageEvent, state: T_State):

    global groups
    if groups[str(event.group_id)]['status'] == False and len(groups[str(event.group_id)]['players']) > 0:
        idx = random.randint(0, len(idioms) - 1)
        init_word = idioms[idx]['word']
        init_abbreviation = idioms[idx]['abbreviation']
        init_pinyin = idioms[idx]['pinyin'].split(' ')
        init_end = init_pinyin[len(init_pinyin) - 1]
        await start.send('成语接龙开始⚖️我先说: ' + init_word + '\n解释: ' + idioms[idx]['explanation'] + '\n出自: ' + idioms[idx]['derivation'] + '\n例子: ' + idioms[idx]['example'])
        groups[str(event.group_id)]['prev'] = init_word
        groups[str(event.group_id)]['prev_end'] = init_end
        await start.send('''1.成语接龙只可以接成语(系统会检测，如不是成语会提醒)🔮\n2.本次的接龙可以使用同音字🛡️\n3.接龙有/无时间限制⚔️\n4.确认玩家及其先后顺序🐺''')
    else:
        await start.send('成语接龙已经开始或者人数不足')

end = on_command('结束接龙', aliases = {'结束成语接龙'}, priority=12, block=True)
@end.handle()
async def end_handle(event: MessageEvent, state: T_State):

    global groups
    if groups[str(event.group_id)]['status'] == False:
        await start.send('还没开始怎么结束')
    else:
        groups['event.group_id'] = {}
        await start.send('已经结束成语接龙')
        groups[str(event.group_id)]['status'] = False



main = on_command('我接', aliases={'接龙', '接', 'jl'}, priority=12, block=True)

@main.handle()
async def main_handle(event: MessageEvent, state: T_State, msg: Message = CommandArg()):
    global groups
    msg = msg.extract_plain_text().strip()
    if msg:
        res = test(str(event.group_id), msg)
        if (res['status']):
            if msg in groups[str(event.group_id)]['multiples'] and groups[str(event.group_id)]['multiples']['msg'] > 3:
                await main.finish('这个词已经在本次游戏被用了太多次♠️')
            elif msg in groups[str(event.group_id)]['multiples'] and groups[str(event.group_id)]['multiples']['msg'] <= 3:
                groups[str(event.group_id)]['prev'] = msg
                groups[str(event.group_id)]['prev_end'] = res['end']
                earn = random.randint(-5, 20)
                try: 
                    diamonds[str(event.user_id)] += earn
                    save_diamond()
                except:
                    diamonds[str(event.user_id)] = earn
                    save_diamond()
                await main.send('🎉' + str(res['word']) + '🎉 ' + str(res['pinyin']) + '\n解释: ' + str(res['explanation']) + '\n出自: ' + str(res['derivation']) + '\n例子: ' + str(res['example']) + '💎' + str(earn))

                groups[str(event.group_id)]['multiples']['msg'] += 1
            else:
                groups[str(event.group_id)]['prev'] = msg
                groups[str(event.group_id)]['prev_end'] = res['end']
                earn = random.randint(-5, 20)
                try: 
                    diamonds[str(event.user_id)] += earn
                    save_diamond()
                except:
                    diamonds[str(event.user_id)] = earn
                    save_diamond()
                await main.send('🎉' + str(res['word']) + '🎉 ' + str(res['pinyin']) + '\n解释: ' + str(res['explanation']) + '\n出自: ' + str(res['derivation']) + '\n例子: ' + str(res['example']) + '💎' + str(earn))
                groups[str(event.group_id)]['multiples']['msg'] = 1
        else:
            await main.send('这个词好像不是成语或者它接不上啊, 上一个成语是: ' + groups[str(event.group_id)]['prev'] + ' 音节: '+ groups[str(event.group_id)]['prev_end'])

query_diamond = on_command('我的钻石')

@query_diamond.handle()
async def query_diamond_handle(event: MessageEvent, state: T_State, msg: Message = CommandArg()):
    try: 
        await query_diamond.send('你的钻石为: ' + str(diamonds[str(event.user_id)]))
    except:
        await query_diamond.send('你还没有钻石, 参加接龙吧')

query_rank = on_command('钻石排行')

@query_rank.handle()
async def query_rank_handle(event: MessageEvent, state: T_State, msg: Message = CommandArg()):
    global diamonds
    rank = sorted(diamonds.items(), key=lambda item:item[1], reverse=True)
    await query_rank.send('钻石排行榜:\n' + str(rank))


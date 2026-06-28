from contextlib import asynccontextmanager
import asyncio
'''
yield之前在整个项目中负责执行的是项目的预热
例如 bge-m3模型的加载 mysql的预热
yield之后的代码是应用关闭 with清理任务残留
'''

@asynccontextmanager
async def init(model):
    print(f'正在加载模型---->{model}')
    yield
    print(f'模型{model}初始化完成')

async def mian():
    async with init('BGE-M3'):
        print('请求任务正在处理中....')

if __name__ == '__main__':
    asyncio.run(mian())

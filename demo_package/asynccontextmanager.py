from contextlib import asynccontextmanager
import asyncio


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

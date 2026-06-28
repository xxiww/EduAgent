import asyncio
import time


async def demo(name,time):
    print(f'开始{name}--->wait:{time}s')
    await asyncio.sleep(time)
    print(f'结束{name}')

async def main():
    start = time.time()
    result = await asyncio.gather(
        demo('A',2),
        demo('B',1),
        demo('C',3)
    )
    print(f'耗时:{time.time() - start}s')
    return result
if __name__ == '__main__':
    asyncio.run(main())

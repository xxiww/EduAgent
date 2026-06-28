import asyncio
import time

def demo(name,num):
    print(f'{name}--->start,即将阻塞5s')
    time.sleep(5)
    result = num * num
    return result

async def main1(num):
    await asyncio.sleep(2)
    print(f'进入main{num}函数')

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None,demo,'Tom',12)
    print(f'结果1---->{result}')
    await asyncio.gather(
        main1(1),
        main1(2),
        main1(3)
    )
    result1 = await loop.run_in_executor(None,demo,'Amy',19)
    print(f'结果2---->{result1}')

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时:{time.time() - start}s')

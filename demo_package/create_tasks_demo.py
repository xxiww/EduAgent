import asyncio
import time

_background_tasks : set[asyncio.Task] = set()

async def grade_exam(exam_id):
    print(f'正在进行作业批改,作业id{exam_id}')
    await asyncio.sleep(1)
    print(f'作业{exam_id}批改完成')

async def submit():
    task = asyncio.create_task(grade_exam('EX-001'))
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)
    print('接口立即返回--->已收到,后台正在进行作业批改...')

async def main():
    await submit()
    await asyncio.sleep(3)
    print(f'当前任务数:{len(_background_tasks)}')

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时:{time.time() - start}s')

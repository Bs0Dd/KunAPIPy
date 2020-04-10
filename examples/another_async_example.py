from kunapipy.asynkundelik import kundelik
import asyncio
from kunapipy.asynkundelik.utils import TaskManager


async def get_dn_info():
    async with kundelik.AsyncKunAPI("login", "password") as dn:
        feed = await dn.get_feed()
        print(feed)
        info = await dn.get_info()
        print(info)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task_manager = TaskManager(loop)
    task_manager.add_task(get_dn_info)
    task_manager.run()

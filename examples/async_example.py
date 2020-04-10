from kunapipy.asynkundelik import kundelik
import asyncio
from datetime import datetime
from kunapipy.asynkundelik.utils import TaskManager


async def get_dn_info():
    homework = await dn.get_school_homework(
        1000002283077, str(datetime(2019, 9, 5)), str(datetime(2019, 9, 15))
    )
    print(homework)
    edu_groups = await dn.get_edu_groups()
    print(edu_groups)


async def close_session():
    await dn.close_session()


if __name__ == "__main__":
    dn = kundelik.AsyncKunAPI("login", "password")

    loop = asyncio.get_event_loop()
    task_manager = TaskManager(loop)
    task_manager.add_task(get_dn_info)
    task_manager.run(on_shutdown=close_session)

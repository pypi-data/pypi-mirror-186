import os
import asyncio
import logging

from typing import Tuple, Optional
from datetime import datetime


async def _run_tap_and_target(tap_cmd: str, target_cmd: str) -> Tuple[int, int]:
    start = datetime.now()
    logging.info(f"Starting command {tap_cmd} and {target_cmd}")

    read, write = os.pipe()
    tap = await asyncio.subprocess.create_subprocess_shell(
        tap_cmd, stdout=write, stderr=asyncio.subprocess.PIPE
    )
    os.close(write)
    target = await asyncio.subprocess.create_subprocess_shell(
        target_cmd, stdin=read, stderr=asyncio.subprocess.PIPE
    )
    os.close(read)

    await asyncio.wait([_log_stderr_msg(tap.stderr), _log_stderr_msg(target.stderr)])
    tap_return_code = await tap.wait()
    target_return_code = await target.wait()

    finish = datetime.now()
    logging.debug(
        f"Finished command {tap_cmd} and {target_cmd} at {finish.isoformat()}"
    )
    logging.info(
        f"Command {tap_cmd} and {target_cmd} finished in {(finish - start).total_seconds()} seconds"
    )
    return tap_return_code, target_return_code


async def _log_stderr_msg(stream: Optional[asyncio.StreamReader]):
    if isinstance(stream, asyncio.StreamReader):
        while True:
            line = await stream.readline()
            if line:
                msg = line.decode().strip()
                if "level=CRITICAL" in msg:
                    logging.critical(msg)
                elif "level=ERROR" in msg:
                    logging.error(msg)
                elif "level=WARNING" in msg:
                    logging.warning(msg)
                elif "level=DEBUG" in msg:
                    logging.debug(msg)
                else:
                    logging.info(msg)
            else:
                break

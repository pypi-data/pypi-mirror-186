from watchdog.events import FileSystemEventHandler, FileSystemEvent
from watchdog.observers import Observer
import asyncio
import logging
import traceback
import typing

log = logging.getLogger("dphyr.normal")

class Normal(FileSystemEventHandler):
    def __init__(self, reloader: typing.Callable, condition: typing.Callable) -> None:
        self.reload = reloader
        self.condition = condition
    def on_modified(self, event: FileSystemEvent) -> typing.NoReturn:
        log.info(f"File changed: {event.src_path}")
        if self.condition(event):
            log.info("Reloading...")
            path = event.src_path.replace("\\", "/").replace("/", ".")[:-3] # Convert to module path :D
            try:
                asyncio.run(self.reload(path))
                log.info(f"Reloaded {path}")
            except Exception as e:
                log.error(f"Failed to reload {path}")
                log.error(e)
                log.error(traceback.format_exc())
                
def normal_start(*paths: str, reloader: typing.Callable, condition: typing.Callable, recursive: bool, **kwargs) -> typing.NoReturn:
    """
    Internal function for starting normal observer.
    Please use dphyr.run() instead.
    """
    normal_observer = Observer(**kwargs)
    for path in paths:
        log.debug(f"Adding {path} to observer")
        normal_observer.schedule(Normal(reloader, condition), path, recursive=True)
    normal_observer.start()
    log.info("Started normal observer")
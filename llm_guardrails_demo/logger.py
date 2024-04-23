import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = logging.StreamHandler()

log_dir = Path(__file__).resolve().parent.parent / "data" / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = log_dir / f"{current_time}.log"
file_handler = logging.FileHandler(log_file, delay=True)

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# the formatter determines what our logs will look like
fmt_shell = "%(levelname)s %(asctime)s %(message)s"
fmt_file = "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"

shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# here we hook everything together
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)

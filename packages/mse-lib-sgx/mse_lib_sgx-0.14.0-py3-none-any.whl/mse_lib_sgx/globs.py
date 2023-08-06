"""mse_lib_sgx.global module."""

import os
from pathlib import Path
import threading
from typing import Optional

CODE_SECRET_KEY: Optional[bytes] = None

EXIT_EVENT: threading.Event = threading.Event()

UUID: Optional[str] = None

SSL_PRIVATE_KEY: Optional[str] = None
NEED_SSL_PRIVATE_KEY: bool = False

HOME_DIR_PATH: Path = Path(os.getenv("HOME", "/root"))
KEY_DIR_PATH: Path = Path(os.getenv("KEY_PATH", "/key"))
SECRETS_PATH: Path = Path(
    os.getenv("SECRETS_PATH", "/root/.cache/mse/secrets.json"))

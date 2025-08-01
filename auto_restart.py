#!/usr/bin/env python3
"""Helper to relaunch the API server if it crashes."""

import os
import subprocess
import sys
import time

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'OK workspaces', 'main.py')


def main() -> None:
    """Launch ``main.py`` and restart it if the process exits with an error."""
    cmd = [sys.executable, SCRIPT_PATH, *sys.argv[1:]]
    while True:
        process: subprocess.Popen | None = None
        try:
            process = subprocess.Popen(cmd)
            ret = process.wait()
        except KeyboardInterrupt:
            if process and process.poll() is None:
                process.terminate()
            break
        if ret == 0:
            break
        print(
            f"Server exited with status {ret}, restarting in 5 seconds...",
            flush=True,
        )
        time.sleep(5)


if __name__ == '__main__':
    main()

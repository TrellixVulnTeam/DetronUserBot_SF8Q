# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from vampireconfig import Config
else:
    if os.path.exists("vampireconfig.py"):
        from config import Development as Config

# vampire-x

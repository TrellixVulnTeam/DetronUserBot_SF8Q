# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from legendconfig import Config
else:
    if os.path.exists("legendconfig.py"):
        from config import Development as Config

# legendbot

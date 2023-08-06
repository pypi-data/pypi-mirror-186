import os
import dbm
import orjson

from pathlib import Path
from typing import List

from .paths import pisql_home

appname = "pisql"

config_db = dbm.open(f"{appname}-config", "c")

class iSqlConfig:
    def __new__(cls, appname: str, prefixes: List[str] = ["sql"]):
        cls.appname = appname
        cls.config_db = dbm.open(f"{appname}-config", "c")
        cls.user = None
        cls.sql_dir = None
        cls.out_dir = None
        cls.user_config = None
        cls.initUser()
        return cls

    @classmethod
    def initUser(cls):
        cls.user = os.getlogin()
        if not cls.user in cls.config_db:
            cls.sql_dir = (pisql_home / "sql-scripts").mkdir(parents=True, exist_ok=True)
            cls.out_dir = (pisql_home / "sql-results").mkdir(parents=True, exist_ok=True)
            cls.user_config = {"sql-dir": str(cls.sql_dir), "out-dir": str(cls.out_dir)}
            cls.setUserConfig(cls.user, cls.user_config)

    @classmethod
    def importFile(cls, file: Path):
        with open(file, "rb") as f:
            cls.user_config = orjson.loads(f.read())
        cls.setUserConfig(cls.user, cls.user_config)

    @classmethod
    def getAllUsers(cls):
        return cls.config_db.keys()

    @classmethod
    def getUserConfig(cls, user: str):
        cls.initUser() # in case user is not initialized on this machine
        return orjson.loads(cls.config_db[user])
        
    @classmethod
    def setUser(cls, user: str, config: dict):
        cls.config_db[user] = orjson.dumps(config)

    @classmethod
    def delUser(cls, user: str):
        if user in cls.config_db:
            del cls.config_db[user]

    @classmethod
    def reset(cls):
        del cls.config_db[cls.user]

    @classmethod
    def setUserKeyValue(cls, user: str, key: str, value: str):
        cls.config = getUserConfig(user)
        cls.config[key] = value
        iSqlConfig.setUserConfig(user, config)

    @classmethod
    def setUserConfig(cls, user: str, config: dict, overwrite: bool = False):
        cls.sql_dir = (pisql_home / "sql-scripts").mkdir(parents=True, exist_ok=True)
        cls.out_dir = (pisql_home / "sql-results").mkdir(parents=True, exist_ok=True)
        if user in cls.config_db:
            current_config = cls.getUserConfig(user)
            if overwrite:
                current_config = config
            else:
                current_config.update(config)
            sql_condition = not "sql-dir" in current_config or current_config["sql-dir"] in ["", None]
            out_condition = not "out-dir" in current_config or current_config["out-dir"] in ["", None]
            current_config["sql-dir"] = str(cls.sql_dir) if sql_condition else current_config["sql-dir"]
            current_config["out-dir"] = str(cls.out_dir) if out_condition else current_config["out-dir"]
            cls.config_db[user] = orjson.dumps(current_config)
        else:
            cls.config_db[user] = orjson.dumps(config)

    @classmethod
    def setCU(cls, config: dict, overwrite: bool = False):
        cls.setUserConfig(cls.user, config, overwrite)

    @staticmethod
    def getUserKeyValue(user: str, key: str):
        config = iSqlConfig.getUserConfig(user)
        return config[key]

    @classmethod
    def getSqlDir(cls):
        return cls.getUserKeyValue(cls.user, "sql-dir")

    @classmethod
    def getOutDir(cls):
        return cls.getUserKeyValue(cls.user, "out-dir")
    
    @classmethod
    def setSqlDir(cls, sql_dir: str):
        cls.setUserKeyValue(cls.user, "sql-dir", sql_dir)
    
    @classmethod
    def setOutDir(cls, out_dir: str):
        cls.setUserKeyValue(cls.user, "out-dir", out_dir)
    
    @classmethod
    def getCurrentConfig(cls):
        return cls.getUserConfig(cls.user)

    @classmethod
    def gCU(cls):
        return cls.getCurrentConfig()

    @classmethod
    def getCU(cls):
        return cls.getCurrentConfig()

    @classmethod
    def modifyCU(cls, key: str, value: str):
        config = cls.getCurrentConfig()
        config[key] = value
        cls.setUserConfig(cls.user, config)
        return config
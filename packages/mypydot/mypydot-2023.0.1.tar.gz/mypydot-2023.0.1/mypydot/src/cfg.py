import logging
import yaml
from os import getenv, sep
from os.path import join
from dataclasses import dataclass


@dataclass
class Cfg:
    cfg_path: str

    def __post_init__(self):
        self.data = self.__load_cfg()

    def __load_cfg(self) -> dict:
        try:
            with open(self.cfg_path, "r") as f:
                data = yaml.full_load(f)
            res = self._parse_env_vars(data)
            return res
        except FileNotFoundError:
            logging.error(f"Configuration file not found in {self.cfg_path=}")
            exit(1)

    @staticmethod
    def _parse_env_vars(d: dict):
        res = {}

        def parse_env(path):
            if path.startswith("$"):
                return getenv(path[1:])
            if path == "~":
                return getenv("HOME")
            return path

        for k, v in d["symlinks"].items():
            res[k] = {}
            for s, s_value in v.items():
                path_list = list(map(parse_env, s.split("/")))
                s_value_list = list(map(parse_env, s_value.split("/")))
                p = join(sep, *path_list)
                s_v = join(sep, *s_value_list)
                res[k][p] = s_v
        return res

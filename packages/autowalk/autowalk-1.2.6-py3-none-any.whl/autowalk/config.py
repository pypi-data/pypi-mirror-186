#!/usr/bin/env python

from pathlib import Path
from collections import namedtuple
import configparser


class Config(configparser.ConfigParser):
    # auto generate config file for user at home dir
    GLOBAL_CONFIG = None
    CONFIG_NAME = ".autowalk.cfg"  

    # these are default configs, there will be generated into config file
    AUTOJUMP_SECTION = "AutoJump"
    AUTOJUMP_CONFIG = dict(
        recursion_depth = 3,
        recursion_root_list = [
            'd:/',
            'e:/',
        ],
        black_list_dirname = [
            "$RECYCLE.BIN",
            "BaiduNetdiskDownload",
            "Config.Msi",
            "System Volume Information",
            "Recovery",
        ],
        black_list_dirname_prefix = [
            '.',
            '【',
            '_',
            '__',
            '$',
        ],
        weight_value_only_for_autojump = 1000,
        autojump_default_config = str(Path.home() / "AppData/Roaming/autojump/autojump.txt"),

        # for ranger
        prefix_and_suffix_only_for_ranger = [
            "g",
            ","
        ],
        ranger_remap_output_file = "~/.rc_remap.conf",
        default_map_only_for_ranger = [
            'map g/ cd /',
            'map g~ cd ~',  # WSL Home
            'map gr, cd /',
            'map gc, cd /mnt/c',
            'map gd, cd /mnt/d',
            'map ge, cd /mnt/e',
            'map gm, cd /mnt',
            'map gh, cd /mnt/c/Users/96338', # Windows Home
            'map gr, cd ~/.config/ranger',   # Ranger Home
            'map grs, cd /mnt/d/lab/ranger', # ranger script Home
        ]
    )

    def __init__(self, allow_no_value=False, *args, **kwargs) -> None:
        self._allow_no_value = allow_no_value
        super().__init__(allow_no_value=allow_no_value, *args, **kwargs)

    def seta(self,seciton, option="", value="", *args, **kwargs):
        if not self.exist(seciton):
            self[seciton] = {}
        if option:
            self[seciton][option] = value

    def exist(self, section, option=None):
        try:
            self.get(section, "")
        except configparser.NoSectionError:
            return False
        except configparser.NoOptionError:
            if option:
                return True if self.get(section, option, fallback=None) else False
            else:
                return True

    def read(self, filenames, encoding=None, must_exist=True):
        if must_exist and not Path(filenames).exists():
            raise FileNotFoundError(f"file not found => {filenames}")
        super().read(filenames, encoding=encoding)

    def write(self, path, mode="w", space_around_delimiters=True) -> None:
        with Path(path).open(mode) as f:
            super().write(f, space_around_delimiters=space_around_delimiters)
            print(f"Complete to write into: {path}")


    def make_config_dict(self):
        """
            generate config file for user 
            and load global variable for use
        """
        config_path = Path.home() / f'{self.CONFIG_NAME}'

        if not config_path.exists():
            for k,v in self.AUTOJUMP_CONFIG.items():
                v = self.handle_global_config(v)
                self.seta(self.AUTOJUMP_SECTION, k, v)  # type:ignore
            self.write( str(config_path) )

        # all values type is str (cat not update dict to other type because of the inner valid)
        self.read(config_path)

        add_name = namedtuple(
            "GLOBAL_CONFIG",
            self.AUTOJUMP_CONFIG.keys()  # add keys
        )
        # self.AUTOJUMP_CONFIG = { k:eval(v) for k,v in self.AUTOJUMP_CONFIG.items() }
        
        _global_config = self[self.AUTOJUMP_SECTION].values()
        _global_config = [*map(self.handle_global_config, _global_config)]

        self.GLOBAL_CONFIG = add_name._make(
            _global_config
        )  # add value

    def handle_global_config(self, value):
        if value:
            if value.isdigit():
                return int(value)
            else:
                value_list = value.split(",")
                if len(value_list) > 1:
                    return value_list
                else:
                    return value
        else:
            return value
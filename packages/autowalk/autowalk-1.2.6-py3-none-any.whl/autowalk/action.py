#!/usr/bin/env python

import sys
import argparse
import subprocess as sp
from pathlib import Path
from importlib import  import_module

from utils.color import C
from config import Config

CONFIG = Config()

class BaseAction(argparse.Action):
    

    def __init__(self,
                 option_strings,
                 dest=argparse.SUPPRESS,
                 default=argparse.SUPPRESS,
                 help=None):

        # delete -- , but this will cause you can't pass -- in add_argument
        option_strings = option_strings[0:1]

        super(BaseAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

        self.map_dict = {}
        self.dirs_list = []
        self.dup_set = set()
        self.path_set = set()
        self.PINYIN= False

    def __call__(self, parser, namespace, values, option_string=None):
        self._common_action()
        parser.exit()

    def _common_action(self):
        ...


    def _judge_prefix(self,t_dir):
        return  sum ( str( t_dir.name ).startswith(p) for p in CONFIG.black_list_dirname_prefix) 

    def _check_config(self, file_option, default_path_name, check=True):
        try:
            # namedtuple
            path_name = getattr( CONFIG, file_option)
        except:
            path_name = Path.home() / f"{default_path_name}"
            print(C.red("[Warning]"))
            print(C.red(f'\t you not set your autojump config path in {C.green("~/.autowalk.py")}'))

            msg = f"~/{default_path_name}"
            print(C.red(f'\t guess and automatically set the path name to {C.green(msg)}'))

        if str(path_name).startswith("~"):
            path_name = Path.home().joinpath(path_name[2:])

        path = Path(path_name)
        if check:
            if path.exists():
                return path
            else:
                Path(path).resolve().touch()
                print(C.red("[File Not Found]"))
                notice = f"{C.purple(str(path))}"
                print(C.green(f"\t Created It: {notice}"))
                return path
        else:
            return path

    def _check_ranger_config(self):
        return self._check_config(
            file_option = "ranger_remap_output_file",  # DEFAULT_CONFIG's key in config.py
            default_path_name = ".rc_remap.conf",
            check=False
        )

    def _check_autojump_config(self):
        return self._check_config(
            file_option = "autojump_default_config",   # DEFAULT_CONFIG's key in config.py 
            default_path_name = ".local/share/autojump/autojump.txt"
        )

    def _deal_dependency(self, module_name):
        try:
            return import_module(module_name)
        except Exception as e:
            print(C.red("[Dependency]"))

            notice = f"{C.purple(module_name)}"
            print(C.red(f"\t Module Not Found : {notice} "))

            tips = C.green(f"pip install {module_name}")
            print(C.red(f"\t Maybe you can try: {tips}"))
            exit(-1)

    def _collect(self, temp_dir):
        path_name = str( temp_dir )
        if path_name in self.path_set:
            pass
        else:
            self.path_set.add( path_name )
            dir_name = temp_dir.name.lower()
            if dir_name in self.dup_set:
                if self.PINYIN:
                    p = self._deal_dependency("pypinyin")
                    file_name = "".join(p.lazy_pinyin( f'{dir_name}-{temp_dir.parent.name}' ))
                else:
                    file_name = f'{dir_name}-{temp_dir.parent.name}'
            else:
                self.dup_set.add( dir_name )
                if self.PINYIN:
                    p = self._deal_dependency("pypinyin")
                    file_name = "".join(p.lazy_pinyin(dir_name))
                else:
                    file_name = dir_name

            map_str = f'map' \
                      f' ' \
                      f'{CONFIG.prefix_and_suffix_only_for_ranger[0]}' \
                      f'{file_name}' \
                      f'{CONFIG.prefix_and_suffix_only_for_ranger[1]}' \
                      f' ' \
                      f'cd' \
                      f' ' \
                      f'{path_name}'

            self.map_dict[map_str] = file_name         
            self.dirs_list.append( path_name )

    def _generate(self, path_obj_list, depth=0):
        if depth > CONFIG.recursion_depth:
            return
        else:
            for per_dir in path_obj_list:
                try:
                    if per_dir.is_dir() and str(per_dir.name) not in CONFIG.black_list_dirname and  self._judge_prefix(per_dir)==0:
                        self._collect(per_dir)
                        self._generate( list(per_dir.iterdir()), depth+1)
                except PermissionError:
                    ...

    def generate(self):
        path_obj_list = [Path(d).resolve() for d in CONFIG.recursion_root_list]
        self._generate(path_obj_list, depth=0)

    def append_default_and_print(self,):
        self.map_dict.update({}.fromkeys(CONFIG.default_map_only_for_ranger))
        for map_str in self.map_dict.keys():
            print(map_str)
        print()

    def append_default_and_to_file(self,):
        self.map_dict.update({}.fromkeys(CONFIG.default_map_only_for_ranger))
        ranger_path = self._check_ranger_config()
        ranger_path.write_text( "\n".join(self.map_dict.keys())+"\n",encoding="utf-8")
        print(C.purple("[Write Completed]"))
        info = C.green(f"cat {ranger_path}")
        print(C.purple(f'\tcheck it: {info}'))

class RemoveConfigAction(BaseAction):
    def _common_action(self):
        config_path = (Path.home() / f'{Config.CONFIG_NAME}')
        if config_path.exists():
            config_path.unlink()

            print(C.purple("[Delete Completed]"))
            info = C.green(f"cat {config_path}")
            print(C.purple(f'\tcheck it: {info}'))

            msg = C.green("aw -h")
            print(C.purple(f'\tprompt  : use {msg} can recreate config file'))
            print()

class RangerAction(BaseAction):
    def _common_action(self):
        self.generate()
        self.append_default_and_print()

class RangerFileAction(BaseAction):
    def _common_action(self):
        self.generate()
        self.append_default_and_to_file()

class RangerPinAction(BaseAction):
    def _common_action(self):
        self.PINYIN = True # Just For CN
        self.generate()
        self.append_default_and_print()

class RangerPinFileAction(BaseAction):
    def _common_action(self):
        self.PINYIN = True # Just For CN
        self.generate()
        self.append_default_and_to_file()


class JumpBase(BaseAction):
    def _common_action(self):
        self.generate()

        aj_cnofig_path = self._check_autojump_config()
        dirs_set = set(self.dirs_list)
        user_define_weight = CONFIG.weight_value_only_for_autojump

        old_conf = aj_cnofig_path.read_text(encoding="utf-8").strip()
        old_file_name_set = set()



        if not old_conf:
            aj_cnofig_path.write_text( "\n".join( f"{user_define_weight}\t{path_obj}" for path_obj in dirs_set)+"\n" ,encoding="utf-8")
        else:
            old_config_update_set = set()
            for line in old_conf.split("\n"):
                file_name = line.split("\t")[1]
                old_file_name_set.add(file_name)
                old_config_update_set.add (
                    str(float(line.split("\t")[0])+float(user_define_weight)) + "\t" + file_name
                )
            new_config_update_set = {f"{user_define_weight}\t{diff_name}" for diff_name in dirs_set - old_file_name_set}

            new_total_config = {*old_config_update_set,*new_config_update_set}
            aj_cnofig_path.write_text( "\n".join( new_total_config ) + "\n",encoding="utf-8")

        print(C.purple(f'\tUse {C.green("aw -l")} to check show your weights'))
        print()


class JumpListAction(JumpBase):
    def _common_action(self):
        sp.run("autojump -s", stderr=sp.PIPE,shell=True, universal_newlines=True)

class JumpClearAction(JumpBase):
    def find_autojump_config(self,):
        result = sp.run("autojump -s",stdout=sp.PIPE,stderr=sp.PIPE,shell=True, universal_newlines=True).stdout.split("\n")
        autojump_config_path = self._check_autojump_config()

        if Path(autojump_config_path).exists():
            autojump_config_path.write_text("",encoding="utf-8")
            cmd_str = C.green(f"cat {autojump_config_path}")
            cmd_str2 = C.green(f"aw -l")
            print(C.purple(f'\tUse command {cmd_str2} or {cmd_str} to check'))
            print()
        else:
            try:
                p2 = Path(result[-2].split(":")[1].strip())
                p2.write_text("",encoding="utf-8")
                cmd_str = C.green(f"cat {p2}")
                cmd_str2 = C.green(f"aw -l")
                print(C.purple(f'\tUse command {cmd_str2} or {cmd_str} to check'))
                print()
            except Exception as e:
                print(C.red("No Config File Find !"))

    def _common_action(self):
        print(C.purple("[Cleared]"))
        self.find_autojump_config()


class JumpJunkCleanAction(JumpBase):
    def _common_action(self):
        print(C.purple("[Cleaned Junk]"))

        try:
            autojump_config_path = self._check_autojump_config()
            
            with autojump_config_path.open() as f_before:
                before_clean_line_set = set(f_before)

            sp.run("autojump --purge",stdout=sp.PIPE,stderr=sp.PIPE,shell=True, universal_newlines=True).stdout

            with autojump_config_path.open() as f_after:
                after_clean_line_set = set(f_after)

            cleaned_set = before_clean_line_set - after_clean_line_set
            count = len(cleaned_set)
            if count == 0:
                print(f'\t{C.green("Nothing to clean up")}')         
            else:
                print(f'\t{C.red("─" * 55)}')
                for line in cleaned_set:
                    weight, file_name = line.strip().split("\t")

                    cleaned_item = f'{int(float( weight.strip()))}{C.red("│")} {file_name.strip()}'
                    print(f"\t\t{cleaned_item}")
                print(f'\t{C.red("─" * 55)}')
                print(f'\t{C.purple("total cleaned")}{C.red("│")} {C.green(count)}')
                print(f'\t{C.purple("weight config")}{C.red("│")} {C.green(autojump_config_path.resolve())}')
        except:
            print("\t"+C.purple(sp.run("autojump --purge",stdout=sp.PIPE,stderr=sp.PIPE,shell=True, universal_newlines=True).stdout))


class JumpCatConfigFile(BaseAction):
    def _common_action(self):
        print((Path.home() / ".autowalk.py").read_text(encoding="utf-8"))



class IncrWeightAction(argparse._StoreAction):
    def __call__(self, parser, args, values, option_string=None):
        try:
            file, weight = values
            
            _cd = "cd /D" if "win" in sys.platform else "cd"

            auto_jump_cmd = f'{_cd} "{file}" && autojump -a "{file}" && autojump -i {weight}'
            result = sp.run(auto_jump_cmd,stdout=sp.PIPE,stderr=sp.PIPE,shell=True, universal_newlines=True)
            weight_filename = result.stdout.strip().split(":",1)

            final_print = f'\t{C.green(weight_filename[0])}{C.red(":")}{C.purple(weight_filename[1])}'
            print(C.purple("[INCR COMPLETED]"))
            print(final_print)
            print()
        except:
            parser.print_help()


class DecrWeightAction(argparse._StoreAction):
    def __call__(self, parser, args, values, option_string=None):
        try:
            file, weight = values
            _cd = "cd /D" if "win" in sys.platform else "cd"

            auto_jump_cmd = f'{_cd} "{file}" && autojump -a "{file}" && autojump -d {weight}'
            result = sp.run(auto_jump_cmd,stdout=sp.PIPE,stderr=sp.PIPE,shell=True, universal_newlines=True)
            weight_filename = result.stdout.strip().split(":",1)

            final_print = f'\t{C.green(weight_filename[0])}{C.red(":")}{C.purple(weight_filename[1])}'
            print(C.purple("[DECR COMPLETED]"))
            print(final_print)
            print()
        except:
            parser.print_help()
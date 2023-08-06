import calendar
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from getpass import getpass
from threading import Thread
from time import sleep
from grpc import StatusCode
import dataclasses
import importlib.util
import locale
import os
import platform
import json
import pkg_resources
import requests
import re
import subprocess
from subprocess import DEVNULL, STDOUT, CompletedProcess
import sys
from typing import Any, Callable, List, Tuple
import colorama
from colorama import Back, Style, Fore
from prettytable import PrettyTable
import requests
from requests import ConnectTimeout, Response

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.tools import DataTool, EnumTool, PathTool, ResultTool, FullNameTool, PasswordTools, ResultUnpack, DateTimeTool, BitMask as BM, ParameterList
from pih.const import CONST, FIELD_NAME_COLLECTION, FIELD_COLLECTION, FILE, PASSWORD, PATHS, USER_PROPERTY, InternalMessageMethodTypes, MessageChannels, MessageCommands, LogLevels, MarkType, PolibasePersonReviewQuestStep, ServiceCommands, ServiceRoles, Settings, MessageTypes, MessageStatus
from pih.rpc_collection import Subscriber
from pih.collection import ActionValue, T, FieldItem, FieldItemList, FullName, InventoryReportItem, MessageCommandDescription, LoginPasswordPair, Mark, MarkDivision, MarkGroup, MarkGroupStatistics, ParamItem, PasswordSettings, PolibasePerson, PrinterADInformation, PrinterReport, PrinterStatus, Result, ServiceRoleInformation, ServiceRoleDescription, TemporaryMark, TimeTrackingEntity, TimeTrackingResultByDate, TimeTrackingResultByDivision, TimeTrackingResultByPerson, User, UserContainer, UserWorkstation, WhatsAppMessage, WhatsAppMessageListPayload, WhatsAppMessageButtonsPayload, Workstation, SettingsValue, PolibasePersonVisit, PolibasePersonVisitNotification, PolibasePersonVisitNotificationVO, DelayedMessage, MessageSearchCritery, DelayedMessageVO, PolibasePersonInformationQuest, PolibasePersonVisitSearchCritery, ReplicationStatus
from pih.rpc import RPC, Error, SubscribtionType


class MarkOutputAbstract:

    def by_any(self, value: str) -> None:
        raise NotImplemented()

    def result(self, result: Result[List[Mark]], caption: str, use_index: bool = False) -> None:
        raise NotImplemented()

class OutputAbstract:
    
    def indent(self, count: int = 1):
        raise NotImplemented()

    def header(self, caption: str) -> None:
        raise NotImplemented()

    def reset_indent(self):
        raise NotImplemented()

    def restore_indent(self):
        raise NotImplemented()

    def init(self) -> None:
        raise NotImplemented()

    def text_color(self, color: int, text: str) -> str:
        raise NotImplemented()

    def text_black(self, text: str) -> str:
        raise NotImplemented()

    def color_str(self, color: int, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def color(self, color: int, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def write_line(self, text: str) -> None:
        raise NotImplemented()

    def index(self, index: int, text: str, max_index: int = None) -> None:
        raise NotImplemented()

    def input(self, caption: str) -> None:
        raise NotImplemented()

    def input_str(self, caption: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def value(self, caption: str, value: str, text_before: str = None) -> None:
        raise NotImplemented()

    def get_action_value(self, caption: str, value: str, show: bool = True) -> ActionValue:
        raise NotImplemented()

    def head(self, caption: str) -> None:
        raise NotImplemented()

    def head1(self, caption: str) -> None:
        raise NotImplemented()

    def head2(self, caption: str) -> None:
        raise NotImplemented()

    def new_line(self) -> None:
        raise NotImplemented()

    def separated_line(self) -> None:
        self.new_line()

    def error_str(self, caption: str) -> str:
        raise NotImplemented()

    def error(self, caption: str) -> None:
        raise NotImplemented()

    def notify_str(self, caption: str) -> str:
        raise NotImplemented()

    def notify(self, caption: str) -> None:
        raise NotImplemented()

    def good_str(self, caption: str) -> str:
        raise NotImplemented()

    def good(self, caption: str) -> None:
        raise NotImplemented()

    def green_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def green(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def yellow_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def yellow(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def black_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def black(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def white_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def white(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def draw_line(self, color: str = Back.LIGHTBLUE_EX, char: str = " ", width: int = 80) -> None:
        raise NotImplemented()

    def line(self) -> None:
        raise NotImplemented()

    def magenta_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def magenta(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def cyan(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def cyan_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def red(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def red_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def blue(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def blue_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def bright(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def bright_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def get_number(self, value: int) -> str:
        raise NotImplemented()

    def write_result(self, result: Result[T], use_index: bool = True, item_separator: str = "\n", empty_result_text: str = "Не найдено", separated_result_item: bool = True, label_function:  Callable[[Any], str] = None, data_label_function: Callable[[int, FieldItem, Result[T], Any], Tuple[bool, str]] = None, title: str = None) -> None:
        raise NotImplemented()

class MarkOutputBase(MarkOutputAbstract):

    def __init__(self):
        self.parent: OutputBase


class MarkOutput(MarkOutputBase):

    def by_any(self, value: str) -> None:
        self.result(
            PIH.RESULT.MARK.by_any(value), "Результат:", True)

    def result(self, result: Result[List[Mark]], caption: str, use_index: bool = False) -> None:
        self.parent.table_with_caption_first_title_is_centered(result, caption, use_index)


class UserOutputAbstract:

    def result(self, result: Result[List[User]], caption: str = None, use_index: bool = False, root_location: str = CONST.AD.ACTIVE_USERS_CONTAINER_DN) -> None:
        raise NotImplemented()

class OutputExtendedAbstract:

    def main_title(self) -> None:
        raise NotImplemented()  

    def rpc_service_header(self, host: str, port: int, description: str) -> None:
        raise NotImplemented()  

    def service_header(self, role: ServiceRoles) -> None:
        raise NotImplemented()  

    def free_marks(self, show_guest_marks: bool, use_index: bool = False) -> None:
        raise NotImplemented()  

    def guest_marks(self, use_index: bool = False) -> None:
        raise NotImplemented()

    def temporary_candidate_for_mark(self, mark: Mark) -> None:
        raise NotImplemented()  

    def free_marks_group_statistics(self, use_index: bool = False, show_guest_marks: bool = None) -> None:
        raise NotImplemented()  

    def free_marks_by_group(self, group: dict, use_index: bool = False) -> None:
        raise NotImplemented()  

    def free_marks_group_statistics_for_result(self, result: Result, use_index: bool) -> None:
        raise NotImplemented()  

    def free_marks_by_group_for_result(self, group: MarkGroup, result: Result, use_index: bool) -> None:
        raise NotImplemented()  

    def temporary_marks(self, use_index: bool = False,) -> None:
        raise NotImplemented()  

    def containers_for_result(self, result: Result, use_index: bool = False) -> None:
        raise NotImplemented()  

    def table_with_caption_first_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def table_with_caption_last_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def table_with_caption(self, result: Any, caption: str = None, use_index: bool = False, modify_table_function: Callable = None, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def template_users_for_result(self, data: dict, use_index: bool = False) -> None:
        raise NotImplemented()  

    def clear_screen(self):
        raise NotImplemented()

class UserOutputBase(UserOutputAbstract):

    def __init__(self):
        self.parent: OutputBase

class UserOutput(UserOutputBase):

    def result(self, result: Result[List[User]], caption: str = None, use_index: bool = False, root_location: str = CONST.AD.ACTIVE_USERS_CONTAINER_DN) -> None:
        fields: FieldItemList = result.fields
        base_location_list = PIH.DATA.FORMAT.location_list(
            root_location, False)
        root_base_location = base_location_list[0:2]
        root_base_location.reverse()
        base_location = CONST.AD.LOCATION_JOINER.join([".".join(
            root_base_location), CONST.AD.LOCATION_JOINER.join(base_location_list[2:])])
        location_field = fields.get_item_by_name(
            FIELD_NAME_COLLECTION.DN)
        pevious_caption: str = location_field.caption
        location_field.caption = f"{location_field.caption} ({base_location})"
        def modify_data(field: FieldItem, user: User) -> str:
            if field.name == USER_PROPERTY.DN:
                return CONST.AD.LOCATION_JOINER.join(filter(
                    lambda x: x not in base_location_list, PIH.DATA.FORMAT.location_list(user.distinguishedName)))
            if field.name == USER_PROPERTY.USER_ACCOUNT_CONTROL:
                return "\n".join(PIH.DATA.FORMAT.get_user_account_control_values(user.userAccountControl))
            if field.name == USER_PROPERTY.DESCRIPTION:
                return user.description
            if field.name == USER_PROPERTY.NAME:
                return "\n".join(user.name.split(" "))
            return None
        self.parent.table_with_caption(
            result, "Пользватели:" if len(result.data) > 1 else "Пользватель:", False, None, modify_data)
        location_field.caption = pevious_caption


class InputAbstract:

    def input(self, caption: str = None, new_line: bool = True) -> str:
        raise NotImplemented()

    def telephone_number(self, format: bool = True, telephone_prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
        raise NotImplemented()

    def email(self) -> str:
        raise NotImplemented()

    def message(self, caption: str = None, prefix: str = None) -> str:
        raise NotImplemented()

    def description(self) -> str:
        raise NotImplemented()

    def login(self, check_on_exists: bool = False) -> str:
        raise NotImplemented()

    def indexed_list(self, caption: str, name_list: List[Any], caption_list: List[str], by_index: bool = False) -> str:
        raise NotImplemented()

    def indexed_field_list(self, caption: str, list: FieldItemList) -> str:
        raise NotImplemented()

    def index(self, caption: str, data: List, label_function: Callable[[Any, int], str] = None) -> int:
        raise NotImplemented()

    def item_by_index(self, caption: str, data: List[Any], label_function: Callable[[Any, int], str] = None) -> Any:
        raise NotImplemented()

    def tab_number(self, check: bool = True) -> str:
        raise NotImplemented()

    def password(self, secret: bool = True, check: bool = False, settings: PasswordSettings = None, is_new: bool = True) -> str:
        raise NotImplemented()

    def same_if_empty(self, caption: str, src_value: str) -> str:
        raise NotImplemented()

    def name(self) -> str:
        raise NotImplemented()

    def full_name(self, one_line: bool = False) -> FullName:
        raise NotImplemented()

    def yes_no(self, text: str = " ", enter_for_yes: bool = False) -> bool:
        raise NotImplemented()

    def message_for_user_by_login(self, login: str) -> str:
        raise NotImplemented()

    def polibase_person_any(self) -> str:
        raise NotImplemented()


class UserInputAbstract:

    def container(self) -> UserContainer:
        raise NotImplemented()

    def by_name(self) -> User:
        raise NotImplemented()

    def title_any(self, title: str = None) -> str:
        raise NotImplemented()

    def by_any(self, value: str = None, active: bool = None, title: str = None) -> User:
        raise NotImplemented()

    def telephone_number(self, value: str = None, active: bool = None, title: str = None) -> str:
        raise NotImplemented()

    def template(self) -> dict:
        raise NotImplemented()

    def search_attribute(self) -> str:
        raise NotImplemented()

    def search_value(self, search_attribute: str) -> str:
        raise NotImplemented()

    def generate_login(self, full_name: FullName, ask_for_remove_inactive_user_if_login_is_exists: bool = True, ask_for_use: bool = True) -> str:
        raise NotImplemented()

    def generate_password(self, once: bool = False, settings: PasswordSettings = PASSWORD.SETTINGS.DEFAULT) -> str:
        raise NotImplemented()


class UserInputBase(UserInputAbstract):

    def __init__(self):
        self.parent: InputBase


class MarkInputAbstract:

    def free(self, group: MarkGroup = None) -> Mark:
        raise NotImplemented()

    def person_division(self) -> MarkDivision:
        raise NotImplemented()

    def by_name(self) -> Mark:
        raise NotImplemented()

    def by_any(self, value: str = None) -> Mark:
        raise NotImplemented()

    def any(self) -> str:
        raise NotImplemented()


class MarkInputBase(MarkInputAbstract):

    def __init__(self):
        self.parent: InputBase


class InputBase(InputAbstract):

    def __init__(self):
        self.output: OutputBase
        self.mark: MarkInputBase
        self.user: UserInputBase


class OutputBase(OutputAbstract, OutputExtendedAbstract):

    def __init__(self, user_output: UserOutputBase = None, mark_output: MarkOutputBase = None):
        self.TEXT_BEFORE: str = ""
        self.TEXT_AFTER: str = ""
        self.INDEX: str = "  "
        self.INDEX_COUNT: int = 0
        self.user: UserOutputBase = user_output
        self.user.parent = self
        self.mark: MarkOutputBase = mark_output
        self.mark.parent = self


class SessionAbstract:

    def run_forever_untill_enter_not_pressed(self) -> None:
        raise NotImplemented()

    def exit(self, timeout: int = None, message: str = None) -> None:
        raise NotImplemented()

    def get_login(self) -> str:
        raise NotImplemented()

    def get_argv(self, position: int, default: str = "") -> str:
        raise NotImplemented()

    def get_user(self) -> User:
        raise NotImplemented()

    def get_user_given_name(self) -> str:
        raise NotImplemented()

    def start(self, login: str, notify: bool = True) -> None:
        raise NotImplemented()

    def say_hello(self) -> None:
        raise NotImplemented()

    def argv(self, index: int = None) -> List[str]:
        raise NotImplemented()

    def get_file_path(self) -> str:
        raise NotImplemented()

    def get_file_name(self) -> str:
        raise NotImplemented()

    def authenticate(self, exit_on_fail: bool = True) -> bool:
        raise NotImplemented()

    def add_allowable_group(self, value: CONST.AD.Groups) -> None:
        raise NotImplemented()


class SessionBase(SessionAbstract):

    def __init__(self, input: InputBase = None, output: OutputBase = None):
        self.input: InputBase = input
        self.output: OutputBase = output
        self.allowable_groups: List[CONST.AD.Groups] = []


class Session(SessionBase):

    def __init__(self, input: InputBase = None, output: OutputBase = None):
        super().__init__(input, output)
        self.login: str = None
        self.user: User = None

    def run_forever_untill_enter_not_pressed(self) -> None:
        try:
            self.output.green("Нажмите Ввод для выхода...")
            input()
        except KeyboardInterrupt:
            pass

    def exit(self, timeout: int = None, message: str = None) -> None:
        if message is not None:
            self.output.error(message)
        if timeout is None:
            timeout = 5
        sleep(timeout)
        exit()

    def get_login(self) -> str:
        if self.login is None:
            self.start(PIH.OS.get_login())
        return self.login

    def get_argv(self, position: int = 0, default: str = "") -> str:
        argv: List[str] = sys.argv
        argv_len: int = len(argv)
        return argv[position] if argv_len >= position + 1 else default

    def get_user(self) -> User:
        if self.user is None:
            self.user = PIH.RESULT.USER.by_login(
                self.get_login()).data
        return self.user

    def get_user_given_name(self) -> str:
        return FullNameTool.to_given_name(self.get_user().name)

    def add_allowable_group(self, value: CONST.AD.Groups) -> None:
        self.allowable_groups.append(value)

    def start(self, login: str, notify: bool = True) -> None:
        if self.login is None:
            self.login = login
            if notify:
                PIH.MESSAGE.COMMAND.start_session()

    def say_hello(self) -> None:
        user: User = self.get_user()
        if user is not None:
            self.output.good(f"Добро пожаловать, {user.name}")
            self.output.new_line()
            return
        self.output.error(f"Ты кто такой? Давай, до свидания...")
        self.exit()

    def argv(self, index: int = None) -> List[str]:
        if index is None:
            return sys.argv[1:] if len(sys.argv) > 1 else None
        return sys.argv[index] if len(sys.argv) > index else None

    def get_file_path(self) -> str:
        return self.argv(0)

    def get_file_name(self) -> str:
        return PathTool.get_file_name(self.get_file_path())

    def authenticate(self, exit_on_fail: bool = True) -> bool:
        try:
            self.output.green("Инициализация...")
            if PIH.SERVICE.check_accessibility(ServiceRoles.AD):
                self.output.clear_screen()
                self.output.head1("Пройдите, аутентификацию, пожалуйста.")
                login: str = PIH.OS.get_login()
                if not self.input.yes_no(f"Использовать логин '{login}'", True):
                    login = PIH.input.login()
                password: str = PIH.input.password(is_new=False)
                if DataTool.rpc_unrepresent(RPC.call(ServiceCommands.authenticate, (login, password))):
                    self.start(login, False)
                    PIH.MESSAGE.COMMAND.login()
                    self.output.good(self.output.text_black(
                        f"Добро пожаловать, {self.get_user().name}..."))
                    return True
                else:
                    if exit_on_fail:
                        self.exit(
                            5, "Неверный пароль или логин. До свидания...")
                    else:
                        return False
            else:
                self.output.error(
                    "Сервис аутентификации недоступен. До свидания...")
        except KeyboardInterrupt:
            self.exit(0, "Выход")


class Stdin:

    def __init__(self):
        self.data: str = None
        self.wait_for_data_input: bool = False
        self.wait_for_internal_interrupt: bool = False

    def is_empty(self) -> bool:
        return DataTool.is_empty(self.data)

    def set_default_state(self) -> None:
        self.wait_for_internal_interrupt = False
        self.wait_for_data_input = False
        self.data = None


class Output(OutputBase):

    def indent(self, count: int = 1):
        self.INDEX_COUNT = count
        self.TEXT_BEFORE = self.INDEX*count

    def reset_indent(self):
        self.TEXT_BEFORE = ""

    def restore_indent(self):
        self.indent(self.INDEX_COUNT)

    def init(self) -> None:
        colorama.init()

    def text_color(self, color: int, text: str) -> str:
        return f"{color}{text}{Fore.RESET}"

    def text_black(self, text: str) -> str:
        return self.text_color(Fore.BLACK, text)

    def color_str(self, color: int, text: str, text_before: str = None, text_after: str = None) -> str:
        text = f" {text} "
        text_before = text_before if text_before is not None else self.TEXT_BEFORE
        text_after = text_after if text_after is not None else self.TEXT_AFTER
        return f"{text_before}{color}{text}{Back.RESET}{text_after}"

    def color(self, color: int, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.color_str(
            color, text, text_before, text_after))

    def write_line(self, text: str) -> None:
        print(text)

    def index(self, index: int, text: str, max_index: int = None) -> None:
        indent: str = ""
        if max_index is not None:
            indent = " " * (len(str(max_index)) - len(str(index)))
        if index is None:
            self.write_line(f"{indent}{text}")
        else:
            self.write_line(f"{index}. {indent}{text}")

    def input(self, caption: str) -> None:
        self.write_line(self.input_str(
            caption, self.TEXT_BEFORE, text_after=":"))

    def input_str(self, caption: str, text_before: str = None, text_after: str = None) -> str:
        return self.white_str(f"{Fore.BLACK}{caption}{Fore.RESET}", text_before, text_after)

    def value(self, caption: str, value: str, text_before: str = None) -> None:
        text_before = text_before or self.TEXT_BEFORE
        self.cyan(caption, text_before, f": {value}")

    def get_action_value(self, caption: str, value: str, show: bool = True) -> ActionValue:
        if show:
            self.value(caption, value)
        return ActionValue(caption, value)

    def head(self, caption: str) -> None:
        self.cyan(caption)

    def head1(self, caption: str) -> None:
        self.magenta(caption)

    def head2(self, caption: str) -> None:
        self.yellow(self.text_color(Fore.BLACK, caption))

    def new_line(self) -> None:
        print()

    def separated_line(self) -> None:
        self.new_line()

    def error_str(self, caption: str) -> str:
        return self.red_str(caption)

    def error(self, caption: str) -> None:
        self.write_line(self.error_str(caption))

    def notify_str(self, caption: str) -> str:
        return self.yellow_str(caption)

    def notify(self, caption: str) -> None:
        self.write_line(self.notify_str(caption))

    def good_str(self, caption: str) -> str:
        return self.green_str(caption)

    def good(self, caption: str) -> str:
        self.write_line(self.good_str(self.text_black(caption)))

    def green_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.GREEN, text, text_before, text_after)

    def green(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.green_str(text, text_before, text_after))

    def yellow_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.YELLOW, text, text_before, text_after)

    def yellow(self, text: str, text_before: str = None, text_after: str = None) -> None:
        text_before = text_before or self.TEXT_BEFORE
        text_after = text_after or self.TEXT_AFTER
        self.write_line(self.yellow_str(text, text_before, text_after))

    def black_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.BLACK, text, text_before, text_after)

    def black(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.black_str(text, text_before, text_after))

    def white_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.WHITE, text, text_before, text_after)

    def white(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.white_str(text, text_before, text_after))

    def draw_line(self, color: str = Back.LIGHTBLUE_EX, char: str = " ", width: int = 80) -> None:
        self.write_line("") if color is None else self.color(
            color, char*width)

    def line(self) -> None:
        self.new_line()
        self.draw_line(Back.WHITE, self.text_color(
            Fore.BLACK, "_"), width=128)
        self.new_line()

    def magenta_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.LIGHTMAGENTA_EX, text, text_before, text_after)

    def magenta(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.magenta_str(text, text_before, text_after))

    def cyan(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.cyan_str(text, text_before, text_after))

    def cyan_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.CYAN, text, text_before, text_after)

    def red(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.red_str(text, text_before, text_after))

    def red_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.LIGHTRED_EX, text, text_before, text_after)

    def blue(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.blue_str(text, text_before, text_after))

    def blue_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.BLUE, text, text_before, text_after)

    def bright(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.bright_str(text, text_before, text_after))

    def bright_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Style.BRIGHT, text, text_before, text_after)

    def get_number(self, value: int) -> str:
        return CONST.VISUAL.NUMBER_SYMBOLS[value - 1]

    def header(self, caption: str) -> None:
        self.head2(caption)

    def write_result(self, result: Result[T], use_index: bool = True, item_separator: str = "\n", empty_result_text: str = "Не найдено", separated_result_item: bool = True, label_function: Callable[[Any], str] = None, data_label_function: Callable[[int, FieldItem, Result, Any], Tuple[bool, str]] = None, title: str = None) -> None:
        data: list = DataTool.as_list(result.data)
        result_string_list: list[str] = None
        if DataTool.is_empty(data):
            self.new_line()
            self.write_line(empty_result_text)
        else:
            if not DataTool.is_empty(title):
                self.write_line(title)
            for index, data_item in enumerate(data):
                result_string_list = []
                if use_index and len(data) > 1:
                    result_string_list.append(f"*{str(index + 1)}*:")
                if label_function is None:
                    for field_item in result.fields.list:
                        field: FieldItem = field_item
                        if not field.visible:
                            continue
                        item_data_value: str = None
                        if isinstance(data_item, dict):
                            item_data_value = data_item[field.name]
                        elif dataclasses.is_dataclass(data_item):
                            item_data_value = data_item.__getattribute__(field.name)
                        if DataTool.is_empty(item_data_value):
                            if field.default_value is not None:
                                item_data_value = field_item.default_value
                            elif data_label_function is None:
                                continue
                        default_value_label_function: Callable[[int, FieldItem, Result[T], Any], (bool, str)] =  (
                            lambda _, field, _2, data_value: (True, f"*{field.caption}*: {data_value}"))
                        result_data_label_function: Callable[[int, FieldItem, Result[T], Any], (bool, str)] = data_label_function or default_value_label_function 
                        label_value_result: tuple[bool, str] = result_data_label_function(index, field, data_item, item_data_value)
                        label_value: str = None
                        if label_value_result[0] == True:
                            label_value = label_value_result[1]
                        else:
                            label_value = default_value_label_function(index, field, data_item, item_data_value)[1]
                        if label_value is not None:
                            result_string_list.append(label_value)
                else:
                    result_string_list.append(label_function(data_item))  
                if separated_result_item:
                    self.separated_line()
                self.write_line(item_separator.join(result_string_list))

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_title(self) -> None:
        self.cyan(self.text_color(Fore.WHITE, "███ ███ █┼█"))
        self.cyan(
            self.text_color(Fore.WHITE, "█▄█ ┼█┼ █▄█"))
        self.cyan(self.text_color(Fore.WHITE, "█┼┼ ▄█▄ █┼█") +
                         self.text_color(Fore.BLACK, f" {PIH.VERSION.local()}"))
        self.new_line()

    def rpc_service_header(self, host: str, port: int, description: str) -> None:
        self.blue("PIH service")
        self.blue(f"Version: {PIH.VERSION.local()}")
        self.blue(f"PyPi Version: {PIH.VERSION.remote()}")
        self.green(f"Service host: {host}")
        self.green(f"Service port: {port}")
        self.green(f"Service name: {description}")

    def service_header(self, role: ServiceRoles) -> None:
        service_role_value: ServiceRoleDescription = role.value
        if service_role_value.isolate:
            self.blue(f"[Debug]")
        self.blue("Запуск сервиса")
        self.blue(f"PIH версия: {PIH.VERSION.remote()}")
        self.green(f"Хост: {service_role_value.host}")
        self.green(f"Порт: {service_role_value.port}")
        self.green(f"Имя сервиса: {service_role_value.name}")
        self.green(
            f"Описание сервиса: {service_role_value.description}")
        self.green(
            f"Идентификатор процесса: {service_role_value.pid}")

    def free_marks(self, show_guest_marks: bool, use_index: bool = False) -> None:
        self.table_with_caption_first_title_is_centered(
            PIH.RESULT.MARK.free_list(show_guest_marks), "Свободные карты доступа:", use_index)

    def guest_marks(self, use_index: bool = False) -> None:
        mark_list_result: Result[List[Mark]] = PIH.RESULT.MARK.free_list(True)
        mark_list_result.fields.visible(
            FIELD_NAME_COLLECTION.GROUP_NAME, False)

        def filter_function(item: Mark) -> bool:
            return EnumTool.get(MarkType, item.type) == MarkType.GUEST
        ResultTool.data_filter(mark_list_result, filter_function)
        self.table_with_caption_first_title_is_centered(
            mark_list_result, "Гостевые карты доступа:", use_index)

    def temporary_candidate_for_mark(self, mark: Mark) -> None:
        self.mark.result(
            Result(FIELD_COLLECTION.ORION.FREE_MARK, [mark]), "Временная карта")

    def free_marks_group_statistics(self, use_index: bool = False, show_guest_marks: bool = None) -> None:
        self.free_marks_group_statistics_for_result(
            PIH.RESULT.MARK.free_marks_group_statistics(show_guest_marks), use_index)

    def free_marks_by_group(self, group: dict, use_index: bool = False) -> None:
        self.free_marks_by_group_for_result(
            PIH.RESULT.MARK.free_marks_by_group_id(group), group, use_index)

    def free_marks_group_statistics_for_result(self, result: Result, use_index: bool) -> None:
        self.table_with_caption_last_title_is_centered(
            result, "Свободные карты доступа:", use_index)

    def free_marks_by_group_for_result(self, group: MarkGroup, result: Result, use_index: bool) -> None:
        group_name: str = group.GroupName
        self.table_with_caption_last_title_is_centered(
            result, f"Свободные карты доступа для группы доступа '{group_name}':", use_index)

    def temporary_marks(self, use_index: bool = False,) -> None:
        def modify_table(table: PrettyTable, caption_list: List[str]):
            table.align[caption_list[0]] = "c"
            table.align[caption_list[1]] = "c"
        self.table_with_caption(
            PIH.RESULT.MARK.temporary_list(), "Список временных карт:", use_index, modify_table)

    def containers_for_result(self, result: Result, use_index: bool = False) -> None:
        self.table_with_caption(result, "Подразделение:", use_index)

    def table_with_caption_first_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        def modify_table(table: PrettyTable, caption_list: List[str]):
            table.align[caption_list[int(use_index)]] = "c"
        self.table_with_caption(
            result, caption, use_index, modify_table, label_function)

    def table_with_caption_last_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        def modify_table(table: PrettyTable, caption_list: List[str]):
            table.align[caption_list[-1]] = "c"
        self.table_with_caption(
            result, caption, use_index, modify_table, label_function)

    def table_with_caption(self, result: Any, caption: str = None, use_index: bool = False, modify_table_function: Callable = None, label_function: Callable = None) -> None:
        if caption is not None:
            self.cyan(caption)
        is_result_type: bool = isinstance(result, Result)
        field_list = result.fields if is_result_type else ResultUnpack.unpack_fields(
            result)
        data: Any = result.data if is_result_type else ResultUnpack.unpack_data(result)
        if DataTool.is_empty(data):
            self.error("Не найдено!")
        else:
            if not isinstance(data, list):
                data = [data]
            if len(data) == 1:
                use_index = False
            if use_index:
                field_list.list.insert(0, FIELD_COLLECTION.INDEX)
            caption_list: List = field_list.get_caption_list()
            def create_table(caption_list: List[str]) -> PrettyTable:
                from prettytable.colortable import ColorTable, Themes
                table: ColorTable = ColorTable(
                    caption_list, theme=Themes.OCEAN)
                table.align = "l"
                if use_index:
                    table.align[caption_list[0]] = "c"
                return table
            table: PrettyTable = create_table(caption_list)
            if modify_table_function is not None:
                modify_table_function(table, caption_list)
            for index, item in enumerate(data):
                row_data: List = []
                for field_item_obj in field_list.get_list():
                    field_item: FieldItem = field_item_obj
                    if field_item.visible:
                        if field_item.name == FIELD_COLLECTION.INDEX.name:
                            row_data.append(str(index + 1))
                        elif not isinstance(item, dict):
                            if label_function is not None:
                                modified_item_data = label_function(
                                    field_item, item)
                                if modified_item_data is None:
                                    modified_item_data = getattr(
                                        item, field_item.name)
                                row_data.append(DataTool.check(
                                    modified_item_data, lambda: modified_item_data, "") if modified_item_data is None else modified_item_data)
                            else:
                                item_data = getattr(item, field_item.name)
                                row_data.append(DataTool.check(
                                    item_data, lambda: item_data, ""))
                        elif field_item.name in item:
                            item_data = item[field_item.name]
                            if label_function is not None:
                                modified_item_data = label_function(
                                    field_item, item)
                                row_data.append(
                                    item_data if modified_item_data is None else modified_item_data)
                            else:
                                row_data.append(item_data)
                table.add_row(row_data)
            print(table)
            table.clear()

    def template_users_for_result(self, data: dict, use_index: bool = False) -> None:
        def data_handler(field_item: FieldItem, item: User) -> Any:
            filed_name = field_item.name
            if filed_name == FIELD_NAME_COLLECTION.DESCRIPTION:
                return item.description
            return None
        self.table_with_caption(
            data, "Шаблоны для создания аккаунта пользователя:", use_index, None, data_handler)



class Input(InputBase):

    def __init__(self, user_input: UserInputBase, mark_input: MarkInputBase, output: OutputBase):
        self.output: OutputBase = output
        if user_input is not None:
            self.user: UserInputBase = user_input
            self.user.parent = self
        if mark_input is not None:
            self.mark: MarkInputBase = mark_input
            self.mark.parent = self

    def input(self, caption: str = None, new_line: bool = True) -> str:
        try:
            if new_line and caption is not None:
                self.output.input(caption)
            return input(self.output.TEXT_BEFORE) if new_line else input(self.output.TEXT_BEFORE + caption)
        except KeyboardInterrupt:
            raise KeyboardInterrupt()

    def telephone_number(self, format: bool = True, telephone_prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
        while True:
            self.output.input("Номер телефона")
            use_telephone_prefix: bool = telephone_prefix is not None
            telephone_number: str = self.input(
                telephone_prefix if use_telephone_prefix else "", False)
            if use_telephone_prefix:
                if not telephone_number.startswith(telephone_prefix):
                    telephone_number = telephone_prefix + telephone_number
            check: bool = None
            if format:
                telehone_number_after_fix = PIH.DATA.FORMAT.telephone_number(
                    telephone_number, telephone_prefix)
                check = PIH.CHECK.telephone_number(telehone_number_after_fix)
                if check and telehone_number_after_fix != telephone_number:
                    telephone_number = telehone_number_after_fix
                    self.output.value("Телефон отформатирован", telephone_number)
            if check or PIH.CHECK.telephone_number(telephone_number):
                return telephone_number
            else:
                self.output.error("Неверный формат номера телефона!")

    def email(self) -> str:
        while True:
            email = self.input("Электронная почта")
            if PIH.CHECK.email(email):
                return email
            else:
                self.output.error("Неверный формат электронной почты!")

    def message(self, caption: str = None, prefix: str = None) -> str:
        caption = caption or "Введите сообщение"
        self.output.input(caption)
        return (prefix or "") + self.input(prefix, False)

    def description(self) -> str:
        self.output.input("Введите описание")
        return self.input()

    def login(self, check_on_exists: bool = False) -> str:
        login: str = None
        while True:
            login = self.input("Введите логин")
            if PIH.CHECK.login(login):
                if check_on_exists and PIH.CHECK.USER.exists_by_login(login):
                    self.output.error("Логин занят!")
                else:
                    return login
            else:
                self.output.error("Неверный формат логина!")

    def indexed_list(self, caption: str, name_list: List[Any], caption_list: List[str], by_index: bool = False) -> str:
        return self.item_by_index(caption, name_list, lambda item, index: caption_list[index if by_index else item])

    def indexed_field_list(self, caption: str, list: FieldItemList) -> str:
        name_list = list.get_name_list()
        return self.item_by_index(caption, name_list, lambda item, _: list.get_item_by_name(item).caption)

    def index(self, caption: str, data: List, label_function: Callable[[Any, int], str] = None) -> int:
        selected_index: int = -1
        length = len(data)
        if label_function is None:
            label_function = lambda item, _: item
        while True:
            max_index: int = length
            if length > 1:
                for index, item in enumerate(data):
                    self.output.index(
                        index + 1 if length > 1 else None, label_function(item, index), max_index)
            if length == 1:
                return 0
            selected_index = self.input(
                caption + f" (от 1 до {length})")
            if selected_index == "":
                selected_index = 1
            try:
                selected_index = int(selected_index) - 1
                if selected_index >= 0 and selected_index < length:
                    return selected_index
            except ValueError:
                continue

    def item_by_index(self, caption: str, data: List[Any], label_function: Callable[[Any, int], str] = None) -> Any:
        return data[self.index(caption, data, label_function)]

    def tab_number(self, check: bool = True) -> str:
        tab_number: str = None
        while True:
            tab_number = self.input("Введите номер карты доступа")
            if check:
                if PIH.CHECK.MARK.tab_number(tab_number):
                    return tab_number
                else:
                    self.output.error(
                        "Неправильный формат номера карты доступа")
                    #return None
            else:
                return tab_number

    def password(self, secret: bool = True, check: bool = False, settings: PasswordSettings = None, is_new: bool = True) -> str:
        self.output.input(
            "Введите новый пароль" if is_new else "Введите пароль")
        while True:
            value = getpass("") if secret else self.input()
            if not check or PIH.CHECK.password(value, settings):
                return value
            else:
                self.output.error(
                    "Пароль не соответствует требованием безопасности")

    def same_if_empty(self, caption: str, src_value: str) -> str:
        value = self.input(caption)
        if value == "":
            value = src_value
        return value

    def name(self) -> str:
        return self.input("Введите часть имени")

    def full_name(self, one_line: bool = False) -> FullName:
        if one_line:
            while(True):
                value: str = self.input("Введите полное имя")
                if PIH.CHECK.full_name(value):
                    return FullNameTool.from_string(PIH.DATA.FORMAT.name(value))
                else:
                    pass
        else:
            def full_name_part(caption: str) -> str:
                while(True):
                    value: str = self.input(caption)
                    value = value.strip()
                    if PIH.CHECK.name(value):
                        return PIH.DATA.FORMAT.name(value)
                    else:
                        pass
            return FullName(full_name_part("Введите фамилию"), full_name_part("Введите имя"), full_name_part("Введите отчество"))

    def yes_no(self, text: str = " ", enter_for_yes: bool = False) -> bool:
        text = self.output.blue_str(self.output.text_color(Fore.WHITE, text))
        self.output.write_line(f"{text}? \n{self.output.green_str(self.output.text_black('Да (1 или Ввод)'))} / {self.output.red_str(self.output.text_black('Нет (Остальное)'), '')}" if enter_for_yes else
                               f"{text}? \n{self.output.red_str('Да (1)')} / {self.output.green_str(self.output.text_black('Нет (Остальное или Ввод)'), '')}")
        answer = self.input()
        answer = answer.lower()
        return answer == "y" or answer == "yes" or answer == "1" or (answer == "" and enter_for_yes)

    def message_for_user_by_login(self, login: str) -> str:
        user: User = PIH.RESULT.USER.by_login(login).data
        if user is not None:
            head_string = f"Здравствуйте, {FullNameTool.to_given_name(user.name)}, "
            self.output.green(head_string)
            message = self.input("Введите сообщениеt: ")
            return head_string + message
        else:
            pass

    def polibase_person_any(self) -> str:
        return self.input(
            "Введите персональный номер или часть имени пациента")


class MarkInput(MarkInputBase):

    def __init__(self, input: Input = None):
        self.parent = input

    def free(self, group: MarkGroup = None) -> Mark:
        result: Result[List[Mark]] = None
        while True:
            if group is None:
                if self.parent.yes_no("Выбрать группы доступа для карты доступа, введя имени пользователя из этой группы"):
                    result = PIH.RESULT.MARK.by_name(self.parent.name())
                    mark_list: List[Mark] = result.data
                    length = len(mark_list)
                    if length > 0:
                        if length > 1:
                            self.parent.output.table_with_caption_first_title_is_centered(
                                result, "Найденные пользователи:", True)
                        group = self.parent.item_by_index(
                            "Выберите группу доступа", mark_list)
                    else:
                        self.parent.output.error(
                            "Пользователь с введенным именем не найден")
                else:
                    result = PIH.RESULT.MARK.free_marks_group_statistics(False)
                    data = result.data
                    length = len(data)
                    if length > 0:
                        if length > 1:
                            self.parent.output.free_marks_group_statistics_for_result(
                                result, True)
                        group = self.parent.item_by_index(
                            "Выберите группу доступа введя индекс", data)
                    else:
                        self.parent.output.error("Свободный карт доступа нет!")
                        return None
            else:
                result = PIH.RESULT.MARK.free_marks_by_group_id(group.GroupID)
                data = result.data
                length = len(data)
                if length > 0:
                    if length > 1:
                        self.parent.output.free_marks_by_group_for_result(
                            group, result, True)
                    return self.parent.item_by_index(
                        "Выберите карту доступа введя индекс", data)
                else:
                    self.parent.output.error(
                        f"Нет свободных карт для группы доступа '{group.GroupName}'!")
                    return self.free()

    def person_division(self) -> MarkDivision:
        division_list: List[MarkDivision] = PIH.RESULT.MARK.person_divisions().data
        division_list.insert(0, MarkDivision(0, "Без подразделения"))
        return self.parent.item_by_index("Выберите подразделение для персоны, которой принадлежит карта доступа", division_list, lambda item, _: item.name )

    def by_name(self) -> Mark:
        self.parent.output.head2("Введите имя персоны")
        result: Result[List[Mark]] = None
        while result is None:
            try:
                result = PIH.RESULT.MARK.by_name(
                    self.parent.name())
            except NotFound as error:
                self.parent.output.error(error.get_details())
        self.parent.output.mark.result(result, "Карты доступа", True)
        return self.parent.item_by_index("Выберите карточку, введя индекс", result.data)

    def by_any(self, value: str = None) -> Mark:
        result: Result[List[Mark]] = None
        while result is None:
            try:
                result = PIH.RESULT.MARK.by_any(value or self.any())
            except NotFound as error:
                self.parent.output.error(error.get_details())
        self.parent.output.mark.result(result, "Карты доступа", True)
        return self.parent.item_by_index("Выберите карточку, введя индекс", result.data)

    def any(self) -> str:
        return self.parent.input(
            "Введите часть имени или табельный номер держателя карты")


class UserInput(UserInputBase):

    def __init__(self, input: Input = None):
        self.parent = input

    def container(self) -> UserContainer:
        result: Result[List[UserContainer]] = PIH.RESULT.USER.containers()
        self.parent.output.containers_for_result(result, True)
        return self.parent.item_by_index("Выберите контейнер пользователя, введя индекс", result.data)

    def by_name(self) -> User:
        result: Result[List[User]] = PIH.RESULT.USER.by_name(
            self.parent.name())
        result.fields = FIELD_COLLECTION.AD.USER_NAME
        self.parent.output.table_with_caption(
            result, "Список пользователей", True)
        return self.parent.item_by_index("Выберите пользователя, введя индекс", result.data)

    def title_any(self, title: str = None) -> str:
        return self.parent.input(title or "Введите логин, часть имени или другой поисковый запрос")

    def by_any(self, value: str = None, active: bool = None, title: str = None) -> User:
        result: Result[list[User]] = PIH.RESULT.USER.by_any(value or self.title_any(title), active)
        label_function: Callable[[Any, int], str] = (lambda item, _: item.name) if len(
            result.data) > 1 else None
        return self.parent.item_by_index("Выберите пользователя, введя индекс", result.data, label_function)

    def telephone_number(self, value: str = None, active: bool = None, title: str = None) -> str:
        user: User = None
        try:
            user = self.by_any(value, active, title)
            return user.telephoneNumber
        except NotFound as error:
            value: str = error.get_value()
            if A.C.telephone_number(value):
                return value
        return None

    def template(self) -> dict:
        result: Result[List[User]] = PIH.RESULT.USER.template_list()
        self.parent.output.template_users_for_result(result, True)
        return self.parent.item_by_index("Выберите шаблон пользователя, введя индекс", result.data)

    def search_attribute(self) -> str:
        return self.parent.indexed_field_list("Выберите по какому критерию искать, введя индекс",
                                             FIELD_COLLECTION.AD.SEARCH_ATTRIBUTE)

    def search_value(self, search_attribute: str) -> str:
        field_item = FIELD_COLLECTION.AD.SEARCH_ATTRIBUTE.get_item_by_name(
            search_attribute)
        return self.parent.input(f"Введите {field_item.caption.lower()}")

    def generate_password(self, once: bool = False, settings: PasswordSettings = PASSWORD.SETTINGS.DEFAULT) -> str:
        def generate_password_interanal(settings: PasswordSettings = None) -> str:
            return PasswordTools.generate_random_password(settings.length, settings.special_characters,
                                                          settings.order_list, settings.special_characters_count,
                                                          settings.alphabets_lowercase_count, settings.alphabets_uppercase_count,
                                                          settings.digits_count, settings.shuffled)
        while True:
            password = generate_password_interanal(settings)
            if once or self.parent.yes_no(f"Использовать пароль {password} ", True):
                return password
            else:
                pass

    def generate_login(self, full_name: FullName, ask_for_remove_inactive_user_if_login_is_exists: bool = True, ask_for_use: bool = True) -> str:
        login_list: List[str] = []
        inactive_user_list: List[User] = []
        login_is_exists: bool = False

        def show_user_which_login_is_exists_and_return_user_if_it_inactive(login_string: str) -> User:
            user: User = PIH.RESULT.USER.by_login(login_string).data
            is_active: bool = PIH.CHECK.USER.active(user)
            self.parent.output.error(
                f"Логин '{login_string}' занят {'активным' if is_active else 'неактивным'} пользователем: {user.name}")
            self.parent.output.new_line()
            return user if not is_active else None
        login: FullName = NamePolicy.convert_to_login(full_name)
        login_string: str = FullNameTool.to_string(login, "")
        login_list.append(login_string)
        need_enter_login: bool = False

        def remove_inactive_user_action():
            login_string: str = None
            need_enter_login: bool = False
            if self.parent.yes_no("Удалить неактивных пользователей, чтобы освободить логин", True):
                user_for_remove: User = self.parent.item_by_index(
                    "Выберите пользователя для удаления, выбрав индекс", inactive_user_list, lambda item, _: f"{item.name} ({item.samAccountName})")
                self.parent.output.new_line()
                self.parent.output.value(f"Пользователь для удаления",
                                        user_for_remove.name)
                if self.parent.yes_no("Удалить неактивного пользователя", True):
                    if PIH.ACTION.USER.remove(user_for_remove):
                        self.parent.output.good("Удален")
                        login_string = user_for_remove.samAccountName
                        inactive_user_list.remove(user_for_remove)
                    else:
                        self.parent.output.error("Ошибка")
                else:
                    need_enter_login = True
            else:
                need_enter_login = True
            return need_enter_login, login_string
        if PIH.CHECK.USER.exists_by_login(login_string):
            user: User = show_user_which_login_is_exists_and_return_user_if_it_inactive(
                login_string)
            if user is not None:
                inactive_user_list.append(user)
            login_alt: FullName = NamePolicy.convert_to_alternative_login(
                login)
            login_string = FullNameTool.to_string(login_alt, "")
            login_is_exists = login_string in login_list
            if not login_is_exists:
                login_list.append(login_string)
            if login_is_exists or PIH.CHECK.USER.exists_by_login(login_string):
                if not login_is_exists:
                    user = show_user_which_login_is_exists_and_return_user_if_it_inactive(
                        login_string)
                    if user is not None:
                        inactive_user_list.append(user)
                login_reversed: FullName = NamePolicy.convert_to_reverse_login(
                    login)
                login_is_exists = login_string in login_list
                login_string = FullNameTool.to_string(login_reversed, "")
                if not login_is_exists:
                    login_list.append(login_string)
                if login_is_exists or PIH.CHECK.USER.exists_by_login(login_string):
                    if not login_is_exists:
                        user = show_user_which_login_is_exists_and_return_user_if_it_inactive(
                            login_string)
                        if user is not None:
                            inactive_user_list.append(user)
                    if ask_for_remove_inactive_user_if_login_is_exists and len(inactive_user_list) > 0:
                        need_enter_login, login_string = remove_inactive_user_action()
                    if need_enter_login:
                        while True:
                            login_string = self.parent.login()
                            if PIH.CHECK.USER.exists_by_login(login_string):
                                show_user_which_login_is_exists_and_return_user_if_it_inactive(
                                    login_string)
                            else:
                                break
        if not need_enter_login and ask_for_remove_inactive_user_if_login_is_exists and len(inactive_user_list) > 0:
            need_enter_login, login_string = remove_inactive_user_action()
            if need_enter_login:
                return self.generate_login(full_name, False)
        else:
            if ask_for_use and not self.parent.yes_no(f"Использовать логин '{login_string}' для аккаунта пользователя", True):
                login_string = self.parent.login(True)

        return login_string


def while_not_do(action: Callable[[None], bool], attemp_count: int = None, success_handler: Callable = None) -> None:

    while not action():
        if attemp_count is not None:
            if attemp_count == 0:
                break
            attemp_count -= 1
    if success_handler is not None:
        success_handler()


class NotImplemented(BaseException):
    pass


class ZeroReached(BaseException):
    pass


class NotFound(BaseException):

    def get_details(self) -> str:
        return self.args[0]

    def get_value(self) -> str:
        return DataTool.by_index(self.args, 1)


class IncorrectInputFile(BaseException):
    pass


class NotAccesable(BaseException):
    pass


class NamePolicy:

    @staticmethod
    def get_first_letter(name: str) -> str:
        from transliterate import translit
        letter = name[0]
        if letter.lower() == "ю":
            return "yu"
        return translit(letter, "ru", reversed=True).lower()

    @staticmethod
    def convert_to_login(full_name: FullName) -> FullName:
        return FullName(
            NamePolicy.get_first_letter(
                full_name.last_name),
            NamePolicy.get_first_letter(
                full_name.first_name),
            NamePolicy.get_first_letter(full_name.middle_name))

    @staticmethod
    def convert_to_alternative_login(login_list: FullName) -> FullName:
        return FullName(login_list.first_name, login_list.middle_name, login_list.last_name)

    @staticmethod
    def convert_to_reverse_login(login_list: FullName) -> FullName:
        return FullName(login_list.middle_name, login_list.first_name, login_list.last_name)


class PIH:

    NAME: str = "pih"

    def __init__(self, input: InputBase = None, output: OutputBase = None, session: SessionBase = None): 
        if output is None:
            output = Output(UserOutput(), MarkOutput())
            PIH.output: Output = output
        else:
            self.output: Output = output
        if input is None:
            input = Input(
                UserInput(), MarkInput(), PIH.output)
            PIH.input: Input = input
        else:
            self.input: Input = input
        if session is None: 
            PIH.session: Session = Session(input, output)
        else:
            self.session: Session = session

    class VERSION:

        @staticmethod
        def local() -> str:
            return "1.40109"

        @staticmethod
        def need_update() -> bool:
            return importlib.util.find_spec(PIH.NAME) is not None and PIH.VERSION.local() < PIH.VERSION.remote()

        @staticmethod
        def remote() -> str:
            req = requests.get(CONST.PYPI_URL)
            version = parse("0")
            if req.status_code == requests.codes.ok:
                data = json.loads(req.text.encode(req.encoding))
                releases = data.get("releases", [])
                for release in releases:
                    ver = parse(release)
                    if not ver.is_prerelease:
                        version = max(version, ver)
            return str(version)

    class ERROR:

        @staticmethod
        def create_error_header(details: str) -> str:
            return f"\nВерсия: {PIH.VERSION.local()}/{PIH.VERSION.remote()}\nПользователь: {PIH.OS.get_login()}\nКомпьютер: {PIH.OS.get_host()}\n{details}"

        @staticmethod
        def rpc_error_handler(details: str, code: Tuple, role: ServiceRoles, command: ServiceCommands) -> None:
            #and (role != ServiceRoles.MESSAGE or code != StatusCode.UNAVAILABLE):
            if isinstance(command, ServiceCommands) and role != ServiceRoles.MESSAGE:
                if code == StatusCode.DEADLINE_EXCEEDED:
                    pass
                else:
                    PIH.MESSAGE.from_debug_bot(
                        PIH.ERROR.create_error_header(details), LogLevels.ERROR)
            raise Error(details, code) from None

        @staticmethod
        def global_except_hook(exctype, value, traceback):
            details_list: List[str] = []
            for item in value.args:
                if isinstance(item, str):
                    details_list.append(item)
            details = "\n".join(details_list)
            PIH.MESSAGE.from_debug_bot(
                PIH.ERROR.create_error_header(details), LogLevels.ERROR)
            sys.__excepthook__(exctype, value, traceback)

        sys.excepthook = global_except_hook

    class UPDATER:

        @staticmethod
        def update_for_service(service_role: ServiceRoles, pih_update: bool = True, modules_update: bool = True, show_output: bool = False) -> bool:
            service_role_value: ServiceRoleDescription = service_role.value
            returncode: int = 0
            if pih_update:
                remote_executor_command_list: List[str] = PIH.PSTOOLS.create_remote_process_executor_for_service_role(
                    service_role, True)
                command_list: List[str] = remote_executor_command_list + \
                    PIH.UPDATER.get_module_updater_command_list(PIH.NAME, None)
                process_result: CompletedProcess = PIH.PSTOOLS.run_command(
                    command_list, show_output)
                returncode = process_result.returncode
            result: bool = returncode == 0
            if modules_update and result:
                installed_module_list: List[str] = {
                    pkg.key.lower() for pkg in pkg_resources.working_set}
                for module_name in [item.lower() for item in service_role_value.modules]:
                    if module_name not in installed_module_list:
                        result = result and PIH.UPDATER.install_module(
                            module_name, show_output=show_output)
                        if result:
                            pkg_resources.working_set.add_entry(module_name)
                        else:
                            break
            return result

        @staticmethod
        def get_module_updater_command_list(module_name: str, version: str = None) -> List[str]:
            return ["-m", CONST.PYTHON.PYPI, "install"] + ([f"{module_name}=={version}"] if version is not None else [module_name, "-U"])

        @staticmethod
        def update_localy(version: str = None, show_output: bool = False) -> bool:
            return PIH.UPDATER.install_module(PIH.NAME, version, show_output)

        @staticmethod
        def install_module(module_name: str, version: str = None, show_output: bool = False) -> bool:
            command_list = PIH.UPDATER.get_module_updater_command_list(
                module_name, version)
            command_list.pop(0)
            process_result: CompletedProcess = PIH.PSTOOLS.run_command(
                command_list, show_output)
            returncode = process_result.returncode
            return returncode == 0

        @staticmethod
        def update_remote(host: str, show_output: bool = False) -> bool:
            remote_executor_command_list: List[str] = PIH.PSTOOLS.create_remote_process_executor(
                host, True)
            command_list: List[str] = remote_executor_command_list + \
                PIH.UPDATER.get_module_updater_command_list()
            process_result: CompletedProcess = PIH.PSTOOLS.run_command(
                command_list, show_output)
            returncode = process_result.returncode
            return returncode == 0

        @staticmethod
        def update_action(start_handler: Callable, update_start_handler: Callable, update_complete_handler: Callable) -> None:
            need_update: bool = PIH.VERSION.need_update()

            def internal_update_action(need_update: bool, start_handler: Callable, update_start_handler: Callable, update_complete_handler: Callable):
                if need_update:
                    update_start_handler()
                    if PIH.UPDATER.update_localy():
                        import importlib
                        importlib.reload(sys.modules[PIH.NAME])
                        importlib.reload(sys.modules[f"{PIH.NAME}.{PIH.NAME}"])
                        update_complete_handler()
                        start_handler()
                else:
                    start_handler()
            Thread(target=internal_update_action, args=(
                need_update, start_handler, update_start_handler, update_complete_handler,)).start()

    class SETTINGS:

        @staticmethod
        def set(settings_item: Settings, value: Any) -> bool:
            return PIH.ACTION.SETTINGS.set(settings_item, value)

        @staticmethod
        def set_default(settings_item: Settings) -> bool:
            return PIH.ACTION.SETTINGS.set_default(settings_item)

        @staticmethod
        def get(settings_item: Settings) -> Any:
            return PIH.RESULT.SETTINGS.get(settings_item).data

        @staticmethod
        def init() -> None:
            for setting_item in Settings:
                if setting_item.value.auto_init:
                    PIH.SETTINGS.set_default(setting_item)

        class POLIBASE:

            class REVIEW_QUEST:

                @staticmethod
                def start_time() -> datetime:
                    return DateTimeTool.from_string(PIH.SETTINGS.get(Settings.POLIBASE_PERSON_REVIEW_QUEST_START_TIME), CONST.TIME_FORMAT)

                @staticmethod
                def test() -> bool:
                    return PIH.SETTINGS.get(Settings.POLIBASE_PERSON_REVIEW_QUEST_TEST)

    class PSTOOLS:

        @staticmethod
        def create_remote_process_executor(command_list: List, host: str, login: str = None, password: str = None, interactive: bool = False) -> List[str]:
            host = "\\\\" + host
            user: str = login or (CONST.AD.DOMAIN_NAME +
                                  "\\" + CONST.AD.ADMINISTRATOR)
            password = password or CONST.AD.ADMINISTRATOR_PASSOWORD
            ps_executor_path: str = os.path.join(
                PATHS.WS.PATH, CONST.PSTOOLS.NAME, CONST.PSTOOLS.EXECUTOR)
            return [ps_executor_path, "/accepteula", host, "-i" if interactive else "-d", "-u", user, "-p", password] + command_list

        @staticmethod
        def create_remote_process_executor_for_service_role(value: ServiceRoles, interactive: bool = False) -> List[str]:
            service_role_value: ServiceRoleDescription = value.value
            return PIH.PSTOOLS.create_remote_process_executor([CONST.PYTHON.EXECUTOR], PIH.SERVICE.get_host(value), service_role_value.login, service_role_value.password, interactive)

        @staticmethod
        def run_command(command_list: List[str], show_output: bool, capture_output: bool = False) -> CompletedProcess:
            print(" ".join(command_list))
            if show_output:
                if capture_output:
                    process_result = subprocess.run(
                        command_list, stdout=subprocess.PIPE)
                else:
                    process_result = subprocess.run(
                        command_list, text=True)
            else:
                process_result = subprocess.run(
                    command_list, stdout=DEVNULL, stderr=STDOUT, text=True)
            return process_result

    class SERVICE:

        command_map: dict = None

        class ADMIN:

            @staticmethod
            def create_developer_service_role_description(port: int = None) -> ServiceRoleDescription:
                if port is None or port == ServiceRoles.DEVELOPER.value.port:
                    return ServiceRoles.DEVELOPER.value
                return ServiceRoleDescription(f"Developer{port}", host=CONST.HOST.DEVELOPER.NAME, port=CONST.RPC.PORT(port))

            @staticmethod
            def develope(service_role: ServiceRoles, port: int = None) -> None:
                developer_service_role_description: ServiceRoleDescription = PIH.SERVICE.ADMIN.create_developer_service_role_description(
                    port)
                service_role_value: ServiceRoleDescription = service_role.value
                service_role_value.keep_alive = False
                service_role_value.host = developer_service_role_description.host
                service_role_value.port = developer_service_role_description.port

            @staticmethod
            def isolate(service_role: ServiceRoles) -> None:
                service_role_value: ServiceRoleDescription = service_role.value
                service_role_value.isolate = True

            @staticmethod
            def start(service_role: ServiceRoles, check_if_started: bool = True, show_output: bool = False) -> bool:
                if check_if_started:
                    if PIH.SERVICE.check_accessibility(service_role):
                        return None
                service_role_value: ServiceRoleDescription = service_role.value
                remote_executor_command_list: List[str] = PIH.PSTOOLS.create_remote_process_executor_for_service_role(
                    service_role)
                service_file_path: str = None
                if service_role_value.service_path is None:
                    service_file_path = os.path.join(
                        CONST.FACADE.PATH, f"{service_role_value.name}{CONST.FACADE.SERVICE_FOLDER_SUFFIX}", f"{CONST.SERVICE.NAME}.{FILE.EXTENSION.PYTHON}")
                else:
                    service_file_path = os.path.join(
                        service_role_value.service_path, f"{CONST.SERVICE.NAME}.{FILE.EXTENSION.PYTHON}")
                remote_executor_command_list.append(service_file_path)
                #debug = False
                remote_executor_command_list.append("False")
                process_result = PIH.PSTOOLS.run_command(
                    remote_executor_command_list, show_output)
                returncode = process_result.returncode
                if returncode == 2:
                    return False
                service_role_value.pid = returncode
                return True

            @staticmethod
            def stop(role: ServiceRoles, check_if_started: bool = True, show_output: bool = False) -> bool:
                if check_if_started:
                    if not PIH.SERVICE.check_accessibility(role):
                        return None
                service_role_value: ServiceRoleDescription = role.value
                host: str = "\\\\" + PIH.SERVICE.get_host(role)
                ps_kill_executor_path: str = os.path.join(
                    PATHS.WS.PATH, CONST.PSTOOLS.NAME, CONST.PSTOOLS.PSKILL)
                process_result: CompletedProcess = PIH.PSTOOLS.run_command(
                    [ps_kill_executor_path, host, str(service_role_value.pid)], show_output)
                returncode = process_result.returncode
                result: bool = returncode == 0
                if result:
                    service_role_value.pid = -1
                return result

        @staticmethod
        def check_accessibility(role: ServiceRoles) -> bool:
            return PIH.SERVICE.ping(role) is not None

        @staticmethod
        def ping(role: ServiceRoles) -> ServiceRoleInformation:
            service_role_informaion: ServiceRoleInformation = RPC.ping(role)
            if service_role_informaion is not None:
                DataTool.fill_data_from_source(
                    role.value, DataTool.to_data(service_role_informaion))
                service_role_informaion.subscribers = list(map(lambda item: DataTool.fill_data_from_source(
                    Subscriber(), item), service_role_informaion.subscribers))
            return service_role_informaion

        @staticmethod
        def init() -> None:
            if PIH.SERVICE.command_map is None:
                PIH.SERVICE.command_map = {}
                for role in ServiceRoles:
                    for role_command in role.value.commands:
                        PIH.SERVICE.command_map[role_command.name] = role

        @staticmethod
        def get_role_by_command(value: ServiceCommands) -> ServiceRoles:
            return PIH.SERVICE.command_map[value.name] if value.name in PIH.SERVICE.command_map else None

        @staticmethod
        def get_host(service_role: ServiceRoles) -> str:
            role_value: ServiceRoleDescription = service_role.value
            if role_value.isolate:
                host = PIH.OS.get_host()
                role_value.host = host
            return role_value.host

        @staticmethod
        def get_port(service_role: ServiceRoles) -> str:
            role_value: ServiceRoleDescription = service_role.value
            return role_value.port

        @staticmethod
        def subscribe_on(service_command: ServiceCommands, type: int = SubscribtionType.AFTER, name: str = None) -> bool:
            return RPC.Service.subscribe_on(service_command, type, name)

        @staticmethod
        def unsubscribe(service_command: ServiceCommands, type: int) -> bool:
            return RPC.Service.unsubscribe(service_command, type,)

    class PATH(PATHS):

        @staticmethod
        def resolve(value: str) -> str:
            if value[0] == "{" and value[-1] == "}":
                value = value[1: -1]
            return PathTool.resolve(value, PIH.OS.get_host())

    class DATA:

        class USER:

            @staticmethod
            def by_login(value: str) -> User:
                return PIH.RESULT.USER.by_login(value).data

            @staticmethod
            def by_name(value: str) -> User:
                return PIH.RESULT.USER.by_name(value).data

        class MARK:

            @staticmethod
            def by_tab_number(value: str) -> User:
                return PIH.RESULT.MARK.by_tab_number(value).data

        class SETTINGS:

            @staticmethod
            def get(value: Settings) -> Any:
                return PIH.RESULT.SETTINGS.get(value).data

        class FILTER:

            @staticmethod
            def users_by_dn(data: List[User], dn: str) -> List:
                return list(filter(lambda x: x.distinguishedName.find(dn) != -1, data))

        class EXTRACT:

            @staticmethod
            def wappi_telephone_number(value: any) -> str:
                if isinstance(value, str):
                    return PIH.DATA.FORMAT.telephone_number(value.split(CONST.MESSAGE.WHATSAPP.WAPPI.CONTACT_SUFFIX)[0])
                if isinstance(value, dict):
                    return PIH.DATA.FORMAT.telephone_number(value["user"])

            @staticmethod
            def whatsapp_message_from_service_command_parameter_list(parameter_list: ParameterList) -> WhatsAppMessage:
                result: bool = parameter_list.next()
                message: WhatsAppMessage = None
                if result:
                    message_parameters: list = parameter_list.next()
                    message_command: MessageCommands = MessageCommands.WHATSAPP_MESSAGE_RECEIVED
                    if EnumTool.get(MessageCommands, message_parameters[0]) == message_command:
                        param_item: ParamItem = message_command.value.params[0]
                        message = DataTool.fill_data_from_source(
                            WhatsAppMessage(), message_parameters[1][param_item.name])
                return message

            @staticmethod
            def email(value: str) -> str:
                emails: List[str] = re.findall(
                    r"[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,5}", value)
                if len(emails) > 0:
                    return emails[0]
                return None

            @staticmethod
            def number(value: str, min: int = None, max: int = None) -> int:
                value = value.strip()
                result: int = None
                numbers: List[str] = re.findall(r"\d", value)
                if len(numbers) > 0:
                    result = int(numbers[0])
                    if result < min or result > max:
                        result = None
                return result

            @staticmethod
            def parameter(object: dict, name: str) -> str:
                return object[name] if name in object else ""

            @staticmethod
            def tab_number(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.TAB_NUMBER)

            @staticmethod
            def telephone(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.TELEPHONE_NUMBER)

            @staticmethod
            def login(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.LOGIN)

            @staticmethod
            def name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.NAME)

            @staticmethod
            def dn(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.DN)

            @staticmethod
            def group_name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.GROUP_NAME)

            @staticmethod
            def group_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.GROUP_ID)

            @staticmethod
            def as_full_name(mark_object: dict) -> FullName:
                return FullNameTool.from_string(PIH.DATA.EXTRACT.full_name(mark_object))

            @staticmethod
            def full_name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.FULL_NAME)

            @staticmethod
            def person_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.PERSON_ID)

            @staticmethod
            def mark_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.MARK_ID)

            @staticmethod
            def description(object: dict) -> str:
                result = PIH.DATA.EXTRACT.parameter(
                    object, FIELD_NAME_COLLECTION.DESCRIPTION)
                if isinstance(result, Tuple) or isinstance(result, List):
                    return result[0]

            @staticmethod
            def container_dn(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.container_dn_from_dn(PIH.DATA.EXTRACT.dn(user_object))

            @staticmethod
            def container_dn_from_dn(dn: str) -> str:
                return ",".join(dn.split(",")[1:])

        class FORMAT:

            @staticmethod
            def telephone_number(value: str, prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
                src_value: str = value
                if value is not None and len(value) > 0:
                    value = re.sub("[\-\(\) ]", "", value)
                    if value.startswith(prefix):
                        value = value[len(prefix):]
                    if len(value) == 0:
                        return src_value
                    value = prefix + \
                        (value[1:] if (value[0] ==
                         "8" or value[0] == "7") else value)
                    pattern: str = "^\\" + prefix + "[0-9]{10}"
                    matcher: re.Match = re.match(pattern, value)
                    if matcher is not None:
                        return matcher.group(0)
                    else:
                        return src_value
                else:
                    return src_value

            @staticmethod
            def email(value: str) -> str:
                return value.lower()

            @staticmethod
            def name(value: str, remove_non_alpha: bool = False) -> str:
                value_list: List[str] = list(
                    filter(lambda item: len(item) > 0, value.split(" ")))
                if len(value_list) == 1:
                    if len(value) > 2:
                        value = value[0].upper() + value[1:].lower()
                    value = re.sub("[^а-яА-Яa-zA-Z]+", "",
                                   value) if remove_non_alpha else value
                    return value
                return " ".join(list(map(lambda item: PIH.DATA.FORMAT.name(item, remove_non_alpha), value_list)))

            @staticmethod
            def location_list(value: str, remove_first: bool = True, reversed: bool = True) -> List[str]:
                location_list: List[str] = value.split(
                    ",")[1 if remove_first else 0:]
                if reversed:
                    location_list.reverse()
                return list(map(
                    lambda item: item.split("=")[-1], location_list))

            @staticmethod
            def get_user_account_control_values(uac: int) -> List[str]:
                result: List[str] = []
                for count, item in enumerate(CONST.AD.USER_ACCOUNT_CONTROL):
                    if (pow(2, count) & uac) != 0:
                        result.append(item)
                return result

        class TELEPHONE_NUMBER:

            @staticmethod
            def it_administrator() -> str:
                return PIH.DATA.TELEPHONE_NUMBER.by_login(CONST.AD.ADMINISTRATOR)

            @staticmethod
            def call_centre_administrator() -> str:
                return PIH.DATA.TELEPHONE_NUMBER.by_login(CONST.AD.CALL_CENTRE_ADMINISTRATOR)

            @staticmethod
            def by_login(value: str, format: bool = True) -> str:
                result: str = PIH.DATA.USER.by_login(value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_workstation_name(value: str) -> str:
                workstation: UserWorkstation = PIH.RESULT.WORKSTATION.by_name(value).data
                return PIH.DATA.TELEPHONE_NUMBER.by_login(workstation.samAccountName)

            @staticmethod
            def by_mark_tab_number(value: str, format: bool = True) -> str:
                result: str = PIH.DATA.MARK.by_tab_number(
                    value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_polibase_person_pin(value: int, format: bool = True) -> bool:
                result: str = PIH.DATA.POLIBASE.person_by_pin(
                    value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_full_name(value: Any, format: bool = True) -> str:
                value_string: str = None
                if isinstance(value, str):
                    value_string = value
                    value = FullNameTool.from_string(value)
                else:
                    value_string = FullNameTool.to_string(value)
                telephone_number: str = PIH.RESULT.MARK.by_full_name(
                    value_string, True).data.telephoneNumber
                if PIH.CHECK.telephone_number(telephone_number):
                    return PIH.DATA.FORMAT.telephone_number(telephone_number) if format else telephone_number
                telephone_number = PIH.RESULT.USER.by_full_name(
                    value_string, True).data.telephoneNumber
                if PIH.CHECK.telephone_number(telephone_number):
                    return PIH.DATA.FORMAT.telephone_number(telephone_number) if format else telephone_number
                details: str = f"Телефон для {value_string} не найден"
                raise NotFound(details)

        class POLIBASE:

            @staticmethod
            def person_by_pin(value: int, test: bool = None) -> PolibasePerson:
                return PIH.RESULT.POLIBASE.person_by_pin(value, test).data

            @staticmethod
            def duplicate_person_for(person: PolibasePerson, check_birth: bool = True) -> PolibasePerson:
                def check_function(check_person: PolibasePerson) -> bool:
                    return check_person.pin != person.pin and (not check_birth or check_person.Birth != person.Birth)
                return ResultTool.get_first_data_element(ResultTool.data_filter(PIH.RESULT.POLIBASE.persons_by_full_name(person.FullName), lambda item: check_function(item)))

    class OS:

        @staticmethod
        def get_login() -> str:
            return os.getlogin()

        @staticmethod
        def get_host() -> str:
            return platform.node()

        @staticmethod
        def get_pid() -> int:
            return os.getppid()

    class RESULT:

        class DATA_STORAGE:

            def value(name: str, class_type: T, section: str = None) -> Result[T]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_storage_value, (name, section)), class_type)

        class MESSAGE:

            class DELAYED:

                @staticmethod
                def get(search_condition: MessageSearchCritery = None, take_to_work: bool = False) -> Result[List[DelayedMessageVO]]:
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.search_buffered_messages, (search_condition, take_to_work)), DelayedMessageVO)

        class BACKUP:

            @staticmethod
            def status() -> Result[List[ReplicationStatus]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_replicate_status), ReplicationStatus)

        class SETTINGS:

            @staticmethod
            def key(key: str, default_value: Any = None) -> Result[Any]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_settings_value, (key, default_value)))

            @staticmethod
            def get(settings_item: Settings) -> Result[Any]:
                settings_value: SettingsValue = settings_item.value
                return PIH.RESULT.SETTINGS.key(settings_value.key_name or settings_item.name, settings_value.default_value)

        class WORKSTATION:

            @staticmethod
            def all() -> Result[List[Workstation]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_all_workstations), Workstation)

            @staticmethod
            def by_login(value: str) -> Result[List[UserWorkstation]]:
                if PIH.CHECK.USER.exists_by_login(value):
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.get_workstation_by_user, value), UserWorkstation)
                else:
                    details: str = f"Пользователь с логином {value} не найден"
                    raise NotFound(details)

            @staticmethod
            def by_any(value: str) -> Result[List[UserWorkstation]]:
                if PIH.CHECK.WORKSTATION.name(value):
                    return ResultTool.data_as_list(PIH.RESULT.WORKSTATION.by_name(value))
                try:
                    return PIH.RESULT.WORKSTATION.by_login(value)
                except NotFound:
                    detail: str = f"Компьютер с параметром поиска {value} не найден"
                    raise NotFound(detail)

            @staticmethod
            def by_name(value: str) -> Result[UserWorkstation]:
                result: Result[UserWorkstation] = ResultTool.with_first_data_element(ResultTool.data_filter(
                    PIH.RESULT.WORKSTATION.all_with_user(), lambda item: item.name.lower() == value.lower()))
                if ResultTool.data_is_empty(result):
                    details: str = f"Компьютер с именем {value} не найден"
                    raise NotFound(details)
                return result

            @staticmethod
            def all_with_user() -> Result[List[UserWorkstation]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_all_workstations_with_user), UserWorkstation)

        class INVENTORY:

            @staticmethod
            def report(report_file_path: str, open_for_edit: bool = False) -> Result[List[InventoryReportItem]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_inventory_report, (report_file_path, open_for_edit)), InventoryReportItem)

        class TIME_TRACKING:

            @staticmethod
            def today(tab_number: str = None) -> Result[List[TimeTrackingResultByPerson]]:
                return PIH.RESULT.TIME_TRACKING.create(tab_number=tab_number)

            @staticmethod
            def in_period(day_start: int = 1, day_end: int = None, month: int = None, tab_number: str = None) -> Result[List[TimeTrackingResultByPerson]]:
                now: datetime = datetime.now()
                if month is not None:
                    now = now.replace(month=month)
                start_date: datetime = now.replace(hour=0, minute=0, second=0)
                end_date: datetime = now.replace(hour=23, minute=59, second=59)
                if day_start < 0:
                    start_date -= timedelta(days=abs(day_start))
                else:
                    start_date = start_date.replace(day=day_start)
                if day_end is not None:
                    if day_end < 0:
                        day_end -= timedelta(days=abs(day_start))
                    else:
                        day_end = start_date.replace(day=day_start)
                return PIH.RESULT.TIME_TRACKING.create(start_date, end_date, tab_number)

            @staticmethod
            def create(start_date: datetime = None, end_date: datetime = None, tab_number: str = None) -> Result[List[TimeTrackingResultByPerson]]:
                now: datetime = datetime.now() if start_date is None or end_date is None else None
                start_date = start_date or now.replace(
                    hour=0, minute=0, second=0)
                end_date = end_date or now.replace(
                    hour=23, minute=59, second=59)

                def get_date_or_time(entity: TimeTrackingEntity, date: bool) -> str:
                    return DataTool.not_none_check(entity, lambda: entity.TimeVal.split("T")[not date])
                result_data: dict = {}
                full_name_by_tab_number_map: dict = {}
                result_data = defaultdict(
                    lambda: defaultdict(lambda: defaultdict(list)))
                data: List = DataTool.to_result(RPC.call(
                    ServiceCommands.get_time_tracking, (start_date, end_date, tab_number)), TimeTrackingEntity).data
                for time_tracking_entity in data:
                    tab_number: str = time_tracking_entity.TabNumber
                    full_name_by_tab_number_map[tab_number] = time_tracking_entity.FullName
                    result_data[time_tracking_entity.DivisionName][tab_number][get_date_or_time(time_tracking_entity, True)].append(
                        time_tracking_entity)
                result: List[TimeTrackingResultByDivision] = []
                for division_name in result_data:
                    if division_name is None:
                        continue
                    result_division_item: TimeTrackingResultByDivision = TimeTrackingResultByDivision(
                        division_name)
                    result.append(result_division_item)
                    for tab_number in result_data[division_name]:
                        result_person_item: TimeTrackingResultByPerson = TimeTrackingResultByPerson(
                            tab_number, full_name_by_tab_number_map[tab_number])
                        result_division_item.list.append(result_person_item)
                        for date in result_data[division_name][tab_number]:
                            time_tracking_entity_list: List[TimeTrackingEntity] = result_data[division_name][tab_number][date]
                            time_tracking_enter_entity: TimeTrackingEntity = None
                            time_tracking_exit_entity: TimeTrackingEntity = None
                            for time_tracking_entity_list_item in time_tracking_entity_list:
                                if time_tracking_entity_list_item.Mode == 1:
                                    time_tracking_enter_entity = time_tracking_entity_list_item
                                if time_tracking_entity_list_item.Mode == 2:
                                    time_tracking_exit_entity = time_tracking_entity_list_item
                            duration: int = 0
                            if time_tracking_enter_entity is not None:
                                if time_tracking_exit_entity is not None:
                                    enter_time: datetime = datetime.fromisoformat(
                                        time_tracking_enter_entity.TimeVal).timestamp()
                                    exit_time: datetime = datetime.fromisoformat(
                                        time_tracking_exit_entity.TimeVal).timestamp()
                                    if enter_time < exit_time:
                                        #    enter_time, exit_time = exit_time, enter_time
                                        #    time_tracking_enter_entity, time_tracking_exit_entity = time_tracking_exit_entity, time_tracking_enter_entity
                                        duration = int(exit_time - enter_time)
                                    result_person_item.duration += duration
                            result_person_item.list.append(
                                TimeTrackingResultByDate(date, get_date_or_time(time_tracking_enter_entity, False),
                                                         get_date_or_time(time_tracking_exit_entity, False), duration))
                for division in result:
                    for person in division.list:
                        index: int = 0
                        length = len(person.list)
                        for _ in range(length):
                            item: TimeTrackingResultByDate = person.list[index]
                            if item.duration == 0:
                                # if item.enter_time is None and item.exit_time is not None:
                                if index < length - 1:
                                    item_next: TimeTrackingResultByDate = person.list[index + 1]
                                    if item.exit_time is not None:
                                        if item_next.enter_time is not None:
                                            duration = int(datetime.fromisoformat(item.date + "T" + item.exit_time).timestamp(
                                            ) - datetime.fromisoformat(item_next.date + "T" + item_next.enter_time).timestamp())
                                            item.duration = duration
                                            person.duration += duration
                                            if item_next.exit_time is None:
                                                index += 1
                            index += 1
                            if index >= length - 1:
                                break

                return Result(FIELD_COLLECTION.ORION.TIME_TRACKING_RESULT, result)

        class PRINTER:

            @staticmethod
            def all() -> Result[List[PrinterADInformation]]:
                def filter_by_server_name(printer_list: List[PrinterADInformation]) -> List[PrinterADInformation]:
                    return list(filter(lambda item: item.serverName == CONST.HOST.PRINTER_SERVER.NAME, printer_list))
                result: Result[List[PrinterADInformation]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_printers), PrinterADInformation)
                return Result(result.fields, filter_by_server_name(result.data))

            @staticmethod
            def report(redirect_to_log: bool = True) -> Result[List[PrinterReport]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.printers_report, redirect_to_log), PrinterReport)

            @staticmethod
            def status(redirect_to_log: bool = True) -> Result[List[PrinterStatus]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.printers_status, redirect_to_log), PrinterStatus)

        class MARK:

            @staticmethod
            def by_tab_number(value: str) -> Result[Mark]:
                result: Result[Mark] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_mark_by_tab_number, value), Mark)
                if ResultTool.data_is_empty(result):
                    details: str = f"Карта доступа с номером '{value}' не найдена"
                    raise NotFound(details)
                return result

            @staticmethod
            def person_divisions() -> Result[List[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_person_divisions), MarkDivision)

            @staticmethod
            def by_name(value: str, first_item: bool = False) -> Result[List[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_mark_by_person_name, value), Mark, first_item)

            @staticmethod
            def by_full_name(value: FullName, first_item: bool = False) -> Result[List[Mark]]:
                return PIH.RESULT.MARK.by_name(FullNameTool.from_string(value), first_item)

            @staticmethod
            def temporary_list() -> Result[List[TemporaryMark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_temporary_marks), TemporaryMark)

            @staticmethod
            def by_any(value: str) -> Result[List[Mark]]:
                if PIH.CHECK.MARK.tab_number(value):
                    return ResultTool.data_as_list(PIH.RESULT.MARK.by_tab_number(value))
                elif PIH.CHECK.name(value, True):
                    return PIH.RESULT.MARK.by_name(value)
                return Result()

            @staticmethod
            def free_list(show_with_guest_marks: bool = False) -> Result[List[Mark]]:
                result: Result[List[Mark]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_free_marks), Mark)

                def filter_function(item: Mark) -> bool:
                    return EnumTool.get(MarkType, item.type) != MarkType.GUEST
                return result if show_with_guest_marks else ResultTool.data_filter(result, filter_function)

            @staticmethod
            def free_marks_by_group_id(value: int) -> Result[List[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_free_marks_by_group_id, value), Mark)

            @staticmethod
            def free_marks_group_statistics(show_guest_marks: bool = None) -> Result[List[MarkGroupStatistics]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_free_marks_group_statistics, show_guest_marks), MarkGroupStatistics)

            @staticmethod
            def all() -> Result[List[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_all_persons), Mark)

            @staticmethod
            def temporary_mark_owner(mark: Mark) -> Result[Mark]:
                return DataTool.check(mark is not None and EnumTool.get(MarkType, mark.type) == MarkType.TEMPORARY, lambda: DataTool.to_result(RPC.call(ServiceCommands.get_owner_mark_for_temporary_mark, mark.TabNumber), Mark), None)

            @staticmethod
            def temporary_mark_owner_by_tab_number(value: str) -> Result[Mark]:
                return PIH.RESULT.MARK.temporary_mark_owner(PIH.RESULT.MARK.by_tab_number(value).data)

        class POLIBASE:

            class NOTIFICATION:

                @staticmethod
                def by(value: PolibasePersonVisitNotification) -> Result[List[PolibasePersonVisitNotification]]:
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.search_polibase_person_visit_notifications, value), PolibasePersonVisitNotification)

                @staticmethod
                def by_message_id(value: int) -> Result[PolibasePersonVisitNotification]:
                    return ResultTool.with_first_data_element(PIH.RESULT.POLIBASE.NOTIFICATION.by(PolibasePersonVisitNotification(messageID=value)))

            class INFORMATION_QUEST:

                @staticmethod
                def get(search_critery: PolibasePersonInformationQuest) -> Result[List[PolibasePersonInformationQuest]]:
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.search_polibase_person_information_quests, search_critery), PolibasePersonInformationQuest)

            class VISIT:

                @staticmethod
                def after_id(value: int, test: bool = None) -> Result[List[PolibasePersonVisit]]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_no=f">{value}"), test)), PolibasePersonVisit)

                @staticmethod
                def by_id(value: int, test: bool = None) -> Result[PolibasePersonVisit]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_no=value), test)), PolibasePersonVisit, True)

                @staticmethod
                def last_id(test: bool = None) -> Result[int]:
                    return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_visits_last_id, test))

                @staticmethod
                def today(test: bool = None) -> Result[List[PolibasePersonVisit]]:
                    return PIH.RESULT.POLIBASE.VISIT.by_registration_date(DateTimeTool.today(), test)

                @staticmethod
                def prerecording_today(test: bool = None) -> Result[List[PolibasePersonVisit]]:
                    return PIH.RESULT.POLIBASE.VISIT.prerecording_by_registration_date(DateTimeTool.today(), test)

                @staticmethod
                def by_registration_date(value: datetime, test: bool = None) -> Result[List[PolibasePersonVisit]]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_reg_date=DateTimeTool.date_to_string(value, CONST.POLIBASE.DATE_FORMAT)), test)), PolibasePersonVisit)

                @staticmethod
                def prerecording_by_registration_date(value: datetime = None, test: bool = None) -> Result[List[PolibasePersonVisit]]:
                    def filter_function(value: PolibasePersonVisit) -> bool:
                        return value.pin == CONST.POLIBASE.PRERECORDING_PIN
                    return ResultTool.data_filter(PIH.RESULT.POLIBASE.VISIT.by_registration_date(value, test), filter_function)

            @staticmethod
            def person_by_pin(value: int, test: bool = None) -> Result[PolibasePerson]:
                result: Result[PolibasePerson] = DataTool.to_result(RPC.call(
                    ServiceCommands.get_polibase_person_by_pin, (value, test)), PolibasePerson)
                if ResultTool.data_is_empty(result):
                    details: str = f"Пациент с персональным идентификационным номером {value} не найден"
                    raise NotFound(details)
                return result

            @staticmethod
            def persons_pin_by_visit_date(date: datetime, test: bool = None) -> Result[List[int]]:
                if test:
                    return Result(None, [100310])
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_pin_by_visit_date, (date.strftime(CONST.DATE_FORMAT), test)))

            @staticmethod
            def person_creator_by_pin(value: int, test: bool = None) -> Result[PolibasePerson]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_registrator_by_pin, (value, test)), PolibasePerson)

            @staticmethod
            def persons_by_full_name(value: str, test: bool = None) -> Result[List[PolibasePerson]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_full_name, (value, test)), PolibasePerson)

            @staticmethod
            def persons_by_pin(value: List[int], test: bool = None) -> Result[List[PolibasePerson]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_pin, (value, test)), PolibasePerson)

            @staticmethod
            def persons_by_chart_folder_name(value: str, test: bool = None) -> Result[List[PolibasePerson]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_chart_folder_name, (value, test)), PolibasePerson)

            @staticmethod
            def person_pin_list_with_old_format_barcode(test: bool = None) -> Result[List[int]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_pin_list_with_old_format_barcode, test))

            @staticmethod
            def person_by_any(value: str, test: bool = None) -> Result[List[PolibasePerson]]:
                if PIH.CHECK.POLIBASE.person_pin(value):
                    return ResultTool.data_as_list(PIH.RESULT.POLIBASE.person_by_pin(int(value), test))
                if PIH.CHECK.POLIBASE.person_chart_folder_name(value):
                    return PIH.RESULT.POLIBASE.persons_by_chart_folder_name(value, test)
                return ResultTool.data_as_list(PIH.RESULT.POLIBASE.persons_by_full_name(value))

        class USER:

            @staticmethod
            def get_not_found_error(title: str, active: bool, value: str) -> str:
                start: str = None
                if active is None:
                    start = "Пользователь"
                elif active:
                    start = "Активный пользователь"
                else:
                    start = "Неактивный пользователь"
                return NotFound(f"{start} с {title} '{value}' не найден", value)

            @staticmethod
            def by_login(value: str, active: bool = None) -> Result[User]:
                result: Result[User] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_user_by_login, (value, active)), User, True)
                if ResultTool.data_is_empty(result):
                    raise PIH.RESULT.USER.get_not_found_error("логином", active, value)
                return result

            @staticmethod
            def by_telephone_number(value: str, active: bool = None) -> Result[User]:
                result: Result[User] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_user_by_telephone_number, (value, active)), User, True)
                if ResultTool.data_is_empty(result):
                    raise PIH.RESULT.USER.get_not_found_error("номером телефона", active, value)
                return result

            @staticmethod
            def by_polibase_pin(value: int) -> Result[User]:
                return PIH.RESULT.USER.by_name(PIH.RESULT.POLIBASE.person_by_pin(value).data.FullName)

            @staticmethod
            def by_workstation_name(name: str) -> Result[User]:
                name = name.lower()
                user_workstation: UserWorkstation = DataTool.to_result(RPC.call(
                    ServiceCommands.get_user_by_workstation, name), UserWorkstation, True).data
                if user_workstation is None:
                    details: str = f"Компьютер с именем '{name}' не найден!"
                    raise NotFound(details)
                if user_workstation.samAccountName is None:
                    raise NotFound(f"За компьютером {name} нет залогиненного пользователя", name)
                return PIH.RESULT.USER.by_login(user_workstation.samAccountName)

            @staticmethod
            def by_any(value: Any, active: bool = None) -> Result[List[User]]:
                if isinstance(value, Mark):
                    return PIH.RESULT.USER.by_name(value.FullName)
                elif isinstance(value, FullName):
                    return PIH.RESULT.USER.by_full_name(value, False, active)
                elif isinstance(value, (Workstation, UserWorkstation)):
                    return PIH.RESULT.USER.by_any(value.name, active)
                else:
                    try:
                        value_as_telephone_number: str = PIH.DATA.FORMAT.telephone_number(value)
                        if PIH.CHECK.telephone_number(value_as_telephone_number):
                            return ResultTool.data_as_list(PIH.RESULT.USER.by_telephone_number(value_as_telephone_number, active))
                    except Exception:
                        pass
                    if PIH.CHECK.number(value):
                        try:
                            return ResultTool.data_as_list(PIH.RESULT.USER.by_polibase_pin(value))
                        except NotFound:
                            return ResultTool.data_as_list(PIH.RESULT.USER.by_tab_number(value))
                    if PIH.CHECK.WORKSTATION.name(value):
                        return ResultTool.data_as_list(PIH.RESULT.USER.by_workstation_name(value))
                    if PIH.CHECK.login(value):
                        return ResultTool.data_as_list(PIH.RESULT.USER.by_login(value, active))
                    if value == "" or PIH.CHECK.name(value):
                        return PIH.RESULT.USER.by_name(value, active)
                raise PIH.RESULT.USER.get_not_found_error("поисковым значением", active, value)

            @staticmethod
            def by_job_position(job_position: CONST.AD.JobPositions) -> Result[List[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_users_by_job_position, job_position.name), User)

            @staticmethod
            def by_group(group: CONST.AD.Groups) -> Result[List[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_users_in_group, group.name), User)

            @staticmethod
            def template_list() -> Result[List[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_template_users), User)

            @staticmethod
            def containers() -> Result[List[UserContainer]]:
                return DataTool.to_result(RPC.call(
                    ServiceCommands.get_containers), UserContainer)

            @staticmethod
            def by_full_name(value: FullName, get_first: bool = False, active: bool = None) -> Result[List[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_user_by_full_name, (value, active)), User, get_first)

            @staticmethod
            def by_name(value: str, active: bool = None) -> Result[List[User]]:
                result: Result[List[User]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_users_by_name, (value, active)), User)
                if ResultTool.data_is_empty(result):
                    raise PIH.RESULT.USER.get_not_found_error("именем", active, value)
                return result

            @staticmethod
            def list(active: bool = None) -> Result[List[User]]:
                return PIH.RESULT.USER.by_name(CONST.AD.SEARCH_ALL_PATTERN, active)

            @staticmethod
            def list_with_telephone_number(active: bool = None) -> Result[List[User]]:
                def user_with_telephone_number(user: User) -> bool:
                    return PIH.CHECK.telephone_number(user.telephoneNumber)
                return ResultTool.data_filter(PIH.RESULT.USER.list(active), lambda user: user_with_telephone_number(user))

            @staticmethod
            def by_tab_number(value: str) -> Result[User]:
                result: Result[Mark] = PIH.RESULT.MARK.by_tab_number(value)
                if ResultTool.data_is_empty(result):
                    details: str = f"Карта доступа с номером {value} не найдена"
                    raise NotFound(details)
                return PIH.RESULT.USER.by_mark(result.data)

            @staticmethod
            def by_mark(value: Mark) -> Result[User]:
                return Result(FIELD_COLLECTION.AD.USER, DataTool.check(value, lambda: DataTool.get_first_item(PIH.RESULT.USER.by_full_name(FullNameTool.from_string(value.FullName)).data)))

    class CHECK:

        @staticmethod
        def email_accessability(value: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_email_accessibility, value))

        @staticmethod
        def number(value: str) -> bool:
            return value.isdecimal()

        class FILE:

            @staticmethod
            def excel_file(path: str) -> bool:
                return os.path.isfile(path) and PathTool.get_extension(path) in [FILE.EXTENSION.EXCEL_OLD, FILE.EXTENSION.EXCEL_NEW]

        class ACCESS:

            @staticmethod
            def by_group(group: CONST.AD.Groups, exit_on_access_denied: bool = False, session: SessionBase = None, notify_on_fail: bool = True) -> bool:
                session = session or PIH.session
                login: str = session.get_login()
                result: bool = False
                notify: bool = True
                if group in session.allowable_groups:
                    result = True
                    notify = False
                else:
                    user_list: List[User] = PIH.RESULT.USER.by_group(
                        group).data
                    if user_list is not None:
                        for user_item in user_list:
                            user: User = user_item
                            if user.samAccountName == login:
                                session.add_allowable_group(group)
                                result = True
                                break
                if notify:
                    if result or notify_on_fail:
                        PIH.MESSAGE.from_system_bot(
                            f"Запрос на доступа к группе: {group.name} от пользователя {session.get_user().name} ({login}). Доступ {'разрешен' if result else 'отклонен'}.", LogLevels.NORMAL if result else LogLevels.ERROR)
                if exit_on_access_denied:
                    if result:
                        return result
                    session.exit(5, "Функционал недоступен...")
                else:
                    return result

            @staticmethod
            def admin(exit_on_access_denied: bool = False, session: SessionBase = None, notify_on_fail: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(CONST.AD.Groups.Admin, exit_on_access_denied, session, notify_on_fail)

            @staticmethod
            def service_admin(session: SessionBase = None, notify_on_fail: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(CONST.AD.Groups.ServiceAdmin, False, session, notify_on_fail)

            @staticmethod
            def inventory(session: SessionBase = None, notify_on_fail: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(CONST.AD.Groups.Inventory, False, session, notify_on_fail)

            @staticmethod
            def polibase(session: SessionBase = None, notify_on_fail: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(CONST.AD.Groups.Polibase, False, session, notify_on_fail)

        class USER:

            @staticmethod
            def exists_by_login(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_user_exists_by_login, value))

            @staticmethod
            def user(user: User) -> bool:
                return PIH.CHECK.full_name(user.name)

            @staticmethod
            def active(user: User) -> bool:
                return user.distinguishedName.find(CONST.AD.ACTIVE_USERS_CONTAINER_DN) != -1

            @staticmethod
            def exists_by_full_name(full_name: FullName) -> bool:
                return not ResultTool.data_is_empty(PIH.RESULT.USER.by_full_name(full_name))

            @staticmethod
            def search_attribute(value: str) -> bool:
                return value in CONST.AD.SEARCH_ATTRIBUTES

            @staticmethod
            def property(value: str, default_value: str = USER_PROPERTY.USER_STATUS) -> str:
                return value or default_value

            @staticmethod
            def accessible() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.AD)

        class MESSAGE:

            class WHATSAPP:

                class WAPPI:

                    @staticmethod
                    def from_me(value: str) -> bool:
                        return value in [PIH.DATA.TELEPHONE_NUMBER.it_administrator(), PIH.DATA.TELEPHONE_NUMBER.call_centre_administrator()]

        class MARK:

            @staticmethod
            def free(tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_mark_free, tab_number))

            @staticmethod
            def exists_by_full_name(full_name: FullName) -> bool:
                result: Result[List[Mark]] = PIH.RESULT.MARK.by_name(
                    FullNameTool.to_string(full_name))
                return ResultTool.data_is_empty(result)

            @staticmethod
            def accessible() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.MARK)

            @staticmethod
            def tab_number(value: str) -> bool:
                return value.isdecimal()

        class TIME_TRACKING:

            @staticmethod
            def accessible() -> bool:
                return PIH.CHECK.ACCESS.by_group(CONST.AD.Groups.TimeTrackingReport)

        class INVENTORY:

            @staticmethod
            def is_report_file(file_path: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_inventory_report, file_path))

            @staticmethod
            def accessible() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.DOCS) and PIH.CHECK.ACCESS.inventory()

        class POLIBASE:

            @staticmethod
            def accessible() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.POLIBASE) and PIH.CHECK.ACCESS.polibase()

            @staticmethod
            def person_chart_folder_name(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_polibase_person_chart_folder, value))

            @staticmethod
            def person_exists_by_pin(pin: int) -> bool:
                return PIH.RESULT.POLIBASE.person_by_pin(pin).data is not None

            @staticmethod
            def person_pin(value: str) -> bool:
                return value.isnumeric()

            class NOTIFICATION:

                @staticmethod
                def exists(value: PolibasePersonVisitNotification) -> bool:
                    return not ResultTool.data_is_empty(PIH.RESULT.POLIBASE.NOTIFICATION.by(value))

        @staticmethod
        def login(value: str) -> bool:
            pattern: str = r"^[a-z]+[a-z_0-9]{"+str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH - 1) + ",}"
            return re.fullmatch(pattern, value, re.IGNORECASE) is not None

        class WORKSTATION:

            @staticmethod
            def name(value: str) -> bool:
                value = value.lower()
                for prefix in CONST.AD.WORKSTATION_PREFIX_LIST:
                    if value.startswith(prefix):
                        return True
                return False

            @staticmethod
            def exists(name: str) -> bool:
                return not ResultTool.data_is_empty(ResultTool.data_filter(PIH.RESULT.WORKSTATION.all(), lambda workstation: name.lower() == workstation.name.lower()))

            @staticmethod
            def has_property(workstation: Workstation, property: CONST.AD.WSProperies) -> bool:
                return BM.has(workstation.properties, property.value)

            @staticmethod
            def is_watchable(workstation: Workstation) -> bool:
                return PIH.CHECK.WORKSTATION.has_property(workstation, CONST.AD.WSProperies.Watchable)

            @staticmethod
            def is_poweroffable(workstation: Workstation) -> bool:
                return PIH.CHECK.WORKSTATION.has_property(workstation, CONST.AD.WSProperies.Poweroffable)

        @staticmethod
        def telephone_number(value: str) -> bool:
            return not DataTool.is_empty(value) and re.fullmatch(r"^\+[0-9]{11,13}$", value) is not None

        @staticmethod
        def email(value: str, check_accesability: bool = False) -> bool:
            return re.fullmatch(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value) is not None and (not check_accesability or PIH.CHECK.email_accessability(value))

        @staticmethod
        def name(value: str, use_space: bool = False) -> bool:
            pattern = r"[а-яА-ЯёЁ" + (" " if use_space else "") + \
                "]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",}$"
            return re.fullmatch(pattern, value) is not None

        @staticmethod
        def full_name(value: str) -> bool:
            pattern = r"[а-яА-ЯёЁ]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",} [а-яА-ЯёЁ]{" + str(
                CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",} [а-яА-ЯёЁ]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",}$"
            return re.fullmatch(pattern, value) is not None

        @staticmethod
        def password(value: str, settings: PasswordSettings = None) -> bool:
            settings = settings or PASSWORD.SETTINGS.DEFAULT
            return PasswordTools.check_password(value, settings.length, settings.special_characters)

        @staticmethod
        def ping(host: str) -> bool:
            command = ['ping', "-n", '1', host]
            response = subprocess.call(command)
            return response == 0

    message_executor = ThreadPoolExecutor(max_workers=10)

    @staticmethod
    def send_log_message(message: str, channel: MessageChannels = MessageChannels.DEFAULT, level: Any = LogLevels.DEFAULT) -> None:
        level_value: int = None
        level_list: List[LogLevels] = None
        if isinstance(level, LogLevels):
            level_list = [level]
        if isinstance(level, int):
            level_value = level
        if level_value is None:
            level_value = 0
            for level_item in level_list:
                level_value = level_value | level_item.value

        def internal_send_log_message(message: str, channel_name: str, level_value: int) -> None:
            try:
                RPC.call(ServiceCommands.send_log_message,
                         (message, channel_name, level_value))
            except Error as error:
                PIH.output.error("Log send error")
        PIH.message_executor.submit(internal_send_log_message, message,
                                    channel.name, level_value)

    @staticmethod
    def send_command_message(message_command: MessageCommands, parameters: Tuple = None) -> None:
        message_commnad_description: MessageCommandDescription = message_command.value
        parameter_pattern_list: List = DataTool.as_list(
            message_commnad_description.params)
        parameters = parameters or ()
        parameters_dict: dict = {}
        if len(parameter_pattern_list) > len(parameters):
            raise Exception(
                "Income parameter list length is less that parameter list length of command")
        for index, parameter_pattern_item in enumerate(parameter_pattern_list):
            parameter_pattern: ParamItem = parameter_pattern_item
            parameters_dict[parameter_pattern.name] = parameters[index]

        def internal_send_command_message(command_name: str, parameters: dict) -> None:
            try:
                RPC.call(ServiceCommands.send_command_message,
                         (command_name, parameters))
            except Error as error:
                PIH.output.error("Log send error")
        PIH.message_executor.submit(internal_send_command_message,
                                    message_command.name, parameters_dict)

    class MESSAGE:

        class WORKSTATION:

            @staticmethod
            def send_to_user(user: User, message: str, method_type: InternalMessageMethodTypes = InternalMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.send_by_login_or_workstation_name(user.samAccountName, None, message, method_type)

            @staticmethod
            def send_to_workstation(value: Workstation, message: str, method_type: InternalMessageMethodTypes = InternalMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.send_by_workstation_name(value.name, message, method_type)

            @staticmethod
            def send_by_workstation_name(value: str, message: str, method_type: InternalMessageMethodTypes = InternalMessageMethodTypes.REMOTE) -> bool:
                user: User = None
                try:
                    user = PIH.RESULT.USER.by_workstation_name(value).data
                except NotFound:
                    pass
                return PIH.MESSAGE.WORKSTATION.send_by_login_or_workstation_name(user.samAccountName if user is not None else None, value, message, method_type)

            @staticmethod
            def send_by_login_or_workstation_name(login: str, workstation_name: str, message: str, method_type: InternalMessageMethodTypes = InternalMessageMethodTypes.REMOTE) -> bool:
                if RPC.Service.role == ServiceRoles.MESSAGE:
                    method_type = InternalMessageMethodTypes.LOCAL_PSTOOL_MSG
                if method_type == InternalMessageMethodTypes.REMOTE:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.send_internal_message_to_user, (login, workstation_name, message)))
                def internal_send_by_login_and_workstation_name(login: str, workstation_name: str) -> None:
                    if method_type == InternalMessageMethodTypes.LOCAL_PSTOOL_MSG:
                        PIH.PSTOOLS.run_command(PIH.PSTOOLS.create_remote_process_executor(
                            [CONST.MSG.EXECUTOR, login, message],  workstation_name), False)
                    if method_type == InternalMessageMethodTypes.LOCAL_MSG:
                        PIH.PSTOOLS.run_command(
                            [CONST.MSG.EXECUTOR, login, f"/server:{workstation_name}", message], False)
                if workstation_name is None:
                    ResultTool.every(PIH.RESULT.WORKSTATION.by_login(
                        login), lambda workstation: internal_send_by_login_and_workstation_name(login, workstation.name))
                else:
                    if login is None:
                        internal_send_by_login_and_workstation_name(
                            "*", workstation_name)
                    else:
                        internal_send_by_login_and_workstation_name(
                            login, workstation_name)
                return True

            @staticmethod
            def by_login(login: str, message: str, method_type: InternalMessageMethodTypes = InternalMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.send_by_login_or_workstation_name(login, None, message, method_type)

        class WHATSAPP:

            class WAPPI:

                @staticmethod
                def message_list(telephone_number: str, profile_id: str = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT) -> List[WhatsAppMessage]:
                    url: str = f"{CONST.MESSAGE.WHATSAPP.WAPPI.URL_GET_MESSAGES}{profile_id}&chat_id={telephone_number}{CONST.MESSAGE.WHATSAPP.WAPPI.CONTACT_SUFFIX}"
                    headers: dict = {
                        "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORICATION,
                        "Content-Type": "application/json"
                    }
                    result: List[WhatsAppMessage] = []
                    try:
                        response: Response = requests.get(url, headers=headers)
                    except Exception:
                        return result
                    response_result: dict = json.loads(response.text)
                    for message_item in response_result["messages"]:
                        if message_item["type"] == "chat":
                            result.append(WhatsAppMessage(
                                message_item["body"], message_item["fromMe"], message_item["time"]))
                    return result

                @staticmethod
                def send(telephone_number: str, message: Any, profile_id: str = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value) -> bool:
                    url: str = None
                    payload: dict = {"recipient": telephone_number}
                    if isinstance(message, str):
                        payload["body"] = message
                        url: str = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_MESSAGE
                    elif isinstance(message, (WhatsAppMessageListPayload, WhatsAppMessageButtonsPayload)):
                        for item in message.__dataclass_fields__:
                            item_value: Any = message.__getattribute__(item)
                            if not DataTool.is_empty(item_value):
                                payload[item] = item_value
                        if isinstance(message, WhatsAppMessageListPayload):
                            url = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_LIST_MESSAGE
                        else:
                            url = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_BUTTONS_MESSAGE
                    url += profile_id
                    headers: dict = {"accept": "application/json",
                                     "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORICATION, "Content-Type": "application/json"}
                    try:
                        response: Response = requests.post(
                            url, data=json.dumps(payload), headers=headers)
                    except ConnectTimeout:
                        return False
                    if response.status_code == CONST.ERROR.WAPPI.PROFILE_NOT_PAID:
                        PIH.MESSAGE.from_it_bot(
                            "Аккаунт Wappi (сервис для отправики сообщений в WhatsApp) не оплачен", LogLevels.ERROR)
                    status_code: int = response.status_code
                    return status_code == 200

                @staticmethod
                def send_video(telephone_number: str, caption: str, base64_value: str, profile_id: str = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value) -> bool:
                    payload: dict = {"recipient": telephone_number,
                                     "caption": caption,
                                     "b64_file": base64_value}
                    headers: dict = {"accept": "application/json",
                                     "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORICATION, "Content-Type": "application/json"}
                    url: str = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_VIDEO + profile_id
                    try:
                        response: Response = requests.post(
                            url, data=json.dumps(payload), headers=headers)
                    except ConnectTimeout:
                        return False
                    if response.status_code == CONST.ERROR.WAPPI.PROFILE_NOT_PAID:
                        PIH.MESSAGE.from_it_bot(
                            "Аккаунт Wappi (сервис для отправики сообщений в WhatsApp) не оплачен", LogLevels.ERROR)
                    return response.status_code == 200

                @staticmethod
                def send_image(telephone_number: str, caption: str, base64_value: str, profile_id: str = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value) -> bool:
                    payload: dict = {"recipient": telephone_number,
                                     "caption": caption,
                                     "b64_file": base64_value}
                    headers: dict = {"accept": "application/json",
                                     "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORICATION, "Content-Type": "application/json"}
                    url: str = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_IMAGE + profile_id
                    try:
                        response: Response = requests.post(
                            url, data=json.dumps(payload), headers=headers)
                    except ConnectTimeout:
                        return False
                    if response.status_code == CONST.ERROR.WAPPI.PROFILE_NOT_PAID:
                        PIH.MESSAGE.from_it_bot(
                            "Аккаунт Wappi (сервис для отправики сообщений в WhatsApp) не оплачен", LogLevels.ERROR)
                    return response.status_code == 200

            @staticmethod
            def send_via_browser(telephone_number: str, message: str) -> bool:
                pywhatkit_is_exists: bool = importlib.util.find_spec(
                    "pywhatkit") is not None
                if not pywhatkit_is_exists:
                    PIH.output.green(
                        "Установка библиотеки для отправки сообщения. Ожидайте...")
                    if not PIH.UPDATER.install_module("pywhatkit"):
                        PIH.output.error(
                            "Ошибка при установке библиотеки для отправки сообщений!")
                try:
                    import pywhatkit as pwk
                    pwk.sendwhatmsg_instantly(telephone_number, message)
                except Exception as уrror:
                    PIH.output.error("Ошибка при отправке сообщения!")

            @staticmethod
            def send(telephone_number: str, message: Any, via_wappi: bool = True, use_alternative: bool = True, wappi_profile_id: str = None) -> bool:
                wappi_profile_id = wappi_profile_id or CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value
                result: bool = False
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                if via_wappi:
                    result = PIH.MESSAGE.WHATSAPP.WAPPI.send(
                        telephone_number, message, wappi_profile_id)
                if result:
                    return result
                if use_alternative or not via_wappi:
                    return PIH.MESSAGE.WHATSAPP.send_via_browser(telephone_number, message)
                return False

            @staticmethod
            def send_video(telephone_number: str, caption: str, base64_value: str, wappi_profile_id: str = None) -> bool:
                wappi_profile_id = wappi_profile_id or CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                return PIH.MESSAGE.WHATSAPP.WAPPI.send_video(telephone_number, caption, base64_value, wappi_profile_id)

            @staticmethod
            def send_image(telephone_number: str, caption: str, base64_value: str, wappi_profile_id: str = None) -> bool:
                wappi_profile_id = wappi_profile_id or CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE_ID.DEFAULT.value
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                return PIH.MESSAGE.WHATSAPP.WAPPI.send_image(telephone_number, caption, base64_value, wappi_profile_id)

            @staticmethod
            def send_to_user(user: User, message: Any, via_wappi: bool = True, use_alternative: bool = True, wappi_profile_id: str = None) -> bool:
                return PIH.MESSAGE.WHATSAPP.send(user.telephoneNumber, message, via_wappi, use_alternative, wappi_profile_id)

            """
            @staticmethod
            def send_to_login(login: str, message: Any, via_wappi: bool = True, use_alternative: bool = True, wappi_profile_id: str = None) -> bool:
                return PIH.MESSAGE.WHATSAPP.send(PIH.DATA.TELEPHONE_NUMBER.by_login(login), message, via_wappi, use_alternative, wappi_profile_id)
            """
            
        class COMMAND:

            @staticmethod
            def polibase_persons_with_old_format_barcode_was_detected(persons_pin: List[int]) -> None:
                PIH.send_command_message(
                    MessageCommands.POLIBASE_PERSONS_WITH_OLD_FORMAT_BARCODE_WAS_DETECTED, (len(persons_pin), persons_pin))

            @staticmethod
            def all_polibase_persons_barcode_with_old_format_was_created(persons_pin: List[int]) -> None:
                PIH.send_command_message(
                    MessageCommands.POLIBASE_ALL_PERSON_BARCODES_WITH_OLD_FORMAT_WAS_CREATED, (persons_pin,))

            @staticmethod
            def polibase_person_visit_was_registered(value: PolibasePersonVisit) -> None:
                PIH.send_command_message(MessageCommands.POLIBASE_PERSON_VISIT_WAS_REGISTERED, (
                    value.FullName, "Предзапись" if value.pin == CONST.POLIBASE.PRERECORDING_PIN else value.pin, value.pin, value))

            @staticmethod
            def polibase_person_visit_notification_was_registered(visit: PolibasePersonVisit, notification: PolibasePersonVisitNotificationVO) -> None:
                PIH.send_command_message(MessageCommands.POLIBASE_PERSON_VISIT_NOTIFICATION_WAS_REGISTERED, (
                    visit.FullName, "Предзапись" if visit.pin == CONST.POLIBASE.PRERECORDING_PIN else visit.pin, notification))

            @staticmethod
            def login() -> None:
                login: str = PIH.session.get_login()
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.send_command_message(
                    MessageCommands.LOG_IN, (user.name, login, PIH.OS.get_host()))

            def whatsapp_message_received(message: WhatsAppMessage) -> None:
                PIH.send_command_message(
                    MessageCommands.WHATSAPP_MESSAGE_RECEIVED, (message,))

            @staticmethod
            def start_session() -> None:
                argv = PIH.session.argv()
                argv_str: str = ""
                if argv is not None:
                    argv_str = " ".join(argv)
                    argv_str = f"({argv_str})"
                login: str = PIH.session.get_login()
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.send_command_message(MessageCommands.START_SESSION, (user.name, login,
                                         f"{PIH.session.get_file_name()} {argv_str}", f"{PIH.VERSION.local()}/{PIH.VERSION.remote()}", PIH.OS.get_host()))

            @staticmethod
            def backup_notify_about_replication_start(status: str) -> None:
                PIH.send_command_message(
                    MessageCommands.BACKUP_NOTIFY_ABOUT_REPLICATION_JOB_START, (status, ))

            @staticmethod
            def backup_notify_about_replication_completed(status: str) -> None:
                PIH.send_command_message(
                    MessageCommands.BACKUP_NOTIFY_ABOUT_REPLICATION_JOB_COMPLETE, (status, ))

            @staticmethod
            def service_started(role: ServiceRoles) -> None:
                service_role_value: ServiceRoleDescription = role.value
                PIH.send_command_message(MessageCommands.SERVICE_START, (role.name, service_role_value.description,
                                         service_role_value.host, service_role_value.port, service_role_value.pid))

            @staticmethod
            def service_not_started(role: ServiceRoles) -> None:
                service_role_value: ServiceRoleDescription = role.value
                PIH.send_command_message(MessageCommands.SERVICE_NOT_START, (role.name, service_role_value.description,
                                         service_role_value.host, service_role_value.port))

            @staticmethod
            def hr_notify_about_new_employee(login: User) -> None:
                user: User = PIH.RESULT.USER.by_login(login).data
                hr_user: User = ResultTool.get_first_data_element(
                    PIH.RESULT.USER.by_job_position(CONST.AD.JobPositions.HR))
                PIH.send_command_message(MessageCommands.HR_NOTIFY_ABOUT_NEW_EMPLOYEE, (FullNameTool.to_given_name(hr_user.name),
                                                                                        user.name, user.mail))

            @staticmethod
            def it_notify_about_user_creation(login: str, password: str) -> None:
                it_user_list: List[User] = PIH.RESULT.USER.by_job_position(
                    CONST.AD.JobPositions.IT).data
                me_user_login: str = PIH.session.get_login()
                it_user_list = list(
                    filter(lambda user: user.samAccountName != me_user_login, it_user_list))
                it_user: User = it_user_list[0]
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.send_command_message(MessageCommands.IT_NOTIFY_ABOUT_CREATE_USER, (
                    user.name, user.description, user.samAccountName, password, user.telephoneNumber, user.mail))
                PIH.send_command_message(MessageCommands.IT_TASK_AFTER_CREATE_NEW_USER, (FullNameTool.to_given_name(
                    it_user.name), user.name, user.mail, password))

            @staticmethod
            def it_notify_about_mark_creation(temporary: bool, full_name: Any, tab_number: str = None) -> None:
                name: str = FullNameTool.to_string(full_name) if isinstance(
                    full_name, FullName) else full_name
                mark: Mark = PIH.RESULT.MARK.by_name(name, True).data
                telephone_number: str = PIH.DATA.FORMAT.telephone_number(
                    mark.telephoneNumber)
                if temporary:
                    PIH.send_command_message(MessageCommands.IT_NOTIFY_ABOUT_CREATE_TEMPORARY_MARK,
                                             (name, tab_number, telephone_number))
                else:
                    PIH.send_command_message(MessageCommands.IT_NOTIFY_ABOUT_CREATE_NEW_MARK, (
                        name, telephone_number, mark.TabNumber, mark.GroupName))

            @staticmethod
            def it_notify_about_temporary_mark_return(mark: Mark, temporary_tab_number: int) -> None:
                PIH.send_command_message(
                    MessageCommands.IT_NOTIFY_ABOUT_TEMPORARY_MARK_RETURN, (mark.FullName, temporary_tab_number))

            @staticmethod
            def it_notify_about_mark_return(mark: Mark) -> None:
                PIH.send_command_message(
                    MessageCommands.IT_NOTIFY_ABOUT_MARK_RETURN, (mark.FullName, mark.TabNumber))

            @staticmethod
            def it_notify_about_create_new_mark(full_name: Any) -> None:
                PIH.MESSAGE.COMMAND.it_notify_about_mark_creation(
                    False, full_name)

            @staticmethod
            def it_notify_about_create_temporary_mark(full_name: Any, tab_number: str) -> None:
                PIH.MESSAGE.COMMAND.it_notify_about_mark_creation(
                    True, full_name, tab_number)

            @staticmethod
            def printer_report(name: str, location: str, report: str) -> bool:
                return PIH.send_command_message(MessageCommands.PRINTER_REPORT, (name, location, report))

        @staticmethod
        def to_debug_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.DEBUG_BOT, level)

        @staticmethod
        def from_debug_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.DEBUG, level)

        @staticmethod
        def from_system_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.SYSTEM, level)

        @staticmethod
        def to_system_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.SYSTEM_BOT, level)

        @staticmethod
        def backup(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.BACKUP, level)

        @staticmethod
        def notification(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.NOTIFICATION, level)

        @staticmethod
        def from_printer_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.PRINTER, level)

        @staticmethod
        def to_printer_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.PRINTER_BOT, level)

        @staticmethod
        def from_it_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.IT, level)

        @staticmethod
        def from_feedback_call_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.POLIBASE_PERSON_FEEDBACK_CALL, level)

        @staticmethod
        def from_review_request_result(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.POLIBASE_PERSON_REVIEW_QUEST_RESULT, level)

        @staticmethod
        def to_it_bot(message: str, level: Any = LogLevels.DEFAULT) -> Any:
            return PIH.send_log_message(message, MessageChannels.IT_BOT, level)

    class ACTION:

        class BACKUP:

            @staticmethod
            def replicate(source: str, destination: str = None, job_name: str = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.replicate, (source, destination, job_name)))

        class DATA_STORAGE:

            def value(value: object, name: str = None, section: str = None) -> bool:
                try:
                    name = name or value.__getattribute__("name")
                except AttributeError as error:
                    pass
                else:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_storage_value, (name, value, section)))

        class MESSAGE:

            class DELAYED:

                @staticmethod
                def update(value: DelayedMessageVO, search_critery: MessageSearchCritery) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_buffered_message, (value, search_critery)))

                @staticmethod
                def update_status(value: DelayedMessageVO, status: MessageStatus) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update(DelayedMessageVO(status=status.value), MessageSearchCritery(id=value.id))

                @staticmethod
                def complete(value: DelayedMessageVO) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update_status(value, MessageStatus.COMPLETE)

                @staticmethod
                def abort(value: DelayedMessageVO) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update_status(value, MessageStatus.ABORT)

                @staticmethod
                def register(message: DelayedMessage) -> int:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_buffered_message, PIH.ACTION.MESSAGE.DELAYED.prepeare_message(message)))

                @staticmethod
                def send(message: DelayedMessage) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.send_buffered_message, PIH.ACTION.MESSAGE.DELAYED.prepeare_message(message)))

                @staticmethod
                def prepeare_message(message: DelayedMessage) -> DelayedMessage:
                    if message.type is None:
                        message.type = MessageTypes.WHATSAPP.value
                    if message.date is not None:
                        if isinstance(message.date, datetime):
                            message.date = DateTimeTool.to_string(
                                message.date, CONST.DATA_STORAGE.DATE_TIME_FORMAT)
                    return message

        class SETTINGS:

            @staticmethod
            def key(key: str, value: Any) -> bool:
                return DataTool.rpc_unrepresent(
                    RPC.call(ServiceCommands.set_settings_value, (key, value)))

            @staticmethod
            def set(settings_item: Settings, value: Any) -> bool:
                return PIH.ACTION.SETTINGS.key(settings_item.value.key_name or settings_item.name, value)

            @staticmethod
            def set_default(settings_item: Settings) -> bool:
                return PIH.ACTION.SETTINGS.set(settings_item, settings_item.value.default_value)

        class USER:

            @staticmethod
            def create_from_template(container_dn: str,
                                     full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_by_template, (container_dn, full_name, login, password, description, telephone, email)))

            @staticmethod
            def create_in_container(container_dn: str,
                                    full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_in_container, (container_dn, full_name, login, password, description, telephone, email)))

            @staticmethod
            def set_telephone_number(user: User, telephone: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_telephone, (user.distinguishedName, telephone)))

            @staticmethod
            def set_password(user: User, password: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_password, (user.distinguishedName, password)))

            @staticmethod
            def set_status(user: User, status: str, container: UserContainer) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_status, (user.distinguishedName, status, DataTool.check(container, lambda: container.distinguishedName))))

            @staticmethod
            def remove(user: User) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.remove_user, user.distinguishedName))

        class TIME_TRACKING:

            @staticmethod
            def report(path: str, start_date: datetime, end_date: datetime, tab_number: str = None) -> bool:
                now: datetime = datetime.now()
                start_date = now.replace(
                    hour=0, minute=0, day=start_date.day, second=0, month=start_date.month, year=start_date.year)
                end_date = now.replace(hour=23, minute=59, second=0, day=end_date.day,
                                       month=end_date.month, year=end_date.year)
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_time_tracking_report, (path, start_date, end_date, tab_number)))

        class INVENTORY:

            @staticmethod
            def create_barcodes(report_file_path: str, result_directory: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_barcodes_for_inventory, (report_file_path, result_directory)))

            @staticmethod
            def save_report_item(report_file_path: str, item: InventoryReportItem) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.save_report_item, (report_file_path, item)))

            @staticmethod
            def close_report(report_file_path: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.close_inventory_report, report_file_path))

        class PRINTER:

            @staticmethod
            def report() -> bool:
                return not ResultTool.data_is_empty(PIH.RESULT.PRINTER.report())

            @staticmethod
            def status() -> bool:
                return not ResultTool.data_is_empty(PIH.RESULT.PRINTER.status())

        class POLIBASE:

            class SETTINGS:

                #work in process
                def set_for_workstation(name: str, test: bool = False, show_result: bool = False) -> None:
                    if PIH.CHECK.WORKSTATION.exists(name):
                        settings_name: str = PATHS.POLIBASE_APP_DATA.SETTINGS.TEST if test else PATHS.POLIBASE_APP_DATA.SETTINGS.MAIN
                        process_result: CompletedProcess = PIH.PSTOOLS.run_command(PIH.PSTOOLS.create_remote_process_executor(["powershell", PathTool.resolve(os.path.join(
                            PATHS.POLIBASE_APP_DATA.SERVICE_FOLDER_PATH, settings_name))], name), show_result)
                        returncode = process_result.returncode
                        return returncode != 0
                    return False

            class NOTIFICATION:

                @staticmethod
                def register(value: PolibasePersonVisitNotificationVO) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_polibase_person_visit_notification, value))

            class INFORMATION_QUEST:

                @staticmethod
                def register(person: PolibasePerson) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_polibase_person_information_quest, PolibasePersonInformationQuest(person.pin, person.FullName, person.telephoneNumber)))

                @staticmethod
                def update(value: PolibasePersonInformationQuest, search_critery: PolibasePersonInformationQuest) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_polibase_person_information_quest, (value, search_critery)))

            @staticmethod
            def create_barcode_for_person(pid: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_barcode_for_polibase_person, (pid, test)))

            @staticmethod
            def set_chart_folder_for_person(name: str, pid: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_chart_folder, (name, pid, test)))

            @staticmethod
            def create_barcode_for_person_chart_folder(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_barcode_for_polibase_person_chart_folder, (value, value)))

            @staticmethod
            def set_email(value: str, pin: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_email, (value, pin, test)))

            @staticmethod
            def set_person_barcode_by_pin(barcode_file_name: str, pin: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_barcode_by_pin, (barcode_file_name, pin, test)))

            class DB:

                @staticmethod
                def backup(file_name: str = None, debug: bool = None) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_polibase_database_backup, (file_name, debug)))

            class VISIT:

                @staticmethod
                def register(value: PolibasePersonVisit = None) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_polibase_person_visit, value))

            class REVIEW_QUEST:

                def clear() -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.clear_polibase_persons_review_quest))

                @staticmethod
                def begin(pin: int) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.begin_polibase_person_review_quest, pin))

                @staticmethod
                def complete(pin: int) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.complete_polibase_person_review_quest, pin))

                @staticmethod
                def set_step(pin: int, step: PolibasePersonReviewQuestStep) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_review_quest_step, (pin, step.value)))

                @staticmethod
                def confirm_step(pin: int) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.confirm_polibase_person_review_quest_step, pin))

                @staticmethod
                def set_grade(pin: int, value: int) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_review_quest_grade, (pin, value)))

                @staticmethod
                def set_information_way(pin: int, value: int):
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_review_quest_information_way, (pin, value)))

                @staticmethod
                def set_message(pin: int, value: str) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_review_quest_message, (pin, value)))

                @staticmethod
                def set_feedback_call_status(pin: int, value: int) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_review_quest_feedback_call_status, (pin, value == 1)))

        class MARK:

            @staticmethod
            def create(full_name: FullName, person_division_id: int,  tab_number: str, telephone: str = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_mark, (full_name, person_division_id, tab_number, telephone)))

            @staticmethod
            def set_full_name_by_tab_number(full_name: FullName, tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_full_name_by_tab_number, (full_name, tab_number)))

            @staticmethod
            def set_telephone_by_tab_number(telephone: str, tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_telephone_by_tab_number, (telephone, tab_number)))

            @staticmethod
            def make_as_free_by_tab_number(tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.make_mark_as_free_by_tab_number, tab_number))

            @staticmethod
            def make_as_temporary(temporary_mark: Mark, owner_mark: Mark) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.make_mark_as_temporary, (temporary_mark.TabNumber, owner_mark.TabNumber)))

            @staticmethod
            def remove(mark: Mark) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.remove_mark_by_tab_number, mark.TabNumber))

        class DOCUMENTS:

            @staticmethod
            def create_for_user(path: str, full_name: FullName, tab_number: str, pc: LoginPasswordPair, polibase: LoginPasswordPair, email: LoginPasswordPair) -> bool:
                locale.setlocale(locale.LC_ALL, 'ru_RU')
                date_now = datetime.now().date()
                date_now_string = f"{date_now.day} {calendar.month_name[date_now.month]} {date_now.year}"
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_document, (path, date_now_string, CONST.SITE_ADDRESS, CONST.SITE_PROTOCOL + CONST.SITE_ADDRESS, CONST.EMAIL_ADDRESS, full_name, tab_number, pc, polibase, email)))

        class WORKSTATION:
    
            @staticmethod
            def reboot(name: str, force: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.reboot, (name, force)))

            @staticmethod
            def shutdown(name: str, force: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.shutdown, (name, force)))

        @staticmethod
        def generate_email(login: str) -> str:
            return "@".join((login, CONST.SITE_ADDRESS))

        @staticmethod
        def generate_user_principal_name(login: str) -> str:
            return "@".join((login, CONST.AD.DOMAIN_MAIN))


class ActionStack(List):

    def __init__(self, caption: str = "", *argv, input: InputBase = None, output: OutputBase = None):
        self.input = input or PIH.input
        self.output = output or PIH.output
        self.acion_value_list: List[ActionValue] = []
        self.caption = caption
        for arg in argv:
            self.append(arg)
        self.start()

    def call_actions_by_index(self, index: int = 0, change: bool = False):
        previous_change: bool = False
        while True:
            try:
                action_value: ActionValue = self[index]()
                if action_value:
                    if change or previous_change:
                        previous_change = False
                        if index < len(self.acion_value_list):
                            self.acion_value_list[index] = action_value
                        else:
                            self.acion_value_list.append(action_value)
                    else:
                        self.acion_value_list.append(action_value)
                index = index + 1
                if index == len(self) or change:
                    break
            except KeyboardInterrupt:
                self.output.new_line()
                self.output.error("Повтор предыдущих действия")
                self.output.new_line()
                if index > 0:
                    previous_change = True
                    # self.show_action_values()
                    #index = index - 1
                else:
                    continue

    def show_action_values(self) -> None:
        def label(item: ActionValue, _):
            return item.caption
        self.call_actions_by_index(self.input.index(
            "Выберите свойство для изменения, введя индекс", self.acion_value_list, label), True)

    def start(self):
        self.call_actions_by_index()
        while True:
            self.output.new_line()
            self.output.head2(self.caption)
            for action_value in self.acion_value_list:
                self.output.value(action_value.caption, action_value.value)
            if self.input.yes_no("Данные верны", True):
                break
            else:
                self.show_action_values()


class A:

    root = PIH()

    R = root.RESULT
    D = root.DATA
    D_TN = D.TELEPHONE_NUMBER
    D_FL = D.FILTER
    D_E = D.EXTRACT
    D_M = D.MARK
    A = root.ACTION
    ME = root.MESSAGE
    A_WS = A.WORKSTATION
    R_ME = R.MESSAGE
    A_ME = A.MESSAGE
    R_ME_D = R_ME.DELAYED
    A_ME_D = A_ME.DELAYED
    ME_WS = ME.WORKSTATION
    ME_C = ME.COMMAND
    ME_WH = ME.WHATSAPP
    ME_WH_W = ME_WH.WAPPI
    S = root.SETTINGS
    C = root.CHECK
    C_M = C.MARK
    C_A = C.ACCESS
    C_WS = C.WORKSTATION
    C_ME = C.MESSAGE
    C_ME_WH = C_ME.WHATSAPP
    C_ME_WH_W = C_ME_WH.WAPPI
    A_M = A.MARK
    R_M = R.MARK
    R_U = R.USER
    A_U = A.USER
    C_U = C.USER
    D_F = D.FORMAT
    A_P = A.POLIBASE
    A_P_S = A_P.SETTINGS
    C_P = C.POLIBASE
    D_P = D.POLIBASE
    R_P = R.POLIBASE
    A_P_V = A_P.VISIT
    R_P_V = R_P.VISIT
    A_P_N = A_P.NOTIFICATION
    R_P_N = R_P.NOTIFICATION
    C_P_N = C_P.NOTIFICATION
    R_WS = R.WORKSTATION
    C_WS = C.WORKSTATION
    A_P_IQ = A_P.INFORMATION_QUEST
    R_P_IQ = R_P.INFORMATION_QUEST
    SRV = root.SERVICE
    SRV_A = SRV.ADMIN
    I = root.input
    I_U = I.user
    A_B = A.BACKUP
    R_B = R.BACKUP
    O = root.output
    SE = root.session
    A_DS = A.DATA_STORAGE
    R_DS = R.DATA_STORAGE
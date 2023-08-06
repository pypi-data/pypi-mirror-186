from dataclasses import dataclass
from datetime import datetime
from typing import List
from pih.collection import FullName, InventoryReportItem, LoginPasswordPair

from pih.const import CONST, MessageChannels, MessageCommands, ServiceCommands
from pih.rpc import RPC
from pih.tools import DataTool


@dataclass
class rpcCommand:
    host: str
    port: int
    name: str


class RPC_COMMANDS:

    @staticmethod
    def ping(host: str, port: int) -> rpcCommand:
        return RPC.call(rpcCommand(host, CONST.RPC.PORT(port), CONST.RPC.PING_COMMAND))

    @staticmethod
    def event(host: str, port: int, type: int) -> rpcCommand:
        return RPC.call(rpcCommand(host, port, CONST.RPC.EVENT_COMMAND), (type))

    class MARK:

        @staticmethod
        def create_rpc_command(command_name: str) -> rpcCommand:
            return rpcCommand(CONST.HOST.ORION.NAME(), CONST.RPC.PORT(), command_name)

        @staticmethod
        def ping() -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command(CONST.RPC.PING_COMMAND))

        @staticmethod
        def get_free_marks() -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_free_marks"))

        @staticmethod
        def get_person_divisions() -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_person_divisions"))

        @staticmethod
        def get_time_tracking(start_date: datetime, end_date: datetime, tab_number: str=None) -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_time_tracking"), (start_date, end_date, tab_number))

        @staticmethod
        def is_mark_free(tab_number: str) -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("is_mark_free"), tab_number)

        @staticmethod
        def get_by_tab_number(value: str) -> dict:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_mark_by_tab_number"), value)

        @staticmethod
        def get_by_person_name(value: str) -> dict:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_mark_by_person_name"), value)

        @staticmethod
        def get_free_marks_group_statistics() -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_free_marks_group_statistics"))

        @staticmethod
        def get_free_marks_by_group_id(value: int) -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_free_marks_by_group_id"), value)

        @staticmethod
        def set_full_name_by_tab_number(value: FullName, tab_number: str) -> bool:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("set_full_name_by_tab_number"), (value, tab_number))

        @staticmethod
        def create(full_name: FullName, person_division_id: int,  tab_number: str, telephone: str = None) -> bool:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("create"), (full_name, person_division_id, tab_number, telephone))

        @staticmethod
        def set_telephone_by_tab_number(value: str, tab_number: str) -> bool:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("set_telephone_by_tab_number"), (value, tab_number))

        @staticmethod
        def make_mark_as_free_by_tab_number(tab_number: str) -> bool:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("make_mark_as_free_by_tab_number"), tab_number)

        @staticmethod
        def remove_by_tab_number(tab_number: str) -> bool:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("remove_by_tab_number"), tab_number)

        @staticmethod
        def get_all() -> str:
            return RPC.call(RPC_COMMANDS.MARK.create_rpc_command("get_all_persons"))


    class AD:
    
        @staticmethod
        def create_rpc_command(command_name: str) -> rpcCommand:
            return rpcCommand(CONST.HOST.AD.NAME(), CONST.RPC.PORT(), command_name)

        @staticmethod
        def ping() -> str:
            return RPC.call(RPC_COMMANDS.AD.create_rpc_command(CONST.RPC.PING_COMMAND))

        @staticmethod
        def printer_list() -> List:
            return RPC.call(RPC_COMMANDS.AD.create_rpc_command("printer_list"))

    class SCHEDULE:
        
        @staticmethod
        def create_rpc_command(command_name: str) -> rpcCommand:
            return rpcCommand(CONST.HOST.SCHEDULER.NAME(), CONST.RPC.PORT(2), command_name)

        @staticmethod
        def subscribe(host: str, port: int, type: int) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.SCHEDULE.create_rpc_command(CONST.RPC.SUBSCRIBE_COMMAND), (host, port, type)))

    class USER(AD):

        @staticmethod
        def ping() -> str:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command(CONST.RPC.PING_COMMAND))

        @staticmethod
        def user_is_exists_by_login(value: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("user_is_exists_by_login"), value))

        @staticmethod
        def set_telephone(user_dn: str, telephone: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("user_set_telephone"), (user_dn, telephone)))

        @staticmethod
        def authenticate(login: str, password: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("authenticate"), (login, password)))
         
        @staticmethod
        def get_users_by_job_position(job_position: CONST.AD.JobPositions) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_users_by_job_position"), job_position.name)

        @staticmethod
        def get_users_in_group(group: CONST.AD.Groups) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_users_in_group"), group.name)

        @staticmethod
        def set_password(user_dn: str, password: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("user_set_password"), (user_dn, password)))

        @staticmethod
        def set_status(user_dn: str, status: str, container_dn: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("user_set_status"), (user_dn, status, container_dn)))

        @staticmethod
        def user_remove(user_dn: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("user_remove"), user_dn))

        @staticmethod
        def get_user_by_full_name(value: FullName) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_user_by_full_name"), value)

        @staticmethod
        def get_users_by_name(value: str) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_users_by_name"), value)

        @staticmethod
        def get_active_users_by_name(value: str) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_active_users_by_name"), value)

        @staticmethod
        def get_user_by_login(value: str) -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_user_by_login"), value)

        @staticmethod
        def get_template_list() -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_template_list"))

        def get_containers() -> dict:
            return RPC.call(RPC_COMMANDS.USER.create_rpc_command("get_containers"))

        @staticmethod
        def create_from_template(templated_user_dn: str, full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("create_user_from_template"), (templated_user_dn, full_name, login, password, description, telephone, email)))

        @staticmethod
        def create_in_container(container_dn: str, full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
            return DataTool.rpc_unrepresent(RPC.call(RPC_COMMANDS.USER.create_rpc_command("create_user_in_container"), (container_dn, full_name, login, password, description, telephone, email)))


    class BACKUP_WORKER:
        
        @staticmethod
        def create_rpc_command(command_name: str) -> rpcCommand:
            return rpcCommand(CONST.HOST.BACKUP_WORKER.NAME(), CONST.RPC.PORT(), command_name)
            
        @staticmethod
        def ping() -> str:
            return RPC.call(RPC_COMMANDS.BACKUP_WORKER.create_rpc_command(CONST.RPC.PING_COMMAND))

    class PRINTER:

        @staticmethod
        def create_rpc_command(command_name: str) -> rpcCommand:
            return rpcCommand(CONST.HOST.PRINTER.NAME(), CONST.RPC.PORT(2), command_name)

        @staticmethod
        def ping() -> str:
            return RPC.call(RPC_COMMANDS.PRINTER.create_rpc_command(CONST.RPC.PING_COMMAND))

        @staticmethod
        def status(redirect_to_log: bool = True) -> str:
            return RPC.call(RPC_COMMANDS.PRINTER.create_rpc_command("printers_status"), redirect_to_log)

        @staticmethod
        def report(redirect_to_log: bool = True) -> bool:
            return RPC.call(RPC_COMMANDS.PRINTER.create_rpc_command("printers_report"), redirect_to_log)
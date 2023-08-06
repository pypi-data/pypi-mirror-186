from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Generic, List, Tuple, TypeVar


@dataclass
class FieldItem:
    name: str
    caption: str
    visible: bool = True
    class_type: Any = None
    default_value: str = None


@dataclass
class FullName:
    last_name: str = ""
    first_name: str = ""
    middle_name: str = ""


@dataclass
class ReplicationStatus:

    name: str = None
    active: bool = False
    last_created: str = None
    last_status: int = None


@dataclass
class ActionValue:
    caption: str
    value: str


@dataclass
class LoginPasswordPair:
    login: str = None
    password: str = None


@dataclass
class ServiceRoleDescriptionBase:
    name: str = None
    description: str = None
    host: str = None
    login: str = None
    password: str = None
    port: str = None
    service_path: str = None
    pid: int = -1
    pih_version: str = None
    isolate: bool = False
    visible_for_admin: bool = True
    keep_alive: bool = True
    weak_subscribtion: bool = False


@dataclass
class ServiceRoleInformation(ServiceRoleDescriptionBase):
    subscribers: List = None


@dataclass
class ServiceRoleDescription(ServiceRoleDescriptionBase):
    commands: List = field(default_factory=list)
    modules: List[str] = field(default_factory=list)


class FieldItemList:

    list: List[FieldItem]

    def copy_field_item(self, value: FieldItem) -> FieldItem:
        return FieldItem(
            value.name, value.caption, value.visible, value.class_type, value.default_value)

    def __init__(self, *args):
        self.list = []
        arg_list = list(args)
        for arg_item in arg_list:
            if isinstance(arg_item, FieldItem):
                item: FieldItem = self.copy_field_item(arg_item)
                self.list.append(item)
            elif isinstance(arg_item, FieldItemList):
                for item in arg_item.list:
                    self.list.append(self.copy_field_item(item))
            elif isinstance(arg_item, list):
                self.list.extend(arg_item)

    def get_list(self) -> List[FieldItem]:
        return self.list

    def get_item_and_index_by_name(self, value: str) -> Tuple[FieldItem, int]:
        index: int = -1
        result: FieldItem = None
        for item in self.list:
            index += 1
            if item.name == value:
                result = item
                break
        return result, -1 if result is None else index

    def get_item_by_name(self, value: str) -> FieldItem:
        result, _ = self.get_item_and_index_by_name(value)
        return result

    def position(self, name: str, position: int):
        _, index = self.get_item_and_index_by_name(name)
        if index != -1:
            self.list.insert(position, self.list.pop(index))
        return self

    def get_name_list(self):
        return list(map(lambda x: str(x.name), self.list))

    def get_caption_list(self):
        return list(map(lambda x: str(x.caption), filter(lambda y: y.visible, self.list)))

    def visible(self, name: str, value: bool):
        item, _ = self.get_item_and_index_by_name(name)
        if item is not None:
            item.visible = value
        return self

    def caption(self, name: str, value: bool):
        item, _ = self.get_item_and_index_by_name(name)
        if item is not None:
            item.caption = value
        return self

    def length(self) -> int:
        return len(self.list)


T = TypeVar("T")
R = TypeVar("R")


@dataclass
class Result(Generic[T]):
    fields: FieldItemList = None
    data: T = None


@dataclass
class UserContainer:
    name: str = None
    description: str = None
    distinguishedName: str = None


@dataclass
class User(UserContainer):
    samAccountName: str = None
    mail: str = None
    telephoneNumber: str = None
    userAccountControl: int = None


@dataclass
class Workstation:
    name: str = None
    properties: int  = 0
    description: str = None


@dataclass
class UserWorkstation(Workstation):
    samAccountName: str = None
    accessable: bool = None


@dataclass
class MarkBase:
    FullName: str = None
    TabNumber: str = None


@dataclass
class MarkSimple(MarkBase):
    DivisionName: str = None


@dataclass
class TemporaryMark(MarkBase):
    OwnerTabNumber: str = None


@dataclass
class PolibasePersonBase:
    pin: int = None
    FullName: str = None
    telephoneNumber: str = None


@dataclass
class PolibasePerson(PolibasePersonBase):
    Birth: datetime = None
    Comment: str = None
    ChartFolder: str = None
    mail: str = None


@dataclass
class PolibasePersonVisit(PolibasePersonBase):
    id: int = None
    registrationDate: str = None
    beginDate: str = None
    completeDate: str = None
    status: int = None


@dataclass
class PolibasePersonVisitSearchCritery:
    vis_no: Any = None
    vis_pat_no: Any = None
    vis_pat_name: Any = None
    vis_place: Any = None
    vis_reg_date: Any = None
    vis_date_ps: Any = None
    vis_date_pf: Any = None
    vis_date_fs: Any = None
    vis_date_ff: Any = None


@dataclass
class PolibasePersonVisitNotificationVO:
    visitID: int = None
    messageID: int = None
    type: int = None


@dataclass
class DelayedMessage:
    message: str = None
    recipient: str = None
    date: Any = None
    type: int = None
    
@dataclass
class DelayedMessageVO(DelayedMessage):
    id: int = None
    status: int = None

@dataclass
class MessageSearchCritery:
    id: Any = None
    recipient: str = None
    date: str = None
    type: Any = None
    status: int = None

@dataclass
class PolibasePersonVisitNotification(PolibasePersonVisit, PolibasePersonVisitNotificationVO):
    pass

@dataclass
class PolibasePersonVisitVO(PolibasePersonVisit):
    registrationDate: datetime = None
    beginDate: datetime = None
    completeDate: datetime = None
    beginDate2: datetime = None
    completeDate2: datetime = None
    status: int = None

@dataclass
class PolibasePersonQuest:
    step: int = None
    stepConfirmed: bool = None
    timestamp: int = None


@dataclass
class PolibasePersonInformationQuest(PolibasePersonBase):
    confirmed: int = None
    errors: int = None


@dataclass
class PolibasePersonReviewQuest(PolibasePersonQuest):
    beginDate: str = None
    completeDate: str = None
    grade: int = None
    message: str = None
    informationWay: int = None
    feedbackCallStatus: int = None


@dataclass
class Mark(MarkSimple):
    pID: int = None
    mID: int = None
    GroupName: str = None
    GroupID: int = None
    Comment: str = None
    telephoneNumber: str = None
    type: int = None


@dataclass
class MarkDivision:
    id: int = None
    name: str = None


@dataclass
class TimeTrackingEntity(MarkSimple):
    TimeVal: str = None
    Mode: int = None


@dataclass
class TimeTrackingResultByDate:
    date: str = None
    enter_time: str = None
    exit_time: str = None
    duration: int = None


@dataclass
class TimeTrackingResultByPerson:
    tab_number: str = None
    full_name: str = None
    duration: int = 0
    list: List[TimeTrackingResultByDate] = field(
        default_factory=list)


@dataclass
class WhatsAppMessage:
    message: str = None
    from_me: bool = None
    sender: str = None
    recipient: str = None
    profile_id: str = None
    time: int = None


@dataclass
class WhatsAppMessagePayload:
    title: str
    body: str


@dataclass
class WhatsAppMessageListPayload(WhatsAppMessagePayload):
    btn_text: str
    list: dict


@dataclass
class WhatsAppMessageButtonsPayload(WhatsAppMessagePayload):
    buttons: List = None


@dataclass
class TimeTrackingResultByDivision():
    name: str
    list: List[TimeTrackingResultByPerson] = field(
        default_factory=list)


@dataclass
class PrinterADInformation:
    driverName: str = None
    adminDescription: str = None
    description: str = None
    portName: str = None
    serverName: str = None
    name: str = None


@dataclass
class InventoryReportItem:
    name: str = None
    inventory_number: str = None
    row: str = None
    quantity: int = None
    name_column: int = None
    inventory_number_column: int = None
    quantity_column: int = None


@dataclass
class PrinterStatus:
    ip: str = None
    desc: str = None
    variant: str = None
    port: int = None
    community: str = None 
    accessable: bool = None


@dataclass
class PrinterReport(PrinterStatus):
    name: str = None
    model: str = None
    serial: int = None
    meta: str = None
    printsOverall: int = None
    printsColor: int = None
    printsMonochrome: int = None
    fuserType: int = None
    fuserCapacity: int = None
    fuserRemaining: int = None
    wasteType: int = None
    wasteCapacity: int = None
    wasteRemaining: int = None
    cleanerType: int = None
    cleanerCapacity: int = None
    cleanerRemaining: int = None
    transferType: int = None
    transferCapacity: int = None
    transferRemaining: int = None
    blackTonerType: str = None
    blackTonerCapacity: int = None
    blackTonerRemaining: int = None
    cyanTonerType: int = None
    cyanTonerCapacity: int = None
    cyanTonerRemaining: int = None
    magentaTonerType: int = None
    magentaTonerCapacity: int = None
    magentaTonerRemaining: int = None
    yellowTonerType: int = None
    yellowTonerCapacity: int = None
    yellowTonerRemaining: int = None
    blackDrumType: str = None
    blackDrumCapacity: int = None
    blackDrumRemaining: int = None
    cyanDrumType: int = None
    cyanDrumCapacity: int = None
    cyanDrumRemaining: int = None
    magentaDrumType: int = None
    magentaDrumCapacity: int = None
    magentaDrumRemaining: int = None
    yellowDrumType: int = None
    yellowDrumCapacity: int = None
    yellowDrumRemaining: int = None


@dataclass
class MarkGroup:
    GroupName: str = None
    GroupID: int = None


@dataclass
class MarkGroupStatistics(MarkGroup):
    Comment: str = None 
    Count: int = None


@dataclass
class PasswordSettings:
    length: int
    special_characters: str
    order_list: List[str]
    special_characters_count: int
    alphabets_lowercase_count: int
    alphabets_uppercase_count: int
    digits_count: int = 1
    shuffled: bool = False


@dataclass
class MessageCommandDescription:
    message: str
    log_channel: Enum
    log_level: int
    params: Tuple = None


@dataclass
class ParamItem:
    name: str
    caption: str
    description: str = None


@dataclass
class SettingsValue:
    key_name: str
    default_value: Any
    description: str = None
    auto_init: bool = True

import re
from pathlib import Path
from typing import BinaryIO, Dict, Optional

from typing_extensions import Literal, TypedDict

event_type_list = Literal[
    "add_role_to_profile",
    "attach_gateway_to_router",
    "attach_subnet_to_router",
    "create_vm",
    "create_machine_image",
    "create_scheduler" "create_worker",
    "delete_machine_image",
    "create_fw_rule",
    "create_fw",
    "create_network_cidr",
    "create_subnet",
    "create_network",
    "create_log_sink",
    "create_router",
    "create_iam_role",
    "create_log_bucket",
    "create_storage_bucket",
    "create_instance_profile",
    "check_log_sink_exists",
    "check_or_attach_cloudwatch_policy",
    "delete_vm",
    "delete_route",
    "get_firewall",
    "get_network",
    "get_subnet",
    "get_policy_arn",
    "get_log_group",
    "gcp_instance_create",
    "net_gateways_get_or_create",
    "scale",
]


class CondaPlaceHolder(dict):
    pass


class PackageInfo(TypedDict):
    name: str
    path: Optional[Path]
    source: Literal["pip", "conda"]
    channel_url: Optional[str]
    channel: Optional[str]
    subdir: Optional[str]
    conda_name: Optional[str]
    version: str
    wheel_target: Optional[str]


class PackageSchema(TypedDict):
    name: str
    source: Literal["pip", "conda"]
    channel: Optional[str]
    conda_name: Optional[str]
    client_version: str
    specifier: str
    include: bool
    file: Optional[int]


class ResolvedPackageInfo(TypedDict):
    name: str
    source: Literal["pip", "conda"]
    channel: Optional[str]
    conda_name: Optional[str]
    client_version: str
    specifier: str
    include: bool
    note: Optional[str]
    error: Optional[str]
    sdist: Optional[BinaryIO]
    md5: Optional[str]


class ApproximatePackageRequest(TypedDict):
    name: str
    priority_override: Optional[int]
    python_major_version: str
    python_minor_version: str
    python_patch_version: str
    source: Literal["pip", "conda"]
    channel_url: Optional[str]
    channel: Optional[str]
    subdir: Optional[str]
    conda_name: Optional[str]
    version: str
    wheel_target: Optional[str]


class ApproximatePackageResult(TypedDict):
    name: str
    specifier: Optional[str]
    include: bool
    note: Optional[str]
    error: Optional[str]


class PackageLevel(TypedDict):
    name: str
    level: int


class CondaPackage:
    def __init__(self, meta_json: Dict, prefix: Path):
        self.prefix = prefix
        self.name: str = meta_json["name"]
        self.version: str = meta_json["version"]
        self.subdir: str = meta_json["subdir"]
        self.files: str = meta_json["files"]
        channel_regex = rf"(.*\.\w*)/?(.*)/{self.subdir}$"
        result = re.match(channel_regex, meta_json["channel"])
        if not result:
            self.channel_url = f"https://conda.anaconda.org/{meta_json['channel']}"
            self.channel: str = meta_json["channel"]
        else:
            self.channel_url = result.group(1) + "/" + result.group(2)
            self.channel: str = result.group(2)

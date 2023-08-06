import attr
from requests import Session
from requests.auth import HTTPBasicAuth
from typing import List

from . import Mac, Onu


@attr.dataclass(slots=True)
class Ha7304:
    url: str
    username: str
    password: str
    session: Session = attr.ib(factory=Session)

    def __attrs_post_init__(self) -> None:
        if self.url.endswith("/"):
            self.url = self.url.rstrip("/")
        self.session.auth = HTTPBasicAuth(self.username, self.password)

    def all_pon_onu(self, retry: int = 3):
        while retry > 0:
            try:
                datas = self._all_pon_onu()
                break
            except IndexError:
                pass
            retry -= 1
        results: List[Onu] = list()
        for data in datas.splitlines():
            results.append(Onu.from_all_onu_data(data))
        return results

    def mac_list(self, retry: int = 3):
        while retry > 0:
            try:
                datas = self._all_mac_list()
                break
            except IndexError:
                pass
            retry -= 1
        results: List[Mac] = list()
        for data in datas.splitlines():
            results.append(Mac.from_all_mac_data(data))
        return results

    def _all_pon_onu(self) -> str:
        res = self.session.get(self.url + "/onuAllPonOnuList.asp")
        data = res.text
        data = data.split("'\n);\nfunction Reload()")[0]
        data = data.split("Array(\n'")[1]
        return data

    def _all_mac_list(self) -> str:
        res = self.session.get(self.url + "/oltMacFdb.asp")
        data = res.text
        data = data.split("'\n);\nfunction Reload()")[0]
        data = data.split("Array(\n'")[1]
        return data

    def setOnu(self, onu: Onu, operation: str):
        data = {"onuId": onu.id, "onuName": onu.name, "onuOperation": operation}
        self.session.post(self.url + "/goform/setOnu", data, allow_redirects=False)

    def reboot(self, onu: Onu):
        return self.setOnu(onu, "rebootOp")

    def activate(self, onu: Onu):
        return self.setOnu(onu, "activeOp")

    def deactivate(self, onu: Onu):
        return self.setOnu(onu, "noactiveOp")

    def factory(self, onu: Onu):
        return self.setOnu(onu, "restoreOp")

    def clean_loop_flag(self, onu: Onu):
        return self.setOnu(onu, "cleanLoopOp")

    def set_onu_port_vlan(
        self,
        port_id: str,
        vlan_mode: str,
        vlan_id: str,
        port_name: str = None,
    ):
        data = {
            "onuPortName": port_id,
            "onuPortVlanMode": vlan_mode,
            "onuPortVlanPvid": vlan_id,
            "onuPortId": port_name if port_name else port_id,
        }
        self.session.post(
            self.url + "/goform/setOnuPortVlan",
            data,
            allow_redirects=False,
        )

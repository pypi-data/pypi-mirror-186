import attr
from typing import Optional


@attr.dataclass(slots=True)
class Onu:
    id: str
    name: str
    mac_address: str
    status: str
    fw_version: str
    chip_id: int
    ports: int
    rtt: int
    ctc_status: int
    ctc_ver: int
    activate: int
    temperature: Optional[float]
    tx_power: Optional[float]
    rx_power: Optional[float]
    online_time: str
    offline_time: str
    offline_reason: int
    online: int
    deregister_cnt: int
    distance: float = 0

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    def __attrs_post_init__(self) -> None:
        distance = self.rtt * 1.6393 - 157
        if distance > 157:
            self.distance = distance - 157.0
        else:
            self.distance = 0

    @classmethod
    def from_all_onu_data(cls, data: str) -> "Onu":
        d = data.split("','")
        return cls(
            id=d[0].lstrip("'"),
            name=d[1],
            mac_address=d[2],
            status=d[3],
            fw_version=d[4],
            chip_id=int(d[5]),
            ports=int(d[6]),
            rtt=int(d[10]),
            ctc_status=int(d[7]),
            ctc_ver=int(d[8]),
            activate=int(d[9]),
            temperature=None if d[11] == "--" else float(d[11]),
            tx_power=None if d[14] == "--" else float(d[14]),
            rx_power=None if d[15] == "--" else float(d[15]),
            online_time=d[16],
            offline_time=d[17],
            offline_reason=int(d[18]),
            online=int(d[19]),
            deregister_cnt=int(d[20]),
        )

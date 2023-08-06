import attr


@attr.dataclass(slots=True)
class Mac:
    id: str
    learn_type: int
    vid: int
    aging: int
    mac_address: str

    @classmethod
    def from_all_mac_data(cls, data: str) -> "Mac":
        d = data.split("','")
        return cls(d[0].lstrip("'"), int(d[1]), int(d[2]), int(d[3]), d[4])

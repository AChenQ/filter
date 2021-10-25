def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
    label = data.get("label", {}).get("BOX2D", [])
    if not label:
        return False

    for box in label:
        category = box.get("category", None)
        if category in ("traffic sign", "traffic light"):
            return False
    return True


def teardown():
    pass

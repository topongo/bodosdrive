config_types = {
    "version": float,
    "test": {
        "x": int,
        "y": int,
        "z": {
            0: str,
            2: str
        }
    }

}

config_defaults = {
    "version": 0.1,
    "test": {
        "x": 10,
        "y": 20,
        "z": {
            0: "zoz",
            2: "zez"
        }
    }
}

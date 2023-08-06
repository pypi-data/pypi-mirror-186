CLI_CONFIG = {
    "serial_plugin": {},
}
CONFIG = {
    "serial_plugin": {
        "help": "The plugin used to serialize data. Defaults to json",
        "default": "json",
    },
    "error_callback_ref": {
        "help": "A reference to a function on the hub that will handle messages that failed to publish",
        "default": None,
    },
}
DYNE = {
    "log": ["log"],
    "evbus": ["evbus"],
    "ingress": ["ingress"],
    "match": ["match"],
}

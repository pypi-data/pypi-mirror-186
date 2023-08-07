class ConfigError(Exception):
    pass


class ConfigFieldError(ConfigError):
    pass


class ConfigNotFoundError(ConfigError):
    pass

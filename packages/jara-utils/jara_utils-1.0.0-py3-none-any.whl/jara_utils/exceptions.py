class JaraError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

    def __unicode__(self):  # pragma: no cover
        return self.message


class EnvironmentVariableNotFound(JaraError):
    """Raise this exception when an environment variable is not defined, but should be."""
    def __init__(self, variable_name: str):
        super().__init__(f'Environment variable with name {variable_name} not found!')

import yaml

class Config():
    def __init__(self, h):
        for k, v in h.items():
            if (type(v) == dict):
                setattr(self, k, Config(v))
            else:
                setattr(self, k, v)

class Settings:
    config = None

    @staticmethod
    def load(path):
        if Settings.config:
            return False

        with open(path, 'r') as f:
            Settings.config = yaml.safe_load(f)
            for k, v in Settings.config.items():
                setattr(Settings, k, Config(v))

        return True

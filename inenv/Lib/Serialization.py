import yaml


class Serialization:

    @staticmethod
    def save(self, path):
        with open(path, "w", encoding="UTF-8") as f:
            yaml.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, "r", encoding="UTF-8") as f:
            return yaml.load(f, yaml.Loader)

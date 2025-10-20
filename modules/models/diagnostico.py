from config import LABELS

class Diagnostico:
    def __init__(self, raw_str):
        self.raw_str = raw_str
        self.labels = self._parse_labels()
        self.binary_dict = self._to_binary_dict()
        self.target_vector = [self.binary_dict[k] for k in LABELS]
        self.primer_label = self.labels[0] if self.labels else None

    def _parse_labels(self):
        return [d.strip().upper() for d in self.raw_str.split(",") if d.strip().upper() in LABELS]

    def _to_binary_dict(self):
        return {label: int(label in self.labels) for label in LABELS}
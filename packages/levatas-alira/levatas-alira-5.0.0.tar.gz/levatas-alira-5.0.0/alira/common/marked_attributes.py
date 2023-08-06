class MarkedAttributes:
    def __init__(self, instance, attributes: list):
        self.instance = instance

        attributes.extend([
            {
                "label": "Prediction",
                "value": "Anomaly" if instance.prediction == 1 else "Normal",
            },
            {
                "label": "Confidence",
                "value": f"{(instance.confidence * 100):.2f}%"
            },
        ])
        self.attributes = attributes

    def add(self, label: str, metadata_field: str, default_value: str = "N/A", units: str = None):
        if metadata_field in self.instance.instance_metadata:
            value = str(self.instance.instance_metadata[metadata_field])
            value += f" {units}" if units else ""
        else:
            value = default_value

        self.attributes.append({
            "label": label,
            "value": value
        })

    def remove(self, label: str):
        for attribute in self.attributes:
            if attribute["label"] == label:
                self.attributes.remove(attribute)
                break

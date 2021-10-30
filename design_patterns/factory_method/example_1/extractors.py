from abc import ABC, abstractmethod
import json
import xmltodict


class Extractor(ABC):
    """Abstract Base Extractor class"""

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def extract(self) -> dict:
        """factory method"""
        pass

    def parsed_data(self):
        data = self.extract()
        return "\n".join([
            f"{k}=>{v}" for k, v in data.items()
        ])


class JSONDataExtractor(Extractor):

    def extract(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                data = {"results": data}

        return data


class XMLDataExtractor(Extractor):

    def extract(self):
        with open(self.filepath, mode='r', encoding='utf-8') as f:
            data = dict(xmltodict.parse(f.read()))

        return data


def extract_from_filepath(filepath: str):
    file_extension = filepath.split(".")[-1]

    extractors = {
        "json": JSONDataExtractor,
        "xml": XMLDataExtractor,
    }

    try:
        extractor = extractors[file_extension]
    except KeyError:
        raise ValueError(f"Unsupported File type, can not extract from {filepath}")

    return extractor(filepath)

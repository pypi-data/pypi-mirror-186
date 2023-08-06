from pathlib import Path
from lxml import etree


class Schema:
    slots = ("_parts", "_xml_filename", "_xml")

    def __new__(cls, *args, **kwargs):
        cls._xml_filename = args[0]
        cls._xml = etree.fromstring(Path(cls._xml_filename).read_text(encoding='UTF-8'))
        return cls._from_parsed_parts([cls._xml.tag])

    def __truediv__(self, key):
        args = key.split('/')
        return self._from_parsed_parts([*self._parts, *args])

    def __str__(self):
        parts = list()
        xpath_list = list()
        for part in self._parts:
            parts.append(part)
            xpath_list.append(self._xml.xpath(f"/{'/'.join(parts)}")[0].text.strip())
        return '.'.join([xpath for xpath in xpath_list if xpath])

    def __repr__(self):
        return self.__str__()

    @property
    def parent(self):
        return Schema(self._xml_filename) / '/'.join(self._parts[1:-1])

    @classmethod
    def _from_parsed_parts(cls, args):
        self = object.__new__(cls)
        parts = []
        for a in args:
            if isinstance(a, str):
                parts.append(str(a))
            else:
                raise TypeError(f"argument should be a str object, not {type(a)}")
        self._parts = parts
        return self

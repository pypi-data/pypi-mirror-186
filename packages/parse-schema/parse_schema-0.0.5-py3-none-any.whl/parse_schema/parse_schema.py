from pathlib import Path
from lxml import etree


class Schema(str):
    slots = ("_parts", "_xml_filepath", "_xml")

    def __new__(cls, *args, **kwargs):
        cls._xml_filepath = Path(args[0]).resolve()
        cls._xml = etree.fromstring(cls._xml_filepath.read_text(encoding='UTF-8'))
        return cls._from_parsed_parts([cls._xml.tag])

    def __truediv__(self, key):
        args = key.split('/')
        return self._from_parsed_parts([*self._parts, *args])

    @classmethod
    def _to_str(cls, _parts):
        parts = list()
        xpath_list = list()
        for part in _parts:
            parts.append(part)
            xpath_list.append(cls._xml.xpath(f"/{'/'.join(parts)}")[0].text.strip())
        return ''.join([xpath for xpath in xpath_list if xpath])

    @property
    def parent(self):
        return Schema(self._xml_filepath) / '/'.join(self._parts[1:-1])

    @classmethod
    def _from_parsed_parts(cls, args):
        parts = []
        for a in args:
            if isinstance(a, str):
                parts.append(str(a))
            else:
                raise TypeError(f"argument should be a str object, not {type(a)}")
        self = str.__new__(cls, cls._to_str(parts))
        self._parts = parts
        return self

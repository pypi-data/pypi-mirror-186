import xml.etree.ElementTree as ET


class OutputFactory:
    def builder(element):
        if not isinstance(element, ET.Element):
            raise ValueError("must pass Element object")
        if 'id' in element.attrib and element.attrib["id"] != "":
            if element.tag == "curve":
                return Curve(value=element, id=element.attrib["id"], type=element.tag)
            elif element.tag == "number":
                return Number(value=element, id=element.attrib["id"], type=element.tag)
            elif element.tag == "integer":
                return Integer(value=element, id=element.attrib["id"], type=element.tag)
            elif element.tag == "string":
                return String(value=element, id=element.attrib["id"], type=element.tag)
            elif element.tag == "log":
                return String(value=element, id=element.attrib["id"], type=element.tag)
            elif element.tag == "sequence":
                return Sequence(value=element, id=element.attrib["id"], type=element.tag)
            else:
                return Output(value=element, id=element.attrib["id"], type=element.tag)
        return None


class Output:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
        self.label = kwargs.get('label', None)
        self.description = kwargs.get('description', None)
        self.value = kwargs.get('value', None)

    def xmltodict_handler(self, parent_element):
        result = dict()
        for element in parent_element:
            if len(element):
                obj = self.xmltodict_handler(element)
            else:
                obj = element.text

            if result.get(element.tag):
                if hasattr(result[element.tag], "append"):
                    result[element.tag].append(obj)
                else:
                    result[element.tag] = [result[element.tag], obj]
            else:
                result[element.tag] = obj
        return result

    def xmltodict(self, element):
        if not isinstance(element, ET.Element):
            raise ValueError("must pass Element object")
        return {element.tag: self.xmltodict_handler(element)}

    def validate_value(self, newval):
        if (newval != None):
            if isinstance(newval, ET.Element):
                newval = self.xmltodict(newval)
                if self.type in newval:
                    newval = newval[self.type]
        return newval

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newval):
        self._value = self.validate_value(newval)

    def to_dict(self):
        res = {'type': 'Output'}
        res['id'] = self.id
        if (self.description is not None):
            res['description'] = self.description
        if (self.label is not None):
            res['label'] = self.label
        if (self.value is not None):
            res['value'] = self.value
        return res

    def __repr__(self):
        res = "{"
        repr = self.to_dict()
        for k, v in repr.items():
            res += k.__repr__() + " : " + v.__repr__() + ", "
        res += "}"
        return res


class Curve(Output):
    def __init__(self, **kwargs):
        Output.__init__(self, **kwargs)

    def xmltodict_handler(self, parent_element):
        result = dict()
        for element in parent_element:
            if len(element):
                obj = self.xmltodict_handler(element)
            else:
                if element.tag == "xy":
                    obj = element.text
                    obj = obj.replace("--", " ")
                    obj = obj.replace("\n", " ")
                    obj = obj.strip()
                else:
                    obj = element.text

            if result.get(element.tag):
                if hasattr(result[element.tag], "append"):
                    result[element.tag].append(obj)
                else:
                    result[element.tag] = [result[element.tag], obj]
            else:
                result[element.tag] = obj
        return result

    def to_dict(self):
        res = Output.to_dict(self)
        res["type"] = "Curve"
        return res


class Number(Output):
    def __init__(self, **kwargs):
        Output.__init__(self, **kwargs)

    def to_dict(self):
        res = Output.to_dict(self)
        res["type"] = "Number"
        return res


class Integer(Output):
    def __init__(self, **kwargs):
        Output.__init__(self, **kwargs)

    def to_dict(self):
        res = Output.to_dict(self)
        res["type"] = "Integer"
        return res


class String(Output):
    def __init__(self, **kwargs):
        Output.__init__(self, **kwargs)

    def to_dict(self):
        res = Output.to_dict(self)
        res["type"] = "String"
        return res


class Sequence(Output):
    def __init__(self, **kwargs):
        Output.__init__(self, **kwargs)

    def validate_value(self, newval):
        if (newval != None):
            if isinstance(newval, ET.Element):
                elements = newval.findall('element')
                newval = {e.find("index").text.strip(): [OutputFactory.builder(
                    e[i]) for i in range(1, len(e))] for e in elements}
        return newval

    def to_dict(self):
        res = Output.to_dict(self)
        res["type"] = "Sequence"
        return res

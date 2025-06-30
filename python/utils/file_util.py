import os
import json
from dataclasses import fields
from typing import Type, TypeVar, List, Any

T = TypeVar('T')


def from_dict(cls: Type[T], data: dict) -> T:
    """将字典转换为指定类的对象，忽略未知属性"""
    field_names = {f.name for f in fields(cls)}
    filtered_data = {k: v for k, v in data.items() if k in field_names}

    field_types = {f.name: f.type for f in fields(cls)}
    processed_data = {}

    for field_name, value in filtered_data.items():
        field_type = field_types[field_name]

        if hasattr(field_type, '__dataclass_fields__'):
            # 嵌套dataclass
            if value is None:
                processed_data[field_name] = None
            else:
                processed_data[field_name] = from_dict(field_type, value)
        elif (
                hasattr(field_type, '__origin__') and
                field_type.__origin__ is list and
                len(field_type.__args__) > 0
        ):
            # 列表类型
            item_type = field_type.__args__[0]
            if hasattr(item_type, '__dataclass_fields__'):
                # 列表元素为dataclass
                processed_data[field_name] = [
                    from_dict(item_type, item) for item in value
                ] if value is not None else []
            else:
                # 基本类型列表
                processed_data[field_name] = value if value is not None else []
        else:
            # 基本类型
            processed_data[field_name] = value

    return cls(**processed_data)

def read_json_file(file_path: str, cls: Type[T]) -> List[T]:
    """读取JSON文件并将其转换为指定类的对象"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        return [from_dict(cls, item) for item in data_list]


def dataclass_to_json(obj: Any, indent: int = None) -> str:
    def _serialize(obj):
        if hasattr(obj, '__dataclass_fields__'):
            return {f.name: _serialize(getattr(obj, f.name)) for f in fields(obj)}
        elif isinstance(obj, list):
            return [_serialize(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: _serialize(v) for k, v in obj.items()}
        else:
            return obj
    return json.dumps(_serialize(obj), ensure_ascii=False, indent=indent)

def read_jsonl_file(file_path, cls: Type[T]) -> List[T]:
    jsons = []
    if not os.path.exists(file_path):
        return jsons
    with open(file_path, encoding='utf-8') as json_file:
        json_list = json_file.readlines()
        for line in json_list:
            if not line:
                continue
            data = json.loads(line)
            jsons.append(from_dict(cls, data))
    return jsons

def append_jsonl_file(file_path, json_obj):
    with open(file_path, 'a', encoding='utf-8') as f:
        json_line = dataclass_to_json(json_obj)
        f.write(json_line + '\n')

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
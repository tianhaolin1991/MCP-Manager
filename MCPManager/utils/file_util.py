import os
import json
from dataclasses import fields
from typing import Type, List, get_origin, get_args, TypeVar, Union, Any

T = TypeVar('T')

from dataclasses import fields
from typing import Type, Dict, List, get_type_hints, get_origin, get_args
import inspect


def from_dict(cls: Type[T], data: dict) -> T:
    """将字典递归转换为数据类对象，处理所有嵌套层级和前向引用"""
    # 获取类的类型提示（包括前向引用）
    type_hints = get_type_hints(cls)

    # 过滤掉不在类字段中的键
    field_names = {f.name for f in fields(cls)}
    filtered_data = {k: v for k, v in data.items() if k in field_names}

    processed_data = {}
    for field_name, value in filtered_data.items():
        if value is None:
            processed_data[field_name] = None
            continue

        # 获取字段的实际类型（处理前向引用）
        field_type = type_hints.get(field_name)
        if field_type is None:
            processed_data[field_name] = value
            continue

        # 解析泛型类型
        origin = get_origin(field_type)

        if origin is list:
            # 处理列表类型
            item_type = get_args(field_type)[0] if get_args(field_type) else None
            if item_type:
                # 解析列表元素类型（处理前向引用）
                resolved_item_type = _resolve_type(item_type, cls)
                if _is_dataclass(resolved_item_type):
                    # 列表元素为数据类
                    processed_data[field_name] = [
                        from_dict(resolved_item_type, item) if isinstance(item, dict) else item
                        for item in value
                    ]
                else:
                    # 基本类型列表
                    processed_data[field_name] = value
            else:
                # 无泛型参数的列表
                processed_data[field_name] = value

        elif origin is dict:
            # 处理字典类型
            _, value_type = get_args(field_type) if get_args(field_type) else (None, None)
            if value_type:
                # 解析字典值类型（处理前向引用）
                resolved_value_type = _resolve_type(value_type, cls)
                if _is_dataclass(resolved_value_type):
                    # 字典值为数据类
                    processed_data[field_name] = {
                        k: from_dict(resolved_value_type, v) if isinstance(v, dict) else v
                        for k, v in value.items()
                    }
                else:
                    # 普通字典
                    processed_data[field_name] = value
            else:
                # 无泛型参数的字典
                processed_data[field_name] = value

        else:
            # 处理非容器类型
            resolved_type = _resolve_type(field_type, cls)
            if _is_dataclass(resolved_type):
                # 嵌套数据类
                processed_data[field_name] = from_dict(resolved_type, value)
            else:
                # 基本类型
                processed_data[field_name] = value

    return cls(**processed_data)


def _resolve_type(type_obj, parent_cls):
    """解析类型（处理前向引用和字符串类型注解）"""
    if isinstance(type_obj, str):
        # 处理字符串形式的前向引用
        globalns = inspect.getmodule(parent_cls).__dict__
        return eval(type_obj, globalns)
    return type_obj


def _is_dataclass(obj):
    """检查对象是否为数据类或数据类的实例"""
    if not obj:
        return False
    return hasattr(obj, '__dataclass_fields__')

def read_json_file(file_path: str, cls: Type[T]) -> T:
    """读取JSON文件并将其转换为指定类的对象"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return from_dict(cls, data)

def read_json(file_path:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def dataclass_to_json(obj: Any, indent: int = None) -> str:
    def _serialize(obj):
        if hasattr(obj, '__dataclass_fields__'):
            return {
                f.name: _serialize(getattr(obj, f.name))
                for f in fields(obj)
                if not f.metadata.get('exclude', False)
            }
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

def read_jsonl(file_path:str):
    jsons = []
    if not os.path.exists(file_path):
        return jsons
    with open(file_path, encoding='utf-8') as json_file:
        json_list = json_file.readlines()
        for line in json_list:
            if not line:
                continue
            data = json.loads(line)
            jsons.append(data)
    return jsons

def append_jsonl_file(file_path, json_obj):
    with open(file_path, 'a', encoding='utf-8') as f:
        json_line = dataclass_to_json(json_obj)
        f.write(json_line + '\n')


def append(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

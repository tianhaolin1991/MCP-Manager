import random
from typing import List, Dict, Any, Tuple
import copy
import sys

from bean.bean import ManagerServer, ManagerTool
from utils.file_util import read_jsonl_file

class ToolSampler:
    """
    Sample a specified number of tools from the dataset, and select the target tool
    """
    
    def __init__(self, data_path: str, seed:int = 42):
        self.data_path = data_path
        self.servers_data = None
        self.all_tools = []  # each item is: (server_index, tool_index, tool_data)
        self.load_data()
        random.seed(seed)
        
    def load_data(self) -> None:
        try:
            self.servers_data = read_jsonl_file(self.data_path, ManagerServer)
            for server_idx, server in enumerate(self.servers_data):
                for tool_idx, tool in enumerate(server.tools):
                    self.all_tools.append((server_idx, tool_idx, tool))
            
            print(f"Count: {len(self.servers_data)} servers, {len(self.all_tools)} tools.")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def sample_tools(self, n: int) -> List[ManagerServer]:
        if n <= 0:
            raise ValueError
        
        if n >= len(self.all_tools):
            return copy.deepcopy(self.servers_data)
        
        sampled_tool_indices = random.sample(range(len(self.all_tools)), n)
        sampled_tools = [self.all_tools[i] for i in sampled_tool_indices]
        
        server_tool_map = {}  # Tool to record which samples are included for each server
        
        for server_idx, tool_idx, _ in sampled_tools:
            if server_idx not in server_tool_map:
                server_tool_map[server_idx] = []
            server_tool_map[server_idx].append(tool_idx)
        
        result = []
        for server_idx, tool_indices in server_tool_map.items():
            server_copy = copy.deepcopy(self.servers_data[server_idx])
            result.append(server_copy)
        
        return result
    
    def select_target_tool(self, sampled_data: List[ManagerServer], position_index: int = 0) -> Tuple[ManagerServer, ManagerTool]:
        """
        Select a target tool by proportional location from sampled data.
        Used for the needle test.
        For example: position_index=0.5 means selecting tool in the middle of the dataset.
        
        Args:
            sampled_data
            position_index: range at [0, len(all_sampled_tools)-1]
        
        Returns:
            (target_server, target_tool, tool_fullname)
        """
        if not sampled_data:
            raise ValueError
        
        all_sampled_tools = []
        for server in sampled_data:
            for tool in server.tools:
                all_sampled_tools.append((server, tool))
        
        if not all_sampled_tools:
            raise ValueError
        
        target_index = max(0, min(len(all_sampled_tools)-1, position_index))
        target_server, target_tool = all_sampled_tools[target_index]        
        return target_server, target_tool
    
    def select_target_tool_random(self, sampled_data: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], Dict[str, Any], str]:
        """
        Select a tool randomly.
        
        Args:
            sampled_data
        
        Returns:
            (target_server, target_tool, tool_fullname)
        """
        if not sampled_data:
            raise ValueError
        
        all_sampled_tools = []
        for server in sampled_data:
            for tool in server.tools:
                all_sampled_tools.append((server, tool))
        
        if not all_sampled_tools:
            raise ValueError
        
        target_server, target_tool = random.choice(all_sampled_tools)
        return target_server, target_tool

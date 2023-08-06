import math
import os
import struct

class RpltReader:
    """
    RecurDyn Plot Data Reader class
    """
    def __init__(self, file_path=None):
        self.__file_path = file_path

        self.__sub_number = 0
        self.__data_number = 0
        self.__total_index = 0

        self.__sel_index = [-1, -1, -1, -1]
        self.__root_node = None
        self.__sub_node = None
        self.__parent_flag = False
        self.__match_flag = False
        self.__component_count = 0
        self.__node_dim = 0

        self.__header_end_position = None

        self.__unit = None

        if self.__file_path:
            self.import_file(self.__file_path)

    def _get_unit(self):
        return self.unit

    unit = property(_get_unit, None)

    class __Node:
        """
        Inner class for rplt header
        """
        def __init__(self, name, text):
            self.name = name
            self.text = text
            self.image_key = "-1"
            self.nodes = []
            self.next_node = None
            self.parent = None

        def add_node(self, node):
            node.parent = self
            previous_node_idx = len(self.nodes) - 1
            if previous_node_idx != -1:
                self.nodes[previous_node_idx].next_node = node
            self.nodes.append(node)

        def get_dim_parent_node(self, node_dim):
            parent_node = self
            for dim in range(node_dim):
                parent_node = parent_node.parent
                if not parent_node:
                    break
            else:
                return parent_node

            return None

        def _get_child_name_list_recursive(self, name_list):
            child_name_list = []
            for node in self.nodes:
                node._get_child_name_list_recursive(child_name_list)
            if not child_name_list:
                name_list.append(self.text)
            else:
                for child_name in child_name_list:
                    name = self.text + "/" + child_name
                    name_list.append(name)
                child_name_list.clear()

        def get_child_name_list(self):
            name_list = []
            for node in self.nodes:
                node._get_child_name_list_recursive(name_list)
            if not name_list:
                return None

            return name_list

    def _read_binary_int32(self, f):
        return int.from_bytes(f.read(4), byteorder='little')

    def _read_binary_int8(self, f):
        return int.from_bytes(f.read(1), byteorder='little')

    def _read_binary_double(self, f):
        return struct.unpack('<d', f.read(8))[0]

    def _read_binary_string(self, f):
        _ = f.read(3)
        count = self._read_binary_int8(f)
        data = f.read(count*2)
        return data.decode('utf-16')

    def _read_header(self, file_path):
        self.__file_path = file_path

        self.__sub_number = 0
        self.__data_number = 0
        self.__total_index = 0

        with open(file_path, 'rb') as f:
            version = self._read_binary_int32(f)
            if version == 2:
                version = 1

            recurdyn_pro_sdk = self._read_binary_int32(f)
            recurdyn_version = self._read_binary_int32(f)

            f.read(8)

            self.__unit = [self._read_binary_string(f) for i in range(5)]

            model_name = self._read_binary_string(f)
            self.__root_node = self.__Node("", model_name)

            entity_count = self._read_binary_int32(f)
            for i in range(entity_count):
                self.__node_dim = 0
                self._read_plot_recursive(f, version, self.__root_node)

            self.__header_end_position = f.tell()
            f.close()

        self.__sub_node = None

    def _read_plot_recursive(self, f, version, node):
        self.__sub_number += 1
        dimension_type = 0

        name = self._read_binary_string(f)
        entity_count = self._read_binary_int32(f)

        if version >= 1:
            if entity_count <= 0:
                dimension_type = self._read_binary_int32(f)
                if dimension_type == -1: # dimension_type_user_define
                    _ = self._read_binary_string(f)

        self.__sub_node = self.__Node(str(dimension_type), name)
        if entity_count > 0:
            if self.__parent_flag and node is not None and node.parent is not None:
                dim_parent_node = node.get_dim_parent_node(self.__node_dim)
                dim_parent_node.add_node(self.__sub_node)
            else:
                node.add_node(self.__sub_node)

            self.__parent_flag = False
            for i in range(entity_count):
                self._read_plot_recursive(f, version, self.__sub_node)
            self.__parent_flag = True
            self.__node_dim += 1

        else:
            image_key = str(entity_count)
            if entity_count == 0:
                image_key = str(self.__data_number)
                self.__total_index = self.__data_number
                self.__data_number += 1
                self.__node_dim = 0

            self.__sub_node.image_key = image_key

            if node.parent is None:
                node.add_node(self.__sub_node)
            else:
                node.add_node(self.__sub_node)
                self.__sub_node = node

        self.__sub_number -= 1

    def _find_component(self, list_find):
        self.__sel_index = [-1, -1, -1, -1]

        self.__match_flag = False
        self.__component_count = 0
        self._find_component_recursive(self.__root_node, list_find)

    def _find_component_recursive(self, node, list_find):
        len_node_nodes = len(node.nodes)
        if len_node_nodes == 0:
            self.__match_flag = True
            c_index = int(node.image_key)
            if c_index >= 0:
                self.__sel_index[0] = c_index
            if c_index == -2:
                self.__sel_index[0] = c_index
                self.__sel_index[1] = int(node.next_node.image_key)
                self.__sel_index[2] = int(node.next_node.next_node.image_key)
            if c_index == -3:
                self.__sel_index[0] = c_index
                self.__sel_index[1] = int(node.next_node.image_key)
                self.__sel_index[2] = int(node.next_node.next_node.image_key)
                self.__sel_index[2] = int(node.next_node.next_node.next_node.image_key)
        elif len_node_nodes > 0:
            for child_node in node.nodes:
                if self.__match_flag:
                    break

                child_node_text = child_node.text
                if child_node_text[-1] == " ":
                    child_node_text = child_node_text[:-1]
                if list_find[self.__component_count] == child_node_text:
                    self.__component_count += 1
                    self._find_component_recursive(child_node, list_find)

    def _read_data_from_rplt(self, list_component):
        data = None
        self._find_component(list_component)
        if self.__sel_index[0] >= 0:
            data = self._read_data(self.__header_end_position, self.__sel_index[0], self.__total_index)
        elif self.__sel_index[0] == -2:
            x_data = self._read_data(self.__header_end_position, self.__sel_index[1], self.__total_index)
            y_data = self._read_data(self.__header_end_position, self.__sel_index[2], self.__total_index)

            len_x_data = len(x_data)
            data = [math.sqrt(x_data[idx] ** 2 + y_data[idx] ** 2) for idx in range(len_x_data)]

            x_data.clear()
            y_data.clear()
        elif self.__sel_index[0] == -3:
            x_data = self._read_data(self.__header_end_position, self.__sel_index[1], self.__total_index)
            y_data = self._read_data(self.__header_end_position, self.__sel_index[2], self.__total_index)
            z_data = self._read_data( self.__header_end_position, self.__sel_index[3], self.__total_index)

            len_x_data = len(x_data)
            data = [math.sqrt(x_data[idx]**2 + y_data[idx]**2 + z_data[idx]**2) for idx in range(len_x_data)]

            x_data.clear()
            y_data.clear()
            z_data.clear()

        return data

    def _read_data(self, data_start_position, data_index, total_index):
        data = None
        with open(self.__file_path, 'rb') as f:
            current_data_position = data_start_position + data_index * 8

            f.seek(0, os.SEEK_END)
            data_length = f.tell()

            f.seek(current_data_position, 0)

            data_size = data_length - data_start_position
            data_size = int(data_size / (8 * (total_index+1)))

            data_offset = 8 * total_index
            data = [0.0] * data_size
            for idx in range(data_size):
                data[idx] = self._read_binary_double(f)
                f.seek(data_offset, 1)

            f.close()

        return data

    def clear(self):
        """
        Clear memory
        """
        self.__file_path = None

        self.__sub_number = 0
        self.__data_number = 0
        self.__total_index = 0

        self.__sel_index = [-1, -1, -1, -1]

        if self.__root_node:
            self.__root_node.clear_all()
            self.__root_node = None

        self.__sub_node = None
        self.__parent_flag = False
        self.__match_flag = False
        self.__component_count = 0
        self.__node_dim = 0

        self.__header_end_position = None

        if self.__unit:
            self.__unit.clear()
            self.__unit = None

    def import_file(self, file_path):
        """
        Import *.rplt file.

        :param file_path: str
        """
        self._read_header(file_path)

    def get_plot_data(self, string_component):
        """
        Input the data name to be imported as follows.
        "Bodies/Body1/Pos_TM"

        :param file_path: str
        """
        if self.__file_path is None:
            raise Exception("Please import the file first.")
        list_component = string_component.replace('\\', '/').split('/')
        return self._read_data_from_rplt(list_component)

    def get_plottable_name_list(self):
        return self.__root_node.get_child_name_list()
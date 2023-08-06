    #! :param means parameter
def search_all(lists:list,value,index_range:tuple):
    """
    It returns the index of the first occurrence of the value in the list, or a tuple of all the indices
    of the value in the list if the index range is specified
    
    :param lists: list
    :type lists: list
    :param value: the value you want to search for
    :param index_range: tuple
    :type index_range: tuple
    :return: A tuple of all the indexes of the value in the list
    """
    if len(index_range) >2:
        raise Exception("length of index range must be either 0 or 2")
    if len(index_range) == 0:
        return lists.index(value,index_range[0],index_range[1])
    elif len(index_range) == 2:
        index_list = [index for values,index in zip(lists[index_range[0]:index_range[1]],range(index_range[0],index_range[1])) if values == value]
        if index_list == []:
            raise IndexError(f"{value} is not in the specified index")
        return tuple(index_list)

# It's a class that takes a dictionary as an argument and stores it as an attribute
class Flexi:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def is_value(self, value):
        """
        It returns True if the value is in the dictionary, and False if it is not
        :param value: The value to search for
        """
        return value in self.dictionary.values()

    def is_item(self, key,value):
        """
        The function is_item() takes in a key and a value and returns True if the key and value are in
        the dictionary and False if they are not
        :param key: The key to search for
        :param value: The value to be searched for
        """
        return (key,value) in self.dictionary.items()

    def d_index(self, kev,start_pos:int = None, stop_pos:int = None,condition="key" ):
        """
        > It returns the index of the key or value in the dictionary
        
        :param kev: the key or value you want to search for
        :param start_pos: The starting index of the search
        :type start_pos: int
        :param stop_pos: The position of the last element to be included in the search
        :type stop_pos: int
        :param condition: This is the condition for the search. It can be either "key" or "value", defaults
        to key (optional)
        :return: The index of the key or value in the dictionary.
        """
        # checking the keywords in return_type
        if condition not in ["key", "value"]:
            raise Exception("return_type should be key or value")
        # checking the keys and values
        if kev not in self.dictionary.keys() and condition == "key":
            raise Exception ("key not present in the dictionary")
        elif kev not in self.dictionary.values() and condition == "value":
            raise Exception ("value not present in the dictionary")
        # checking the index
        if start_pos != None and stop_pos != None:
            if start_pos  not in range(len(self.dictionary)) or stop_pos  not in range(len(self.dictionary)+1):
                raise IndexError("invalid index")
        
        kev_list = []
        if condition == "key":
            kev_list = list(self.dictionary.keys())
        else:
            kev_list = list(self.dictionary.values())
        
        if start_pos == None and stop_pos == None:
            return kev_list.index(kev)
        if start_pos != None and stop_pos != None:
            key = search_all(kev_list, kev, index_range=(start_pos, stop_pos))
            if len(key) == 1:
                return key[0]
            elif len(key)>1:
                return key
        else:
            raise Exception(
                        "both start_pose and stop_pose should be filled")

    def d_get(self,value):
        """
        If the value is in the dictionary, return the key(s) associated with the value
        :param value: The value you want to get the key of
        :return: The key of the value.
        """
        if value in self.dictionary.values():
            index = Flexi.d_index(self,value,start_pos = 0,stop_pos = len(self.dictionary),condition="value")
            if  isinstance(index,int):
                return Flexi.d_key(self,index)
            elif isinstance(index,tuple):
                key_list = []
                for indexs in index:
                    key_list.append(Flexi.d_key(self,indexs))
                return tuple(key_list)
        else:
            return None

    def d_key(self, index: int):
        """
        It returns the key of the dictionary at the given index
        :param index: int
        :type index: int
        :return: The key of the dictionary at the given index.
        """
        if index not in range(len(self.dictionary)):
            raise IndexError("invalid index")
        return list(self.dictionary.keys())[index]

    def d_value(self, index: int):
        """
        It returns the value of the dictionary at the given index
        :param index: int
        :type index: int
        :return: The value of the dictionary at the given index.
        """
        if index not in range(len(self.dictionary)):
            raise IndexError("invalid index")
        return list(self.dictionary.values())[index]
    
    def d_item(self, index: int):
        """
        It returns the item at the given index in the dictionary
        :param index: int
        :type index: int
        :return: A tuple of the key and value of the item at the given index.
        """
        if index not in range(len(self.dictionary)):
            raise IndexError("invalid index")
        item = list(self.dictionary.items())[index]
        return item

    def d_exchange(self, no_of_exchanges=1, return_type="no_update"):
        """
        It exchanges the keys and values of a dictionary
        :param no_of_exchanges: the number of times the dictionary is exchanged, defaults to 1 (optional)
        :param return_type: if you want to update the dictionary or not, defaults to no_update (optional)
        :return: the exchanged dictionary.
        """
        if isinstance(no_of_exchanges, int) == False:
            raise Exception("type(no_of_exchanges) == int")
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")
        exchanged_dictionary = self.dictionary
        if no_of_exchanges % 2 != 0:
            exchanged_dictionary = {value: key for key,
                                    value in self.dictionary.items()}
        if len(self.dictionary) == len(exchanged_dictionary):
            if return_type == "update":
                self.dictionary.clear()
                self.dictionary.update(exchanged_dictionary)
            if return_type == "no_update":
                return exchanged_dictionary
        else:
            raise Exception("the dictionary has identical values so it cannot be exchanged")

    def d_reverse(self, no_of_times=1, return_type="no_update"):
        """
        It reverses the dictionary and returns the reversed dictionary. 
        :param no_of_times: The number of times you want to reverse the dictionary, defaults to 1 (optional)
        :param return_type: If you want to update the dictionary, then set return_type to "update". If you
        want to return a new dictionary, then set return_type to "no_update", defaults to no_update
        (optional)
        :return: The reversed dictionary is being returned if return_type is "no_update"
        """
        if isinstance(no_of_times, int) == False:
            raise Exception("type(no_of_times) == int")
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        reversed_dictionary = self.dictionary
        if no_of_times % 2 != 0:
            reversed_dictionary = dict(reversed(self.dictionary.items()))
            if return_type == "update":
                self.dictionary.clear()
                self.dictionary.update(reversed_dictionary)

        if return_type == "no_update":
            return reversed_dictionary

    def sort_keys(self, return_type="no_update"):
        """
        It takes a dictionary, sorts it by key, and returns a new dictionary

        :param return_type: This is the type of return value you want. If you want the dictionary to be
        updated, then you should pass "update" as the value. If you want a new dictionary to be returned,
        then you should pass "no_update" as the value, defaults to no_update (optional)
        :return: The sorted dictionary is being returned if the return_type is no_update
        """
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        items_list = list(self.dictionary.items())
        items_list.sort()
        sorted_dictionary = dict(items_list)

        if return_type == "no_update":
            return sorted_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(sorted_dictionary)

    def sort_values(self, return_type="no_update"):
        """
        It sorts the values of the dictionary and returns a new dictionary with the sorted values if return_type is no_update
        
        :param return_type: This is the type of return you want. If you want to update the dictionary, then
        you can use "update" as the parameter. If you want to return a new dictionary, then you can use
        "no_update" as the parameter, defaults to no_update (optional)
        :return: A dictionary with the same keys as the original dictionary, but with the values sorted.
        """
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        value_list = list(self.dictionary.values())
        value_list.sort()
        sorted_dictionary = {}
        for values in value_list:
            sorted_dictionary.update(Flexi.similar_values(self,values))

        if return_type == "no_update":
            return sorted_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(sorted_dictionary)

    def d_insert(self, index: int, key, value, return_type="no_update"):
        """
        It takes a dictionary, an index, a key and a value as input and returns a new dictionary with the
        key-value pair inserted at the index if the return_type is no_update
        
        :param index: the index where you want to insert the key-value pair
        :type index: int
        :param key: The key to be inserted
        :param value: The value to be inserted
        :param return_type: if you want to update the dictionary or not, defaults to no_update (optional)
        :return: The dictionary with the new key-value pair inserted at the specified index.
        """
        # checking the keywords
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")
        length = len(self.dictionary)+1 
        if index > length:
            index = length

        item_list = list(self.dictionary.items())
        item_list.insert(index, (key, value))
        inserted_dictionary = dict(item_list)

        if return_type == 'no_update':
            return inserted_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(inserted_dictionary)

    def d_remove(self, index: int):
        """
        It takes the dictionary, copies it, and then removes the key at the index
        
        :param index: the index of the item to be removed
        :type index: int
        :return: A new dictionary with the key removed.
        """
        new_dictionary = self.dictionary.copy()
        new_dictionary.pop(Flexi.d_key(self, index))
        return new_dictionary

    def d_replace(self, index: int, key, value, return_type="no_update"):
        """
        It inserts a new key-value pair at the specified index, and then removes the key-value pair that was
        previously at that index
        
        :param index: The index of the key-value pair you want to replace
        :type index: int
        :param key: The key of the item you want to replace
        :param value: The value to be inserted
        :param return_type: This is the type of return value you want. If you want the dictionary to be
        updated, then you should use "update". If you want a new dictionary to be returned, then you should
        use "no_update", defaults to no_update (optional)
        :return: The dictionary with the key and value at the index removed.
        """
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        inserted_dictionary = Flexi.d_insert(
            self, index, key, value, return_type=return_type)
        if return_type == "no_update":
            replaced_dictionary = Flexi(inserted_dictionary)
            return replaced_dictionary.d_remove(index+1)
        else:
            self.dictionary.pop(Flexi.d_key(self, index+1))

    def d_slicing(self, start_index:int=None, stop_index:int=None, step_index:int=None, return_type="no_update"):
        """
        It takes a dictionary, slices it, and returns a new dictionary
        
        :param start_index: The starting index of the slicing. Default is 0
        :type start_index: int
        :param stop_index: The index of the last element in the list
        :type stop_index: int
        :param step_index: The step size of the slicing. Default is 1
        :type step_index: int
        :param return_type: if you want to update the dictionary, then set it to "update", else set it to
        "no_update", defaults to no_update (optional)
        :return: A dictionary
        """
        start_index = 0 if start_index == None else start_index
        stop_index = len(self.dictionary) if stop_index == None else stop_index
        step_index = 1 if step_index == None else step_index

        # checking the keywords
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        item_list = list(self.dictionary.items())
        sliced_item_list = item_list[start_index:stop_index:step_index]
        sliced_dictionary = dict(sliced_item_list)
        if return_type == 'no_update':
            return sliced_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(sliced_dictionary)

    def swap_keys(self, start_index: int, stop_index: int, return_type="no_update"):
        """
        It swaps the keys of the dictionary at the given indices
        
        :param start_index: the index of the key you want to swap
        :type start_index: int
        :param stop_index: the index of the key you want to swap with the start_index key
        :type stop_index: int
        :param return_type: if you want to update the dictionary, then you should pass "update" as the
        return_type, defaults to no_update (optional)
        :return: a dictionary with the keys swapped.
        """
        if start_index not in range(len(self.dictionary)) or stop_index not in range(len(self.dictionary)):
            raise IndexError("invalid index")
        # checking the keywords
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        exchanged_list = [[key, value]
                          for key, value in list(self.dictionary.items())]
        exchanged_list[start_index][0], exchanged_list[stop_index][0] = exchanged_list[stop_index][0], exchanged_list[start_index][0]
        exchanged_dictionary = dict(exchanged_list)

        if return_type == "no_update":
            return exchanged_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(exchanged_dictionary)

    def swap_values(self, start_index: int, stop_index: int, return_type="no_update"):
        """
        It swaps the values of two keys in a dictionary
        
        :param start_index: the index of the first value to be swapped
        :type start_index: int
        :param stop_index: the index of the value you want to swap with the value at start_index
        :type stop_index: int
        :param return_type: if you want to update the dictionary, set it to "update", otherwise, set it to
        "no_update", defaults to no_update (optional)
        :return: The dictionary is being returned.
        """
        if start_index not in range(len(self.dictionary)) or stop_index not in range(len(self.dictionary)):
            raise IndexError("invalid index")
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")

        exchanged_list = [[key, value]
                          for key, value in list(self.dictionary.items())]
        exchanged_list[start_index][1], exchanged_list[stop_index][1] = exchanged_list[stop_index][1], exchanged_list[start_index][1]
        exchanged_dictionary = dict(exchanged_list)

        if return_type == "no_update":
            return exchanged_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(exchanged_dictionary)

    def count_value(self, value):
        """
        It returns the number of times a value appears in the dictionary
        
        :param value: The value to be counted
        :return: The number of times the value appears in the dictionary.
        """
        return list(self.dictionary.values()).count(value)

    def has_similar_value(self, value):
        """
        If the value is present in the dictionary, and the count of the value is greater than 1, then return
        True, otherwise return False
        
        :param value: The value to be checked for similarity
        """
        if Flexi.is_value(self,value):
            if Flexi.count_value(self,value) > 1:
                return True
            else:
                return False
        else:
            raise Exception("value is not present in dictionary")

    def similar_values(self, value):
        """
        It returns a dictionary of all the keys and values that have the same value as the value you pass to
        the function
        
        :param value: The value to be searched for
        :return: A dictionary with the key and value of the similar values.
        """
        if Flexi.has_similar_value(self, value):
            multiple_index = Flexi.d_index(self, value, 0, len(
                self.dictionary), condition="value")
            similar_dictionaries = {}
            for no in multiple_index:
                key = Flexi.d_key(self, no)
                value = Flexi.d_value(self, no)
                similar_dictionaries.update({key: value})
            return similar_dictionaries
        else:
            key = Flexi.d_get(self, value)
            return {key:value}

    def d_split(self,stop_index:int):
        """
        It takes a dictionary and splits it into two dictionaries, the first one containing the first half
        of the original dictionary and the second one containing the second half of the original dictionary
        
        :param stop_index: The index at which the dictionary is split
        :type stop_index: int
        :return: A tuple of two dictionaries.
        """
        first_dictionary = Flexi.d_slicing(self, 0, stop_index,1,"no_update")
        second_dictionary = Flexi.d_slicing(self,stop_index, len(self.dictionary),1,"no_update")
        return first_dictionary, second_dictionary
    
    def auto_arrange(self,index_list:list,return_type = "no_update"):
        """
        It takes a list of indices and returns a dictionary with the keys in the same order as the indices
        
        :param index_list: list of indices in the order you want to arrange the dictionary
        :type index_list: list
        :param return_type: If you want to update the dictionary, set this to "update". If you want to
        return a new dictionary, set this to "no_update", defaults to no_update (optional)
        :return: A dictionary with the same keys as the original dictionary, but in the order specified by
        the index_list.
        """
        if return_type not in ["no_update", "update"]:
            raise Exception("return_type should be either update or no_update")
        if isinstance(index_list,int) == False:
            raise Exception("indices must be integers")

        index_list.extend(list(set(range(len(self.dictionary))) - set(index_list)))
        
        key_list = []
        for no in index_list:
            key_list.append(Flexi.d_key(self,no))
        
        new_dictionary = {key:self.dictionary[key] for key in key_list}

        if return_type == "no_update":
            return new_dictionary
        else:
            self.dictionary.clear()
            self.dictionary.update(new_dictionary)
    
    def d_max(self,condition="key"):
        """
        It returns the key-value pair of the maximum value in the dictionary
        
        :param condition: This is the condition for the return type. It can be either key or value, defaults
        to key (optional)
        :return: The maximum key or value in the dictionary.
        """
        if condition not in ["key","value"]:
            raise Exception("return type should be either key or value")
        
        if condition == "key":
            max_key = max(list(self.dictionary.keys()))
            max_key_element = {max_key:self.dictionary[max_key]}
            return max_key_element
        
        else:
            max_value = max(list(self.dictionary.values()))
            index_list = Flexi.d_index(self,max_value,start_pos=0,stop_pos=len(self.dictionary),condition="value")
            max_value_element = {}
            if type(index_list) != int:
                for index in index_list:
                    max_value_element.update({Flexi.d_key(self,index):max_value})
                return max_value_element
            else:
                max_value_element.update({Flexi.d_key(self,index_list):max_value})
                return max_value_element

    def d_min(self,condition="key"):
        """
        It returns the minimum value of the dictionary, and if there are multiple minimum values, it returns
        all the keys associated with the minimum value
        
        :param condition: This is the condition for the return type. It can be either key or value, defaults
        to key (optional)
        :return: The minimum value of the dictionary.
        """
        if condition not in ["key","value"]:
            raise Exception("return type should be either key or value")
        
        if condition== "key":
            min_element = min(list(self.dictionary.keys()))
            return {min_element:self.dictionary[min_element]}
        else:
            min_value = min(list(self.dictionary.values()))
            index_list = Flexi.d_index(self,min_value,start_pos=0,stop_pos=len(self.dictionary),condition="value")
            min_value_element = {}
            if type(index_list) != int:
                for index in index_list:
                    min_value_element.update({Flexi.d_key(self,index):min_value})
                return min_value_element
            else:
                min_value_element.update({Flexi.d_key(self,index_list):min_value})
                return min_value_element

    def d_type(self):
        """
        It returns a dictionary with the same keys as the original dictionary, but the values are the types
        of the original values.
        :return: A dictionary with the same keys as the original dictionary, but the values are the types of
        the original values.
        """
        new_dictionary = self.dictionary.copy()
        for key,value in list(self.dictionary.items()):
            new_dictionary[key] = type(value)
        return new_dictionary

    def d_group(self):
        """
        It takes a dictionary and returns a tuple of dictionaries, in which the key:value pairs are grouped/segregated based on the value types
        :return: A tuple of dictionaries.
        """
        type_dict = Flexi.d_type(self)
        value_list = set(type_dict.values())
        grouped_dictionary = []
        new_object = Flexi(type_dict)
        for values in value_list:
            new_dictionary = new_object.similar_values(values)
            grouped_dictionary.append({keys:self.dictionary[keys] for keys in new_dictionary.keys()})
        return tuple(grouped_dictionary)

    def is_common_key(self,other_dictionary:dict,key):
        """
        If the key is in both dictionaries, return True. Otherwise, return False
        
        :param other_dictionary: The dictionary to compare to
        :type other_dictionary: dict
        :param key: the key to check
        :return: The value of the key in the dictionary.
        """
        return key in self.dictionary and key in other_dictionary
    
    def is_common_value(self,other_dictionary:dict,value):
        """
        It checks if the value is present in both the dictionaries.
        
        :param other_dictionary: The dictionary to compare with
        :type other_dictionary: dict
        :param value: The value to check for
        :return: The function is_common_value is returning a boolean value.
        """
        new_dictionary = Flexi(other_dictionary)
        return Flexi.is_value(self,value) and new_dictionary.is_value(value)

    def is_common_item(self,other_dictionary:dict,key,value):
        """
        If the key and value are in both dictionaries, return True
        
        :param other_dictionary: The dictionary to compare with
        :type other_dictionary: dict
        :param key: the key to check
        :param value: The value of the key
        :return: The function is_common_item is returning a boolean value.
        """
        new_dictionary = Flexi(other_dictionary)
        return Flexi.is_item(self,key,value) and new_dictionary.is_item(key,value)
    
    def item_with_common_key(self,other_dictionary:dict):
        """
        It takes a dictionary as an argument and returns a tuple of dictionaries containing the common keys
        and their values
        
        :param other_dictionary: The dictionary that you want to compare with
        :type other_dictionary: dict
        :return: A tuple of dictionaries.
        """
        common_key_list = []
        for key in self.dictionary.keys():
            if Flexi.is_common_key(self,other_dictionary,key):
                common_key_list.append({key:self.dictionary[key]})
                common_key_list.append({key:other_dictionary[key]})
        return tuple(common_key_list)

    def item_with_common_value(self,other_dictionary:dict):
        """
        It returns a tuple of dictionaries of the keys that have the same value in both dictionaries.
        
        :param other_dictionary: The dictionary that you want to compare with the dictionary that you have
        created the object with
        :type other_dictionary: dict
        :return: A tuple of dictionaries.
        """
        value_list = list(self.dictionary.values())
        for i in value_list:
            if value_list.count(i) >1:
                value_list.remove(i)
        common_value_list = []
        for value in value_list:
            if Flexi.is_common_value(self,other_dictionary,value):
                new_object = Flexi(other_dictionary)
                common_value_list.append(Flexi.similar_values(self,value))
                common_value_list.append(new_object.similar_values(value))
        return tuple(common_value_list)

    def common_item(self,other_dictionary:dict):
        """
        It takes two dictionaries as input and returns a tuple of dictionaries that have the same key and
        value
        
        :param other_dictionary: The dictionary to be compared with the current dictionary
        :type other_dictionary: dict
        :return: A tuple of dictionaries
        """
        common_item_list = []
        items_tuple = Flexi.item_with_common_key(self,other_dictionary)
        if len(items_tuple) != 0:
            for items in items_tuple:
                if items_tuple.count(items) == 2:
                    common_item_list.append(dict(items))
        return tuple(common_item_list)


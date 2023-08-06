# Copyright 2022 Tiger Miao and collaborators.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""compare tools"""
import os
import torch
import numpy as np
import mindspore as ms
from pprint import pprint
from troubleshooter import log as logger
from troubleshooter.common.format_msg import print_diff_result
from troubleshooter.common.format_msg import print_weight_compare_result
from troubleshooter.common.format_msg import print_convert_result
from troubleshooter.common.util import validate_and_normalize_path, find_file
from troubleshooter.migrator.mapping_relation.weight_mapping_lib import weight_map

class DifferenceFinder:

    def __init__(self, orig_dir, target_dir):
        self.orig_dir = orig_dir
        self.target_dir = target_dir
    def get_filename_map_list(self):
        name_map_list = []
        orig_name_list = find_file(self.orig_dir)
        orig_name_list.sort()
        target_name_list = find_file(self.target_dir)
        none_flag = False

        if not (orig_name_list and target_name_list):
            logger.user_error("The comparison file is not found in the directory. Please check whether the directory is correct")
            exit(1)

        for name in orig_name_list:
            if name in target_name_list:
                name_map_list.append((name, name))
                target_name_list.remove(name)
            else:
                name_map_list.append((name, None))
                none_flag = True

        if target_name_list:
            target_name_list.sort()
            for name in target_name_list:
                name_map_list.append((None, name))
            none_flag = True

        if none_flag:
            logger.user_warning("The files in the original directory and the target directory cannot be fully mapped. "
                                "Please manually complete the mapping of file names")
            print("filename mapping list:" + str(name_map_list))
        return name_map_list


    def compare_npy_dir(self, name_map_list=None, **kwargs):
        """
        """
        if name_map_list is None:
            name_map_list = self.get_filename_map_list()


        rtol = kwargs.get('rtol', 1e-05)
        atol = kwargs.get('atol', 1e-08)
        equal_nan = kwargs.get('equal_nan', False)

        result_list = []
        diff_detail = ()
        normal_orig_dir = validate_and_normalize_path(self.orig_dir)
        normal_target_dir = validate_and_normalize_path(self.target_dir)
        for name_map in name_map_list:
            orig_name = name_map[0]
            target_name = name_map[1]

            if orig_name is None or target_name is None:
                result = False
                diff_detail = ()
                result_list.append((orig_name, target_name, result, diff_detail))
                continue

            orig_file = os.path.join(normal_orig_dir, orig_name)
            target_file = os.path.join(normal_target_dir, target_name)

            if not os.path.isfile(orig_file) or not os.path.isfile(target_file):
                continue

            orig_value = np.load(orig_file)
            target_value = np.load(target_file)
            result = np.allclose(orig_value, target_value, rtol=rtol, atol=atol, equal_nan=equal_nan)

            if not result:
                value_diff = np.abs(orig_value - target_value)
                value_mean = value_diff.mean()
                value_max = value_diff.max()
                value_min = value_diff.min()
                diff_detail = value_mean, value_max, value_min
            else:
                diff_detail = ()

            result_list.append((orig_name, target_name, result, diff_detail))
        print_diff_result(result_list)



class WeightMigrator:

    def __init__(self, pt_model=None, pth_file_path=None, ckpt_save_path=None):
        self.weight_map = weight_map
        self.ckpt_path = ckpt_save_path
        self.pt_model = pt_model
        self.pt_para_dict = torch.load(pth_file_path, map_location='cpu')
        self.ms_para_list = []

    def _get_object(self, name):
        object_res = None
        index = name.rfind(".")
        if index:
            module_name = name[:index]
            class_name = name[index + 1:]
            import importlib
            imp_module = importlib.import_module(module_name)
            object_res = getattr(imp_module, class_name)
        return object_res


    def get_weight_map(self, print_map=False):
        res_weight_map = {}
        for name, module in  self.pt_model.named_modules():
            for api_name in weight_map:
                obj = self._get_object(api_name)
                if isinstance(module,obj):
                    para_map = weight_map.get(api_name)
                    for pt_para_name, ms_para_name in para_map.items():
                        pt_para_item = name + "." + pt_para_name
                        ms_para_item  = name + "." + ms_para_name
                        res_weight_map[pt_para_item] = ms_para_item
                    break
        if print_map:
            pprint(res_weight_map)
        return res_weight_map


    def convert(self, weight_map=None, print_conv_info=True):
        if weight_map is None:
            weight_map = self.get_weight_map()

        new_params_list = []
        print_params_list = []

        for name in self.pt_para_dict:
            pth_param_name = name
            parameter = self.pt_para_dict[name]
            ms_para_item = weight_map.get(name)

            if ms_para_item:
                name = ms_para_item

            new_params_list.append({"name": name, "data": ms.Tensor(parameter.numpy())})

            if print_conv_info:
                print_params_list.append((pth_param_name, name, bool(ms_para_item), parameter.size()))

        self.ms_para_list = new_params_list
        ms.save_checkpoint(self.ms_para_list , self.ckpt_path)
        if print_conv_info:
             print_convert_result(print_params_list)
        logger.user_attention("The PTH has been converted to the checkpoint of MindSpore. "
                              "Please check whether the conversion result is correct. "
                              "The saved path is: %s",self.ckpt_path)



    def compare_ckpt(self, ckpt_path=None, converted_ckpt_path=None, print_result=1):
        name_map_list = []
        if converted_ckpt_path is None:
            ckpt_after_convert_path = self.ckpt_path
        ckpt_dict = ms.load_checkpoint(ckpt_path)
        ckpt_after_conv_dict = ms.load_checkpoint(ckpt_after_convert_path)

        for ms_para_name, ms_para in ckpt_dict.items():
            ms_para_after_conv = ckpt_after_conv_dict.get(ms_para_name)

            if ms_para_after_conv is not None:
                name_map_list.append((ms_para_name, ms_para_name, (ms_para.shape == ms_para_after_conv.shape), ms_para.shape, ms_para_after_conv.shape))
                ckpt_after_conv_dict.pop(ms_para_name)
            else:
                name_map_list.append((ms_para_name, None, None, ms_para.shape, None))

        for name in ckpt_after_conv_dict:
            name_map_list.append((None, name, None, None, ms_para_after_conv.shape))
        print_weight_compare_result(name_map_list, print_type=print_result)

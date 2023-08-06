from ibm_ray_config.modules.config_builder import ConfigBuilder, update_decorator, spinner
from typing import Any, Dict
from ibm_ray_config.modules.utils import get_option_from_list, find_default, find_obj, get_confirmation, get_profile_resources


class ProfileConfig(ConfigBuilder):
    
    def __init__(self, base_config: Dict[str, Any]) -> None:
        super().__init__(base_config)
        self.worker_instance_profile = None  # used by the workers module to assign a separate worker's profile  

    def run(self) -> Dict[str, Any]:

        @spinner
        def get_instance_profile_objects():
            return self.ibm_vpc_client.list_instance_profiles().get_result()['profiles']

        instance_profile_objects = get_instance_profile_objects()

        default = find_default(
            self.base_config, instance_profile_objects, name='instance_profile_name')
        head_instance_profile = get_option_from_list(
            'Choose instance profile for the Head node, please refer to https://cloud.ibm.com/docs/vpc?topic=vpc-profiles', instance_profile_objects, default=default)['name']
        
        separate_worker_profile = get_confirmation("Would you like to use a different instance profile for worker nodes?")
        if separate_worker_profile:
            # 'worker_instance_profile' will be used in the workers module 
            self.base_config['worker_instance_profile'] = get_option_from_list(
                'Choose instance profile for the worker node, please refer to https://cloud.ibm.com/docs/vpc?topic=vpc-profiles', instance_profile_objects, default=default)['name']
            
        cpu_num, memory, gpu_num = get_profile_resources(head_instance_profile)

        self.base_config['available_node_types']['ray_head_default']['node_config']['instance_profile_name'] = head_instance_profile
        self.base_config['available_node_types']['ray_head_default']['resources']['CPU'] = cpu_num
        self.base_config['available_node_types']['ray_head_default']['resources']['memory'] = memory
        if gpu_num:
            self.base_config['available_node_types']['ray_head_default']['resources']['GPU'] = gpu_num
        
        return self.base_config
    
    @update_decorator
    def verify(self, base_config):
        profile_name = self.defaults['profile_name']
        instance_profile_objects = self.ibm_vpc_client.list_instance_profiles().get_result()['profiles']
        profile = find_obj(instance_profile_objects, 'dummy', obj_name=profile_name)
        if not profile:
            raise Exception(f'Specified profile {profile_name} not found in the profile list {instance_profile_objects}')
        return profile_name

    @update_decorator    
    def create_default(self):
        return 'bx2-2x8'

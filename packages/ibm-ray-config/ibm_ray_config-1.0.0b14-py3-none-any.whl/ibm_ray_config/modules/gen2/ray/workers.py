import re
import copy
from typing import Any, Dict

import inquirer
from ibm_ray_config.modules.config_builder import ConfigBuilder
from ibm_ray_config.modules.utils import validate_cluster_name, get_profile_resources

class WorkersConfig(ConfigBuilder):

    def run(self) -> Dict[str, Any]:
        default_cluster_name = self.base_config.get('cluster_name', 'default')
        default_min_workers = self.base_config.get('min_workers', '0')
        default_max_workers = default_min_workers

        question = [
            inquirer.Text(
                'name', message="Enter cluster name following the pattern `[a-z]|[a-z][-a-z0-9]*[a-z0-9]`", validate = validate_cluster_name, default=default_cluster_name),
            inquirer.Text('min_workers', message="Minimum number of worker nodes",
                          default=default_min_workers, validate=lambda _, x: re.match('^[+]?[0-9]+$', x)),
            inquirer.Text('max_workers', message="Maximum number of worker nodes", default=default_max_workers,
                          validate=lambda answers, x: re.match('^[+]?[0-9]+$', x) and int(x) >= int(answers['min_workers']))
        ]
        answers = inquirer.prompt(question, raise_keyboard_interrupt=True)
        self.base_config['cluster_name'] = answers['name']
        self.base_config['max_workers'] = int(answers['max_workers'])

        if self.base_config.get('worker_instance_profile', None):
            self.base_config['available_node_types']['ray_head_default']['min_workers'] = 0 
            self.base_config['available_node_types']['ray_head_default']['max_workers'] = 0

            worker_dict = copy.deepcopy(self.base_config['available_node_types']['ray_head_default'])
            worker_dict['node_config'].pop('head_ip',None)

            worker_dict['min_workers'] = int(answers['min_workers'])
            worker_dict['max_workers'] = int(answers['max_workers'])
            worker_dict['node_config']['instance_profile_name'] = self.base_config['worker_instance_profile']
            
            cpu, memory, gpu = get_profile_resources(self.base_config['worker_instance_profile'])
            if gpu:
                worker_dict['resources']['GPU'] = gpu
            worker_dict['resources']['CPU'] = cpu
            worker_dict['resources']['memory'] = memory

            self.base_config['available_node_types']['ray_worker_default'] = worker_dict
            del self.base_config['worker_instance_profile']
        else:
            self.base_config['available_node_types']['ray_head_default']['min_workers'] = int(answers['min_workers'])
            self.base_config['available_node_types']['ray_head_default']['max_workers'] = int(answers['max_workers'])

        return self.base_config
    
    def verify(self, base_config):
        min_workers = base_config['available_node_types']['ray_head_default']['min_workers']
        max_workers = base_config['available_node_types']['ray_head_default']['max_workers']
        
        if max_workers < min_workers:
            raise Exception(f'specified min workers {min_workers} larger than max workers {max_workers}')

        return base_config

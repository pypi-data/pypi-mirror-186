import importlib
import pkg_resources
import os
import click
import yaml

from ibm_ray_config.modules.utils import color_msg, Color, verify_paths, dump_cluster_folder

# currently supporting configuration for ray above IBM Gen2 VPC. 
IBM_VPC = 'IBM VPC'
backends =[{'name': IBM_VPC, 'path': 'gen2.ray'}]

def select_backend(input_file, default_config_suffix=''):
    """returns a base config file for the backend and its package """
    backend = backends[0] # currently supporting a single backend
   
    base_config = {}

    if input_file:
        with open(input_file) as f:
            base_config = yaml.safe_load(f)
    else:
        base_config = load_base_config(backend, default_config_suffix)

    # find the right modules
    backend_pkg = importlib.import_module(f"ibm_ray_config.modules.{backend['path']}")

    return base_config, backend_pkg

def load_base_config(backend, default_config_suffix=''):
    """returns a default base configuration dict for the chosen backend """
    backend_path = backend['path'].replace('.', '/')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{dir_path}/modules/{backend_path}/defaults{default_config_suffix}.yaml"

    base_config = None
    with open(input_file) as f:
        base_config = yaml.safe_load(f)

    return base_config

def validate_api_keys(base_config, modules, iam_api_key, compute_iam_endpoint):
    """validates the api key specified.
    returns a base config dict, updated with the api-key field populated and the post api-key module removal modules list  """
    # The API_KEY module is invoked and popped from the list. 
    api_key_module = modules[0]
    base_config = api_key_module(base_config).run(api_key=iam_api_key,
                                                  compute_iam_endpoint=compute_iam_endpoint)

    modules = modules[1:]
    return base_config, modules
    
@click.command()
@click.option('--output-folder', '-o', help='Output folder to save configurations')
@click.option('--input-file', '-i', help=f'Template for the new configuration')
@click.option('--iam-api-key', '-a', help='IAM_API_KEY')
@click.option('--version', '-v', help=f'Get package version', is_flag=True)
@click.option('--compute-iam-endpoint', help='IAM endpoint url used for compute instead of default https://iam.cloud.ibm.com')
@click.option('--endpoint', help='IBM Cloud API endpoint')
@click.option('--pr', '-g', help=f'Temporary workaround for ray gen2 only. If specified, use provider setup from PR github', is_flag=True, default=False)
def builder(iam_api_key, output_folder, input_file, version, compute_iam_endpoint, endpoint, pr):
    defaults = None  # to be replaced by a flag  
    if version:
        print(f"{pkg_resources.get_distribution('ibm-ray-config').project_name} "
              f"{pkg_resources.get_distribution('ibm-ray-config').version}")
        exit(0)

    print(color_msg("\nWelcome to ibm_ray_config export helper\n", color=Color.YELLOW))

    input_file, output_folder = verify_paths(input_file, output_folder)

    default_config_suffix = ''
    if pr:
        default_config_suffix = '_pr'

    base_config, backend_pkg = select_backend(input_file, default_config_suffix)
    
    modules = backend_pkg.MODULES
    base_config['create_defaults'] = defaults
    base_config, modules = validate_api_keys(base_config, modules, iam_api_key, compute_iam_endpoint)

    if endpoint:
        base_config['provider']['endpoint'] = endpoint

    for module in modules:
        next_module = module(base_config)
        
        if defaults:
            base_config = next_module.create_default()
        else:
            base_config = next_module.run()
    del base_config['create_defaults']

    cluster_folder = dump_cluster_folder(base_config, output_folder)
    
    print("\n\n=================================================")
    print(color_msg(f"Cluster config folder: {cluster_folder}", color=Color.LIGHTGREEN))
    print("=================================================")

def error(msg):
    print(msg)
    raise Exception(msg)

def generate_config(*args, **kwargs):
    """A programmatic avenue to create configuration files. To be used externally by user."""
    backend = backends[0] # currently supporting a single backend
    _, output_file = verify_paths(None, None)
    
    # now update base config with backend specific params
    base_config = importlib.import_module(f"ibm_ray_config.modules.{backend['path']}").load_config(backend, *args, **kwargs)
    
    # now find the right modules
    modules = importlib.import_module(f"ibm_ray_config.modules.{backend['path']}").MODULES
    
    for module in modules:
        base_config = module(base_config).verify(base_config)

    with open(output_file, 'w') as outfile:
        yaml.dump(base_config, outfile, default_flow_style=False)

    print("\n\n=================================================")
    print(color_msg(f"Cluster config file: {output_file}", color=Color.LIGHTGREEN))
    print("=================================================")

    return output_file

def delete_config(config_file_path):
    config = None
    with open(config_file_path) as f:
        config = yaml.safe_load(f)
        
    from ibm_ray_config.modules.gen2 import delete_config
    delete_config(config)      
    
if __name__ == '__main__':
    try:
        builder()
    except KeyboardInterrupt:
        # User interrupt the program
        exit()

# Ray Configuration Generator For IBM-Cloud Services

ibm-ray-config is a CLI tool that greatly simplifies user experience by generating Ray configuration files for IBM services.
Currently supporting only IBM Virtual Private Cloud (VPC).

## Setup

The tool has been mostly tested with Ubuntu 18.04/20.04 and Fedora 35, but should work with most Linux systems.   
Requirements: `ssh-keygen` utility installed:
```
sudo apt install openssh-client
```

Install `ibm-ray-config` from pip repository

```
pip install ibm-ray-config
```

## Usage
Use the configuration tool as follows:

```
ibm-ray-config [--iam-api-key IAM_API_KEY] [--endpoint ENDPOINT] [-i INPUT_FILE] [-o OUTPUT_PATH] [--compute-iam-endpoint IAM_ENDPOINT] [--version] 
```

Get a short description of the available flags via ```ibm-ray-config --help```

<br/>

#### Flags Detailed Description

<!--- <img width=125/> is used in the following table to create spacing --->
 |<span style="color:orange">Key|<span style="color:orange">Default|<span style="color:orange">Mandatory|<span style="color:orange">Additional info|
 |---|---|---|---|
 | iam-api-key   | |yes|IBM Cloud API key. To generate a new API Key, adhere to the following [guide](https://www.ibm.com/docs/en/spectrumvirtualizecl/8.1.3?topic=installing-creating-api-key)
 | input-file    |<compute_backend>/defaults.py| no | Existing config file to be used as a template in the configuration process |
 | output-path   |A randomly generated path to a folder | no |A custom location for the program's outputs |
 | version       | | no |Returns ibm-ray-config's package version|
 |endpoint| | no|Geographical location for deployment and scope for available resources by the IBM-VPC service. Endpoint urls are listed <a href="https://cloud.ibm.com/docs/vpc?topic=vpc-creating-a-vpc-in-a-different-region&interface=cli"> here</a>. |
 compute_iam_endpoint|https://iam.cloud.ibm.com|no|Alternative IAM endpoint url for the cloud provider, e.g. https://iam.test.cloud.ibm.com|



### Using ibm-ray-config Config Tool Programmatically
Attention: though not all fields are mandatory, unspecified resources will be created automatically on the backend.

#### IBM VPC

Mandatory fields are: `iam_api_key` and `region`.
Processor architecture: Intel x86.    

Unspecified Fields will be replaced with the following values:     
- `vpc_id` - If available a random one will be chosen.
         Otherwise (if no VPC exists) a new VPC named:ray-default-vpc-<INT> will be created and a random floating-ip will be assigned to the subnet's gateway. The process may create a new floating-ip if no unbound ip exists. 
- `ssh_key_filename` (path to private ssh-key) - A new one will be created and registered under the specified region. 
- `key_id` (ssh-key on the IBM-VPC platform) - If ssh_key_filename instead specified the public key will be generated and registered, otherwise, a new key will be created and registered.   
- `image_id` - The VMs image will be Ubuntu 20.04.
- `profile_name` - 'bx2-2x8', which equates to: 2CPUs, 8GiB RAM, 100GB storage.
- `min_workers` - 0.
- `max_workers` - 0.

Example:
```
from ibm_ray_config import generate_config

api_key = '<IAM_API_KEY>'
region = 'eu-de'
generate_config(iam_api_key=api_key, region=region, image_id='r010-5a674db7-95aa-45c5-a2f1-a6aa9d7e93ad', key_id='r010-fe6cb103-60e6-46bc-9cb5-14e415990849', ssh_key_filename='/home/kpavel/.ssh/id_rsa', profile_name='bx2-2x8', vpc_id='r010-af1adda4-e4e5-4060-9aa2-7a0c981aff8e', min_workers=1, max_workers=1)
```

Minimal example using mandatory fields:

```
from ibm_ray_config import generate_config

api_key = <IAM_API_KEY>
region = 'eu-de'
config_file = generate_config(iam_api_key=api_key, region=region)
```

### Test and Usage 
Attention: to run multiple clusters under the same VPC, make sure their cluster names (`cluster_name` in the config file) are unique.      

To deploy a Ray cluster with the configuration created, please use the <a href="https://github.com/project-codeflare/ibm-vpc-ray-connector"> ibm-vpc-ray-connector </a>. Follow the instructions via the provided link to test your configuration files. 
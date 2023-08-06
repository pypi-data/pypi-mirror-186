import logging
import sys
import time

import yaml
from satella.coding import silence_excs

logger = logging.getLogger(__name__)
from pfizer_stratus_swagger.read_template_yml import read_template


def run_from_commandline():
    if len(sys.argv) < 3:
        print('''Usage:

* pfizer-stratus-swagger <directory containing template.yaml> <directory containing functions> -o swagger.yml- generate Swagger file based on a directory
''')
        sys.exit(0)

    s = time.monotonic()
    tpl_dir = sys.argv[1]
    funcs_dir = sys.argv[2]
    o_arg = sys.argv[3]
    output_swagger = sys.argv[4]
    if o_arg != '-o':
        print('Argument must be -o')
        sys.exit(1)

    tpl = read_template(funcs_dir, tpl_dir)

    # Add ServiceLayer to PYTHONPATH
    sl_v = tpl.get_service_layer()
    sl_v.add_to_path()

    output_yaml = {'openapi': '3.0', 'paths': []}

    for sl in tpl.get_serverless_functions():
        try:
            yml = sl.to_yaml()
            output_yaml['paths'].append(yml)
            print(yml)
        except ModuleNotFoundError as e:
            logger.error('Module not found, exc_info=e')

    with open(output_swagger, 'w') as f_in:
        yaml.dump(output_yaml, f_in, Dumper=yaml.Dumper)

    took_minutes = (time.monotonic() - s) / 60
    print(f'Took {took_minutes} minutes to process {" ".join(sys.argv[1:])}')

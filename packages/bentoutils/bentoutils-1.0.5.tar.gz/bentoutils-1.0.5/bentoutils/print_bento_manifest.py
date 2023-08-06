import os
import re
import sys
import yaml


def gen_manifest(bento_tag, pod_name, download_url=None, node_selector=None, svcname=None, tolerations=None, labels=None):
    envvars = read_env_variables()
    env = [{'name': key, 'value': val} for key, val in envvars.items()]
    
    manifest = {
        'apiVersion': 'resources.yatai.ai/v1alpha1',
        'kind': 'BentoRequest',
        'metadata': {
            'name': svcname or pod_name,
            'namespace': 'yatai-builders',
        },
        'spec': {
            'bentoTag': bento_tag
        },
    }

    if download_url:  # The url to download the bento tar file. If not specified, yatai-image-builder will fetch this information from yatai.
        manifest['spec']['downloadUrl'] = download_url

    if env:
        manifest['spec']['imageBuilderExtraContainerEnv'] = env

    if labels:
        print(labels)
        manifest['metadata']['labels'] = labels
        manifest['spec']['imageBuilderExtraPodMetadata'] = {'labels': labels}
        print(manifest['spec']['imageBuilderExtraPodMetadata'])
        
    if envvars.get('GPU_ENABLED', None) == 'true':
        manifest['spec']['imageBuilderContainerResources'] = {
            'limits': {
                'nvidia.com/gpu': 1
            }
        }

    if tolerations:
        manifest['spec']['imageBuilderExtraPodSpec'] = {'tolerations': convertTolerations(tolerations)}

    if node_selector:
        if manifest['spec']['imageBuilderExtraPodSpec']:
            manifest['spec']['imageBuilderExtraPodSpec']['nodeSelector'] = node_selector
        else:
            manifest['spec']['imageBuilderExtraPodSpec'] = {'nodeSelector': node_selector}

    return yaml.dump(manifest)


def camel_to_kebab(name):
    out = re.sub(r'([a-z0-9]|(?=[A-Z]))([A-Z])', r'\1-\2', name)
    out = re.sub(r':', '-', out)
    out = out.lower()
    if out[0] == '-':
        out = out[1:]
    return out


def read_env_variables():
    envvars = {}
    if not os.path.exists('.env'):
        return envvars

    with open('.env', 'r') as f:
        for line in f:
            key, val = line.split('=')
            envvars[key] = val.strip()

    return envvars


def convertTolerations(tolerations_str):
    if tolerations_str is None:
        return []

    pairs = [[y.strip() for y in x.strip().split('=')]
             for x in tolerations_str.split(',')]
    tolerations = []
    for key, value in pairs:
        tolerations.append({
            'key': key,
            'operator': 'Equal',
            'value': value,
            'effect': 'NoSchedule',
        })
    return tolerations

def convert_labels(labels_str):
    pairs = [[y.strip() for y in x.strip().split('=')]
             for x in labels_str.split(',')]
    return {p[0]:convert_value(p[1]) for p in pairs}

def convert_value(val):
    if val == 'True':
        return True
    elif val == 'False':
        return False
    # elif val.isdigit():
    #     return int(val)
    # try:
    #     return float(val)
    # except ValueError:
    #     return val
    return val

if __name__ == '__main__':
    bento = str(sys.argv[1])
    if ':' not in bento:
        version = 'latest'
        bento = "{}:{}".format(bento, version)

    if len(sys.argv) == 7:
        download_url = str(sys.argv[2])
        node_selector = str(sys.argv[3])
        svcname = str(sys.argv[4])
        tolerations = str(sys.argv[5])
        labels = convert_labels(str(sys.argv[6])) if sys.argv[6] else None
        print(labels)
        print(gen_manifest(bento, pod_name=bento, download_url=download_url, node_selector=node_selector, svcname=svcname, tolerations=tolerations, labels=labels))

    else:
        print('Error: insufficient args')

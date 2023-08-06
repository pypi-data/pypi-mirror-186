import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='bentoutils',
    version='1.0.5',
    author='Mark Moloney',
    author_email='m4rkmo@gmail.com',
    description='Utilities for working with BentoML V1.x',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/markmo/bentoutils',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'BentoML==1.0.8',
        'boto3',
        'click',
        'kubernetes==11.0.0',
        'PyYAML',
        'stringcase',
        'text-unidecode',
    ],
    entry_points='''
        [console_scripts]
        bentopack=bentoutils.cli:pack
        bentopacks3=bentoutils.cli:pack_from_s3
        get_pod_name=bentoutils.cli:get_pod_name
        get_kaniko_manifest=bentoutils.cli:get_kaniko_manifest
        get_knative_manifest=bentoutils.cli:get_knative_manifest
        get_route_manifest=bentoutils.cli:get_route_manifest
        get_saved_path=bentoutils.cli:get_saved_path
        first_bento_with_label=bentoutils.cli:first_bento_with_label
        containerize=bentoutils.cli:containerize
        delete_containerize_job=bentoutils.cli:delete_containerize_job
        apply_bento_crd=bentoutils.cli:apply_bento_crd
        delete_bento_crd=bentoutils.cli:delete_bento_crd
        deploy_to_knative=bentoutils.cli:deploy_to_knative
    ''',
    python_requires='>=3.6',
)

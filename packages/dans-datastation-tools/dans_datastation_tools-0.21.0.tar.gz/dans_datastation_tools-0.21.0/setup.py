# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['datastation', 'datastation.scripts']

package_data = \
{'': ['*']}

install_requires = \
['dicttoxml>=1.7.4,<2.0.0',
 'lxml>=4.8.0,<5.0.0',
 'psycopg>=3.0.16,<4.0.0',
 'pyYAML>=6.0,<7.0',
 'requests>=2.26.0,<3.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['dans-bag-validate = '
                     'datastation.scripts.validate_dans_bag:main',
                     'dv-banner = datastation.scripts.dv_banner:main',
                     'dv-datacite-records-update = '
                     'datastation.scripts.update_datacite_records:main',
                     'dv-dataset-add-role-assignment = '
                     'datastation.scripts.add_role_assignments:main',
                     'dv-dataset-delete-draft = '
                     'datastation.scripts.delete_draft_datasets:main',
                     'dv-dataset-delete-role-assignment = '
                     'datastation.scripts.delete_role_assignments:main',
                     'dv-dataset-destroy = '
                     'datastation.scripts.dataset_destroy:main',
                     'dv-dataset-destroy-migration-placeholder = '
                     'datastation.scripts.dataset_destroy_migration_placeholder:main',
                     'dv-dataset-find-with-role-assignment = '
                     'datastation.scripts.find_datasets_with_roleassignment:main',
                     'dv-dataset-locks = '
                     'datastation.scripts.manage_dataset_lock:main',
                     'dv-dataset-oai-harvest = '
                     'datastation.scripts.oai_harvest:main',
                     'dv-dataset-publish = '
                     'datastation.scripts.publish_datasets:main',
                     'dv-dataset-reindex = '
                     'datastation.scripts.reindex_datasets:main',
                     'dv-dataset-replace-metadata-field-values = '
                     'datastation.scripts.replace_metadata_field_values:main',
                     'dv-dataset-retrieve-metadata = '
                     'datastation.scripts.retrieve_dataset_metadata:main',
                     'dv-dataset-retrieve-metadata-field = '
                     'datastation.scripts.retrieve_dataset_metadata_field:main',
                     'dv-dataset-verify = '
                     'datastation.scripts.verify_dataset:main',
                     'dv-dataverse-oai-harvest = '
                     'datastation.scripts.oai_harvest:main',
                     'dv-dataverse-retrieve-pids = '
                     'datastation.scripts.retrieve_dataset_pids:main',
                     'dv-file-prestage = '
                     'datastation.scripts.prestage_files:main',
                     'dv-user-import = datastation.scripts.import_user:main',
                     'ingest-flow-copy-batch-to-ingest-area = '
                     'datastation.scripts.ingest_flow_copy_batch_to_ingest_area:main',
                     'ingest-flow-list-events = '
                     'datastation.scripts.ingest_flow_list_events:main',
                     'ingest-flow-move-batch-to-ingest-area = '
                     'datastation.scripts.ingest_flow_move_batch_to_ingest_area:main',
                     'ingest-flow-progress-report = '
                     'datastation.scripts.ingest_flow_progress_report:main',
                     'ingest-flow-start-import = '
                     'datastation.scripts.ingest_flow_start_import:main',
                     'ingest-flow-start-migration = '
                     'datastation.scripts.ingest_flow_start_migration:main']}

setup_kwargs = {
    'name': 'dans-datastation-tools',
    'version': '0.21.0',
    'description': 'Command line utilities for Data Station application management',
    'long_description': 'None',
    'author': 'DANS-KNAW',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)

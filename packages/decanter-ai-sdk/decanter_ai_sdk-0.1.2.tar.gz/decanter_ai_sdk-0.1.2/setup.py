# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['decanter_ai_sdk', 'decanter_ai_sdk.enums', 'decanter_ai_sdk.web_api']

package_data = \
{'': ['*'], 'decanter_ai_sdk.web_api': ['data/*']}

install_requires = \
['black>=22.6.0,<23.0.0',
 'pandas>=1.4.3,<2.0.0',
 'poethepoet>=0.16.0,<0.17.0',
 'pydantic>=1.9.2,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'decanter-ai-sdk',
    'version': '0.1.2',
    'description': 'Decanter AI is a powerful AutoML tool which enables everyone to build ML models and make predictions without data science background. With Decanter AI SDK, you can integrate Decanter AI into your application more easily with Python.',
    'long_description': '[![Coverage Status](https://coveralls.io/repos/github/MoBagel/decanter-ai-sdk/badge.svg?branch=coveralls)](https://coveralls.io/github/MoBagel/decanter-ai-sdk?branch=coveralls)\n[![tests](https://github.com/MoBagel/decanter-ai-sdk/workflows/main/badge.svg)](https://github.com/MoBagel/decanter-ai-sdk)\n[![PyPI version](https://badge.fury.io/py/decanter-ai-sdk.svg)](https://badge.fury.io/py/decanter-ai-sdk)\n# Mobagel decanter ai sdk\n\nDecanter AI is a powerful AutoML tool which enables everyone to build ML models and make predictions without data science background. With Decanter AI SDK, you can integrate Decanter AI into your application more easily with Python.\n\nIt supports actions such as data uploading, model training, and prediction to run in a more efficient way and access results more easily.\n\nTo know more about Decanter AI and how you can be benefited with AutoML, visit [MoBagel website](https://mobagel.com/tw/) and contact us to try it out!\n\n## How it works\n\n- Upload train and test files in both csv and pandas dataframe.\n- Setup different standards and conduct customized experiments on uploaded data.\n- Use different models to run predictions\n- Get predict data in pandas dataframe form.\n\n## Requirements\n\n- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)\n- [poetry](https://python-poetry.org/)\n\n## Usage\n\n### Installation\n\n`pip install decanter-ai-sdk`\n### Constructor\nTo use this sdk, you must first construct a client object.\n```python\nfrom decanter_ai_sdk.client import Client\n    client = Client(\n        auth_key="auth_API_key",\n        project_id="project_id",\n        host="host_url",\n    )\n```\n\n### Upload\nAfter the client is constructed, now you can use it to upload your training and testing files in both csv and pandas dataframe. This function will return uploaded data id in Decanter server.\n```python\nimport os\nsys.path.append("..")\n\ncurrent_path = os.path.dirname(os.path.abspath(__file__))\ntrain_file_path = os.path.join(current_path, "ts_train.csv")\ntrain_file = open(train_file_path, "rb")\ntrain_id = client.upload(train_file, "train_file")\n```\n\n### Experiment\nTo conduct an experiment, you need to first specify which type of data you are going to use , i.e., iid or ts, then you can input parameters by following our pyhint to customize your experiment.\nAfter the experiment, the function will return an object which you can get experiment attributes from it.\n```python\n# Training iid data\nexperiment = client.train_iid(\n    experiment_name=exp_name,\n    experiment_table_id=train_id,\n    target="Survived",\n    evaluator=ClassificationMetric.AUC,\n    custom_feature_types={\n        "Pclass": DataType.categorical,\n        "Parch": DataType.categorical,\n    },\n)\n```\n\n```python\n# Training ts data\nexperiment = client.train_ts(\n    experiment_name=exp_name,\n    experiment_table_id=train_id,\n    target="Passengers",\n    datetime="Month",\n    time_groups=[],\n    timeunit=TimeUnit.month,\n    groupby_method="sum",\n    max_model=5,\n    evaluator=RegressionMetric.MAPE,\n    custom_feature_types={"Pclass": DataType.numerical},\n)\n```\nTo get its attributes, you can either extract them by simply using dot or its functions.\n```python\n# Experiment object usage\nbest_model = experiment.get_best_model()\nmodel_list = experiment.get_model_list()\nbest_auc_model = experiment.get_best_model_by_metric(ClassificationMetric.AUC)\n```\n### Prediction\nNow you can use model data to run prediction.\n```python\n# Predicting iid data\npredict = client.predict_iid(\n    keep_columns=[], \n    non_negative=False, \n    test_table_id=test_id, \n    model=best_model\n)\n```\n\n```python\n# Predicting ts data\npredict = client.predict_ts(\n    keep_columns=[], \n    non_negative=False, \n    test_table_id=test_id, \n    model=best_model\n)\n```\nTo get prediction result, do\n```python\npredict_data = predict.get_predict_df()\n```\n## Development\n\n### Installing poetry\n\n1. `pip install poetry poethepoet`\n2. `poetry install` #Project setup.\n3. `poetry shell` #Start your project in poetry env.\n\nNow you can create your own branch to start developing new feature.\n\n### Testing\nTo run test, do:\n```\npoe test\n```\n\n### Lint and format\nTo lint, do:\n```\npoe lint\n```\n\nTo reformat, do:\n```\npoe format\n```\n\n## Releasing\n#TODO\n\n## Enums\n#TODO\n\n## License\n#TODO\n\n## TODO\n#TODO\n\n\n\n',
    'author': 'chaokuanlin',
    'author_email': 'can@mobagel.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MoBagel/decanter-ai-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

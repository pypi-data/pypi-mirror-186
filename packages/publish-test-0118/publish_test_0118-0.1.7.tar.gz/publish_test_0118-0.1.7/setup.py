# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['publish_test_0118', 'publish_test_0118.dynbatch', 'publish_test_0118.rlog']

package_data = \
{'': ['*']}

install_requires = \
['azure-eventhub>=5.10.1,<6.0.0',
 'azure-identity>=1.7.0,<2.0.0',
 'dataclasses-json>=0.5.7,<0.6.0',
 'typeguard>=2.13.3,<3.0.0']

setup_kwargs = {
    'name': 'publish-test-0118',
    'version': '0.1.7',
    'description': '',
    'long_description': '# pyraisdk\n\nAML models are meant to be deployed to GPU instances to provide inference service. If the code that operates the model uses the GPU for inferencing in each request separately,\nthe overall performance of the model will be quite inefficent. This SDK has APIs that can allocate batches of inference requests to run on the GPU in a separate thread, thereby considerably\nimproving the usage efficiency of GPU and making the model more performant. \n\nThe SDK also collects telemetry data for each so the performance of the model can be evaluated and tracked and provides logging primitives that can be used\nto produce additional troubleshooting information.\n\n## Dynamic Batching Support\n\nThere are APIs you **must** implement in your model to support batching of inference requests for best model performance. Those APIs allow the SDK\nto distribute load efficiently to the GPU instances. The APIs are:\n\n* ```preprocess``` Modifies the input to the model, if necessary. For example, if your model needs the input in a special JSON format instead of as a list\nof strings, you can do that modification in the *preprocess* method.\n* ```predict``` Executes the model inference for a list of input strings\n\n### Usage Examples\n\nBuild `YourModel` class inherited from `pyraisdk.dynbatch.BaseModel`.\n\n```python\nfrom typing import List\nfrom pyraisdk.dynbatch import BaseModel\n\nclass YourModel(BaseModel):\n    def predict(self, items: List[str]) -> List[int]:\n        rs = []\n        for item in items:\n            rs.append(len(item))\n        return rs\n            \n    def preprocess(self, items: List[str]) -> List[str]:\n        rs = []\n        for item in items:\n            rs.append(f\'[{item}]\')\n        return rs\n```\n\nInitialize a `pyraisdk.dynbatch.DynamicBatchModel` with `YourModel` instance, and call `predict / predict_one` for inferencing.\n\n```python\nfrom pyraisdk.dynbatch import DynamicBatchModel\n\n# prepare model\nsimple_model = YourModel()\nbatch_model = DynamicBatchModel(simple_model)\n\n# predict\nitems = [\'abc\', \'123456\', \'xyzcccffaffaaa\']\npredictions = batch_model.predict(items)\nassert predictions == [5, 8, 16]\n\n# predict_one\nitem = \'abc\'\nprediction = batch_model.predict_one(item)\nassert prediction == 5\n```\n\nConcurrent requests to `predict / predict_one`, in different threads.\n\n```python\nfrom threading import Thread\nfrom pyraisdk.dynbatch import DynamicBatchModel\n\n# prepare model\nsimple_model = YourModel()\nbatch_model = DynamicBatchModel(simple_model)\n\n# thread run function\ndef run(name, num):\n    for step in range(num):\n        item = f\'{name}-{step}\'\n        prediction = batch_model.predict_one(item)\n        assert prediction == len(item) + 2\n\n# start concurrent inference\nthreads = [Thread(target=run, args=(f\'{tid}\', 100)) for tid in range(20)]\nfor t in threads:\n    t.start()\nfor t in threads:\n    t.join()\n```\n\n## Loging & Events\n\n### Description\nThis module is for logging and event tracing.\n\n### interface\n\n```python\ndef initialize(\n    eh_hostname: Optional[str] = None,\n    client_id: Optional[str] = None,\n    eh_conn_str: Optional[str] = None,\n    eh_structured: Optional[str] = None,\n    eh_unstructured: Optional[str] = None,\n    role: Optional[str] = None,\n    instance: Optional[str] = None,\n)\n```\n\nParameter description for `initialize`:\n- **eh_hostname**: Fully Qualified Namespace aka EH Endpoint URL (*.servicebus.windows.net). Default, read $EVENTHUB_NAMESPACE\n- **client_id**: client_id of service principal. Default, read $UAI_CLIENT_ID\n- **eh_conn_str**: connection string of eventhub namespace. Default, read $EVENTHUB_CONN_STRING\n- **eh_structured**: structured eventhub name. Default, read $EVENTHUB_AUX_STRUCTURED\n- **eh_unstructured**: unstructured eventhub name. Default, read $EVENTHUB_AUX_UNSTRUCTURED\n- **role**: role, Default: RemoteModel_${ENDPOINT_NAME}\n- **instance**: instance, Default: "${ENDPOINT_VERSION}|{os.uname()[1]}" or "${ENDPOINT_VERSION}|{_probably_unique_id()}"\n\n```python\ndef event(self, key: str, code: str, numeric: float, detail: str=\'\', corr_id: str=\'\', elem: int=-1)\ndef infof(self, format: str, *args: Any)\ndef infocf(self, corr_id: str, elem: int, format: str, *args: Any)\ndef warnf(self, format: str, *args: Any)\ndef warncf(self, corr_id: str, elem: int, format: str, *args: Any)\ndef errorf(self, format: str, *args: Any)\ndef errorcf(self, corr_id: str, elem: int, ex: Optional[Exception], format: str, *args: Any)\ndef fatalf(self, format: str, *args: Any)\ndef fatalcf(self, corr_id: str, elem: int, ex: Optional[Exception], format: str, *args: Any)\n```\n\n### examples\n\n```python\n# export EVENTHUB_AUX_UNSTRUCTURED=\'ehunstruct\'\n# export EVENTHUB_AUX_STRUCTURED=\'ehstruct\'\n# export UAI_CLIENT_ID=\'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\'\n# export EVENTHUB_NAMESPACE=\'xxx.servicebus.windows.net\'\n\nfrom pyraisdk import rlog\nrlog.initialize()\n\nrlog.infof(\'this is a info message %s\', 123)\nrlog.event(\'LifetimeEvent\', \'STOP_GRACEFUL_SIGNAL\', 0, \'detail info\')\n```\n\n```python\n# export EVENTHUB_AUX_UNSTRUCTURED=\'ehunstruct\'\n# export EVENTHUB_AUX_STRUCTURED=\'ehstruct\'\n# export EVENTHUB_CONN_STRING=\'<connection string>\'\n\nfrom pyraisdk import rlog\nrlog.initialize()\n\nrlog.infocf(\'corrid\', -1, \'this is a info message: %s\', 123)\nrlog.event(\'RequestDuration\', \'200\', 0.01, \'this is duration in seconds\')\n```\n\n```python\nfrom pyraisdk import rlog\nrlog.initialize(eh_structured=\'ehstruct\', eh_unstructured=\'ehunstruct\', eh_conn_str=\'<eventhub-conn-str>\')\n\nrlog.errorcf(\'corrid\', -1, Exception(\'error msg\'), \'error message: %s %s\', 1,2)\nrlog.event(\'CpuUsage\', \'\', 0.314, detail=\'cpu usage\', corr_id=\'corrid\', elem=-1)\n```',
    'author': 'Xiaodong Yang',
    'author_email': 'xiaoyan@microsoft.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

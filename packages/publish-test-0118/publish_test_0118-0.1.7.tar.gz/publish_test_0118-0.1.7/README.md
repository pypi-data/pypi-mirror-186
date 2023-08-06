# pyraisdk

AML models are meant to be deployed to GPU instances to provide inference service. If the code that operates the model uses the GPU for inferencing in each request separately,
the overall performance of the model will be quite inefficent. This SDK has APIs that can allocate batches of inference requests to run on the GPU in a separate thread, thereby considerably
improving the usage efficiency of GPU and making the model more performant. 

The SDK also collects telemetry data for each so the performance of the model can be evaluated and tracked and provides logging primitives that can be used
to produce additional troubleshooting information.

## Dynamic Batching Support

There are APIs you **must** implement in your model to support batching of inference requests for best model performance. Those APIs allow the SDK
to distribute load efficiently to the GPU instances. The APIs are:

* ```preprocess``` Modifies the input to the model, if necessary. For example, if your model needs the input in a special JSON format instead of as a list
of strings, you can do that modification in the *preprocess* method.
* ```predict``` Executes the model inference for a list of input strings

### Usage Examples

Build `YourModel` class inherited from `pyraisdk.dynbatch.BaseModel`.

```python
from typing import List
from pyraisdk.dynbatch import BaseModel

class YourModel(BaseModel):
    def predict(self, items: List[str]) -> List[int]:
        rs = []
        for item in items:
            rs.append(len(item))
        return rs
            
    def preprocess(self, items: List[str]) -> List[str]:
        rs = []
        for item in items:
            rs.append(f'[{item}]')
        return rs
```

Initialize a `pyraisdk.dynbatch.DynamicBatchModel` with `YourModel` instance, and call `predict / predict_one` for inferencing.

```python
from pyraisdk.dynbatch import DynamicBatchModel

# prepare model
simple_model = YourModel()
batch_model = DynamicBatchModel(simple_model)

# predict
items = ['abc', '123456', 'xyzcccffaffaaa']
predictions = batch_model.predict(items)
assert predictions == [5, 8, 16]

# predict_one
item = 'abc'
prediction = batch_model.predict_one(item)
assert prediction == 5
```

Concurrent requests to `predict / predict_one`, in different threads.

```python
from threading import Thread
from pyraisdk.dynbatch import DynamicBatchModel

# prepare model
simple_model = YourModel()
batch_model = DynamicBatchModel(simple_model)

# thread run function
def run(name, num):
    for step in range(num):
        item = f'{name}-{step}'
        prediction = batch_model.predict_one(item)
        assert prediction == len(item) + 2

# start concurrent inference
threads = [Thread(target=run, args=(f'{tid}', 100)) for tid in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Loging & Events

### Description
This module is for logging and event tracing.

### interface

```python
def initialize(
    eh_hostname: Optional[str] = None,
    client_id: Optional[str] = None,
    eh_conn_str: Optional[str] = None,
    eh_structured: Optional[str] = None,
    eh_unstructured: Optional[str] = None,
    role: Optional[str] = None,
    instance: Optional[str] = None,
)
```

Parameter description for `initialize`:
- **eh_hostname**: Fully Qualified Namespace aka EH Endpoint URL (*.servicebus.windows.net). Default, read $EVENTHUB_NAMESPACE
- **client_id**: client_id of service principal. Default, read $UAI_CLIENT_ID
- **eh_conn_str**: connection string of eventhub namespace. Default, read $EVENTHUB_CONN_STRING
- **eh_structured**: structured eventhub name. Default, read $EVENTHUB_AUX_STRUCTURED
- **eh_unstructured**: unstructured eventhub name. Default, read $EVENTHUB_AUX_UNSTRUCTURED
- **role**: role, Default: RemoteModel_${ENDPOINT_NAME}
- **instance**: instance, Default: "${ENDPOINT_VERSION}|{os.uname()[1]}" or "${ENDPOINT_VERSION}|{_probably_unique_id()}"

```python
def event(self, key: str, code: str, numeric: float, detail: str='', corr_id: str='', elem: int=-1)
def infof(self, format: str, *args: Any)
def infocf(self, corr_id: str, elem: int, format: str, *args: Any)
def warnf(self, format: str, *args: Any)
def warncf(self, corr_id: str, elem: int, format: str, *args: Any)
def errorf(self, format: str, *args: Any)
def errorcf(self, corr_id: str, elem: int, ex: Optional[Exception], format: str, *args: Any)
def fatalf(self, format: str, *args: Any)
def fatalcf(self, corr_id: str, elem: int, ex: Optional[Exception], format: str, *args: Any)
```

### examples

```python
# export EVENTHUB_AUX_UNSTRUCTURED='ehunstruct'
# export EVENTHUB_AUX_STRUCTURED='ehstruct'
# export UAI_CLIENT_ID='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
# export EVENTHUB_NAMESPACE='xxx.servicebus.windows.net'

from pyraisdk import rlog
rlog.initialize()

rlog.infof('this is a info message %s', 123)
rlog.event('LifetimeEvent', 'STOP_GRACEFUL_SIGNAL', 0, 'detail info')
```

```python
# export EVENTHUB_AUX_UNSTRUCTURED='ehunstruct'
# export EVENTHUB_AUX_STRUCTURED='ehstruct'
# export EVENTHUB_CONN_STRING='<connection string>'

from pyraisdk import rlog
rlog.initialize()

rlog.infocf('corrid', -1, 'this is a info message: %s', 123)
rlog.event('RequestDuration', '200', 0.01, 'this is duration in seconds')
```

```python
from pyraisdk import rlog
rlog.initialize(eh_structured='ehstruct', eh_unstructured='ehunstruct', eh_conn_str='<eventhub-conn-str>')

rlog.errorcf('corrid', -1, Exception('error msg'), 'error message: %s %s', 1,2)
rlog.event('CpuUsage', '', 0.314, detail='cpu usage', corr_id='corrid', elem=-1)
```
import os
import threading
from typing import Optional
import uuid

from typeguard import typechecked
from azure.identity import ManagedIdentityCredential

from .eventhub import EventHubSink
from .log import EventLogger
from .logimp import AsyncEventLogger, StdoutSink

__all__ = [
    "infof", 
    "infocf", 
    "warnf", 
    "warncf", 
    "errorf", 
    "errorcf", 
    "fatalf",
    "fatalcf",
    "event",
    "initialize",
]

# create logger
_logger: EventLogger = AsyncEventLogger()


# logger interface
infof = _logger.infof
infocf = _logger.infocf
warnf = _logger.warnf
warncf = _logger.warncf
errorf = _logger.errorf
errorcf = _logger.errorcf
fatalf = _logger.fatalf
fatalcf = _logger.fatalcf
event = _logger.event


# logger init
_logger_init_lock = threading.Lock()
_logger_initialized = False

@typechecked
def initialize(
    eh_hostname: Optional[str] = None,
    client_id: Optional[str] = None,
    eh_conn_str: Optional[str] = None,
    eh_structured: Optional[str] = None,
    eh_unstructured: Optional[str] = None,
    role: Optional[str] = None,
    instance: Optional[str] = None,
):
        '''
        Args:
            eh_hostname: Fully Qualified Namespace aka EH Endpoint URL (*.servicebus.windows.net). Default, read $EVENTHUB_NAMESPACE
            client_id: client_id of service principal. Default, read $UAI_CLIENT_ID
            eh_conn_str: connection string of eventhub namespace. Default, read $EVENTHUB_CONN_STRING
            eh_structured: structured eventhub name. Default, read $EVENTHUB_AUX_STRUCTURED
            eh_unstructured: unstructured eventhub name. Default, read $EVENTHUB_AUX_UNSTRUCTURED
            role: role, Default: RemoteModel_${ENDPOINT_NAME}
            instance: instance, Default: "${ENDPOINT_VERSION}|{os.uname()[1]}" or "${ENDPOINT_VERSION}|{_probably_unique_id()}"
        
        Note: 
            1. either (eh_hostname, client_id, eh_structured or eh_unstructured) 
               or (eh_conn_str, eh_structured or eh_unstructured) is provided, 
               event hub sink will be added
        '''
        global _logger_initialized
        with _logger_init_lock:
            # skip
            if _logger_initialized:
                return
        
            # set default value
            if eh_hostname is None:
                eh_hostname = os.getenv('EVENTHUB_NAMESPACE')
            if client_id is None:
                client_id = os.getenv('UAI_CLIENT_ID')
            if eh_conn_str is None:
                eh_conn_str = os.getenv('EVENTHUB_CONN_STRING')
            if eh_structured is None:
                eh_structured = os.getenv('EVENTHUB_AUX_STRUCTURED')
            if eh_unstructured is None:
                eh_unstructured = os.getenv('EVENTHUB_AUX_UNSTRUCTURED')
            if role is None:
                endpoint_name = os.getenv('ENDPOINT_NAME', 'unknown')
                role = f'RemoteModel_{endpoint_name}'
            if instance is None:
                endpoint_version = os.getenv('ENDPOINT_VERSION', 'unknown')
                instance = f'{endpoint_version}|{os.uname()[1]}'
                if len(instance) > 60:
                    instance = f'{endpoint_version}|{_probably_unique_id()}'
            
            # set variables
            _logger.role = role
            _logger.instance = instance
            
            # event hub sink
            if eh_conn_str:
                if eh_structured:
                    structured_sink = EventHubSink(conn_str=eh_conn_str, name=eh_structured)
                    _logger.add_sink_structured(structured_sink)
                if eh_unstructured:
                    unstructured_sink = EventHubSink(conn_str=eh_conn_str, name=eh_unstructured)
                    _logger.add_sink_unstructured(unstructured_sink)
                
            elif eh_hostname and client_id:
                credential = ManagedIdentityCredential(client_id=client_id)
                if eh_structured:
                    structured_sink = EventHubSink(hostname=eh_hostname, credential=credential, name=eh_structured)
                    _logger.add_sink_structured(structured_sink)
                if eh_unstructured:
                    unstructured_sink = EventHubSink(hostname=eh_hostname, credential=credential, name=eh_unstructured)
                    _logger.add_sink_unstructured(unstructured_sink)
                
            else:
                print('WARNING: logger eventhub sink is disabled')
        
            # stdout sink
            _logger.add_sink_structured(StdoutSink())
            _logger.add_sink_unstructured(StdoutSink())

            # start
            _logger.start()
            _logger_initialized = True
        
                
def _probably_unique_id() -> str:
	u = str(uuid.uuid4())
	return "%s-%s%s" % (u[0:5], u[5:8], u[9:11])

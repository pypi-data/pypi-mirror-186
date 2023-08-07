# audit_logging_pepsico

Under construction! Can be Used to write logs in pepsico format.
More Functions will come soon. 

Developed by Jatin Talati

## Examples of How To Use

For plain Logging into Log files
```python
from audit_logging_pepsico.audit_config import Logger

logger = Logger("<Service_Name")
logger.info("Info Message")
logger.error("Error Message")
logger.debug("Debug Message")

# Other Code
```

For Audit Logging into log files
```python
from audit_logging_pepsico.audit_config import AuditLog, Logger

logger = Logger("<Service_Name")
auditlog = AuditLog(logger)

auditlog.audit_log()

# Other Code
```

For Audit Logging into blob
```python
from audit_logging_pepsico.audit_config import AuditLog, Logger

logger = Logger("<Service_Name")
auditlog = AuditLog()
client = auditlog.get_block_blob_client("Connection_String", "Container_Name", "Logs_Blob_name")
auditlog.audit_log(logger, write_to_blob=True, client)

# Other Code
```

Explore the AuditLog class to use other parameters. 

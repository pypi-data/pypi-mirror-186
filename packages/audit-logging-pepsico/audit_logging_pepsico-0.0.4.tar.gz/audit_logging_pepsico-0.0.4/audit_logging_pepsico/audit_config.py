import os
import logging
import traceback
from audit_logging_pepsico.audit import Audit
import audit_logging_pepsico.constants as con
import uuid
from datetime import datetime
from urllib.request import urlopen
import re as r
from azure.storage.blob import BlobServiceClient

class Logger(object):

    service_name = ""

    def __init__(self, name):
        name = name.replace('.log', '')
        logger = logging.getLogger('log_namespace.%s' % name)
        logger.setLevel(logging.DEBUG)
        self.service_name = name
        if not logger.handlers:
            file_name = os.path.join('%s.log' % name)
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger


class AuditLog:
    def get_block_blob_client(self, blobConnStr=None, containerName=None, logs_blob_name=None):
        try:
            blob_service_client = BlobServiceClient.from_connection_string(conn_str=blobConnStr)
            container_client = blob_service_client.get_container_client(containerName)
            block_blob_client = container_client.get_blob_client(logs_blob_name)
            return block_blob_client
        except:
            traceback.print_exc()
            return str(traceback.format_exc())

    def get_ip_address(self):
        d = str(urlopen('http://checkip.dyndns.com/').read())
        ip_addr = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        return ip_addr

    def audit_log(self, logger, channelId=None, systemId=None, customerId=None,
                  userId=None, url=None, operationName=None, orderId=None, coRelationId=None,
                  sourceOrderNumber=None, externalId=None, requestHeader=None, responseCode=None, documentType=None,
                  componentName=None, methodName=None, requestInput=None, responseOutput=None, gpid=None, route=None,
                  write_to_blob=False, block_blob_client=None):
        try:
            ip_addr = self.get_ip_address()
            id = con.AUDIT_PRIFIX + con.ID_DELIMITER + str(uuid.uuid4())
            createdDate = datetime.now()
            interfaceName = con.INTERFACE_NAME
            type = con.AUDIT_SERVICE
            audit_obj = Audit(id, channelId, systemId, ip_addr,
                              userId, customerId, createdDate, url, interfaceName, operationName, orderId,
                              coRelationId, sourceOrderNumber,
                              externalId, requestHeader, responseCode, type, documentType, componentName,
                              methodName, requestInput, responseOutput, gpid, route)
            logs = audit_obj.__str__()
            if not write_to_blob:
                logger.debug(logs)
            else:
                block_blob_client.append_block(logs, length=len(logs))
        except:
            logger.error("----------ERROR----------")
            logger.error(str(traceback.format_exc()))


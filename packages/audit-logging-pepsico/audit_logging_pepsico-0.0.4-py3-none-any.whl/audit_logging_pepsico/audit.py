import audit_logging_pepsico.constants as con
class Audit:
    serialVersionUID = 1

    def __init__(self, id, channelId, systemId, ipAddress, userId, customerId, createdDate, url, interfaceName,
                 operationName, orderId, coRelationId, sourceOrderNumber, externalId, requestHeader, responseCode, type,
                 documentType, componentName, methodName, requestInput, responseOutput, gpid, route):

        self.prefix = con.PREFIX
        self.id = id
        self.channelId = channelId
        self.systemId = systemId
        self.ipAddress = ipAddress
        self.userId = userId
        self.customerId = customerId
        self.createdDate = createdDate
        self.url = url
        self.interfaceName = interfaceName
        self.operationName = operationName
        self.orderId = orderId
        self.coRelationId = coRelationId
        self.sourceOrderNumber = sourceOrderNumber
        self.externalId = externalId
        self.requestHeader = requestHeader
        self.responseCode = responseCode
        self.type = type
        self.documentType = documentType
        self.componentName = componentName
        self.methodName = methodName
        self.requestInput = requestInput
        self.responseOutput = responseOutput
        self.gpid = gpid
        self.route = route

    def equals(self, value):
        return self == value

    def hashCode(self):
        return 31

    def __str__(self):
        return "Audit{" + \
            "prefix='" + str(self.prefix) + '\'' + \
            ", id='" + str(self.id) + '\'' + \
            ", channelId='" + str(self.channelId) + '\'' + \
            ", systemId='" + str(self.systemId) + '\'' + \
            ", ipAddress='" + str(self.ipAddress) + '\'' + \
            ", userId='" + str(self.userId) + '\'' + \
            ", customerId='" + str(self.customerId) + '\'' + \
            ", createdDate=" + str(self.createdDate) + \
            ", url='" + str(self.url) + '\'' + \
            ", interfaceName='" + str(self.interfaceName) + '\'' + \
            ", operationName='" + str(self.operationName) + '\'' + \
            ", orderId='" + str(self.orderId) + '\'' + \
            ", coRelationId='" + str(self.coRelationId) + '\'' + \
            ", sourceOrderNumber='" + str(self.sourceOrderNumber) + '\'' + \
            ", externalId='" + str(self.externalId) + '\'' + \
            ", requestHeader='" + str(self.requestHeader) + '\'' + \
            ", responseCode=" + str(self.responseCode) + \
            ", type='" + str(self.type) + '\'' + \
            ", documentType='" + str(self.documentType) + '\'' + \
            ", componentName='" + str(self.componentName) + '\'' + \
            ", methodName='" + str(self.methodName) + '\'' + \
            ", requestInput=" + str(self.requestInput) + \
            ", responseOutput=" + str(self.responseOutput) + \
            ", gpid='" + str(self.gpid) + '\'' + \
            ", route='" + str(self.route) + '\'' + \
            '}'

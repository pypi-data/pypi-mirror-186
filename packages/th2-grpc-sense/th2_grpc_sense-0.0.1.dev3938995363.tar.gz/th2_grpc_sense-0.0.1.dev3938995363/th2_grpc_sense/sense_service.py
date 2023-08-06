from . import sense_pb2_grpc as importStub

class SenseService(object):

    def __init__(self, router):
        self.connector = router.get_connection(SenseService, importStub.SenseStub)

    def NotifyOnEvents(self, request, timeout=None, properties=None):
        return self.connector.create_request('NotifyOnEvents', request, timeout, properties)

    def AwaitNotificationOnEvents(self, request, timeout=None, properties=None):
        return self.connector.create_request('AwaitNotificationOnEvents', request, timeout, properties)

    def RegisterProcessor(self, request, timeout=None, properties=None):
        return self.connector.create_request('RegisterProcessor', request, timeout, properties)

    def UnregisterProcessor(self, request, timeout=None, properties=None):
        return self.connector.create_request('UnregisterProcessor', request, timeout, properties)
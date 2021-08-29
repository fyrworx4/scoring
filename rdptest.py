from rdpy.protocol.rdp import rdp

class MyRDPFactory(rdp.ClientFactory):

    def clientConnectionLost(self, connector, reason):
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def buildObserver(self, controller, addr):

        class MyObserver(rdp.RDPClientObserver):

            def onReady(self):
                """
                @summary: Call when stack is ready
                """
                #send 'r' key
                self._controller.sendKeyEventUnicode(ord(unicode("r".toUtf8(), encoding="UTF-8")), True)
                #mouse move and click at pixel 200x200
                self._controller.sendPointerEvent(200, 200, 1, True)

        return MyObserver(controller)

from twisted.internet import reactor
reactor.connectTCP("10.100.10.145", 3389, MyRDPFactory())
reactor.run()
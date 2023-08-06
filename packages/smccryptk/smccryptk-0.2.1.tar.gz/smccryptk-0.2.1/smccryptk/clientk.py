# Clientk
import http.client
import time
from .cryptk import Cryptk


class Clientk():
    def __init__(self) -> None:
        """ Initialize client to request and communicate with SMC coordinator """
        self.ck = Cryptk()
        self.coordinator_node = None
    
    def request_analysis(self, coordinator_node):
        """ Sends a request to start an analysis operation to the given coordinator address node.
            Returns (response-code, response-msg) tuple from coordinator node. Raises exception on error. """
        self.coordinator_node = coordinator_node
        pub_key = Cryptk.key2string(self.ck.get_public_key())

        # Send start analysis request to the coordinator node.
        # If the node is not coordinator then the request is dropped.
        # Sends its public key as the result will be encrypted 
        conn = http.client.HTTPConnection(self.coordinator_node, timeout=60)
        conn.request("GET", "/start_analysis", body=pub_key)
        resp = conn.getresponse()
        conn.close()
        content = resp.read().decode()
        return (resp.status, content)
        
    
    def get_result(self, tries=100, ms=50):
        """ Sends http request to coordinator node for the result of a requestes analysis operation.
            Returns the result (if received) (response-code, response-msg) tuple, otherwise if not received, returns from last message sent.
            Raises exception on error.
            Params:
                @tries  : Max number of get-requests sent until result is ready
                @ms     : Sleep in ms between each request try. """

        if self.coordinator_node == None:
            raise Exception("No SMC request has been sent to coordinator")
        if tries <= 0 or ms < 0:
            raise Exception("Invalid arguments tries=%d, ms=%d given" % (tries, ms))

        pub_key = Cryptk.key2string(self.ck.get_public_key())
        response_code = 0
        response_msg = "No response"

        # Request for the result from the coordinator. Asks every second until it receives the result.
        for i in range(0, tries):
            conn = http.client.HTTPConnection(self.coordinator_node, timeout=60)
            conn.request("GET", "/get_result", body=pub_key)
            resp = conn.getresponse()
            conn.close()
            response_code = resp.status
            response_msg = resp.read().decode()
            if response_code == 200:
                break
            
            time.sleep(0.001*ms)
        
        return (response_code, response_msg)

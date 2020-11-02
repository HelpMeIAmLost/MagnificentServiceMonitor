#! /usr/bin/env python
from urllib2 import urlopen
from socket import socket
from sys import argv
import time
import datetime
import platform
import os
import subprocess

class Test_Application(object):
    def __init__(self, service, server, interval):
        self.service = service
        self.server = server
        
        self.interval = interval

    def run(self):
        service = self.service.upper()
        server = self.server
        interval = self.interval
        fail_counter = 0
        
        logfile = open('server.log', 'a+')
        
        try:
            while True:
                timestamp = time.time()
                timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M:%S')

                server_status = self.server_test(service, server)
                if server_status:
                    logfile.write(timestamp + ': Magnificent up and running\n')
                    print('%s: Magnificent up and running' % (timestamp))
                else:
                    logfile.write(timestamp + ': Magnificent has not responded\n')
                    print('%s: Magnificent has not responded' % (timestamp))
                    fail_counter += 1
                    five_minutes = int(60 / interval)
                    if fail_counter >= five_minutes:
                        os_platform = platform.system()
                        args = []
                        title = "Magnificent Service Monitor"
                        message = "The Magnificent service has stopped responding!"

                        if os_platform == 'Darwin':
                            args.append('osascript')
                            args.append('-e')
                            args.append('display notification "%s" with title "%s"' % (message, title))
                            subprocess.call(args)
                        elif os_platform == 'Linux':
                            args.append('notify-send')
                            args.append('"%s" "%s"' % (message, title))
                            subprocess.call(args)
                        fail_counter = 0

        	time.sleep(interval)
        except KeyboardInterrupt:
            print('Application terminated!')

        logfile.close()

    def tcp_test(self, server_info):
        separator = server_info.find(':')
        try:
            sock = socket()
            sock.connect((server_info[:separator], int(server_info[separator+1:])))
            sock.close
            return True
        except:
            return False

    def http_test(self, server_info):
        try:
            data = urlopen(server_info).read()
            return True
        except:
            return False

    def server_test(self, test_type, server_info):
        if test_type.lower() == 'tcp':
            return self.tcp_test(server_info)
        elif test_type.lower() == 'http':
            return self.http_test(server_info)

if __name__ == '__main__':
    if len(argv) < 3:
        print('Usage: ./service_monitor.py service server administrator-email [interval]')
    else:
        if len(argv) < 5:
            if len(argv) == 3:
                interval = 10
            else:
                interval = float(argv[3])
                            
            service_app = Test_Application(argv[1], argv[2], interval)
            service_app.run()
        else:
            print('Usage: ./service_monitor.py service server administrator-email [interval]')

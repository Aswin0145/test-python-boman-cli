import os

cmd = "docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable touch /zap/wrk/test.txt"


cmd2 = "docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t https://demo.testfire.net/ -g gen.conf -J full_scan_02.json"

os.system(cmd2)
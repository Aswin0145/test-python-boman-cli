import os

cmd = "docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable touch /zap/wrk/test.txt"


bind_folder = '/zap/wrk/'
url = 'https://demo.testfire.net/'
file_name = 'boman_baseline.json'


cmd2 = "docker run -v $(pwd):{bind}:rw -t owasp/zap2docker-stable zap-baseline.py -t {url} -g gen.conf -J {file}"

final_command = "% s" % cmd2.format(url = url, bind = bind_folder, file = file_name)

##print(final_command);

os.system(cmd2)
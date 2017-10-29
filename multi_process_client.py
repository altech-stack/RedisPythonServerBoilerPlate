import urllib2
import json
from time import sleep

response = urllib2.urlopen('http://localhost:5000/api/do_work')
response_json = response.read()

response_json = json.loads(response_json)

job_id = response_json['result'].get('job_id')

wait_time = 60
while (wait_time > 0):
	check_job = urllib2.urlopen('http://localhost:5000/api/job_status/{}'.format(job_id))
	check_job_json = check_job.read()

	if check_job_json == 'Nay':
            print "Waiting for response to come back.. {} tries left..".format(wait_time)
            wait_time = wait_time - 1
            sleep(2)
        else:
            print "found response!"
            print check_job_json
            wait_time = 0


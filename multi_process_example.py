from flask import Flask, request, jsonify, make_response
from rq import Queue
from rq.job import Job
import worker
from time import sleep

class API():

    app = Flask('multi_process')



    def __init__(self):
        pass

    # API endpoint that receives requests to do work, pass it onto worker, and returns a job ID
    @staticmethod
    @app.route('/api/do_work', methods=['GET'])
    def do_work():
        results = {}
        arguments = ["hello","world"]
        q = Queue(connection=worker.conn)
        
        job = q.enqueue_call(
            func=worker.long_running_work, 
            args=arguments,
            result_ttl=5000,
            timeout=3600
        )

        results['job_id'] = job.get_id()
        return jsonify({'result': results})


    @staticmethod
    @app.route('/api/job_status/<job_key>', methods=['GET'])
    def get_results(job_key):
        results = {}

        job = Job.fetch(job_key,connection=worker.conn)
        if job.is_finished:
            return str(job.result),200
        else:
            return 'Nay',202


    # error handling
    @staticmethod
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    # Running the flask server
    def run(self,debug=True,port=5000):
        self.app.run(host="0.0.0.0",port=port, debug=debug,threaded=True)


ab = API()
ab.run(True)



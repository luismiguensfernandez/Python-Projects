import beanstalkc


def worker():
    beanstalk = beanstalkc.Connection(host='localhost', port=11300)
    task = beanstalk.reserve()
    print task.body
    task.delete()

if __name__ == '__main__':
    worker()


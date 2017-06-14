import beanstalkc
import sys


def worker(queue_name):
    beanstalk = beanstalkc.Connection(host='localhost', port=11300)
    beanstalk.watch(queue_name)
    task = beanstalk.reserve()
    print task.body
    task.delete()


def tubes_list():
    beanstalk = beanstalkc.Connection(host='localhost', port=11300)
    print 'List of tubes'
    print beanstalk.tubes()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print sys.argv[1] + ':'
        worker(sys.argv[1])
    else:
        tubes_list()



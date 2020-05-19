'''
import time
import threading
import random
import multiprocessing
import math

ball = ['红球','黄球','绿球']
box = []
con = threading.Condition()
maxcount = 100

class MakeBall(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.__name = name

	def run(self):
		global box
		global maxcount
		while True:
			con.acquire()
			if maxcount==0:
				con.notify()
				con.release()
				print(self.__name+"说：今天一共做了100个球，我不再做了")
				break
			seq = random.randint(0,2)
			myball = ball[seq]
			box.append(myball)
			maxcount=maxcount-1
			print(self.__name+"添加了一个"+myball+'还剩下'+str(len(box))+"个球,已经做了共"+ str(100-maxcount))
			con.notify()
			con.release()
			time.sleep(0.1)


class TakeBall(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.__name = name
	def run(self):
		global box
		global maxcount
		while True:
			con.acquire()

			while len(box)==0:
				print(self.__name+"发现没有球，在等待")
				con.wait()
			if maxcount==0:
				con.notify()
				con.release()
				print(self.__name+"说：今天一共做了100个球,已经别大家取光了")
				break
			try:
				seq =random.randint(0,len(box)-1)
			except:
				print(box)
			myball = box[seq]
			box.remove(myball)
			print(self.__name+"拿走了一个"+myball+'还剩下'+str(len(box))+"个球,已经做了共"+ str(100-maxcount))
			con.release()
			time.sleep(0.1)
if __name__ == '__main__':
    for i in range(3):
        s=MakeBall('[造球者'+str(i+1)+"]")
        s.start()
    for i in range(5):
        b=TakeBall('[取球者'+str(i+1)+"]")
        b.start()
'''

import datetime
from multiprocessing import Process, Manager, RLock
from itertools import islice
"""
多进程分块读取文件
"""

class File_Manager(object):

    def func_countfileline(self, filepath):
        """
        计算文件的总行数
        :param filepath: 文件
        :return:int，文件总行数
        """
        num =1
        thefile=open(filepath, 'rb')
        while True:
            buffer = thefile.read(102400)
            if not buffer:
                break

            num += buffer.count('\n')
        thefile.close()
        return num

    def process_found_new(self, FILE_COUNT, pid, result, file, rlock):
        """
        对文件内容进行统计，每次读取最多2000行
        :param FILE_COUNT: 文件读取的起始行
        :param pid: 进程id
        :param result: dict格式，处理的结果
        :param file: 文件
        :param rlock: 锁
        :return:
        """
        # import os
        # print os.getpid()
        global BLOCKLINE
        with open(file, 'rb') as fstream:
            rlock.acquire()
            print ('pid%s'% pid)
            count = 0
            for line in islice(fstream, FILE_COUNT, None):
                if count < BLOCKLINE:
                    func_name = line.split(' ')[2]
                    if result.get(func_name):
                        result[func_name] += 1
                    else:
                        result[func_name] = 1
                    count += 1
                else:
                    break
            rlock.release()
            print ('pid%s end!'% pid)

    def main(self, file):
        """
        根据文件总行数，每次处理2000行， 判断起几个进程，然后每个进程对文件进行处理
        :param file: 文件
        :return: result，最终对文件的统计结果
        """
        BLOCKLINE = 10000
        global BLOCKLINE
        print (datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
        count = self.func_countfileline(file)
        WORKERS = count/BLOCKLINE + 1 if count % BLOCKLINE else count/BLOCKLINE
        rlock = RLock()
        manager = Manager()
        result = manager.dict()
        processes = []
        for i in range(WORKERS):
            p=Process(target=self.process_found_new, args=[i*BLOCKLINE, i, result, file, rlock])
            p.daemon = True
            processes.append(p)
        for i in range(WORKERS):
            processes[i].start()
        for i in range(WORKERS):
            processes[i].join()
        print (result)
        print (datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))

if __name__ == '__main__':
    file = "D:\\webcgi.std"
    file_manager = File_Manager()
    file_manager.main(file)

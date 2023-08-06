import datetime,builtins,platform,time,math,os,urllib,sys,hashlib
from urllib import request
dicts={}
IS_WIN=False if platform.system().find('Linux')>-1 else True
NOW=datetime.datetime.now()
NOW_TS=math.floor(NOW.timestamp())
NOW=NOW.strftime('%Y-%m-%d %H:%M:%S')
start_time=0
def is_numeric(x):
	try:float(x);return True
	except:return False
def now(x=None):#x=micro return microsecond;x='str' return string;x is int means convert timestamp to string;x is sting means convert string to timestamp
	if not x:return int(datetime.datetime.now().timestamp())
	elif x=='micro':return datetime.datetime.now().timestamp()
	elif x=='str':return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(x,int):return datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')
	else:
		try: import dateutil.parser;return int(dateutil.parser.parse(x).timestamp())
		except Exception: return int(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S').timestamp())
def print(*a,func=None,time='%m/%d %H:%M:%S',pretty=False,**s):
	a=list(a)
	if func:
		for i,x in enumerate(a):
			a[i]=func(x)
	if time:
		a.insert(0,datetime.datetime.now().strftime(time)+' :')
	if pretty:
		import pprint
		for x in a:
			pprint.pprint(x)
	else:
		builtins.print(*a,**s)
def split_str(strs,num=1):
	_=[]
	for x in range(math.ceil(len(strs)/num)):
		_.append(strs[x*num:x*num+num])
	return _
def diff(a,b):
	diff={}
	for x in a:
		if b.get(x)!=a[x]: diff[x]=[a[x],b.get(x)]
	return diff
def notice(x,c='default'):request.urlopen(r'http://call.ff2.pw/?%s=%s&passwd=frank'%(c,urllib.parse.quote_plus(x)))
def rand_sleep(i=0.4,a=0.8):import random;time.sleep(random.randint(i*1000,a*1000)/1000);
def rand(i=9,a=None):import random;return random.randint(int(i),int(a)) if a else random.randint(0,int(i-1));
def md5(x):hl = hashlib.md5();hl.update(x.encode('utf-8') if isinstance(x,str) else x);return hl.hexdigest();
def bin2hex(x):import binascii;return binascii.hexlify(x.encode('utf-8') if isinstance(x,str) else x);
def base64_encode(x):import base64;return base64.b64encode(x) if isinstance(x,bytes) else base64.b64encode(x.encode('utf-8'))
def base64_decode(x):import base64;return base64.b64decode(x)
def log(*x,path=None):#已经带有时间
	if path is None:
		path='/tmp/frank.log' if os.path.exists('/tmp') else './FPC.log'
	with open(path,'a',encoding='utf-8') as f:
		print(*x,file=f)
def parse(o):#print class/obj's attr beatiful
	method=[];attr=[]
	for x in dir(o):
		if x[:2]=='__':continue
		method.append(x) if callable(getattr(o,x)) else attr.append(x)
	builtins.print('method',method)
	builtins.print('attr',attr)
#save or open a python varible,name and expire just for local
def obj(obj=None,remote=False,name:str =None,expire:(str,int)=None):
	import pickle
	if remote:
		return pickle.loads(request.urlopen(r'http://a.ff2.pw/obj.php').read()) if obj is None else request.urlopen(r'http://a.ff2.pw/obj.php',pickle.dumps(obj))
	else:
		os.path.exists('/tmp') or os.makedirs('/tmp')
		if name is None:
			path='/tmp/'+(sys.argv[0][sys.argv[0].replace('\\','/').rindex('/')+1:] if '/' in sys.argv[0] or '\\' in sys.argv[0] else sys.argv[0])+'.obj'
		else: path=f'/tmp/_named_{name}.obj'
		if obj is None: return pickle.load(open(path,'rb')) if os.path.exists(path) else None
		else:
			if expire:
				_={'s':1,'m':60,'h':3600,'d':86400}
				if isinstance(expire,str): expire=int(expire[:-1])*_[expire[-1]]
				if NOW_TS-os.path.getmtime(path)>expire:
					os.remove(path)
					return None
			return pickle.dump(obj,open(path,'wb'))
def encrypt(string,password=None):
	if isinstance(string,bytes): string=string.decode('latin')
	first_letter=string[0]
	hl = hashlib.sha512()
	hl.update(first_letter.encode('utf-8')if password is None else password.encode('utf-8'))
	sha512=hl.digest()
	_= sha512[0]%64
	sha512=(sha512[_:]+sha512[:_])*math.ceil(len(string)/64)
	encrypted=''
	for i,x in enumerate(string):
		encrypted+=chr((ord(x)+sha512[i])%94+33)
	if password is None:
		encrypted=chr((ord(first_letter)+ord(encrypted[-1]))%94+33)+encrypted[1:]
	return encrypted
def decrypt(string,password=None):
	hl = hashlib.sha512()
	if not password:
		for i in range(6):
			_=94*i+ord(string[0])-(ord(string[-1])+33)
			if _ >=33 and _<127:break
		first_letter=chr(_)
	hl.update(first_letter.encode('utf-8')if password is None else password.encode('utf-8'))
	sha512=hl.digest()
	_= sha512[0]%64
	sha512=(sha512[_:]+sha512[:_])*math.ceil(len(string)/64)
	decrypted=''
	for i,x in enumerate(string):
		for ii in range(6):
			_=94*ii+ord(x)-(sha512[i]+33)
			if _ >=33 and _<127:break
		decrypted+=chr(_)
	if password is None:
		decrypted=first_letter+decrypted[1:]
	return decrypted
def start():
	global start_time
	start_time=now('micro')
def end():
	print(now('micro')-start_time)
class mysql(object):
	conn=None
	def __init__(self, host='127.0.0.1',**args):
		import pymysql
		self.pymysql=pymysql
		connect_config={'host':host,'user':'root','password':'','db':'localhost','charset':'utf8','cursorclass':pymysql.cursors.DictCursor,'autocommit':None}
		if 'table' in args:
			self.table=args['table']
			del args['table']
		if not args:
			args=obj(name='mysql')
		for x in args:
			connect_config[x]=args[x]
		self.connect_config = connect_config
	def __init_connect__(self):
		self.conn = self.pymysql.connect(**self.connect_config)
	def __getattr__(self,attr):
		return getattr(self.conn,attr)
	def _decide_type(self,value):
		if isinstance(value,(int,float)):
			pass
		elif isinstance(value,bytes):
			value=value.decode('utf-8')
		elif value is None:
			value='NULL'
		else:
			value='"'+self.pymysql.converters.escape_string(value)+'"'
		return value
	def _split_dict(self,dicts,splitor=','):
		string=''
		for field in dicts:
			if isinstance(dicts[field],(list,tuple)):
				operator= dicts[field][0].upper()
				if 'IN' in operator:
					value=''
					for in_value in dicts[field][1]:
						value+=f'{self._decide_type(in_value)},'
					value=value[:-1]
					string+=f' `{field}` {operator} ({value}) {splitor}'
				elif 'BETWEEN' in operator:
					value=[self._decide_type(dicts[field][1][0]),self._decide_type(dicts[field][1][1])]
					string+=f' `{field}` {operator} {value[0]} and {value[1]} {splitor}'
				else:
					value=self._decide_type(dicts[field][1])
					string+=f' `{field}` {operator} {value} {splitor}'
			else:
				value=self._decide_type(dicts[field])
				string+=f' `{field}`={value} {splitor}'
		return string[:-len(splitor)]
	def _split_add_dict(self,dicts):
		key=value=''
		for x in dicts:
			key+=r'`%s`,'%x
			if dicts[x] is None:value+='null,'
			else:value+=r'%s,'%(dicts[x]) if is_numeric(dicts[x]) else r'"%s",'%(self.pymysql.converters.escape_string(dicts[x]))
		return key[:-1],value[:-1]
	def execute(self,strs):
		if not self.conn:self.__init_connect__()
		strs=strs.strip()
		is_query = True if strs[:4].lower() in ['sele','show'] else False
		with self.conn.cursor() as cur:
			cur.execute(strs)
			data=cur.fetchall() if is_query else cur.lastrowid
		# is_query or self.conn.commit()
		return data
	def add(self,dicts,table=None,ignore=False,duplicate=[]):
		'''table is optional,dicts can be list or dict,duplicate should be list'''
		if not isinstance(table,str):
			if table is None:
				table=self.table
			else:#table is not none and reverse two args
				table_=dicts
				dicts=table
				table=table_
		if not dicts:return
		if isinstance(dicts,dict): dicts=[dicts]
		values=''#values like (1,2),(2,3) 
		for x in dicts:
			key,value=self._split_add_dict(x)
			values+=r'(%s),'%(value)
		ignore='' if not ignore else 'ignore'
		duplicate_str=''
		if duplicate:
			duplicate_str='on duplicate key update '
			for x in duplicate:
				duplicate_str+=f' `{x}`=values(`{x}`),'
			duplicate_str=duplicate_str[:-1]
		return self.execute(f''' insert {ignore} `{table}`({key}) values{values[:-1]} {duplicate_str}''')
	def update(self,where,data,table=None):
		'''where can be str or dict'''
		table=self.table if table is None else table
		where=self._split_dict(where,'and') if isinstance(where,dict) else where
		data=self._split_dict(data)
		return self.execute(r''' update `%s` set %s where %s'''%(table,data,where))
	def select(self,where=None,table=None,where_splitor='and',field='*',order=None,limit=None):
		table=self.table if table is None else table
		query_str=f'select {field} from {table} '
		if where:
			where=self._split_dict(where,where_splitor) if isinstance(where,dict) else where
			query_str+=f'where {where} '
		if order:
			query_str+=f'order by {order} '
		if limit:
			query_str+=f'limit {limit} '
		return self.execute(query_str)

class redis(object):
	server=False
	def __init__(self,host='127.0.0.1',db=0,port=6379,ssh_host=None,ssh_username='root',ssh_password=None):
		import redis
		if ssh_host:
			import sshtunnel
			sshtunnel.DAEMON=True 
			sshtunnel.SSHTunnelForwarder.daemon_forward_servers=True
			sshtunnel.SSHTunnelForwarder.daemon_transport=True
			self.server = sshtunnel.SSHTunnelForwarder(ssh_address_or_host=ssh_host,ssh_username=ssh_username,ssh_password=ssh_password,remote_bind_address=(host,6379))
			self.server.start()
			port=self.server.local_bind_port
		self.redis=redis.StrictRedis(host=host, port=port, db=db,decode_responses=True)
	def __getattr__(self,attr):
		return getattr(self.redis,attr)
def process(target,is_thread=True,join=False,num=1,sleep=None,**args):
	if isinstance(target,str):#args:target,[sync=False]
		import subprocess
		proc=subprocess.Popen(target,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True);
		return proc.communicate() if args.get('sync',True) else proc
	pros=[]
	if 'args' in args:#args can be list or tuple : [('',),('',)]
		assert isinstance(args['args'],list)
		args_list=args['args']
		num=len(args_list)
	if is_thread:
		import threading
		for x in range(num):
			if 'args' in args:
				args['args']=args_list[x]
			pros.append(threading.Thread(target=target,**args))
			pros[-1].start()
			if sleep:time.sleep(sleep)
	else:
		from multiprocessing import Process
		for x in range(num):
			if 'args' in args:
				args['args']=args_list[x] if isinstance(args_list[x],(tuple,list)) else [args_list[x]]
			pros.append(Process(target=target,**args))
			pros[-1].start()
			if sleep:time.sleep(sleep)
	if join:
		for x in range(num):
			pros[x].join()
	return pros[0] if len(pros)==1 else pros
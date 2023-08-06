import os, sys, requests, time
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

def wget(url, verify=True):
	to = url.split('/')[-1].replace('%20','_')
	if not os.path.exists(to):
		resp = requests.get(url, allow_redirects=True,verify=verify)
		open(to,'wb').write(resp.content)
	return to

def open_port():
	"""
	https://gist.github.com/jdavis/4040223
	"""

	import socket

	sock = socket.socket()
	sock.bind(('', 0))
	x, port = sock.getsockname()
	sock.close()

	return port


def checkPort(port):
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = bool(sock.connect_ex(('127.0.0.1', int(port))))
	sock.close()
	return result


def getPort(ports=[], prefix="-p"):
	if ports is None or ports == []:
		return ''
	return ' '.join([
		f"{prefix} {port if checkPort(port) else open_port()}:{port}" for port in ports
	])

@dataclass
class dock:
	"""Class for keeping track of an item in inventory."""
	docker: str = "docker"
	image: str = "frantzme/pythondev:lite"
	ports: list = field(default_factory=list)
	cmd: str = None
	nocmd: bool = False
	nonet: bool = False
	dind: bool = False
	shared: bool = False
	detach: bool = False
	sudo: bool = False
	remove: bool = True
	mountto: str = "/sync"
	mountfrom: str = None
	name: str = "current_running"
	login: bool = False
	loggout: bool = False
	logg: bool = False
	macaddress: str = None
	postClean: bool = False
	preClean: bool = False
	extra: str = None

	def clean(self):
		return "; ".join([
			"{} kill $({} ps -a -q)".format(self.docker, self.docker),
			"{} kill $({} ps -q)".format(self.docker, self.docker),
			"{} rm $({} ps -a -q)".format(self.docker, self.docker),
			"{} rmi $({} images -q)".format(self.docker, self.docker),
			"{} volume rm $({} volume ls -q)".format(self.docker, self.docker),
			"{} image prune -f".format(self.docker),
			"{} container prune -f".format(self.docker),
			"{} builder prune -f -a".format(self.docker)
		])

	def string(self):
		if self.dind or self.shared:
			import platform
			if False and platform.system().lower() == "darwin":  # Mac
				dockerInDocker = "--privileged=true -v /private/var/run/docker.sock:/var/run/docker.sock"
			else:  # if platform.system().lower() == "linux":
				dockerInDocker = "--privileged=true -v /var/run/docker.sock:/var/run/docker.sock"
		else:
			dockerInDocker = ""

		if self.shared:
			exchanged = "-e EXCHANGE_PATH=" + os.path.abspath(os.curdir)
		else:
			exchanged = ""

		dir = '%cd%' if sys.platform in ['win32', 'cygwin'] else '`pwd`'
		use_dir = "$EXCHANGE_PATH" if self.shared else (self.mountfrom if self.mountfrom else dir)

		if self.nocmd:
			cmd = ''
		else:
			cmd = self.cmd or '/bin/bash'

		network = ""
		if self.nonet:
			network = "--network none" #https://docs.docker.com/network/none/

		return str(self.clean()+";" if self.preClean else "") + "{0} run ".format(self.docker) + " ".join([
			dockerInDocker,
			'--rm' if self.remove else '',
			'-d' if self.detach else '-it',
			'-v "{0}:{1}"'.format(use_dir, self.mountto),
			exchanged,
			network,
			getPort(self.ports),
			'--mac-address ' + str(self.macaddress) if self.macaddress else '',
			self.extra if self.extra else '',
			self.image,
			cmd
		]) + str(self.clean()+";" if self.postClean else "")

	def __str__(self):
		return self.string()

def exe(string):
	print(string)
	os.system(string)

@dataclass
class vb:
	"""Class for keeping track of an item in inventory."""
	vmname: str = "takenname"
	username: str = None
	ovafile: str = None
	isofile: str = None
	disablehosttime: bool = True
	biosoffset: str = None
	vmdate: str = None
	network: str = None
	cpu: int = 2
	ram: int = 4096
	sharedfolder: str = None
	uploadfiles:list = field(default_factory=list)
	vboxmanage: str = "VBoxManage"
	cmds_to_exe_with_network:list = field(default_factory=list)
	cmds_to_exe_without_network:list = field(default_factory=list)
	min_to_wait: int = 2
	choco_packages:list = field(default_factory=list)
	python_packages:list = field(default_factory=list)

	@property
	def wrap(self):
		return self.vb_wrap(self.vboxmanage, self.vmname,self.min_to_wait)

	@property
	def wrap_off(self):
		return self.vb_wrap(self.vboxmanage, self.vmname,self.min_to_wait,internet_on=False)

	class vb_wrap(object):
		def __init__(self,vboxmanage,vmname,min_to_wait,internet_on=True):
			self.vboxmanage = vboxmanage
			self.vmname = vmname
			self.min_to_wait = min_to_wait
			self.internet_on = internet_on

		def __enter__(self):
			if self.internet_on:
				exe("{0} modifyvm {1} --nic1 nat".format(self.vboxmanage, self.vmname))

			exe("{0} startvm {1} --type headless".format(self.vboxmanage,self.vmname))
			time.sleep(self.min_to_wait*60)

		def __exit__(self, type, value, traceback):
			exe("{0} controlvm {1} poweroff".format(self.vboxmanage, self.vmname))
			time.sleep(self.min_to_wait*60)
			exe("{0} modifyvm {1} --nic1 null".format(self.vboxmanage, self.vmname))

	def set_vmname(self, vmname):
		self.vmname = vmname

	def start(self,headless:bool=True):
		cmd = "{0} startvm {1}".format(self.vboxmanage,self.vmname)
		if headless:
			cmd += " --type headless"

		exe(cmd)
		time.sleep(self.min_to_wait*60)

	def vbexe(self, cmd):
		string = "{0} guestcontrol {1} run ".format(self.vboxmanage, self.vmname)
		
		if self.username:
			string += " --username {0} ".format(self.username)

		string += str(" --exe \"C:\\Windows\\System32\\cmd.exe\" -- cmd.exe/arg0 /C '" + cmd.replace("'","\'") + "'")
		exe(string)

	def vbpowershell(self, cmd):
		string = "{0} guestcontrol {1} run ".format(self.vboxmanage, self.vmname)

		string += str(" \"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" -- " + cmd.replace("'","\'"))
		
		if self.username:
			string += " --username {0} ".format(self.username)

		exe(string)

	def __shared_folder(self, folder):
		exe("{0}  sharedfolder add {1} --name \"share_{1}\" --hostpath \"{2}\" --automount".format(self.vboxmanage, self.vmname, folder))

	def import_ova(self, ovafile):
		self.ovafile = ovafile

		exe("{0}  import {1} --vsys 0 --vmname {2} --ostype \"Windows10\" --cpus {3} --memory {4}".format(self.vboxmanage, self.ovafile, self.vmname, self.cpu, self.ram))

	def disable(self):
		if self.disablehosttime:
			exe("{0} setextradata {1} VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled 1".format(self.vboxmanage, self.vmname))

		if self.biosoffset:
			exe("{0} modifyvm {1} --biossystemtimeoffset {2}".format(self.vboxmanage, self.vmname, self.biosoffset))

		if self.vmdate:
			TO_DATE = datetime.strptime(self.vmdate, '%m/%d/%Y')
			ms = round((TO_DATE - datetime.utcnow()).total_seconds()*1000)

			exe("{0} modifyvm {1} --biossystemtimeoffset {2}".format(self.vboxmanage, self.vmname, ms))

		if self.network is None:
			network = "null"
		exe("{0} modifyvm {1} --nic1 {2}".format(self.vboxmanage, self.vmname, network))

	def prep(self, upload_files=True):
		if self.ovafile:
			self.import_ova(self.ovafile)

		self.disable()
		if self.sharedfolder:
			self.__shared_folder(self.sharedfolder)
		
		if upload_files:
			for file in self.uploadfiles:
				self.uploadfile(file)

		if self.cmds_to_exe_with_network and len(self.cmds_to_exe_with_network) > 0:
			with self.wrap:
				for cmd in self.cmds_to_exe_with_network:
					self.vbexe(cmd)

		if self.cmds_to_exe_without_network and len(self.cmds_to_exe_without_network) > 0:
			with self.wrap_off:
				for cmd in self.cmds_to_exe_without_network:
					self.vbexe(cmd)

		if self.python_packages and len(self.python_packages) > 0:
			self.choco_packages += ["python38"]
			self.python_packages += ["pip"]

		if self.choco_packages and len(self.choco_packages) > 0:
			with self.wrap:
				for package in self.choco_packages:
					self.vbpowershell("choco install {0} -y".format(package))

		if self.python_packages and len(self.python_packages) > 0:
			with self.wrap:
				for package in self.python_packages:
					self.vbpowershell("python -m pip install --upgrade {0}".format(package))

	def run(self, headless:bool = True):
		self.prep()
		self.start(headless)
	
	def __enter__(self):
		self.start(True)
	
	def stop(self):
		exe("{0} controlvm {1} poweroff".format(self.vboxmanage, self.vmname))
		time.sleep(self.min_to_wait*60)

	def __exit__(self, type, value, traceback):
		self.stop()
	
	def uploadfile(self, file:str):
		exe("{0} guestcontrol {1} copyto {2} --target-directory=c:/Users/{3}/Desktop/ --user \"{3}\"".format(self.vboxmanage, self.vmname, file, self.username))
	
	def destroy(self, deletefiles:bool=True):
		cmd = "{0} unregistervm {1}".format(self.vboxmanage, self.vmname)

		if deletefiles:
			cmd += " --delete"

		exe(cmd)

class vagrant(vb):
	def __init__(self,
		vagrant_base:str = "talisker/windows10pro",
		disablehosttime: bool = True,
		biosoffset: str = None,
		vmdate: str = None,
		network: str = None,
		cpu: int = 2,
		ram: int = 4096,
		sharedfolder: str = None,
		uploadfiles: list = None,
		scripts_to_run:list = None,
		cmds_to_exe_with_network:list = None,
		cmds_to_exe_without_network:list = None,
		min_to_wait: int = 2,
		choco_packages:list = None,
		no_python: bool = False,
		python_packages:list = None,
		vb_path: str = None
	):
		super().__init__(
			vmname = None,
			username = "vagrant",
			ovafile = None,
			isofile = None,
			disablehosttime = True,
			biosoffset = None,
			vmdate = None,
			network = None,
			cpu = self.cpu,
			ram = self.ram,
			sharedfolder = None,
			uploadfiles = None, #self.uploadfiles,
			vboxmanage = "VBoxManage",
			cmds_to_exe_with_network = cmds_to_exe_with_network or [],
			cmds_to_exe_without_network = cmds_to_exe_without_network or [],
			min_to_wait = min_to_wait,
		)

		self.vagrant_base = vagrant_base
		self.disablehosttime = disablehosttime
		self.biosoffset = biosoffset
		self.vmdate = vmdate
		self.network = network
		self.cpu = cpu
		self.ram = ram
		self.sharedfolder = sharedfolder
		self.uploadfiles = uploadfiles or []
		self.scripts_to_run = scripts_to_run or []
		self.cmds_to_exe_with_network = cmds_to_exe_with_network or []
		self.cmds_to_exe_without_network = cmds_to_exe_without_network or []
		self.min_to_wait = min_to_wait
		self.choco_packages = choco_packages or []
		self.no_python = no_python
		self.python_packages = python_packages or []
		self.vagrantfile = None
		self.vb_path = vb_path
		self.min_to_wait = min_to_wait

	@property
	def vagrant_name(self):
		if not self.vb_path:
			return

		vag_name = None

		folder_name = os.path.basename(os.path.abspath(os.curdir))
		for item in os.listdir(self.vb_path):
			if not os.path.isfile(item) and folder_name in item:
				vag_name = item.split('/')[-1].strip()

		print(vag_name)
		super().set_vmname(vag_name)

		return vag_name

	def create_vagrant_file(self):
		uploading_file_strings = []
		for foil in self.uploadfiles:
			uploading_file_strings += [
				""" win10.vm.provision "file", source: "{0}", destination: "C:\\\\Users\\\\vagrant\\\\Desktop\\\\{0}" """.format(foil)
			]
		
		scripts = []
		for script in self.scripts_to_run:
			scripts += [
				"""win10.vm.provision "shell", inline: <<-SHELL
{0}
SHELL""".format(script)
			]
		
		if not self.no_python and self.python_packages != []:
			self.choco_packages += [
				"python38"
			]

		if self.choco_packages:
			choco_script = """win10.vm.provision "shell", inline: <<-SHELL
[Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls"
iex (wget 'https://chocolatey.org/install.ps1' -UseBasicParsing)
"""

			for choco_package in set(self.choco_packages):
				choco_script += """choco install -y {0} \n""".format(choco_package)	
			
			choco_script += """
SHELL"""

			scripts += [choco_script]

		if self.python_packages != []:
			scripts += [
				""" win10.vm.provision :shell, :inline => "python -m pip install --upgrade pip {0} " """.format(" ".join(self.python_packages))
			]

		contents = """# -*- mode: ruby -*- 
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.define "win10" do |win10| 
    	win10.vm.box = "{0}"
		{1}
		{2}
	end
end
""".format(
	self.vagrant_base,
	"\n".join(uploading_file_strings),
	"\n".join(scripts)
)
		with open("Vagrantfile", "w+") as vagrantfile:
			vagrantfile.write(contents)

		self.vagrantfile = "Vagrantfile"

	def start(self,headless=True):
		self.vagrant_name
		super().disable()
		super().start(headless=headless)

	def off(self):
		self.vagrant_name
		super().stop()
	
	def prep(self):
		self.create_vagrant_file()
		exe(""" vagrant up""")
		exe(""" vagrant halt """)
		self.vagrant_name
		time.sleep(self.min_to_wait * 60)
		super().prep(False)
		pass
	
	def destroy(self):
		self.vagrant_name
		exe(""" vagrant destroy -f """)
		exe("rm Vagrantfile")
		exe("yes|rm -r .vagrant/")
		for foil in self.uploadfiles:
			exe("rm {0}".format(foil))
		#super().destroy()


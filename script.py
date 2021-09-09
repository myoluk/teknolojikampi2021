"""* HAVELSAN PARDUS ve Liman Teknoloji Kampı
   * 3. gün ödevi : https://github.com/aciklab/teknolojikampi2021.git
   * 9 Eylül 2021
   * 
   * Script argümansız çalıştırılırsa sistemde yüklü paket sayısını verir
   * Script argümanlı çalıştırılırsa argüman olarak verilen paketin;
   *  - Kurulu olup olmadığını,
   *  - Bağımlılıklarını ve sayısını,
   *  - Bağımlılıklarından yüklü olmayanları ve sayısını,
   *  - Bağımlılıklarından yüklü olanları ve sayısını
   *  verir.
   *
   * @author: myoluk
"""
import os
import sys
import subprocess
import re

try:
	pkgArg = sys.argv[1]
except:
	pkgArg = None

# Verilen string komutları çıktı vermeden shell üzerinde çalıştırır
def cmdRun(cmd):
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	stdoutdata, stderrdata = p.communicate()
	return stdoutdata, stderrdata

# Script argüman ile çağrılmış ise
if (pkgArg):
	cmdInstalled = "dpkg -s " + str(pkgArg) + " | grep 'install ok'"
	outInstalled, errInstalled = cmdRun(cmdInstalled)
	
	# argüman olarak verilen paket kurulu ise
	if (outInstalled):
		os.system('echo "' + str(pkgArg) + ' paketi kurulu.\n"')
	
	# argüman olarak verilen paket kurulu değil ise
	else:
		os.system('echo "' + str(pkgArg) + ' paketi kurulu değil."')
		
		# kurulu olmayan paketin bağımlılıkları
		cmdDepends = "apt-cache depends " + str(pkgArg) + " | grep 'epends'"
		outDepends, errDepends = cmdRun(cmdDepends)
		outDepends = re.sub("  Depends: ", '', outDepends)
		outDepends = outDepends.split('\n')
		outDepends = outDepends[:-1]
		for depend in outDepends:
			if (re.search(':any>', depend)):
				dependTemp = depend
				outDepends.remove(depend)
				dependTemp = re.sub(':any>', '', depend)
				dependTemp = re.sub('<', '', dependTemp)
				outDepends.append(dependTemp)

		# kurulu olmayan paketin bağımlılıklarının sayısı
		countDepends = len(outDepends)
		os.system('echo "\n' + str(pkgArg) + ' paketi bağımlılıkları (' + str(countDepends) + '):"')
		for depend in outDepends:
			os.system('echo "• ' + str(depend) + '"')

		# kurulu olmayan paketin bağımlılıklarından yüklü olanlar ve olmayanlar
		installedDepends = []
		notInstalledDepends = []
		for depend in outDepends:
			cmdInstalledDepend = "dpkg -s " + str(depend) + " | grep 'install ok'"
			outInstalledDepend, errInstalledDepend = cmdRun(cmdInstalledDepend)
			if (outInstalledDepend):
				installedDepends.append(depend)
			else:
				notInstalledDepends.append(depend)
		
		# yüklü olmayanlar
		os.system('echo "\nBağımlılıklardan yüklü olmayanlar (' + str(len(notInstalledDepends)) + '):"')
		for depend in notInstalledDepends:
			os.system('echo "• ' + str(depend) + '"')
		
		# yüklü olanlar
		os.system('echo "\nBağımlılıklardan yüklü olanlar (' + str(len(installedDepends)) + '):"')
		for depend in installedDepends:
			os.system('echo "• ' + str(depend) + '"')
		os.system('echo ')

# Script argümansız çağrılmış ise
else:
	cmd = "dpkg -l | wc -l"
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	stdoutdata, stderrdata = p.communicate()
	os.system('echo "Kurulu paket sayısı: ' + str(stdoutdata) + '"')
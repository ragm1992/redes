
import os, urllib2, sys, zipfile, shutil 

os.system("#! /bin/bash")

os.system("echo labredesML340 | sudo apt-get install apache2 -y")
os.system("echo labredesML340 | sudo apt-get install php5 -y")

os.system("sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password labredesML340'")
os.system("sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password labredesML340'")
os.system("sudo apt-get -y install mysql-server-5.5")

# crear carpeta Downloads
directorio = os.path.join(os.pardir, '/home/labredes/Downloads')
if not os.path.isdir(directorio):
    os.mkdir(directorio)
os.chdir(directorio)

#Bajar y Descomprimir
tmp_path = '/home/labredes/Downloads'
os.mkdir('/home/labredes/Downloads/www')
os.mkdir('/home/labredes/Downloads/www/var')
os.chdir(tmp_path)
doc_url = "http://sourceforge.net/projects/phpscheduleit/files/Booked/2.5/booked-2.5.1.zip"
 
u = urllib2.urlopen(doc_url)
localFile = open(tmp_path + "/booked-2.5.1.zip" , 'w')
localFile.write(u.read())
localFile.close()
 
sourceZip = zipfile.ZipFile( tmp_path + "/booked-2.5.1.zip" ,  'r')
for name in sourceZip.namelist():
    print name
    sourceZip.extract(name, tmp_path + "/www/var/" + name )
sourceZip.close()

#dar permisos
os.chdir('/home/labredes/Downloads/www/var/booked')
os.system("chmod +x ./tpl")
os.system("chmod +x ./tpl_c")
os.system("chmod +x ./uploads")

#cambiar duenio
os.system("sudo chown www-data ./tpl")
os.system("sudo chown www-data ./tpl_c")
os.system("sudo chown www-data ./uploads")

#copiar a nuevo archivo
os.system("cp ./config/config.dist.php ./config/config.php")

#ocultar archivo .zip
def hide(*path): 
    if not os.path.exists(*path): 
        return 
    archive = os.path.basename(*path) 
    if archive[0] == '.': 
        return 
    else: 
        directorio = os.path.dirname(*path) 
        newfile = directorio+'/''.'+archive 
        os.rename(*path, newfile) 
        
hide("/home/labredes/Downloads/booked-2.5.1.zip")

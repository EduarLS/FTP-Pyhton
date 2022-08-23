#Autor: Eduardo Lopez Solis
# 20/11/2020 17:26 hrs

from ftplib import FTP
archivo = '1865221.txt'
miarchivo = open(archivo, 'rb')
ftp = FTP("ftp.dlptest.com")
ftp.login("dlpuser@dlptest.com","eUj8GeW55SvYaswqUyDSm5v6N")
ftp.retrlines('LIST')
ftp.retrbinary('RETR csv.csv', open('csv.txt', 'wb').write)
ftp.storbinary('STOR' +  archivo, miarchivo)
ftp.retrlines('LIST')
ftp.quit()

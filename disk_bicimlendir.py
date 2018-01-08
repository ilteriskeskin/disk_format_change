import os
import time

mavi = '\033[94m'

def diskGoster():
    print(os.system("sudo fdisk -l"))

def cikis():
    os.system("exit")

while (1):
    print("1-Diskleri Görüntüle")
    print("2-Çıkış")

    secim = input("Bir seçim yapınız: ")

    if secim == '1':
        diskGoster()

        while (1):
            print(mavi + "------------------------------------------------------")
            print("1-Fat32")
            print("2-Ext4")
            print("3-Çıkış")

            kalıp = input("Çevirmek istediğiniz formatı seçiniz: ")

            if kalıp == '1':
                disk = input("Fat32 formatına çevirmek istediğiniz diskin ismini yazınız (dev/sdb1 gibi): ")
                print("Bekleyiniz...")
                os.system("sudo mkfs.vfat " + disk)
                time.sleep(1.5)
                print("Belleğiniz artık hazır.")
                break

            elif kalıp == '2':
                disk = input("Fat32 formatına çevirmek istediğiniz diskin ismini yazınız (dev/sdb1 gibi): ")
                print("Bekleyiniz...")
                os.system("sudo mkfs.ext4 " + disk)
                time.sleep(1.5)
                print("Belleğiniz artık hazır.")
                break

            elif kalıp == '3':
                print("Çıkış yapılıyor...")
                time.sleep(2)
                break
            else:
                print("Hatalı seçim !")

    elif secim == '2':
        print("Çıkış yapılıyor...")
        time.sleep(2)
        cikis()
        break

    else:
        print("Hatalı seçim !")

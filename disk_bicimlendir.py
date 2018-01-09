import os
import time

mavi = '\033[94m'

def diskGoster():
    print(os.system("sudo fdisk -l"))

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
            print("3-Ext3")
            print("4-Geri")
            print(mavi + "------------------------------------------------------")

            kalip = input("Çevirmek istediğiniz formatı seçiniz: ")

            if kalip == '1':
                disk = input("Fat32 formatına çevirmek istediğiniz diskin ismini yazınız (dev/sdb1 gibi): ")
                print("Bekleyiniz...")
                os.system("sudo mkfs.vfat " + disk)
                time.sleep(1)
                print("İşlem tamamlandı.")
                break

            elif kalip == '2':
                disk = input("Ext4 formatına çevirmek istediğiniz diskin ismini yazınız (dev/sdb1 gibi): ")
                print("Bekleyiniz...")
                os.system("sudo mkfs.ext4 " + disk)
                time.sleep(1)
                print("İşlem tamamlandı.")
                break

            elif kalip == '3':
                disk = input("Ext3 formatına çevirmek istediğiniz diskin ismini yazınız (dev/sdb1 gibi): ")
                print("Bekleyiniz...")
                os.system("sudo mkfs.ext3 " + disk)
                time.sleep(1)
                print("İşlem tamamlandı.")
                break

            elif kalip == '4':
                time.sleep(1)
                break
            else:
                print("Hatalı seçim !")

    elif secim == '2':
        print("Çıkış yapılıyor...")
        time.sleep(2)
        break

    else:
        print("Hatalı seçim, tekrar deneyin.")
from os import system, name

def Soal(Nomor,NoSoal,Skor):
    system('cls')
    int(NoSoal)
    
    while NoSoal > 0:
        print(f"Skor : {Skor}") 
        if NoSoal <=10:
            if NoSoal == 1:
                Skor = Soal1(Skor)
                
            elif NoSoal == 2:                
                Skor = Soal2(Skor)

            Nomor.append(NoSoal)
            SoalTerjawab(Nomor)
            print(Skor) 
            NoSoal = NextSoal(NoSoal)    
        
        elif NoSoal >10:
            break
        
        NoSoal+=1
              
    return Skor

def SoalTerjawab(Nomor):
    AllNomor = range(1, 11)
    Nomor.sort()
    Nomor = list(set(Nomor))
    system('cls')
    NomorBelum = list(set(AllNomor) - set(Nomor))
    print(f"Nomor Sudah : {Nomor}")
    print(f"Nomor yang belum : {NomorBelum}")

    return Nomor

def NextSoal(NoSoal):
    Next = input("Ingin Kerjakan selanjutnya ? (y/n/q) ")
    print(Next)
    if Next == "y":
        NoSoal -=1
        NoSoal +=1

    elif Next == "n":
        system('cls')
        Input = int(input("Ingin kerjakan Nomor berapa lagi ? "))
        NoSoal = Input
        NoSoal -=1
    else:
        NoSoal = 0
        NoSoal -=1
    
    system('cls')

    return NoSoal

def SkorHasil(Skor):
    print(f"Nilai anda adalah : {Skor}")
    return Skor

def Soal1(Skor):  
    print("Soal 1")
    Jawaban = input("Siapakah Nama Anda ? ")
    if Jawaban.lower() == "pande":
        print("Jawaban Benar")
        PerSkor = 0
    else:
        print("Jawaban Salah")
        PerSkor = 10  
    
    Skor = Skor - PerSkor
    return Skor

def Soal2(Skor):
    print("Soal 2")  
    Jawaban = input("Siapakah Pacar Anda ? ")
    if Jawaban.lower() == "lista":
        print("Jawaban Benar")
        PerSkor = 0
    else:
        print("Jawaban Salah")
        PerSkor = 10  
    
    Skor = Skor - PerSkor
    return Skor


def KerjakanSoal(Nomor, Skor):
    NoSoal = int(input("Ingin menerjakan dari 1 atau Pilih Nomor ? "))
    Skor = Soal(Nomor, NoSoal,Skor)

    return Skor

def main():
    Skor = 100
    affirmative = ["ya", "iya" ,"gas", "pasti", "masa ngga", "kuy"]
    Nomor = []

    Input = input("Apakah anda ingin bermain ? ")
    if Input.lower() in affirmative:
        print("Selamat Datang")
        system('cls')
        Skor = KerjakanSoal(Nomor, Skor)

    else:
        print("Silahakan buka lain kali")
    print(f"Soal yang terjawab : {Nomor}")
    print(f"Skor Akhir : {Skor}")

main()
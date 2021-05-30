from tabulate import tabulate
from getpass import getpass
from abc import ABC,abstractmethod
import mysql.connector, random, os



def clear():
    if os.name =='posix':
        os.system('clear')
    else:
        os.system('CLS')

def start():
    while True:
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                database="BurningHeroes"
            )
            cursor= con.cursor()
            break
        except:
            a = input("Database belum terkoneksi, silahkan koneksikan database terlebih dahulu!\nTekan apa saja untuk melanjutkan ")
    while True:
        print('''Apakah sudah memiliki akun ?
1. Sudah memiliki akun
2. Belum memiliki akun''')
        regis = input("Pilihan anda : ")
        if regis == '1':
            while True:
                try:
                    print("Silahkan masukkan username dan password anda:")
                    username = input("Username\t: ")
                    password = getpass('Password\t:')
                    cursor.execute("Select password From user where username = '{}'".format(username))
                    res = cursor.fetchall()
                    if password == res[0][0]:
                        return username
                    else:
                        clear()
                        print("Password salah!")
                except:
                    clear()
                    print("Username salah!")
        elif regis == '2':
            daftar()
        else:
            clear()
            print("Mohon maaf inputan salah, silahkan menginput kembali!")

def daftar():
    username = input("Masukkan username yang anda inginkan \t: ")
    password = getpass("Masukkan password yang anda inginkan \t: ")
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="BurningHeroes"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO user(username,password,stage,koins) VALUES (%s, %s, %s, %s)"
        val = [(username,password,0,200)]
        mycursor.executemany(sql, val)
        mydb.commit()
        
        sql = "INSERT INTO hero(heroname, herorole, heroattack, herohp, maxhp, username) VALUES (%s, %s, %s, %s,%s, %s)"
        val = [
        ('lucas','fist',15,150,150,username),
        ('kimshin','bow',50,75,75,username),
        ('alibaba','sword',35,80,80,username)]
        mycursor.executemany(sql, val)
        mydb.commit()
        
        sql = "INSERT INTO item(NamaItem, value, storage, price, notes,username) VALUES (%s, %s,%s, %s, %s, %s)"
        val = [
        ('potion',20,0,15,'Potion can be used to replenish hero hp',username),
        ('machinegun',20,0,15,'Machine gun can be used to increase heros attack demage',username),
        ('soultrap',20,0,15,'Soul Trap can be used to increase heros max hp',username)]
        mycursor.executemany(sql, val)
        mydb.commit()
        clear()
        print("Berhasil registrasi!")
    except:
        print("username telah digunakan, silahkan ganti username anda !")
        daftar()

def stageFinder(username):
    while True:
        try:
            con=mysql.connector.connect(
                host="localhost",
                user="root",
                database="BurningHeroes"
            )
            cursor= con.cursor()
            break
        except:
            a = input("Database belum terkoneksi, silahkan koneksikan database terlebih dahulu!\nTekan apa saja untuk melanjutkan ")
    while True:
        try:
            cursor.execute("Select stage From user where username = '{}'".format(username))
            res = cursor.fetchall()
            return res[0][0]
        except:
            clear()
            print("Username salah!")

class deklarasi(ABC):
    def __init__(self,name):
        pass

    @abstractmethod
    def info(self):
        pass

class Hero():
    def __init__(self,name,role,attack,hp,maxHP):
        self.name = name
        self.role = role
        self.attack = attack
        self.hp = hp
        self.maxHP = maxHP
        self.__info = "Nama \t: {}\nAttack \t: {}\nHP\t: {}".format(self.name,self.attack,self.hp)

    def get_info(self):
        return("Nama \t: {}\nAttack \t: {}\nHP\t: {}".format(self.name,self.attack,self.hp))
    
    #override
    def menyerang(self,lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.hp = lawan.hp - self.attack

    def cekKemenangan(self,a,b,c,d):
        self.cursor.execute("Select koins, stage From user where username = '{}'".format(c))
        koin = self.cursor.fetchall()
        if a <= 0 :
            print(defeat)
            z = input("Tekan enter untuk melanjutkan ")
            sql= "UPDATE user SET koins = %s WHERE username = %s"
            val = (koin[0][0]+100, c)
            self.uppdateDBO(sql,val)
            sql= "UPDATE hero SET heroHP = %s WHERE username = %s and HeroName = %s"
            val = (0,c,d)
            self.uppdateDBO(sql,val)
            self.menu()
        elif b <= 0:
            print(victory)
            z = input("Tekan enter untuk melanjutkan ")
            stage = koin[0][1] + 1
            if stage >= 5:
                print("Game Over")
                z = input("Tekan enter untuk melanjutkan ")
                exit()
            sql= "UPDATE user SET koins = %s, stage= %s WHERE username = %s"
            val = (koin[0][0]+200,stage, c)
            self.uppdateDBO(sql,val)
            sql= "UPDATE hero SET heroHP = %s WHERE username = %s and HeroName = %s"
            val = (a,c,d)
            self.uppdateDBO(sql,val)
            self.menu()
        else:
            pass



class HeroFist(Hero):
    def __init__(self,stage):
        self.name = 'Lucas'
        self.role = 'Fist'
        self.attack = 30 + (stage * 1.6 * 30)
        self.hp = 170 + (stage * 1.6 * 170)
        self.maxHP = 170 + (stage * 1.6 *170)
    #override
    def menyerang(self,hero,lawan):
        print(hero.name + " menghantam " + lawan.name)
        lawan.hp = lawan.hp - hero.attack

        


class HeroBow(Hero):
    def __init__(self,stage):
        self.name = 'KimShin'
        self.role = 'Bow'
        self.attack = 50 + (stage * 1.7 * 50)
        self.hp = 75 + (stage * 1.8 * 75)
        self.maxHP = 75 + (stage * 1.8 * 75)
    #override
    def menyerang(self,hero,lawan):
        print(hero.name + " menembak " + lawan.name)
        lawan.hp = lawan.hp - hero.attack


class HeroSword(Hero):
    def __init__(self,stage):
        self.name = 'AliBaBa'
        self.role = 'Sword'
        self.attack = 35 + (stage * 1.5 * 35)
        self.hp = 80 + (stage * 1.7 * 80)
        self.maxHP = 80 + (stage * 1.7 * 80)
    #override
    def menyerang(self,hero,lawan):
        print(hero.name + " menebas " + lawan.name)
        lawan.hp = lawan.hp - hero.attack




class User(HeroBow,HeroFist,HeroSword):
    def __init__(self,username,stage):
        self.username = username
        self.__stage = stage
        try:
            self.con=mysql.connector.connect(
                host="localhost",
                user="root",
                database="BurningHeroes"
            )
            self.cursor= self.con.cursor()
        except:
            a = input("Database belum terkoneksi, silahkan koneksikan database terlebih dahulu!\nTekan apa saja untuk melanjutkan ")
            exit()

    #encapsulation
    def set_stage(self,stage):
        self.__stage = stage
        return self.__stage

    def get_stage(self):
        return self.__stage

    def viewHero(self,userHero):
        if userHero is None:
            print("Mohon maaf inventory anda kosong!")
        else:
            header = ['Nama','Role','Attack','HP','Max HP']
            self.showData(header,userHero)

    def inventory(self):
        self.cursor.execute("Select NamaItem, value, storage, notes From item where username = '{}'".format(self.username))
        userItem = list(self.cursor.fetchall())
        self.cursor.execute("Select koins,stage From user where username = '{}'".format(self.username))
        userKoins = list(self.cursor.fetchall())
        print("Koin anda \t: ",userKoins[0][0])
        print("Stage anda \t: ",userKoins[0][1],'\n')
        self.set_stage(userKoins[0][1])
        if userItem is None:
            print("Mohon maaf inventory anda kosong!") 
        else:
            header = ['Nama Item','Nilai','Jumlah Item','Keterangan']
            self.showData(header,userItem)
            return userItem

    def cekHero(self,userHero,pilihan1,pilihan2):
        if pilihan1 != pilihan2:
            for a in range(len(userHero)):
                if pilihan1 in userHero[a]:
                    userHero2 = []
                    userHero2.append(list(userHero[a]))
                    for a in range(len(userHero)):
                        if pilihan2 in userHero[a]:
                            userHero2.append(list(userHero[a]))
                            return True and userHero2
            else:
                print("Inputan salah, silahkan menginput kembali dengan benar!")
        else:
            print("Hero yang dipilih tidak boleh sama!")

    def updateItem(self,item,userItem):
        userItem2 = []
        for a in range(len(userItem)):
            userItem2.append(list(userItem[a]))
        userItem = userItem2
        a = input()
        if item == 'potion':
            indeks = 0
        elif item == 'machinegun':
            indeks = 1
        else:
            indeks = 2
        userItem[indeks][2] = userItem[indeks][2] - 1
        sql= "UPDATE item SET storage = %s WHERE username = %s and NamaItem = %s"
        val = (userItem[indeks][2], self.username,item)
        self.uppdateDBO(sql,val)
        return userItem[indeks][2]

    def uppdateDBO(self,sql,val):
        try:
            self.cursor.execute(sql, val)
            self.con.commit()
            clear()
            print("Data berhasil diupdate")
        except mysql.connector.Error as e:
            print("c")
            print(format(e))

    def fight(self):
        while True:
            print("Silahkan memilih hero yang ingin digunakan!\n")
            self.cursor.execute("Select HeroName, HeroRole,HeroAttack,HeroHP,MaxHP From hero where username = '{}'".format(self.username))
            userHero = list(self.cursor.fetchall())
            self.viewHero(userHero)
            print()
            pilihan1 = input("Nama Hero pertama yang dipilih : ")
            pilihan2 = input("Nama Hero kedua yang dipilih : ")
            pilihan1 = pilihan1.lower()
            pilihan2 = pilihan2.lower()
            clear()
            if self.cekHero(userHero,pilihan1,pilihan2):
                userHero = self.cekHero(userHero,pilihan1,pilihan2)
                break
        while True:
            self.cursor.execute("Select HeroName, HeroRole,HeroAttack,HeroHP,MaxHP From hero where username = '{}'".format(self.username))
            userHero = list(self.cursor.fetchall())
            userHero = self.cekHero(userHero,pilihan1,pilihan2)
            print("Hero yang digunakan : ")
            self.viewHero(userHero)
            print("\nSilahkan memilih item yang ingin digunakan!\n")
            userItem = self.inventory()
            print("\nMasukkan 0 apabila tidak ingin menggunakan item dan masukkan 'menu' apabila ingin kembali ke menu utama\n")
            item = input("Nama item yang ingin digunakan : ")
            item = item.lower()
            if item == 'potion' or item == 'machinegun' or item == 'soultrap':
                while True:
                    pilih = input("Nama Hero yang dipilih : ")
                    if pilih == pilihan1 or pilih == pilihan2:
                        break
                    else:
                        print("Inputan salah, silahkan menginput nama hero dengan benar!")
                if item == 'potion':
                    indek = 3
                    value = 10
                elif item == 'machinegun':
                    indek = 2
                    value = 20
                else:
                    indek = 4
                    value = 20
                for a in range(len(userHero)):
                    if pilih in userHero[a]:
                        if item == 'potion':
                            value = userHero[a][3] + value
                            if value > userHero[a][indek]:
                                value = userHero[a][4]
                            sql= "UPDATE hero SET heroHP = %s WHERE username = %s and HeroName = %s"
                        elif item == 'machinegun':
                            value = userHero[a][indek] + value
                            sql= "UPDATE hero SET heroAttack = %s WHERE username = %s and HeroName = %s"
                        else:
                            value = userHero[a][indek] + value
                            sql= "UPDATE hero SET maxHP = %s WHERE username = %s and HeroName = %s"
                        val = (value,self.username,pilih)
                        self.uppdateDBO(sql,val)
                        userItem = self.updateItem(item,userItem)
                        userHero[a][indek] = value
                print(f'{item} berhasil digunakan pada hero {pilih}')
                print("Apakah anda ingin menggunakan item lagi?\n")
            elif item == 'menu':
                self.menu()
            elif item == '0':
                break
            else:
                clear()
                print("Inputan salah, silahkan menginput kembali dengan benar!")
        clear()
        print("Pertandingan dimulai!!!\n")
        acak = random.randint(0,2)
        botStage = [
['Lucas','Fist'],
['KimShin','Bow'],
['AliBaBa','Sword'],
['Lucas','Fist'],
['KimShin','Bow'],
['AliBaBa','Sword'],
['Lucas','Fist'],
['KimShin','Bow'],
['AliBaBa','Sword'],
['Lucas','Fist']]
        c = ['musuh1','musuh2','hero1','hero2']
        stage = self.get_stage()
        self.prepare(c,botStage,stage,userHero)
        x = 0
        y = 2
        if acak == 1:
            print("Anda mendapat giliran pertama\n")
            self.userTurn(c,x,y)
        else:
            print("Komputer mendapat giliran pertama\n")
            self.botTurn(c,x,y)
            
    def infoGame(self,hero,lawan):
        HeroInGame = [
['Nama Hero',hero.name,'',lawan.name],
['Role Hero',hero.role,'',lawan.role],
['Attack Point',hero.attack,'',lawan.attack],
['HP / MaxHP',f'{hero.hp} / {hero.maxHP}','',f'{lawan.hp} / {lawan.maxHP}']]
        header = ['','USER','vs','KOMPUTER']
        self.showData(header,HeroInGame)
        self.cekKemenangan(hero.hp,lawan.hp,self.username,hero.name)
        
    def botTurn(self,c,x,y):
        print("\nBot Turn")
        self.infoGame(c[y],c[x])
        botChoice = random.randint(1,3)
        if botChoice == 1   :
            print("\n-----Bot menyerang")
            self.menyerang(c[x],c[y])
        else:
            print("\n-----Bot ganti hero")
            if x == 0:
                x = 1
            else:
                x = 0
        self.userTurn(c,x,y)

    def userTurn(self,c,x,y):
        self.infoGame(c[y],c[x])
        while True:
            pilihan = input('''
Menu pilihan :
1. Menyerang
2. Ganti Hero
Pilihan anda : ''')
            clear()
            if pilihan == '1':
                self.menyerang(c[y],c[x])
                self.botTurn(c,x,y)
            elif pilihan == '2':
                if y == 2:
                    y = 3
                else:
                    y = 2
                self.botTurn(c,x,y)
            else:
                print("Inputan salah mohon menginput dengan benar!")


    def prepare(self,c,botStage,stage,userHero):
        party = []
        party.append(botStage[stage + stage])
        party.append(botStage[stage + stage + 1])
        party.append(userHero[0])
        party.append(userHero[1])
        for a in range(2):
            if party[a][1] == 'Fist':
                c[a] = HeroFist(stage)
            elif party[a][1] == 'Bow':
                c[a] = HeroBow(stage)
            else:
                c[a] = HeroSword(stage)
        for a in range(2):
            b = a + 2
            c[b] = Hero(userHero[a][0],userHero[a][1],userHero[a][2],userHero[a][3],userHero[a][4])

    def shop(self):
        self.cursor.execute("Select NamaItem,price,notes From item where ItemID <= 3")
        res = self.cursor.fetchall()
        self.cursor.execute("Select koins From user where username = '{}'".format(self.username))
        koin = list(self.cursor.fetchall())
        print("Koin anda : ",koin[0][0],'\n')
        header = ["Nama","Harga","Keterangan"]
        self.showData(header,res)
        while True:
            item = input("Nama item yang ingin dibeli : ")
            item = item.lower()
            if item == 'potion' or item == 'machinegun' or item == 'soultrap':
                break
            else:
                print("Inputan salah, mohon masukkan input dengan benar!")
        self.cursor.execute("Select storage From item where username = '{}' and NamaItem = '{}'".format(self.username,item))
        storage = self.cursor.fetchall()
        for a in range(len(item)):
            if res[a][0] == item:
                koins = res[a][1]
                break
        print("Masukkan 0 apabila tidak ingin membeli item!")
        while True:
            jumlah = input("Jumlah {} yang ingin dibeli : ".format(item))
            try:
                jumlah = int(jumlah)
                break
            except:
                clear()
                print("Inputan harus dalam bentuk angka!")
        if jumlah < 0:
            print("Mohon maaf inputan salah, silahkan inputkan kembali dengan benar!")
        elif jumlah == 0:
            self.menu()
        else:
            if jumlah*koins <= koin[0][0]:
                sql= "UPDATE item SET storage = %s WHERE username = %s and NamaItem = %s"
                val = (jumlah + storage[0][0], self.username,item)
                self.uppdateDBO(sql,val)
                sql= "UPDATE user SET koins = %s WHERE username = %s"
                val = (koin[0][0]-(jumlah*koins), self.username)
                self.uppdateDBO(sql,val)
            else:
                print("Mohon maaf koin anda tidak mencukupi ")

    def showData(self,header,res):
        isi = []
        for a in res:
            isi.append(a)
        print(tabulate(isi, headers = header))

    def menu(self):
        print('''Menu :
1. Fight
2. Shop
3. Inventory
4. Petunjuk Permainan
5. Log Out
6. Exit''')
        pilihan = input("Pilihan anda : ")
        clear()
        if pilihan == '1':
            self.fight()
        elif pilihan == '2':
            self.shop()
        elif pilihan == '3':
            self.inventory()
        elif pilihan == '4':
            print('''
1. Menu Figth\n\tUser diharuskan memilih 2 hero dari 3 hero yang ada, kemudian user dapat memilih menggunakan item yang dimiliki kepada hero yang dipilih. Lawan akan terus bertingkat seiring bertambahnya stage. Untuk memenangkan fight maka harus menghabiskan salah satu dari HP hero lawan dan apabila User menang maka stage akan bertambah
\n2. Menu Shop\n\tUser dapat membeli item melalui fitur menu
\n3. Menu Inventory\n\tUser dapat melihat stage, jumlah koin dan item yang dimiliki''')
        elif pilihan == '5':
            start()
        elif pilihan == '6':
            exit()
        else:
            print("Mohon maaf pilihan tidak ada, silahkan memilih kembali")
        a = input("\nTekan enter untuk melanjutkan")
        clear()
        self.menu()

victory ='''
   QQQ       QQQ QQQ    QQQQQQQQQ   QQQQQQQQQQQ   QQQQQQQQQ    QQQQQQQQQ  QQQ    QQQ
    QQQ     QQQ  QQQ   QQQQ   QQQQ  QQQQQQQQQQQ  QQQQ   QQQQ   QQQ     QQ  QQQ  QQQ 
     QQQ   QQQ   QQQ  QQQQ     QQQQ     QQQ     QQQQ     QQQQ  QQQ      QQ  QQ  QQ  
      QQQ QQQ    QQQ QQQQ               QQQ    QQQQ       QQQQ QQQ     QQ    QQQQ   
       QQQQQ     QQQ  QQQQ     QQQQ     QQQ     QQQQ     QQQQ  QQQQQQQQ      QQQQ   
        QQQ      QQQ   QQQQ   QQQQ      QQQ      QQQQ   QQQQ   QQQ    QQ     QQQQ   
         Q       QQQ    QQQQQQQQQ       QQQ       QQQQQQQQQ    QQQ     QQ    QQQQ   '''

defeat = '''
QQQQQQQ    QQQQQQQQ QQQQQQQQ QQQQQQQQ       Q     QQQQQQQQQQQ
QQQ   QQ   QQQ      QQQ      QQQ           QQQ    QQQQQQQQQQQ
QQQ    QQ  QQQ      QQQ      QQQ          QQQQQ       QQQ
QQQ     QQ QQQQQQQQ QQQQQQQQ QQQQQQQQ    QQQ QQQ      QQQ
QQQ    QQ  QQQ      QQQ      QQQ        QQQ   QQQ     QQQ
QQQ   QQ   QQQ      QQQ      QQQ       QQQ QQQ QQQ    QQQ
QQQQQQQ    QQQQQQQQ QQQ      QQQQQQQQ QQQ       QQQ   QQQ
'''
clear()
a = start()
b = stageFinder(a)
clear()
testing = User(a,b)
testing.menu()
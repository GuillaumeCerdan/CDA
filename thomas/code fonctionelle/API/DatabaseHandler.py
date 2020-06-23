import mysql.connector


class DatabaseHandler:
    connecteur = ''
    cursor = ''
    def __init__(self, database, login, password, host):
        self.connecteur = self.connecter(database, login, password, host)
        self.cursor = self.connecteur.cursor()

    def connecter(self, database, login, password, host):
        connecteur = mysql.connector.connect(
            host = host, 
            user = login,
            password = password,
            database = database,
            charset = 'utf8'
        )
        return(connecteur)

    def get_all_data(self):
        request = '''
        SELECT arrete.id as arreteId, arrete.extrait AS arreteExtrait, arrete.score AS arreteScore, raa.id AS RaaId, raa.titre as RaaTitre, raa.source as raaSource, prefecture.id as PrefId, prefecture.nom as prefNom
        FROM arrete, prefecture, raa 
        WHERE arrete.raaId = raa.id AND prefecture.id = raa.prefecturId
        '''
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return(result)
    
    def add_prefecture(self, id, nom, lon, lat,lien ):
        request = f'''
        INSERT INTO prefecture(id, nom, longitude, latitude, lien) 
        VALUES ('{id}','{nom}',{lon},{lat},'{lien}')
        '''
        self.cursor.execute(request)
        self.connecteur.commit()

    def get_Id_Pref(self, nomPref):
        request= f'''
        SELECT prefecture.id FROM `prefecture` WHERE prefecture.nom = '{nomPref}'
        '''
        self.cursor.execute(request)
        result = self.cursor.fetchall()[0] 
        return(result)
    
    def add_raa(self,id, titre, date, source,nomPref):
        request = f'''
        INSERT INTO `raa`(`id`, `titre`, `date`, `source`, `prefecturId`) 
        VALUES ('{id}','{titre}','{date}','{source}','{self.get_Id_Pref(nomPref)}')
        '''
        self.cursor.execute(request)
        self.connecteur.commit()
    
    def get_id_raa(self, titre_raa): 
        request = f'''
        SELECT raa.id FROM raa WHERE titre = '{titre_raa}'
        '''     
        self.cursor.execute(request)
        result = self.cursor.fetchall()[0]
        return(result)

    def add_arrete(self,idArrete, extrait, score, titre_raa ):
        request = f'''
        INSERT INTO `arrete`(`id`, `extrait`, `score`, `raaId`) 
        VALUES ('{idArrete}','{extrait}',{score},{self.get_id_raa(titre_raa)})
        '''
        print(request)
        self.cursor.execute(request)
        self.connecteur.commit()

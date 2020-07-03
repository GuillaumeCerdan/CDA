import mysql.connector


class DatabaseHandler:
    connecteur = ''
    cursor = ''

    def __init__(self, database, login, password, host):
        """
        methode qui permet d'initialisé l'objet DatabaseHandler et ce
        créé les attribut connecteur et cursor
        -------------------------------------------------------
        database = le nom de la base de données
        login = le login de connection a la base de données
        password = le mot de passe de la base de données
        host =  l'hote du serveur de base de données
        -------------------------------------------------------
        """
        self.connecteur = self.connecter(database, login, password, host)
        self.cursor = self.connecteur.cursor()

    def connecter(self, database, login, password, host):
        """
        methode qui permet de ce connecter à la base de données
        -------------------------------------------------------
        database = le nom de la base de données
        login = le login de connection a la base de données
        password = le mot de passe de la base de données
        host =  l'hote du serveur de base de données
        -------------------------------------------------------
        retourn l'objet de connexion
        """
        connecteur = mysql.connector.connect(
            host=host,
            user=login,
            password=password,
            database=database,
            charset='utf8'
        )
        return(connecteur)

    def get_all_data(self):
        """
        methode qui permet de recupéré toute les données relative au
        arrete
        -------------------------------------------------------
        -------------------------------------------------------
        retourn la liste de données recupéré dans la base de données
        """
        request = '''
        SELECT arrete.id as arreteId, arrete.extrait AS arreteExtrait,
        arrete.score AS arreteScore, raa.id AS RaaId, raa.titre as RaaTitre,
        raa.source as raaSource, prefecture.id as PrefId,
        prefecture.nom as prefNom
        FROM arrete, prefecture, raa
        WHERE arrete.raaId = raa.id AND prefecture.id = raa.prefecturId
        '''
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return(result)

    def add_prefecture(self, id, nom, lien, lon=0, lat=0):
        """
        methode qui permet d'ajouter une prefecture
        -------------------------------------------------------
        id = id de la prefecture
        nom = nom de la prefecture
        lien = lien vers la prefecture
        long = longitude du lieux de la prefecture
        lat = latitude du lieux de la prefecture
        -------------------------------------------------------
        """
        request = f'''
        INSERT INTO prefecture(id, nom, longitude, latitude, lien)
        VALUES ('{id}','{nom}',{lon},{lat},'{lien}')
        '''
        self.cursor.execute(request)
        self.connecteur.commit()

    def get_Id_Pref(self, nom_Pref):
        """
        methode qui recupere l'id de la prefecture avec son nom
        -------------------------------------------------------
        nom_Pref = nom de la prefecture
        -------------------------------------------------------
        retourne le resultat de la requette
        """
        request = f'''
        SELECT prefecture.id FROM `prefecture`
        WHERE prefecture.nom = '{nom_Pref}'
        '''
        self.cursor.execute(request)
        result = self.cursor.fetchall()[0]
        return(result)

    def add_raa(self, id, titre, date, source, nom_Pref):
        """
        methode qui permet d'ajouter un RAA
        -------------------------------------------------------
        id = id du RAA
        titre = titre du RAA
        date =  la date de reception du RAA
        source = source vers le RAA
        nom_Pref = nom de la prefecture qui a emmit le RAA
        -------------------------------------------------------
        """
        request = f'''
        INSERT INTO `raa`(`id`, `titre`, `date`, `source`, `prefecturId`)
        VALUES ('{id}','{titre}','{date}','{source}','
        {self.get_Id_Pref(nom_Pref)}')
        '''
        self.cursor.execute(request)
        self.connecteur.commit()

    def get_id_raa(self, titre_raa):
        """
        methode qui recupere l'id du RAA avec son nom
        -------------------------------------------------------
        titre_raa = nom de la prefecture
        -------------------------------------------------------
        retourne le resultat de la requette
        """
        request = f'''
        SELECT raa.id FROM raa WHERE titre = '{titre_raa}'
        '''
        self.cursor.execute(request)
        result = self.cursor.fetchall()[0]
        return(result)

    def add_arrete(self, id_arrete, extrait, score=0, titre_raa='raa test'):
        """
        methode qui permet d'ajouter un arrete dans la base de données
        -------------------------------------------------------
        id_arrete = l'id d'un arrete
        extrait = l'extrait de l'arrete
        score = le score de l'arrete
        titre_raa = le titre du raa qui comporte l'arrete
        -------------------------------------------------------
        """
        request = f'''
        INSERT INTO `arrete`(`id`, `extrait`, `score`, `raaId`)
        VALUES ('{id_arrete}',"{extrait}",{score},"1")
        '''
        self.cursor.execute(request)
        self.connecteur.commit()

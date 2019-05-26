import logging as log
import mysql.connector as mariadb

log.basicConfig(filename='database.log',level=log.DEBUG)

mariadb_connection = mariadb.connect(host="localhost", user='brie', password='3th3rn3t', db='Brie')
cursor = mariadb_connection.cursor()

# Enable autocommit
cursor.execute("SET AUTOCOMMIT=1") # https://mariadb.com/resources/blog/every-select-from-your-python-program-may-acquire-a-metadata-lock/
cursor.commit() # not sure if this is needed.

class Database():

    #########################
    #                       #
    #       USER TABLE      #
    #                       #
    #########################

    async def create_new_user(username):
        '''
        Creates new user entry with default values from config.
        '''
        try:
            cursor.execute(
                "INSERT INTO users (username,createdTimestamp,updatedTimestamp,bondLevel,hasFedBrie,lastFedBrieTimestamp,bondsAvailable,happinessLevel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", 
                (username,createdTimestamp,updatedTimestamp,bondLevel,hasFedBrie,lastFedBrieTimestamp,bondsAvailable,happinessLevel)
            )
        except mariadb.Error as error:
            log.error("Failed to create new user: %s", error)

    async def get_created_timestamp(username):
        '''
        Returns timestamp for when the user entry was created.
        '''

    async def get_last_update_timestamp(username):
        '''
        Returns the last time the given User's entry was updated.
        '''

    #################
    #   Affection   #
    #################
    async def set_affection(username, points):
        '''
        Sets User's affections points to a given value.
        '''

    async def add_affection(username, points):
        '''
        Increases given User's affection points by given value.
        - points must be positive int.
        '''

    async def remove_affection(username, points):
        '''
        Decreases given User's affection points by given value.
        - points must be a positive int.
        '''

    async def get_affection(username):
        '''
        Returns User's current affection level
        '''

    ###################
    #   Bond Levels   #
    ###################
    async def set_bond_level(username, level):
        '''
        Sets User's bond level to given value.
        '''

    async def add_bond_level(username, level):
        '''
        Increases User's bond level to given value.
        - level must be a positive int.
        '''
    
    async def remove_bond_level(username, level):
        '''
        Decreases given User's bond level by given value.
        - level must be a positive int.
        '''

    async def get_bond_level(username):
        '''
        Returns User's current bond level.
        '''

    #############
    #   Bonds   #
    #############
    async def set_bonds_available(username, bonds):
        '''
        Sets User's bonds available to them.
        '''

    async def add_bonds(username, bonds):
        '''
        Increases User's bonds by given value.
        - bonds must be a positive int.
        '''

    async def remove_bonds(username, bonds):
        '''
        Decreases User's bond by given value.
        - bonds must be a positive int.
        '''

    async def get_bonds(username):
        '''
        Returns User's available bonds.
        '''

    #################
    #   Feeding     #
    #################
    async def set_has_fed_brie(username, has_fed):
        '''
        Sets User's has_fed status.
        - has_fed must be a Boolean, this will be saved as a 1 (True) or 0 (False).
        - If has_fed is True, update the lastFedBrieTimestamp value as well.
        '''

    async def flip_has_fed_brie(username):
        '''
        Flips the value of the given User's has_fed status.
        '''

    async def get_last_fed_timestamp(username):
        '''
        Returns timestamp of User's last feeding.
        '''

    #################
    #   Happiness   #
    #################

    async def set_current_happiness_level(username, level):
        '''
        Sets current happiness level for a given user.
        '''

    async def add_current_happiness_level(username, amount):
        '''
        Increases current happiness level by given amount for a given user.
        '''

    async def get_current_happiness_level(username):
        '''
        Returns current happiness level for a given user.
        '''
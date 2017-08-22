import abc
from reconbot.notificationprinters.printer import Printer

class Slack(Printer):

    def get_corporation(self, corporation_id, alliance_id=None):
        name = self.eve.get_corporation_name_by_id(corporation_id)
        result = '<https://zkillboard.com/corporation/%d/|%s>' % (corporation_id, name)

        if alliance_id:
            result = '%s (%s)' % (result, self.get_alliance(alliance_id))

        return result

    def get_alliance(self, alliance_id):
        name = self.eve.get_alliance_name_by_id(alliance_id)
        return '<https://zkillboard.com/alliance/%d/|%s>' % (alliance_id, name)

    def get_system(self, system_id):
        system = self.eve.get_system_by_id(system_id)
        return '<http://evemaps.dotlan.net/system/%s|%s>' % (system['name'], system['name'])

    def get_character(self, character_id):
        character = self.eve.get_character_by_id(character_id)

        if 'alliance' in character:
            alliance_id = character['alliance']['id']
        else:
            alliance_id = None

        return '<https://zkillboard.com/character/%d/|%s> (%s)' % (
            character['id'],
            character['name'],
            self.get_corporation(character['corp']['id'], alliance_id)
        )

'''
Tracker
Made by: Oscar Blanco and Victor Colome
'''

from swarm import Swarm
from pyactor.context import interval


class Tracker(object):
    _tell = ['announce', 'init_start', 'check_peers']
    _ask = ['get_peers']
    _ref = ['announce', 'get_peers']

    def __init__(self):
        self.peers = {}

    def init_start(self):
        self.interval_check = interval(self.host, 1, self.proxy, 'check_peers')

    def check_peers(self):
        for peers in self.peers.values():
            peers.remove_unannounced()

    def announce(self, torrent_hash, peer_ref):
        try:
            self.peers[torrent_hash].update(peer_ref)
        except KeyError:
            self.peers[torrent_hash] = Swarm(peer_ref)

    def get_peers(self, torrent_hash, torrent_id=False):
        try:
            if torrent_id:
                return self.peers[torrent_hash].get_peers_id()
            else:
                return self.peers[torrent_hash].get_peers()
        except KeyError:
            return []

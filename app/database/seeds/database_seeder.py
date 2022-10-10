from orator.seeds import Seeder

from .team_mst_seeder import TeamMstSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(TeamMstSeeder)


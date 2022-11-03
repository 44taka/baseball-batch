from orator.migrations import Migration


class CreateTeamMst(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('team_mst') as table:
            table.increments('id')
            table.small_integer('league_kbn')
            table.string('team_name', 50)
            table.string('team_color_cd', 10)
            table.integer('yahoo_team_id').unsigned()
            table.boolean('is_deleted').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('team_mst')

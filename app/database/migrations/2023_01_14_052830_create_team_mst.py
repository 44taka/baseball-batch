from orator.migrations import Migration


class CreateTeamMst(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('team_mst') as table:
            table.increments('id')
            table.small_integer('league_kbn')
            table.string('code', 2).unique()
            table.string('name', 50)
            table.string('short_name', 10)
            table.string('color', 10)
            table.boolean('is_deleted').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('team_mst')

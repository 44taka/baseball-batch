from orator.migrations import Migration


class CreateScoreboardTbl(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('scoreboard_tbl') as table:
            table.increments('id')
            table.date('date')
            table.integer('team_id').unsigned()
            table.integer('vs_team_id').unsigned()
            table.boolean('win').default(0)
            table.boolean('lose').default(0)
            table.boolean('draw').default(0)
            # 得点
            table.integer('runs_scored').unsigned()
            # 失点
            table.integer('runs_allowed').unsigned()
            table.integer('rank').unsigned()
            table.boolean('is_deleted').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('scoreboard_tbl')

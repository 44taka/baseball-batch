from orator.migrations import Migration


class CreateWinLossTbl(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('win_loss_tbl') as table:
            table.increments('id')
            table.date('date')
            table.small_integer('game_status')
            table.boolean('is_win').default(0)
            table.boolean('is_lose').default(0)
            table.boolean('is_draw').default(0)
            table.boolean('is_deleted').default(0)
            table.integer('team_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('win_loss_tbl')

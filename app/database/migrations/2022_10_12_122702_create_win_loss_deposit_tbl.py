from orator.migrations import Migration


class CreateWinLossDepositTbl(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('win_loss_deposit_tbl') as table:
            table.increments('id')
            table.date('date')
            table.integer('deposit')
            table.integer('team_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('win_loss_deposit_tbl')

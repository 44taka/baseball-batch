from orator.migrations import Migration


class CreateScheduleMst(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('schedule_mst') as table:
            table.increments('id')
            table.small_integer('schedule_kbn')
            table.date('start_date')
            table.date('end_date')
            table.boolean('is_deleted').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop_if_exists('schedule_mst')

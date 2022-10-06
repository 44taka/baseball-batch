from orator.seeds import Seeder


class TeamMstSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        # DB登録データ
        data = [
            {
                'id': 1,
                'league_kbn': 1,
                'team_name': '東京ヤクルトスワローズ'
            },
            {
                'id': 2,
                'league_kbn': 1,
                'team_name': '阪神タイガース'
            },
            {
                'id': 3,
                'league_kbn': 1,
                'team_name': '読売ジャイアンツ'
            },
            {
                'id': 4,
                'league_kbn': 1,
                'team_name': '広島東洋カープ'
            },
            {
                'id': 5,
                'league_kbn': 1,
                'team_name': '中日ドラゴンズ'
            },
            {
                'id': 6,
                'league_kbn': 1,
                'team_name': '横浜DeNAベイスターズ'
            },
            {
                'id': 7,
                'league_kbn': 2,
                'team_name': 'オリックスバファローズ'
            },
            {
                'id': 8,
                'league_kbn': 2,
                'team_name': '千葉ロッテマリーンズ'
            },
            {
                'id': 9,
                'league_kbn': 2,
                'team_name': '東北楽天ゴールデンイーグルス'
            },
            {
                'id': 10,
                'league_kbn': 2,
                'team_name': '福岡ソフトバンクホークス'
            },
            {
                'id': 11,
                'league_kbn': 2,
                'team_name': '北海道日本ハムファイターズ'
            },
            {
                'id': 12,
                'league_kbn': 2,
                'team_name': '埼玉西武ライオンズ'
            },
        ]
        # DBにデータがないものだけ登録
        for datum in data:
            result = self.db.table('team_mst').where('id', datum['id']).first()
            if result is None:
                self.db.table('team_mst').insert(data)

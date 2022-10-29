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
                'team_name': '東京ヤクルトスワローズ',
                'yahoo_team_id': 2
            },
            {
                'id': 2,
                'league_kbn': 1,
                'team_name': '阪神タイガース',
                'yahoo_team_id': 5
            },
            {
                'id': 3,
                'league_kbn': 1,
                'team_name': '読売ジャイアンツ',
                'yahoo_team_id': 1
            },
            {
                'id': 4,
                'league_kbn': 1,
                'team_name': '広島東洋カープ',
                'yahoo_team_id': 6
            },
            {
                'id': 5,
                'league_kbn': 1,
                'team_name': '中日ドラゴンズ',
                'yahoo_team_id': 4
            },
            {
                'id': 6,
                'league_kbn': 1,
                'team_name': '横浜DeNAベイスターズ',
                'yahoo_team_id': 3
            },
            {
                'id': 7,
                'league_kbn': 2,
                'team_name': 'オリックスバファローズ',
                'yahoo_team_id': 11
            },
            {
                'id': 8,
                'league_kbn': 2,
                'team_name': '千葉ロッテマリーンズ',
                'yahoo_team_id': 9
            },
            {
                'id': 9,
                'league_kbn': 2,
                'team_name': '東北楽天ゴールデンイーグルス',
                'yahoo_team_id': 376
            },
            {
                'id': 10,
                'league_kbn': 2,
                'team_name': '福岡ソフトバンクホークス',
                'yahoo_team_id': 12
            },
            {
                'id': 11,
                'league_kbn': 2,
                'team_name': '北海道日本ハムファイターズ',
                'yahoo_team_id': 8
            },
            {
                'id': 12,
                'league_kbn': 2,
                'team_name': '埼玉西武ライオンズ',
                'yahoo_team_id': 7
            },
        ]
        # DBにデータがないものだけ登録
        for datum in data:
            result = self.db.table('team_mst').where('id', datum['id']).first()
            if result is None:
                self.db.table('team_mst').insert(data)

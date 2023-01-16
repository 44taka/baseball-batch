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
                'code': 's',
                'name': '東京ヤクルトスワローズ',
                'short_name': 'ヤクルト',
                'color': '#1a854f',
            },
            {
                'id': 2,
                'league_kbn': 1,
                'code': 't',
                'name': '阪神タイガース',
                'short_name': '阪神',
                'color': '#ffdd00',
            },
            {
                'id': 3,
                'league_kbn': 1,
                'code': 'g',
                'name': '読売ジャイアンツ',
                'short_name': '巨人',
                'color': '#ef8200',
            },
            {
                'id': 4,
                'league_kbn': 1,
                'code': 'c',
                'name': '広島東洋カープ',
                'short_name': '広島',
                'color': '#c10016',
            },
            {
                'id': 5,
                'league_kbn': 1,
                'code': 'd',
                'name': '中日ドラゴンズ',
                'short_name': '中日',
                'color': '#104f8f',
            },
            {
                'id': 6,
                'league_kbn': 1,
                'code': 'db',
                'name': '横浜DeNAベイスターズ',
                'short_name': 'DeNA',
                'color': '#0096e0',
            },
            {
                'id': 7,
                'league_kbn': 2,
                'code': 'b',
                'name': 'オリックスバファローズ',
                'short_name': 'オリックス',
                'color': '#43469c',
            },
            {
                'id': 8,
                'league_kbn': 2,
                'code': 'm',
                'name': '千葉ロッテマリーンズ',
                'short_name': 'ロッテ',
                'color': '#818181',
            },
            {
                'id': 9,
                'league_kbn': 2,
                'code': 'e',
                'name': '東北楽天ゴールデンイーグルス',
                'short_name': '楽天',
                'color': '#940028',
            },
            {
                'id': 10,
                'league_kbn': 2,
                'code': 'h',
                'name': '福岡ソフトバンクホークス',
                'short_name': 'ソフトバンク',
                'color': '#ffb300',
            },
            {
                'id': 11,
                'league_kbn': 2,
                'code': 'f',
                'name': '北海道日本ハムファイターズ',
                'short_name': '日本ハム',
                'color': '#00558c',
            },
            {
                'id': 12,
                'league_kbn': 2,
                'code': 'l',
                'name': '埼玉西武ライオンズ',
                'short_name': '西武',
                'color': '#213258',
            },
        ]
        # DBにデータがないものだけ登録
        for datum in data:
            result = self.db.table('team_mst').where('id', datum['id']).first()
            if result is None:
                self.db.table('team_mst').insert(data)

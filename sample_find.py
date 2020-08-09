#! -*- coding:utf-8 -*-

import geolonia


def sample_find(geo, pref, city, area):
    lng, lat = geo.find_long_lat(pref, city, area)
    print(pref, city, area, lng, lat)


def main():
    geo = geolonia.Geolonia()
    sample_find(geo, '東京都', '千代田区', '千代田')
    sample_find(geo, '京都府', '京都市中京区', '二条城町')
    sample_find(geo, '福岡県', '太宰府市', '宰府四丁目')
    sample_find(geo, '沖縄県', '国頭郡本部町', '字石川')
    sample_find(geo, 'XX県', 'XX市', 'XXX')


if __name__ == '__main__':
    main()

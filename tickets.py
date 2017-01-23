# /usr/bin/python3.
# -*- coding: utf-8 -*-

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

def cli():
    from docopt import docopt
    from stations import stations
    import get_data
    import formats

    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    #print(options)
    get_data = get_data.GetData(date, from_station, to_station)
    result = get_data.request_12306()
    if result['httpstatus'] == 200 and result.get('data') is not None and result.get('data') != '':
        format_result = formats.Formats(result.get('data'), options)
        return format_result.format_data()
    else:
        return result['messages']

if __name__ == '__main__':
    print(cli())


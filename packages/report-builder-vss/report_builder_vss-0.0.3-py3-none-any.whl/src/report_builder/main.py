import datetime
import argparse

parser = argparse.ArgumentParser(description="fill string")
parser.add_argument('--folder_path', metavar='folder_path', default="src/materials", type=str, help="write folder path with log files")
parser.add_argument('--driver', metavar='driver', type=str, help="if you want exect driver result, write it")
parser.add_argument('--sort', metavar='sort', choices=["asc", "desc"], type=str, help="if you want exact driver result, write it")
args = parser.parse_args()


folder_path = args.folder_path
driver = args.driver
sort = args.sort

def build_report():
    with open(f"{folder_path}/start.log", "r") as s, \
         open(f"{folder_path}/end.log", "r") as b, \
         open(f"{folder_path}/abbreviations.txt", "r") as q:
        start = s.readlines()
        end = b.readlines()
        abbreviation = q.readlines()
    conclusion_list = []
    for str_f in start:
        ls = {}
        for en in end:
            for abb in abbreviation:
                if separate(str_f)['id'] == separate(en)['id'] and separate(str_f)['id'] == separate(abb)['id']:
                    lap_time = delta_t(separate(str_f)['time'], separate(en)['time'])
                    ls = {"id": separate(str_f)['id'],
                          "Name": separate(abb)['name'],
                          "Team": separate(abb)['team'],
                          "lap_time": str(lap_time)[3:-3],
                          "for_sort": lap_time.total_seconds()}
                    conclusion_list.append(ls)

    conclusion_list = sort_list(conclusion_list)
    print_report(conclusion_list)


def print_report(lists):
    if driver:
        for n, result in enumerate(lists):
            if result["Name"] == driver:
                print(f'{n+1}. {result["Name"]} | {result["Team"]} | {result["lap_time"]}')
    else:
        for n, result in enumerate(lists[:15]):
            print(f'{n+1}. {result["Name"]} | {result["Team"]} | {result["lap_time"]}')
        print("_______________________________________________________________________")
        for n, result in enumerate(lists[15:]):
            print(f'{n+16}. {result["Name"]} | {result["Team"]} | {result["lap_time"]}')


def sort_list(lists):
    if sort == "asc":
        newlist = sorted(lists, key=lambda d: d['for_sort'], reverse=False)
    else:
        newlist = sorted(lists, key=lambda d: d['for_sort'], reverse=True)
    return newlist


def separate(ls):
    dic = {}
    try:
        dic["id"] = ls[:3]
        dic["name"] = ls.strip().split("_")[1]
        dic["team"] = ls.strip().split("_")[2]
        # print(dic)
        return dic
    except:
        dic["id"] = ls[:3]
        dic["time"] = ls.strip().split("_")[1]
        # print(dic)
        return dic


def delta_t(start, end):
    start_time = datetime.datetime.strptime(start, '%H:%M:%S.%f').time()
    end_time = datetime.datetime.strptime(end, '%H:%M:%S.%f').time()
    # print(start_time)
    # print(start_time.microsecond)
    d_start = datetime.timedelta(hours=start_time.hour,
                                 minutes=start_time.minute,
                                 seconds=start_time.second,
                                 microseconds=start_time.microsecond)
    d_end = datetime.timedelta(hours=end_time.hour,
                               minutes=end_time.minute,
                               seconds=end_time.second,
                               microseconds=end_time.microsecond)
    delta_time = d_end-d_start
    return delta_time


if __name__ == "__main__":
    build_report()
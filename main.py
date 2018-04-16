import argparse
import calendar
import datetime
import requests

from bs4 import BeautifulSoup

def main(start_year, start_month, end_year, end_month):
    song_counts = {}
    saturdays = get_saturdays(start_year, start_month, end_year, end_month)
    for saturday in saturdays:
        songs = get_billboard_top_100(saturday)
        for song in songs:
            song_counts[song] = song_counts[song] + 1 if song in song_counts else 1

    songs_ordered = [song[0] for song in reversed(sorted(song_counts.items(), key=lambda s: s[1]))]

    with open('output.txt', 'w') as f:
        f.write('\n'.join(songs_ordered))

def get_saturdays(start_year, start_month, end_year, end_month):
    today = datetime.date.today()
    saturdays = []
    curr_year = start_year
    curr_month = start_month
   
    break_year = end_year + int(end_month / 12)
    break_month = (end_month % 12) + 1
    cal = calendar.Calendar()

    while curr_year is not break_year and curr_month is not break_month:
        for week in cal.monthdayscalendar(curr_year, curr_month):
            if curr_year == today.year and curr_month == today.month and week[5] > today.day:
                continue

            if week[5] is not 0:
                    saturdays.append('{0}-{1:02d}-{2:02d}'.format(curr_year, curr_month, week[5]))
        curr_year += int(curr_month / 12)
        curr_month = (curr_month % 12) + 1

    return saturdays

def get_billboard_top_100(datestring):
    r = requests.get('https://www.billboard.com/charts/hot-100/{0}'.format(datestring))
    soup = BeautifulSoup(r.text, 'html.parser')
    songs = []

    for container in soup.find_all(lambda tag: tag.has_attr('class') and 'chart-row__container' in tag['class']):
        title = container.find(lambda tag: tag.has_attr('class') and 'chart-row__song' in tag['class']).text.strip()
        artist = container.find(lambda tag: tag.has_attr('class') and 'chart-row__artist' in tag['class']).text.strip()
        songs.append('{0} - {1}'.format(artist, title))

    return songs

def parse_args():
    today = datetime.date.today()
    curr_year = today.year
    curr_month = today.month

    parser = argparse.ArgumentParser()
    parser.add_argument('start_year', type=int, nargs='?', default=curr_year)
    parser.add_argument('start_month', type=int, nargs='?', default=curr_month)
    parser.add_argument('end_year', type=int, nargs='?', default=curr_year)
    parser.add_argument('end_month', type=int, nargs='?', default=curr_month)
    return parser.parse_args()

if __name__ == '__main__':
    main(args.start_year, args.start_month, args.end_year, args.end_month)

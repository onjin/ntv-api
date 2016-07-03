# -*- coding: utf-8 -*-
from datetime import datetime

from ntv.shortcuts import search
import parsedatetime


class Root(object):
    @property
    def resources(self):
        return [
            ChannelCollection()
        ]


class Channel(object):
    def __init__(self, id, name, movies, date=None, movie=None):
        self.id = id
        self.name = name
        self.movies = movies
        # filters
        self.date = date
        self.movie = movie

    def find_movies(self, title=None):
        if not title:
            return self.movies
        return [m for m in self.movies if title in m['title']]


class ChannelCollection(object):
    """Channels with today schedule"""

    def __init__(self):
        self.channels = {}

    def get(self, id, date=None, movie=None):
        if not date:
            date = 'today'
        cal = parsedatetime.Calendar()

        channel_id = int(id)
        date, parse_status = cal.parseDT(date)

        result = search(
            date, channel_name=None, channel_id=channel_id,
            movie_title=movie
        )
        if not result:
            return None
        channel = result[channel_id]
        if not channel:
            return None
        return Channel(**channel)

    def find(self, channel_name=None):
        date = datetime.today()
        result = search(date, channel_name=channel_name)
        if not result:
            return []
        return [
            Channel(**channel) for channel in result.values()
        ]


class Movie(object):
    def __init(self, id, title, start_time, end_time):
        self.id = None
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

channel_collection = ChannelCollection()

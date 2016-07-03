# -*- coding: utf-8 -*-
import json
import morepath

from .app import App
from . import model


def render_json(content, request):
    response = morepath.Response(
        json.dumps(
            morepath.generic.dump_json(
                request, content, lookup=request.lookup
            ), indent=2, sort_keys=True
        )
    )
    response.content_type = 'application/json'
    return response


@App.view(model=model.Root, render=render_json)
def view_root(self, request):
    return {
        '@context': {
            'schema': 'http://schema.org/',
            'Collection': 'schema:Collection'
        },
        'collections': [
            {
                '@id': request.link(r),
                '@type': 'Collection',
                'description': r.__class__.__doc__,
            } for r in self.resources
        ]
    }


@App.view(model=model.Channel, render=render_json)
def channel_default(self, request):
    return self


@App.dump_json(model=model.Channel)
def dump_channel(self, request):
    return {
        '@context': {
            'schema': 'http://schema.org/',
            'Channel': 'schema:TelevisionChannel'
        },
        '@type': 'Channel',
        '@id': request.link(self),
        'potentialAction': [
            {
                '@type': 'SearchAction',
                'target': '{}/?date={date}',
                'query-input': 'required name=date',
            },
            {
                '@type': 'SearchAction',
                'target': '{}/?movie={title}',
                'query-input': 'required name=title',
            },
        ],
        'name': self.name,
        'movies': [{
            'title': m.get('title'),
            'start_time': str(m.get('start_time')),
            'end_time': str(m.get('end_time')),
        } for m in self.movies],
    }


@App.dump_json(model=model.ChannelCollection)
def dump_channels(self, request):
    query = {}
    if 'name' in request.params:
        query['channel_name'] = request.params['name'].strip()

    return {
        '@context': {
            'schema': 'http://schema.org/',
            'Collection': 'schema:Collection'
        },
        '@id': request.link(self),
        '@type': 'Collection',
        'potentialAction': [
            {
                '@type': 'SearchAction',
                'target': '{}/?name={name}',
                'query-input': 'required name=name',
            },
        ],
        'channels': [{
                '@id': request.link(channel),
                '@type': 'Channel',
                'name': channel.name,
            } for channel in self.find(**query)
        ],
    }


@App.view(model=model.ChannelCollection, render=render_json)
def channel_collection_default(self, request):
    return self

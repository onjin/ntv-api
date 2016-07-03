from .app import App
from . import model


@App.json(model=model.Root)
def view_root(self, request):
    return [{
        '@id': request.link(r),
        'description': r.__class__.__doc__,
    } for r in self.resources]


@App.json(model=model.Channel)
def channel_default(self, request):
    return self


@App.dump_json(model=model.Channel)
def dump_channel(self, request):
    query = {}
    if 'movie' in request.params:
        query['title'] = request.params['movie'].strip()
    return {
        '@type': 'Channel',
        '@id': self.id,
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
        } for m in self.find_movies(**query)],
    }


@App.dump_json(model=model.ChannelCollection)
def dump_channels(self, request):
    query = {}
    if 'name' in request.params:
        query['channel_name'] = request.params['name'].strip()

    return {
        '@id': request.link(self),
        '@type': 'ChannelCollection',
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


@App.json(model=model.ChannelCollection)
def channel_collection_default(self, request):
    return self

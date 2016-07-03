from .app import App
from . import model


@App.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@App.path(model=model.ChannelCollection, path='/channels/')
def get_channel_collection():
    return model.channel_collection


@App.path(model=model.Channel, path='/channels/{id}')
def get_channel(id, date, movie):
    return model.channel_collection.get(id, date, movie)

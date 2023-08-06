""" Product:  mcdutils

Implement Zope sessions using memcached as the backing store.
"""


class MemCacheError(IOError):
    pass


def initialize(context):

    from .proxy import MemCacheProxy
    from .proxy import addMemCacheProxy
    from .proxy import addMemCacheProxyForm
    context.registerClass(MemCacheProxy,
                          constructors=(addMemCacheProxyForm,
                                        addMemCacheProxy),
                          icon='www/proxy.gif')

    from .sessiondata import MemCacheSessionDataContainer
    from .sessiondata import addMemCacheSessionDataContainer
    from .sessiondata import addMemCacheSessionDataContainerForm
    context.registerClass(MemCacheSessionDataContainer,
                          constructors=(addMemCacheSessionDataContainerForm,
                                        addMemCacheSessionDataContainer),
                          icon='www/sdc.gif')

    from .zcache import MemCacheZCacheManager
    from .zcache import addMemCacheZCacheManager
    from .zcache import addMemCacheZCacheManagerForm
    context.registerClass(MemCacheZCacheManager,
                          constructors=(addMemCacheZCacheManagerForm,
                                        addMemCacheZCacheManager),
                          icon='www/zcm.gif')

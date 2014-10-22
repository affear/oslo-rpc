from oslo.config import cfg

opts = [
	#cfg.StrOpt('rabbit_userid', default='affo'),
	#cfg.IntOpt('rabbit_password', default='affo'),
]

_CONF = cfg.CONF
_CONF.register_opts(opts)
CONF = _CONF

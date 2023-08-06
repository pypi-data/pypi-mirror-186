import logging

from msb_auth.users._token_user import TokenUser


def jwt_user_auth_rule(user: TokenUser):
	return user


def jwt_token_settings(**opt):
	from ._constants import JwtAuthConfig as _def
	from datetime import timedelta
	from msb_config import Config

	access_token_validity_in_minutes = Config.get("JWT_ACCESS_TOKEN_VALIDITY").as_int(default=_def.ACCESS_TOKEN_LIFETIME)
	refresh_token_validity_in_minutes = Config.get("JWT_REFRESH_TOKEN_VALIDITY").as_int(default=_def.REFRESH_TOKEN_LIFETIME)

	_jwt_settings = dict()
	try:
		_jwt_settings['TOKEN_USER_CLASS'] = opt.get('token_user_class') or _def.TOKEN_USER_CLASS
		_jwt_settings['USER_ID_CLAIM'] = opt.get('user_id_claim') or _def.USER_ID_CLAIM
		_jwt_settings['USER_AUTHENTICATION_RULE'] = opt.get('user_auth_rule') or _def.USER_AUTHENTICATION_RULE
		_jwt_settings['ALGORITHM'] = opt.get('algorithm') or _def.ALGORITHM
		_jwt_settings['AUTH_HEADER_TYPES'] = opt.get('auth_header_types') or _def.AUTH_HEADER_TYPES
		_jwt_settings['AUTH_HEADER_NAME'] = opt.get('auth_header_name') or _def.AUTH_HEADER_NAME
		_jwt_settings['USER_ID_FIELD'] = opt.get('user_id_field') or _def.USER_ID_FIELD
		_jwt_settings['TOKEN_TYPE_CLAIM'] = opt.get('token_type_claim') or _def.TOKEN_TYPE_CLAIM
		_jwt_settings['JTI_CLAIM'] = opt.get('jti_claim') or _def.JTI_CLAIM
		_jwt_settings['ROTATE_REFRESH_TOKENS'] = opt.get('rotate_refresh_tokens') or _def.ROTATE_REFRESH_TOKENS
		_jwt_settings['BLACKLIST_AFTER_ROTATION'] = opt.get('blacklist_after_rotation') or _def.BLACKLIST_AFTER_ROTATION
		_jwt_settings['AUDIENCE'] = opt.get('audience') or _def.AUDIENCE
		_jwt_settings['ISSUER'] = opt.get('issuer') or _def.ISSUER
		_jwt_settings['SLIDING_TOKEN_REFRESH_EXP_CLAIM'] = opt.get('sliding_token_refresh_exp_claim') or \
		                                                   _def.SLIDING_TOKEN_REFRESH_EXP_CLAIM

		_jwt_settings['ACCESS_TOKEN_LIFETIME'] = timedelta(minutes=access_token_validity_in_minutes)
		_jwt_settings['REFRESH_TOKEN_LIFETIME'] = timedelta(minutes=refresh_token_validity_in_minutes)
		_jwt_settings['SIGNING_KEY'] = Config.get('JWT_TOKEN_SIGNING_KEY').as_str(default=_def.SIGNING_KEY)
		_jwt_settings['VERIFYING_KEY'] = opt.get('verifying_key') or _jwt_settings.get('SIGNING_KEY')

	except Exception as e:
		logging.warning(e)

	return _jwt_settings

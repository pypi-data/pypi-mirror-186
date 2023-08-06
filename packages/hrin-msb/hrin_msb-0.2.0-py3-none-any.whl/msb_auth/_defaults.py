from msb_auth.users._token_user import TokenUser
from ._constants import DefaultJwtAuthConfig, TokenConst
from datetime import timedelta
from msb_config import Config


def jwt_user_auth_rule(user: TokenUser):
	return user


DEFAULT_AUTHENTICATION_CLASSES = ('msb_auth.validators.JwtTokenValidator',)

JWT_AUTH_SETTINGS_FOR_VALIDATION = {
	'TOKEN_USER_CLASS': DefaultJwtAuthConfig.user_class,
	'USER_ID_CLAIM': DefaultJwtAuthConfig.userid_claim,
	'USER_AUTHENTICATION_RULE': DefaultJwtAuthConfig.auth_rule,
	'ALGORITHM': DefaultJwtAuthConfig.algorithm_hs256,
	'AUTH_HEADER_TYPES': DefaultJwtAuthConfig.auth_header_types,
	'AUTH_HEADER_NAME': DefaultJwtAuthConfig.auth_header_name,
	'USER_ID_FIELD': DefaultJwtAuthConfig.userid_field,
	'TOKEN_TYPE_CLAIM': DefaultJwtAuthConfig.token_type_claim,
	'JTI_CLAIM': DefaultJwtAuthConfig.jti_claim,
	'SIGNING_KEY': Config.get(TokenConst.signing_key_config_name).as_str(),
	'VERIFYING_KEY': Config.get(TokenConst.verification_key_config_name).as_str(),
}

JWT_AUTH_SETTINGS_FOR_AUTHENTICATION = {
	**JWT_AUTH_SETTINGS_FOR_VALIDATION,
	'ROTATE_REFRESH_TOKENS': False,
	'BLACKLIST_AFTER_ROTATION': False,
	'ACCESS_TOKEN_LIFETIME': timedelta(minutes=Config.get(TokenConst.access_token_validity_config_name).as_int(default=30)),
	'REFRESH_TOKEN_LIFETIME': timedelta(
		minutes=Config.get(TokenConst.refresh_token_validity_config_name).as_int(default=1440)),
	'AUDIENCE': Config.get(TokenConst.token_audiance_config_name).as_str(),
	'ISSUER': Config.get(TokenConst.token_issuer_config_name).as_str(),

}

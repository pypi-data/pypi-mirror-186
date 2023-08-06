AUTH_REQUEST_USER_FIELD = "user"
AUTH_REQUEST_PASSWORD_FIELD = "password"


class TokenConst:
	username_field = "username"
	userid_field = "id"
	user_email_field = "email"

	access_token_validity_config_name = 'JWT_ACCESS_TOKEN_VALIDITY'
	refresh_token_validity_config_name = 'JWT_REFRESH_TOKEN_VALIDITY'
	signing_key_config_name = 'JWT_TOKEN_SIGNING_KEY'
	verification_key_config_name = 'JWT_TOKEN_VERIFY_KEY'
	token_audiance_config_name = 'JWT_TOKEN_AUDIENCE'
	token_issuer_config_name = 'JWT_TOKEN_ISSUER'


class DefaultJwtAuthConfig:
	username_field = "username"
	userid_claim = "id"
	userid_field = "userid"
	user_email_field = "email"
	user_class = "msb_auth.TokenUser"
	auth_rule = 'msb_auth.jwt_user_auth_rule'
	algorithm_hs256 = 'HS256'
	auth_header_types = ('Bearer',)
	auth_header_name = 'HTTP_AUTHORIZATION'
	token_type_claim = 'token_type'
	jti_claim = 'jti'


class MsAuthConst:
	AUTH_VALIDATION_USER_VALUE = "token"
	AUTH_VALIDATION_AUTH_TYPE = "ms_sso"


class LdapAuthConst:
	pass

"""
`Configs` is a class that contains the global configuration variables/parameters
to be used in the services
"""


class Configs:
    GRAPHQL_URL: str = "https://in-api-{env}.stxapp.io/graphiql"
    WS_URL: str = "wss://in-api-{env}.stxapp.io/socket/websocket"
    API_ENV = "staging"
    LOGIN_API: str = "login"
    CONFIRM_2FA: str = "confirm2Fa"
    REFRESH_TOKEN_API: str = "newToken"
    CHANNEL_CONNECTION_URL: str = "{url}?token={token}&vsn=2.0.0"

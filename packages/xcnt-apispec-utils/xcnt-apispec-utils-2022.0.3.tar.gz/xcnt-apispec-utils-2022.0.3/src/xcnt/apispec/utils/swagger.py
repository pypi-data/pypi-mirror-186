from flasgger import Swagger


def get_swagger() -> Swagger:
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["swagger_ui_bundle_js"] = "//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"
    swagger_config["swagger_ui_standalone_preset_js"] = "//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js"
    swagger_config["jquery_js"] = "//unpkg.com/jquery@2.2.4/dist/jquery.min.js"
    swagger_config["swagger_ui_css"] = "//unpkg.com/swagger-ui-dist@3/swagger-ui.css"
    return Swagger(config=swagger_config)

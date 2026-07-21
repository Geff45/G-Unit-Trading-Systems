class ConfigValidator:
    
    def validate(self, config):

        if not isinstance(config, dict):
            raise ValueError("Configuration must be a dictionary.")

        return True
import yaml
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class ModelConfig:
    """Configuration for a model to benchmark."""
    base_url: str
    port: int
    name: str = None
    model_name: str = None
    temperature: float = 0.7
    max_tokens: int = None
    extra_body: Dict[str, Any] = None

class ConfigLoader:
    """Loads configuration from YAML file."""
    def __init__(self, config_path: str = "configs.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
        self.models = self._load_models()

    def _load_config(self) -> Dict[str, Any]:
        """Load YAML configuration file."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading config file: {e}")
            return {}

    def _load_models(self) -> Dict[str, ModelConfig]:
        """Load model configurations from config."""
        models = {}
        model_configs = self.config.get("models", {})
        for model_key, model_data in model_configs.items():
            models[model_key] = ModelConfig(
                name=model_data.get("name", model_key),
                base_url=model_data.get("base_url"),
                port=model_data.get("port"),
                model_name=model_data.get("model_name", model_key),
                temperature=model_data.get("temperature", 0.7),
                max_tokens=model_data.get("max_tokens"),
                extra_body=model_data.get("extra_body")
            )
        return models

    def get_model_configs(self) -> Dict[str, ModelConfig]:
        """Get all model configurations."""
        return self.models
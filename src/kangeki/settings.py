from importlib.metadata import version
from typing import Type, Tuple
from pathlib import Path
import click
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

app_dir = Path(click.get_app_dir(app_name="kangeki"))
config_file_path = app_dir / "config.toml"


class Settings(BaseSettings):
    version: str = version("kangeki")

    sqlite_url: str = f"{app_dir / 'db.sqlite3'}"
    theme: str = "dracula"

    model_config = SettingsConfigDict(
        toml_file=config_file_path,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        app_dir.mkdir(parents=True, exist_ok=True)
        return (
            init_settings,
            TomlConfigSettingsSource(settings_cls),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )


if __name__ == "__main__":
    settings = Settings()
    print(settings.model_dump())

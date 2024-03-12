from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    input_dir: list[str]
    output_dir: str
    file_name_mask: str

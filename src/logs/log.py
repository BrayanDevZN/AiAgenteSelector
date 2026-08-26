"""
Define o caminho que vai salvar os logs
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent / "app.log"




"""
Cria os logs
"""
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(BASE_DIR)
    ]
)


#Variavel que carrega as configurações
logger = logging.getLogger(__name__)
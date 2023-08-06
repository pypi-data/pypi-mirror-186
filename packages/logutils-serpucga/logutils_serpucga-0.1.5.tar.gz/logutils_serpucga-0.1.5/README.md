# Logging utils

Este repositorio contiene un código muy básico que sirve para dar un formato
visual e informacionalmente completo a los logs usando la librería estándar
logging. Por supuesto, esta configuración podría realizarse cada vez en cada
proyecto, pero encuentro eso engorroso y una pérdida de tiempo, así que he
considerado mejor externalizarlo todo a una pequeña librería externa.

## Utilización
```
from logutils import get_logger

logger = get_logger(__name__)
logger.info("Hola hola!")
```

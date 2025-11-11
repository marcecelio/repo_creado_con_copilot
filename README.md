# MCP Server - Text Generator

Un servidor MCP (Model Context Protocol) implementado con FastMCP que proporciona herramientas para generar texto.

## Descripción

Este proyecto implementa un servidor MCP personalizado utilizando [FastMCP](https://gofastmcp.com), que permite a los IDEs y otras aplicaciones cliente conectarse y utilizar herramientas personalizadas.

## Características

- **Servidor MCP completo**: Implementado con FastMCP 2.13.0+
- **Herramienta de generación de texto**: Tool personalizada que genera texto basado en un prompt
- **Fácil integración**: Compatible con cualquier cliente MCP (IDEs como VSCode, Cursor, etc.)

## Requisitos

- Python 3.12+
- FastMCP 2.13.0+

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/marcecelio/repo_creado_con_copilot.git
cd repo_creado_con_copilot
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecución del servidor

Para iniciar el servidor MCP:

```bash
python3 mcp_server.py
```

El servidor se iniciará en modo STDIO (Standard Input/Output) por defecto, que es el modo estándar para la comunicación MCP.

### Herramientas disponibles

#### `generate_text`

Genera texto basado en un prompt dado.

**Parámetros:**
- `prompt` (str): El texto inicial o tema para generar texto
- `length` (int, opcional): Longitud aproximada del texto a generar en caracteres (default: 100)

**Ejemplo de uso:**
```python
# El servidor MCP manejará las llamadas automáticamente
# cuando se conecte desde un IDE compatible
generate_text(
    prompt="inteligencia artificial",
    length=150
)
```

## Configuración para IDEs

### Visual Studio Code / Cursor

Para conectar el servidor a tu IDE, agrega la siguiente configuración a tu archivo de configuración MCP:

**Ubicación del archivo de configuración:**
- macOS: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Windows: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`
- Linux: `~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

**Configuración:**
```json
{
  "mcpServers": {
    "text-generator": {
      "command": "python3",
      "args": ["/ruta/absoluta/a/mcp_server.py"],
      "env": {}
    }
  }
}
```

Asegúrate de reemplazar `/ruta/absoluta/a/mcp_server.py` con la ruta completa al archivo `mcp_server.py` en tu sistema.

### Claude Desktop

Para Claude Desktop, agrega la configuración en `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "text-generator": {
      "command": "python3",
      "args": ["/ruta/absoluta/a/mcp_server.py"]
    }
  }
}
```

## Testing

El proyecto incluye un script de prueba para verificar la funcionalidad:

```bash
python3 test_mcp_server.py
```

Este script verifica que:
- La herramienta `generate_text` funciona correctamente
- Se genera texto con diferentes longitudes
- El texto generado respeta los parámetros solicitados

## Estructura del Proyecto

```
repo_creado_con_copilot/
├── mcp_server.py           # Servidor MCP principal
├── test_mcp_server.py      # Tests para verificar funcionalidad
├── requirements.txt        # Dependencias del proyecto
├── mcp_config_example.json # Ejemplo de configuración para IDEs
└── README.md              # Este archivo
```

## Verificación de la conexión

Una vez configurado el servidor en tu IDE:

1. Reinicia el IDE
2. El servidor debería aparecer en la lista de servidores MCP disponibles
3. Deberías poder ver y ejecutar la herramienta `generate_text`
4. Prueba ejecutar la herramienta con diferentes prompts

## Desarrollo

### Agregar nuevas herramientas

Para agregar una nueva herramienta al servidor, simplemente decora una función con `@mcp.tool()`:

```python
@mcp.tool()
def mi_nueva_herramienta(parametro: str) -> str:
    """
    Descripción de la herramienta.
    
    Args:
        parametro: Descripción del parámetro
    
    Returns:
        str: Descripción del resultado
    """
    # Tu lógica aquí
    return resultado
```

## Recursos

- [Documentación de FastMCP](https://gofastmcp.com)
- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y experimental.

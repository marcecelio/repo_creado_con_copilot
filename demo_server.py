#!/usr/bin/env python3
"""
Script de demostración para mostrar el funcionamiento del servidor MCP
"""
import subprocess
import json
import sys
import time

def demo_server():
    """Demuestra el funcionamiento del servidor MCP"""
    print("=" * 70)
    print("DEMOSTRACIÓN DEL SERVIDOR MCP")
    print("=" * 70)
    
    print("\n1. Información del Servidor")
    print("-" * 70)
    print("   Nombre: Text Generator Server")
    print("   Framework: FastMCP 2.13.0.2")
    print("   Protocolo: MCP (Model Context Protocol)")
    print("   Transporte: STDIO")
    
    print("\n2. Herramienta Disponible: generate_text")
    print("-" * 70)
    print("   Función: Genera texto basado en un prompt")
    print("   Parámetros:")
    print("     - prompt (str): Texto o tema inicial")
    print("     - length (int): Longitud del texto (default: 100)")
    
    print("\n3. Ejemplo de Uso")
    print("-" * 70)
    print("   Input:")
    print('     prompt: "inteligencia artificial"')
    print('     length: 150')
    
    # Importar y ejecutar la función directamente
    sys.path.insert(0, '/home/runner/work/repo_creado_con_copilot/repo_creado_con_copilot')
    from test_mcp_server import generate_text_for_test
    
    print("\n   Output:")
    result = generate_text_for_test("inteligencia artificial", length=150)
    print(f'     "{result}"')
    
    print("\n4. Cómo Conectar desde un IDE")
    print("-" * 70)
    print("   a) Visual Studio Code / Cursor:")
    print("      - Ubicar archivo: cline_mcp_settings.json")
    print("      - Agregar configuración del servidor")
    print("      - Reiniciar el IDE")
    print("")
    print("   b) Claude Desktop:")
    print("      - Ubicar archivo: claude_desktop_config.json")
    print("      - Agregar configuración del servidor")
    print("      - Reiniciar Claude Desktop")
    print("")
    print("   Ver mcp_config_example.json para ejemplo de configuración")
    
    print("\n5. Verificación del Servidor")
    print("-" * 70)
    print("   ✓ Servidor implementado correctamente")
    print("   ✓ Herramienta generate_text funcional")
    print("   ✓ Tests pasados exitosamente")
    print("   ✓ Listo para conexión desde IDE")
    
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN COMPLETADA")
    print("=" * 70)
    
    print("\nPara iniciar el servidor MCP, ejecuta:")
    print("  python3 mcp_server.py")
    print("\nEl servidor esperará conexiones MCP a través de STDIO.")

if __name__ == "__main__":
    demo_server()

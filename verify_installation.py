#!/usr/bin/env python3
"""
Script de verificación completa del servidor MCP
Este script verifica todos los componentes del proyecto
"""
import os
import sys

def verify_installation():
    """Verifica que todas las dependencias estén instaladas"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE INSTALACIÓN")
    print("=" * 70)
    
    try:
        import fastmcp
        print(f"✓ FastMCP instalado (versión: {fastmcp.__version__})")
    except ImportError:
        print("✗ FastMCP no está instalado")
        return False
    
    return True

def verify_files():
    """Verifica que todos los archivos necesarios existan"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE ARCHIVOS")
    print("=" * 70)
    
    base_path = "/home/runner/work/repo_creado_con_copilot/repo_creado_con_copilot"
    required_files = [
        "mcp_server.py",
        "requirements.txt",
        "README.md",
        "test_mcp_server.py",
        "mcp_config_example.json",
        ".gitignore"
    ]
    
    all_exist = True
    for file in required_files:
        file_path = os.path.join(base_path, file)
        if os.path.exists(file_path):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (no encontrado)")
            all_exist = False
    
    return all_exist

def verify_server():
    """Verifica que el servidor MCP esté correctamente configurado"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DEL SERVIDOR MCP")
    print("=" * 70)
    
    sys.path.insert(0, '/home/runner/work/repo_creado_con_copilot/repo_creado_con_copilot')
    
    try:
        from mcp_server import mcp
        print(f"✓ Servidor importado correctamente: {mcp.name}")
        return True
    except Exception as e:
        print(f"✗ Error al importar servidor: {e}")
        return False

def verify_tool():
    """Verifica que la herramienta de generación de texto funcione"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE LA HERRAMIENTA")
    print("=" * 70)
    
    sys.path.insert(0, '/home/runner/work/repo_creado_con_copilot/repo_creado_con_copilot')
    
    try:
        from test_mcp_server import generate_text_for_test
        
        # Probar la generación de texto
        result = generate_text_for_test("Python", length=100)
        
        if result and len(result) > 0:
            print("✓ Herramienta generate_text funciona correctamente")
            print(f"  Ejemplo de salida: {result[:50]}...")
            return True
        else:
            print("✗ La herramienta no generó texto")
            return False
    except Exception as e:
        print(f"✗ Error al probar herramienta: {e}")
        return False

def verify_documentation():
    """Verifica que la documentación esté presente"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE DOCUMENTACIÓN")
    print("=" * 70)
    
    readme_path = "/home/runner/work/repo_creado_con_copilot/repo_creado_con_copilot/README.md"
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        checks = [
            ("Instalación", "## Instalación" in content or "## Requisitos" in content),
            ("Uso del servidor", "python3 mcp_server.py" in content or "python mcp_server.py" in content),
            ("Configuración IDE", "mcpServers" in content or "Configuración" in content),
            ("Herramientas", "generate_text" in content)
        ]
        
        all_present = True
        for check_name, check_result in checks:
            if check_result:
                print(f"✓ {check_name} documentado")
            else:
                print(f"✗ {check_name} no documentado")
                all_present = False
        
        return all_present
    except Exception as e:
        print(f"✗ Error al verificar documentación: {e}")
        return False

def main():
    """Función principal de verificación"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN COMPLETA DEL PROYECTO MCP SERVER")
    print("=" * 70)
    
    results = []
    
    # Ejecutar todas las verificaciones
    results.append(("Instalación de dependencias", verify_installation()))
    results.append(("Archivos del proyecto", verify_files()))
    results.append(("Servidor MCP", verify_server()))
    results.append(("Herramienta de generación", verify_tool()))
    results.append(("Documentación", verify_documentation()))
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("RESUMEN DE VERIFICACIÓN")
    print("=" * 70)
    
    all_passed = True
    for check_name, result in results:
        status = "✓ PASÓ" if result else "✗ FALLÓ"
        print(f"{status}: {check_name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓✓✓ TODAS LAS VERIFICACIONES PASARON ✓✓✓")
        print("\nEl servidor MCP está listo para usarse!")
        print("\nPróximos pasos:")
        print("1. Configurar el servidor en tu IDE usando mcp_config_example.json")
        print("2. Ejecutar: python3 mcp_server.py")
        print("3. Conectar desde tu IDE y usar la herramienta generate_text")
    else:
        print("✗✗✗ ALGUNAS VERIFICACIONES FALLARON ✗✗✗")
        print("\nPor favor, revisa los errores anteriores.")
    print("=" * 70 + "\n")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

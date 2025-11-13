#!/usr/bin/env python3
"""
MCP Server con FastMCP
Un servidor MCP que proporciona una herramienta para generar texto.
"""

from fastmcp import FastMCP

# Crear instancia del servidor MCP
mcp = FastMCP("Text Generator Server")


@mcp.tool()
def generate_text(prompt: str, length: int = 100) -> str:
    """
    Genera texto basado en un prompt dado.
    
    Args:
        prompt: El texto inicial o tema para generar texto
        length: Longitud aproximada del texto a generar (en caracteres)
    
    Returns:
        str: Texto generado basado en el prompt
    """
    # Generación simple de texto basada en el prompt
    import random
    
    # Frases de ejemplo para expandir el prompt
    expansions = [
        f"El tema '{prompt}' es fascinante porque abre muchas posibilidades.",
        f"Considerando '{prompt}', podemos explorar diversos aspectos interesantes.",
        f"Sobre '{prompt}', hay mucho que decir y analizar en profundidad.",
        f"La idea de '{prompt}' nos lleva a reflexionar sobre diferentes perspectivas.",
        f"Cuando pensamos en '{prompt}', surgen múltiples conexiones y conceptos relacionados.",
    ]
    
    # Frases adicionales para completar el texto
    additional_phrases = [
        "Esto nos permite comprender mejor el contexto general.",
        "Es importante analizar todos los ángulos posibles.",
        "La complejidad del tema requiere una consideración cuidadosa.",
        "Cada perspectiva aporta valor al entendimiento completo.",
        "Los detalles son cruciales para una comprensión profunda.",
        "La investigación continua revela más información valiosa.",
        "Las conexiones entre conceptos enriquecen el análisis.",
    ]
    
    # Construir el texto generado
    generated_text = f"{random.choice(expansions)} "
    
    # Añadir frases adicionales hasta alcanzar la longitud deseada
    while len(generated_text) < length:
        generated_text += f"{random.choice(additional_phrases)} "
    
    # Recortar al tamaño solicitado y limpiar
    generated_text = generated_text[:length].strip()
    
    # Asegurar que termina con puntuación
    if generated_text and generated_text[-1] not in '.!?':
        generated_text += '.'
    
    return generated_text


if __name__ == "__main__":
    # Ejecutar el servidor MCP
    mcp.run()

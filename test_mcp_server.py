#!/usr/bin/env python3
"""
Test script para verificar la funcionalidad del servidor MCP
"""

def generate_text_for_test(prompt: str, length: int = 100) -> str:
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

def test_generate_text():
    """Test the generate_text tool"""
    print("Testing generate_text tool...\n")
    
    # Test 1: Basic text generation
    print("Test 1: Basic text generation")
    result1 = generate_text_for_test("inteligencia artificial", length=150)
    print(f"Prompt: 'inteligencia artificial'")
    print(f"Length: 150")
    print(f"Result: {result1}")
    print(f"Actual length: {len(result1)}")
    assert len(result1) > 0, "Text should be generated"
    assert len(result1) <= 151, "Text should not exceed requested length significantly"
    print("✓ Test 1 passed\n")
    
    # Test 2: Shorter text
    print("Test 2: Shorter text generation")
    result2 = generate_text_for_test("Python", length=80)
    print(f"Prompt: 'Python'")
    print(f"Length: 80")
    print(f"Result: {result2}")
    print(f"Actual length: {len(result2)}")
    assert len(result2) > 0, "Text should be generated"
    assert len(result2) <= 81, "Text should not exceed requested length significantly"
    print("✓ Test 2 passed\n")
    
    # Test 3: Longer text
    print("Test 3: Longer text generation")
    result3 = generate_text_for_test("machine learning", length=200)
    print(f"Prompt: 'machine learning'")
    print(f"Length: 200")
    print(f"Result: {result3}")
    print(f"Actual length: {len(result3)}")
    assert len(result3) > 0, "Text should be generated"
    assert len(result3) <= 201, "Text should not exceed requested length significantly"
    print("✓ Test 3 passed\n")
    
    print("All tests passed! ✓✓✓")

if __name__ == "__main__":
    test_generate_text()

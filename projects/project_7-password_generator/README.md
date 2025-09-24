# PasswordGenerator 🔒
**Última actualización: 24 de septiembre de 2025, 05:15 PM -05:00**

Bienvenido a mi repositorio de proyectos en Python. Este proyecto es una aplicación de consola que genera contraseñas seguras y aleatorias utilizando el módulo `secrets` para mayor seguridad criptográfica. El código fue desarrollado como parte de mi aprendizaje continuo en Python. ¡Cualquier comentario o sugerencia es bienvenida!

## Proyecto
### PasswordGenerator
- **Descripción**: Este programa genera una contraseña aleatoria con una longitud personalizable y un número mínimo de dígitos, caracteres especiales, letras mayúsculas y minúsculas. Utiliza el módulo `secrets` para selecciones aleatorias seguras y expresiones regulares (`re`) para validar los requisitos de la contraseña.
- **Archivo**: [password_generator.py](password_generator.py)
- **Ejemplo**: Al ejecutar `generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1)`, se genera una contraseña como:  
  `X7$kL9mPqW2zR8vJ`  
  (El resultado varía en cada ejecución debido a la aleatoriedad).
- **Habilidades**: Módulo `secrets`, expresiones regulares (`re`), manipulación de cadenas, lógica condicional, funciones, validación de entrada.
- **Captura de pantalla**:  
  ![Ejemplo PasswordGenerator](password_generator_example.png)

---

## Requisitos
- Python 3.x instalado en el sistema.
- Acceso a una terminal o entorno compatible con Python (como IDLE).
- Módulos necesarios: `secrets`, `re`, `string` (incluidos en la biblioteca estándar de Python).

---

## Instrucciones de Uso
1. Asegúrate de haber clonado el repositorio y de tener Python instalado.
2. Navega a la carpeta del proyecto en tu terminal.
3. Ejecuta el programa con el siguiente comando:
   ```bash
   python password_generator.py



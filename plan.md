# Plan de Aplicación Web de Sorteos

## Fase 1: Interfaz Básica y Gestión Manual de Participantes ✅
- [x] Crear layout principal con header, título y secciones organizadas
- [x] Implementar campo para nombre del sorteo
- [x] Crear formulario para agregar participantes manualmente (nombre, email/identificador opcional)
- [x] Mostrar lista de participantes agregados con opción de eliminar
- [x] Diseño responsive y atractivo con colores llamativos

---

## Fase 2: Carga de Excel y Gestión Avanzada ✅
- [x] Implementar componente de carga de archivos Excel (.xlsx, .xls)
- [x] Procesar archivo Excel y extraer participantes (usando openpyxl)
- [x] Validar datos del Excel y mostrar errores si los hay
- [x] Permitir limpiar todos los participantes y reiniciar sorteo
- [x] Mostrar contador de participantes totales

---

## Fase 3: Sistema de Sorteo con Animación y Celebración ✅
- [x] Crear botón de "Realizar Sorteo" con validaciones
- [x] Implementar animación de cuenta regresiva/ruleta de nombres
- [x] Seleccionar ganador(es) aleatoriamente
- [x] Mostrar ganador con animación de serpentinas/confetti (usando CSS/canvas)
- [x] Permitir múltiples ganadores y sorteos consecutivos
- [x] Agregar sonido de celebración opcional

---

## Fase 4: Verificación UI ✅
- [x] Verificar interfaz principal con sorteo sin nombre personalizado
- [x] Verificar sorteo con 1 ganador después de agregar participantes manualmente
- [x] Verificar sorteo con múltiples ganadores y opción de excluir ganadores previos
- [x] Validar diseño responsive y animaciones de confetti

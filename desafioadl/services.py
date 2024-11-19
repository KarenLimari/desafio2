from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.prefetch_related('subtareas').all()
    return [
        {
            'tarea': tarea,
            'subtareas': list(tarea.subtareas.all())
        }
        for tarea in tareas
    ]

def crear_nueva_tarea(descripcion, estado=True):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, estado=True):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for item in tareas_y_subtareas:
        print(f"[{item['tarea'].id}] {item['tarea'].descripcion}")
        for subtarea in item['subtareas']:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")

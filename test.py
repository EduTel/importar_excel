def _get_selection():
    return [
        ('draft', 'Borrador'),
        ('pending', 'Pendiente'),
        ('approved', 'Aprobada'),
        ('Completed', 'Completado')
    ]
print dict(_get_selection())
print dict(_get_selection())['draft']
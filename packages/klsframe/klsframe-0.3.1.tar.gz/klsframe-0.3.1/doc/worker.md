# Worker module

## CLI

This tool allows you to create and run workers.

Commands:

- Invoke [Myworker]. Runs the Worker's CLI wrapper
- new: creates a new worker

```
kls-worker [invoke <myWorker>] [new <MyNewWorker>]
```

## Directory structure

```yaml
worker:
  - playbooks: # Custom pb created/recorder by the user
      - limpiar.py
      - etiquetar.py
  - utils.py                # Functionalities shared between playbooks
  - worker.conf             # Configuration
  - worker.db               # Storage for pages, elements, and GuiLayout things
  - desktopWorker.py               # Main. CLI wrapper for the worker
```

Example of a simple CLI section. Each section is a function

`````python
def main_menu(*args):
    options = ['sum', 'sub']
    options_advanced = [
        ('sum', sum_callback),
        ('sub', sub_callback)
    ]
    # Si no hay callback devuelve el valor seleccionado
    opt = selectable_list(options)
    if opt == 'sum':
        sum(*args)
    elif opt == 'sub':
        sub(*args)
`````
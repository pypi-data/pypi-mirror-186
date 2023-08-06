# Wrapper

Do you need a wrapper for your script? Do not worry! you are in the right place

## Conf file

```yaml
title: "NVD collector"
description: "Get the details of any vulnerability hosted in the NVD"
banner:
  text: "NVD Collector byURHL"
  style: "default" # Default for plain text, any other to use ascii art
parameters:
  - name: "target" # NO dash prefix means MANDATORY
    placeholder: "IP_RANGE"
    type: "string"
    regex: ['([0-9]{0,3}.){3}[0-9]{1,3}']
  - name: ["-f", "--file"] # dash prefix means OPTIONAL
    placeholder: "OUT_FILE"
    type: "string"
    regex: ['\W*\.json', '\W*.ya?ml']
options:
  - text: "Get vulnerability details by CVE"
    entryPoint: "/path/to/your/module.py"
  - text: "Get vulnerability details by CPE"
    entryPoint: "/path/to/your/module.py"
logFile: "./worker.log"
```

- las opciones del menu llaman a funciones.
- Esas funciones son el entry point a tu programa
- y se especifican en el archivo de configuracion


- Con esta herramienta se cre un wrapper basico.
- Las funciones a las que llama pueden sen oros wrappers
- Cada modulo tiene que estar en un archivo.py separado y tener su propio init


- Wrappers can be executed as CLI or GUI

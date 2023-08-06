# Hyper-V winrm python

На данный момент можно создавать виртуальные машины только через заранее подготовленный шаблон виртуальноф машины.


## Installation

python3 -m pip install hyper-v

## Configuration

```
from hyperv import HyperV
import config

HV = HyperV(
    env_prefix=env_prefix,
    storage_root=storage_root,
    vm_template_pach=vm_template_pach,
    host=hv_host,
    user=hv_user,
    password=hv_password
    )


free_memory = HV.get_free_memory
print(free_memory)
```

* `storage_root` -  Директория, где будет создана папка, для Виртуальной машины
* `vm_template_pach` - Директория, где лежит шаблон Виртуальной машины
* `env_prefix`  -   Префикс, который будет добавлен к имени Виртуальной машины
* `host`    -   Hyper-V хост 
* `user`    - Имя пользователя для доступа по winrm
* `password`    - Пароль пользователя для доступа по winrm

## License

[GPL-3.0](LICENSE)
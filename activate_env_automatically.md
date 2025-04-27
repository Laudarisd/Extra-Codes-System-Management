open the file 

```
nano ~/.bashrc
```

add following 





```bash
activate_virtual_env() {
    if [[ $PWD == /mnt/sdb/sudip* || $PWD == /mnt/sdb/Project* ]]; then
        if [[ -z "$VIRTUAL_ENV" || "$VIRTUAL_ENV" != "/mnt/sdb/sudip/virtual_env" ]]; then
            source /mnt/sdb/sudip/virtual_env/bin/activate
        fi
    elif [[ -n "$VIRTUAL_ENV" && "$VIRTUAL_ENV" == "/mnt/sdb/sudip/virtual_env" ]]; then
        deactivate
    fi
}

PROMPT_COMMAND="activate_virtual_env; $PROMPT_COMMAND"
```


and 
update 

```
source ~/.bashrc

```

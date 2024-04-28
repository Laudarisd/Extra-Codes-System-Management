# unzip multiple zip files

> $ for z in *.zip
> do
> unzip $z;
> done

after the above command, it will start unzipping process

***Single one command**

for z in *.zip; do unzip "$z"; done

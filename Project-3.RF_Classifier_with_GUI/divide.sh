#!/bin/bash
mkdir -p time

count=0
for file in $(ls all | sort -n); do
  ((count++))
  if [[ "$file" =~ ^dump[0-9000]*$ ]]; then
    dir_name="1s"
  else
    dir_name="$((count / 12 + 1))s"
  fi
  echo "Processing file $file, moving to $dir_name"
  mkdir -p "time/$dir_name"
  mv "all/$file" "time/$dir_name"
  if [ $((count % 12)) -eq 0 ]; then
    sleep 0.1 # wait for filesystem to sync (optional)
  fi
done

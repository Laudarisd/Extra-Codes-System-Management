from pathlib import Path
keep_stems = set(file.stem for file in Path('./20/traffic_sign/').glob('*.jpg'))
delete_paths = [file for file in Path('./20/xmls/').glob('*.xml') if file.stem not in keep_stems]
for file in delete_paths:
    file.unlink()
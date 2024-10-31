$exclude = @("venv", "DataBot-19.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "DataBot-19.zip" -Force
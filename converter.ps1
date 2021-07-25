$md = ConvertFrom-Markdown -Path .\sample.md
$md.Html | Out-File -Encoding utf8 .\sample.html
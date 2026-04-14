$enc = [System.Text.Encoding]::UTF8
$path = 'car-build-guide.html'
$text = [System.IO.File]::ReadAllText($path, $enc)
$badSeq = $enc.GetString([byte[]](0xE2, 0x80, 0x93))
$good = [char]0x2013
$fixed = $text.Replace($badSeq, [string]$good)
[System.IO.File]::WriteAllText($path, $fixed, $enc)
Write-Host "Done."

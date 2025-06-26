Start-Process "com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"
sleep -seconds 5
$process = Get-Process "RocketLeague"
$process.WaitForExit()
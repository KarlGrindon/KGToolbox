$host.ui.rawui.windowtitle="Running as: $env:USERNAME"

function prompt {            
    "PS " + "[$(Get-Date -format HH:mm)] " + "$(get-location)> "
}
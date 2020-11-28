<#
.SYNOPSIS
    A simple password generator that generates passwords that contain easily readable words, but with enough
    completixty to be not easily guessed.
.DESCRIPTION
    People will be more inclined to use good passwords when they're more easily remembered. This script takes
    a list of common words (from a txt file) and allows you to choose the amount of words in your password 
    (minimum of 4 for complexity)

    The current chosen format is for each word to be joined by a hyphen.
.EXAMPLE
    New-Password.ps1 -WordList words.txt
.EXAMPLE
    New-Password.ps1 -WordList words.txt -WordCount 6
.NOTES
    The chosen format is something that I like to use; it's easy to remember and type, but should be random and
    complex enough to be a good password.
#>

[CmdletBinding()]
Param (
    # List of words. For example, from a txt file.
    [Parameter(Mandatory)]
    [array]$WordList,

    # The amount of words used in the password.
    [int]$WordCount = 4
)

# Stop people from generating passwords without enough complexity
if ($WordCount -lt 4) {
    throw "Please choose a word count of 4 or greater."
}

[array]$list = Get-Content $WordList
$password = @()

for ($i = 0; $i -lt $WordCount; $i++) {
    $password += Get-Random -InputObject $list

    if ($i -lt ($WordCount - 1)) {
        $password += "-"
    }
}

return ($password -join '')
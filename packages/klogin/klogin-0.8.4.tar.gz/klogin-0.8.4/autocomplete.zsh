_klogin()
{
  local cur
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  local suggestions=()
  if [[ $COMP_CWORD -eq 1 ]]; then
    suggestions=$(klogin clusters)
  fi
  if [[ $COMP_CWORD -eq 2 ]]; then
    suggestions="ro admin"
  fi
  COMPREPLY=( $(compgen -W "${suggestions}" -- ${cur}) )

  return 0
}
complete -o nospace -F _klogin klogin

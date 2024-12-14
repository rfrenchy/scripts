grep -r --include=\*.py '# README ME' ./ | \
awk '{print $1}'

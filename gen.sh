files=$(grep -r --include=\*.py '# README ME' ./ | \
        sed 's/:#//g' | \
        awk '{print $1}')

rm readmetest.md

echo "<!-- GENERATED CONTENT - DO NOT MANUALLY ALTER -->" >> readmetest.md
echo "# scripts" >> readmetest.md

echo "$files" | while read -r f;
do
    # >> readmetest.md

    helptext=$(python3 "$f" --help )

    echo $(echo "$helptext")
   #  echo $(echo "$helptext" | grep usage)
   #  echo $(echo "$helptext" | grep description)
   #  echo $(echo "$helptext" | grep options)

    python3 "$f" --help >> readmetest.md
    # readmetxt=$(python3 $f --help)
    # echo $readmetxt
done

# todo, get heredoc approach working
readmex.md << EOF
    Test
EOF

# xargs -n1 -P 3 python3 $(awk '{print $1}') --help
# awk '{print $1}'

# sed 's/./\//g'
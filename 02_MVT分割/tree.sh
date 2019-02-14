echo 'root : '$1
echo '深さ : '$2
tree -aF -L $2 -I .git $1 | sed 's/   /\t/g' > tree.txt

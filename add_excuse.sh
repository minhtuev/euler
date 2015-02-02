cd /box/www/euler
file="$1"
echo $file >> excuses
git add .
git commit -m "updating excuses"
git push
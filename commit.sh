dayNumber=`git status --short | egrep '^\?\? day[0-9]+\/$' | head -1 | egrep -oh '[0-9]+'`
git add day$dayNumber/
git commit -m "Complete day $dayNumber"
git push -u origin master

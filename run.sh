printf '~~~ ADVENT OF CODE 2021 ANSWERS ~~~\n'
printf '            .-"```"-.\n'
printf '           /_\ _ _ __\\\n'
printf '          | /{` ` `  `}\n'
printf '          {} {_,_,_,_,}\n'
printf '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

dayNumber=1
for day in `ls -d */ | egrep '^day[0-9]+\/$' | sed -e 's/day//g' -e 's/\///g' | sort -n`
do
    printf "Day $dayNumber\n"
    part=1
    dir=day$day/
    for script in `ls $dir | egrep '^part(1|2)\.py$'`
    do
        echo `python3 $dir$script`
        answer=`python3 $dir$script 2>/dev/null || printf "Oops! No answer yet :("`
        printf "\\tAnswer for part $part: $answer\n"
        part=$(( $part + 1 ))
    done
    dayNumber=$(( $dayNumber + 1 ))
done

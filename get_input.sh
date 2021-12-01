input_day=$1
session=`cat .session`
pattern="^[0-9]+$"
iterator=""

if ! [[ -z "$1" ]] && [[ $1 =~ $pattern ]]
then
    iterator=$1
else
    iterator=`(ls -d */ | egrep -oh '[0-9]+' | sed -e 's/^0//g') || 1`
fi

for day in $iterator
do
    dirNum=`printf "%02d" $day`
    mkdir -p day$dirNum
    printf "Getting input for day $day...\n"
    printf '%s' "`curl -H "cookie: session=$session" https://adventofcode.com/2021/day/$day/input`" > day$dirNum/input.txt
done
